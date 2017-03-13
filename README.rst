dmv-appointment-scraper
=======================

What?
-----
Parse the California DMV site to get the next available appointment time.

Why?
----
Because their site's usability is foreshadowing of the fun times you can expect for your visit.

Features
--------
Currently, Chrome is assumed to the browser of choice.
This is trivial to extend, all that is required is to install the webdriver and to add support in the code.

The results can be emailed. Emails are sent via gmail smtp servers.

Installation
-------------
You'll need to install `chromedriver <https://sites.google.com/a/chromium.org/chromedriver/>`_.
This is for selenium to open the site in a browser and navigate the site. 

Selenium versions correspond with browser versions, newer versions of Chrome will need updated selenium.
To use a newer version of selenium, bump the pinned version of selenium in `requirements.txt <https://github.com/ipwnponies/dmv-appointment-scraper/blob/master/requirements.txt#L3>`_.

Usage
-----
``make run`` will launch the DMV site in Chrome,
navigate through multiple pages of their god awful site,
and return the parsed result.

``make email`` will email the results. Configure the sender and recipient in `config.yaml <https://github.com/ipwnponies/dmv-appointment-scraper/blob/master/dmv_appointment_scraper/config.yaml>`_. 

Contributing
-------------
#. Fork it!
#. Create your feature branch: git checkout -b my-new-feature
#. Commit your changes: git commit -am 'Add some feature'
#. Push to the branch: git push origin my-new-feature
#. Submit a pull request 🙌
