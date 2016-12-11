#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import datetime
from bs4 import BeautifulSoup

# Defining user agent
USER_AGENT = \
    "'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.89 Safari/537.36'"

# Define Air Pollution Site
URL = 'http://aqicn.org/city/kosovo/pristina/us-consulate/'

# We want to sue curl, and use a user-agent (-H)
COMMAND = 'curl -s -H {} {}'.format(USER_AGENT, URL)


def get_data():
    # Dirty hack, not the best option, but requests has some weird issues with this site
    file = os.popen(COMMAND).read()

    # Import file into soup and use the html parser 
    soup = BeautifulSoup(file, 'html.parser')

    # Select the air polution value
    air_quality_value = soup.find('div', {'id': 'aqiwgtvalue'})

    # Select the date when they updated the value  
    air_quality_date = soup.find('span', {'id': 'aqiwgtutime'})

    # Date when we visited the site last time
    date_we_run_the_scan = datetime.date.today()

    # Print all of the above
    print(air_quality_value.text, air_quality_date.text, date_we_run_the_scan)


def main():
    get_data()


if __name__ == '__main__':
    main()
