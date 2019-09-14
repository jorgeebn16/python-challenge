import os

# Module for reading CSV files
import csv

title = []
price = []
subscribers = []
reviews = []
review_percent = []
lenght = []

csvpath = os.path.join('..', 'LearnPython', 'web_starter.csv')

found = False

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')