from sys import argv, exit
import itertools
import csv
import re


# Checks the argv inputs.
if len(argv) != 3:
    print(f"Error there should be 2 argv, you have {argv}")
    exit(1)

# Opens csv file and puts it into list.
with open(argv[1], "r") as inputfile:
    reader = list(csv.reader(inputfile))
    reader[0].remove("name")
    i = reader[0]

# Opens the input sequence.
with open(argv[2], "r") as sequence:
    data = sequence.read()

# i contains the dna segment from the CSV file we are searching in.
valuelist = []
for q in range(len(i)):
    maxcounter = 0
    counter = 0
    position = 0
    previouspos = 0

    #  while the dna sequence has not been fully scanned, do the following:
    while position < len(data):

        #  returns position of the sequence.
        position = data.find(i[q], position)
        if position == -1:  # if it's not present, reset.
            counter = 0
            break

        #  if not -1 then the required sequence was found and if (position - sentence length) is also equal to 0, it is a consequtive value if sequence is at the start.
        elif (position != -1) and previouspos == 0:
            counter += 1
            maxcounter = counter
            previouspos = position

        # sequential occurances
        elif (position != -1) and ((position - len(i[q])) == previouspos):
            counter += 1
            previouspos = position
            if maxcounter < counter:
                maxcounter = counter

        # first found and not at the beginning of sequence.
        elif (position != -1) and ((position - len(i[q])) != previouspos):
            counter = 1
            previouspos = position
            if maxcounter < counter:
                maxcounter = counter
        position += 1

    # records the largest number of sequential occurances.
    valuelist.append(maxcounter)

# Compares nucleotides to database.
# updates list into list of strings to allow for comparing.
valuelist = list(map(str, valuelist))
# make a new list to preserve reader
cleaned = list(reader)
cleaned.pop(0)
# compare valuelist to reader and if succesful return name.
for person in cleaned:
    if person[1:] == valuelist:
        print(f"{person[0]}")
        break
    elif person == cleaned[-1]:
        print("No match")