#! python3

import bs4
from selenium import webdriver
from selenium.webdriver.support.ui import Select


def get_dmv_appointment_html():
    browser = webdriver.Chrome()
    browser.get('https://www.dmv.ca.gov/portal/dmv/detail/portal/foa/welcome')
    link_elem = browser.find_element_by_link_text('Office Visit Appointment')
    link_elem.click()

    return browser.page_source


def main():
    dmv_html = get_dmv_appointment_html()

if __name__ == '__main__':
    exit(main())
