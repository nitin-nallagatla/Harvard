import sqlite3
import csv
import sys


def main():

    if (len(sys.argv) != 2):
        sys.exit("Use: import.py file.csv")

    filename = sys.argv[1]
    if not (filename.endswith(".csv")):
        sys.exit("accepts only *.csv")

    # connect to the students.db
    sqlite_file = "students.db"
    # Create the cursor as below
    con = sqlite3.connect(sqlite_file)
    cur = con.cursor()

    # Opening the csv file to import from
    with open(filename, "r") as characters:
        # Create the dictionary reader that go through each through rows
        reader = csv.DictReader(characters)
        for row in reader:
            names = []
            for part in row["name"].split(" "):
                names.append(part)
            names.append(row["house"])
            names.append(row["birth"])
            if (len(names) == 5):
                cur.execute("INSERT INTO students (first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?)", names[:5])

            if (len(names) == 4):
                cur.execute("INSERT INTO students (first, last, house, birth) VALUES(?, ?, ?, ?)", names[:4])
    con.commit()
    con.close()

if __name__ == "__main__":
    main()