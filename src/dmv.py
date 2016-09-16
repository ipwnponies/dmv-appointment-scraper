#! python3

import bs4
from email.mime.text import MIMEText
import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import config


def get_dmv_appointment_html():
    print('Firing up web page in Chrome...')
    browser = webdriver.Chrome()
    dmv_config = config.config['dmv']
    browser.get(dmv_config['welcome_url'])
    link_elem = browser.find_element_by_link_text('Office Visit Appointment')
    link_elem.click()

    # Choose DMV Office
    select_office = Select(browser.find_element_by_name('officeId'))
    select_office.select_by_visible_text(dmv_config['office'])

    # Set number of items to process
    items_to_process = browser.find_element_by_id('one_task').click()

    # Choose reasons for appointment
    browser.find_element_by_id(dmv_config['task']).click()

    # Enter personal information
    user_config = dmv_config['user']
    browser.find_element_by_id('first_name').send_keys(['first_name'])
    browser.find_element_by_id('last_name').send_keys(user_config['last_name'])
    browser.find_element_by_id('area_code').send_keys(user_config['area_code'])
    browser.find_element_by_name('telPrefix').send_keys(user_config['phone_prefix'])
    browser.find_element_by_name('telSuffix').send_keys(user_config['phone_suffix'])

    browser.find_element_by_name('ApptForm').submit()
    return browser.page_source


def get_dmv_appointment_time(soup):
    print('Scraping results page...')
    results_div = soup.find(id='app_content').table

    office_tags = [i for i in results_div.descendants if i.name == 'address']
    result_text =''
    for i in office_tags:
        result_text += office_results(i)

    return result_text


def office_results(office):
    address = [i.text for i in office.descendants if i.name == 'td']

    times = office.parent.parent.next_sibling
    while not hasattr(times, 'td'):
        times = times.next_sibling
    times = [i.text for i in times.td.descendants if i.name == 'p']

    return ''.join(address) + ''.join(times)


def email_dmv_appointment(message):
    '''Requires a SMTP server'''
    message = 'Script ran at {}\n{}'.format(datetime.datetime.now(), message)

    email_message = MIMEText(message)
    mail_config = config.config['mail']
    email_message['Subject'] = mail_config['subject']
    email_message['From'] = mail_config['sender']
    email_message['To'] = ','.join(mail_config['recipients'])

    from subprocess import Popen, PIPE
    p = Popen(['/usr/sbin/sendmail', '-t', '-oi'], stdin=PIPE)
    p.communicate(email_message.as_string().encode())

    print('Mail sent to: {}'.format(' '.join(mail_config['recipients'])))


def main():
    dmv_html = get_dmv_appointment_html()
    result_text = get_dmv_appointment_time(bs4.BeautifulSoup(dmv_html))
    email_dmv_appointment(result_text)
    print('Success!')

if __name__ == '__main__':
    exit(main())
