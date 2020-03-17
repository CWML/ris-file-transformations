#!/usr/bin/env python
# To use:
# python csv-to-ris-format.py csvfile.csv risoutput.txt
#
# Assumes that there is a header row,
# columns are in the same order as the labels list,
# and there are no other columns in the csv.

import csv
from sys import argv

inputfile = 'input-files/2019-12-03_Nyhan.csv'
outputfile = "output-files/resulting-file_2020_test.ris"

items = []
labels = ["TI", "AU", "AB", "PY", "JF", "VL", "IS", "SP", "AN", "DO", "IS", "C1", "NS", "DB"]

with open(inputfile, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    next(reader)

    for row in reader:
        # in order from csv made from Google Sheet
        print("reading a row")
        # create a list of tuples where the first value is the two-letter label,
        # second value is a field in the row from the csv
        item = zip(labels, row)
        items.append(item)

with open(outputfile, 'w') as risfile:
    for citation in items:
        print("writing a row")
        # citation type is article
        risfile.write("TY  - JOUR \n")
        for field in citation:
            line = "{0}  - {1}\n".format(field[0], field[1])
            risfile.write(line)
        # add required end-of-record row
        risfile.write("ER  - \n")