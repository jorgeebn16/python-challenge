import os
import csv

cereal_csv = os.path.join("Resources", "cereal.csv")

with open(cereal_csv, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        print(row)

        # Convert row to float and compare to grams of fiber
        if float(row[7]) >= 5:
            print(row)


