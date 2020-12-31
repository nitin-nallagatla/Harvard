import sqlite3
import csv
import sys


def main():

    # checking argv (needs to be one, house name)
    if (len(sys.argv) != 2):
        sys.exit("Use as: roster.py house_name")

    # Making case sensitivity
    housename = sys.argv[1].lower()
    houses = ["slytherin", "gryffindor", "ravenclaw", "hufflepuff"]
    if housename.lower() not in houses:
        sys.exit("get the house name: Gryffindor, Hufflepuff, Slytherin or Ravenclaw.")

    # Connecting  with the students.db file and creating a cursor
    sqlite_file = "students.db"
    con = sqlite3.connect(sqlite_file)
    cur = con.cursor()
    cur.execute('SELECT first, middle, last, birth FROM students WHERE lower(house) = "{}" ORDER BY last, first;'.format(housename))
    # Fetching all the  rows of the table as a list of tuples with strings.
    houseroster = cur.fetchall()

    # Parsing with each row in table
    for row in houseroster:
        if not row[1]:
            print("{} {}, born {}".format(row[0], row[2], row[3]))
        else:
            print("{} {} {}, born {}".format(row[0], row[1], row[2], row[3]))

    con.close()

if __name__ == "__main__":
    main()