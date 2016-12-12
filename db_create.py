import sqlite3
from _config import DATABASE_PATH

with sqlite3.connect(DATABASE_PATH) as connection:

    # get a cursor object used to execute SQL commands
    c = connection.cursor()

    # create the table
    c.execute("""CREATE TABLE air_pollution(air_value_id INTEGER PRIMARY KEY
    AUTOINCREMENT,
    air_value INTEGER NOT NULL, text_value TEXT NOT NULL, updated_at TEXT NOT NULL, scraped_at
    TEXT NOT NULL)""")

    # insert dummy data into the table
    c.execute(
        'INSERT INTO air_pollution (air_value, text_value, updated_at, scraped_at)'
        'VALUES(57, "Moderate", "Updated on Monday 16:00", "2016-12-12")'
    )