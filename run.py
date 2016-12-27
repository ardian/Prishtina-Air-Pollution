#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import datetime
import sqlite3
from bs4 import BeautifulSoup

# Defining user agent
USER_AGENT = \
    "'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.89 Safari/537.36'"

# Define Air Pollution Site
URL = 'http://aqicn.org/city/kosovo/pristina/us-consulate/'

# We want to sue curl, and use a user-agent (-H)
COMMAND = 'curl -s -H {} {}'.format(USER_AGENT, URL)


#def connect_db():
    #return sqlite3.connect(app.config['DATABASE_PATH'])





# for row in cursor:
#    print ("ID = ", row[0])
#    print ("Air Value = ", row[1])
#    print ("Text Value = ", row[2])
#    print ("Updated at = ", row[3])
#    print ("Scraped at = ", row[4], "\n")





def scraper():
    # Dirty hack, not the best option, but requests has some weird issues with
    # this site
    file = os.popen(COMMAND).read()

    # Import file into soup and use the html parser
    soup = BeautifulSoup(file, 'html.parser')

    # Select the air pollution value
    air_quality_value = soup.find('div', {'id': 'aqiwgtvalue'}).text

    # Select info example: Unhealthy
    info_text = soup.find('div', {'id': 'aqiwgtinfo'}).text

    # Select the date when they updated the value
    air_quality_date = soup.find('span', {'id': 'aqiwgtutime'}).text

    # Date when we visited the site last time
    date_we_run_the_scan = datetime.date.today()
#
#


    print(air_quality_value, info_text, air_quality_date, date_we_run_the_scan)

    #  Write to DB

    #conn = sqlite3.connect('data.db')
    #c = conn.cursor()
    # cursor = conn.execute("SELECT air_value_id, air_value, text_value, updated_at, scraped_at  from AIR_POLLUTION")


    # c = conn.execute('insert into air_pollution(, text_value, updated_at, scraped_at) values (?, ?, ?, ?)', , , , )
    #c = conn.execute("INSERT INTO air_pollution(air_value, text_value, updated_at, scraped_at) VALUES (air_quality_value, info_text, air_quality_date, date_we_run_the_scan);")
    #conn.commit()
    #conn.close()

    #  Get data from db, and compare...
    #
    # cursor = conn.execute("  SELECT * FROM air_pollution ORDER BY air_value_id DESC LIMIT 1")
    #
    # for row in cursor:
    #     if (row == )

    



def main():
    scraper()
    print("Operation done successfully")

if __name__ == '__main__':
    main()
