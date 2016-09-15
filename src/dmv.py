#! python3

import bs4
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


def main():
    dmv_html = get_dmv_appointment_html()

if __name__ == '__main__':
    exit(main())
