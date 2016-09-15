#! python3

import bs4
from email.mime.text import MIMEText
import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import Select


def get_dmv_appointment_html():
    browser = webdriver.Chrome()
    browser.get('https://www.dmv.ca.gov/portal/dmv/detail/portal/foa/welcome')
    link_elem = browser.find_element_by_link_text('Office Visit Appointment')
    link_elem.click()

    # Choose DMV Office
    select_office = Select(browser.find_element_by_name('officeId'))
    select_office.select_by_visible_text('SAN FRANCISCO')

    # Set number of items to process
    items_to_process = browser.find_element_by_id('one_task').click()

    # Choose reasons for appointment
    browser.find_element_by_id('taskDLO').click()

    # Enter personal information
    browser.find_element_by_id('first_name').send_keys('first')
    browser.find_element_by_id('last_name').send_keys('last')
    browser.find_element_by_id('area_code').send_keys('555')
    browser.find_element_by_name('telPrefix').send_keys('555')
    browser.find_element_by_name('telSuffix').send_keys('5555')

    browser.find_element_by_name('ApptForm').submit()
    return browser.page_source


def get_dmv_appointment_time(soup):
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
    email_message['Subject'] = 'DMV appoiontment times'
    email_message['From'] = 'jngu@yelp-jngu.localdomain'
    email_message['To'] = 'ipwnponies@gmail.com'

    from subprocess import Popen, PIPE
    p = Popen(['/usr/sbin/sendmail', '-t', '-oi'], stdin=PIPE)
    p.communicate(email_message.as_string().encode())


def main():
    dmv_html = get_dmv_appointment_html()
    result_text = get_dmv_appointment_time(bs4.BeautifulSoup(dmv_html))
    email_dmv_appointment(result_text)

if __name__ == '__main__':
    exit(main())
