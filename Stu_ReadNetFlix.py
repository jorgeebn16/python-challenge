# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

video = input("What show or movie are you looking for? ")

csvpath = os.path.join('..', 'LearnPython', 'netflix_ratings.csv')

found = False

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    for row in csvreader:
        if row[0] == video:
            print(row[0] + " is rate " + row[1] + " with a rating of " + row[5])

        found = True

        break

    if found is False:
        print("Sorry about this, we don't seem to have wthat you are looking for!")