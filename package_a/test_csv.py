from sys import argv

import csv

input_file = argv[1]
output_file = input_file.replace('.csv', '_stripped.csv')

deleted_cols = ['Year', 'Artist']


with open(input_file, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter='|')

    with open(output_file, "w", newline='') as result:

        writer = csv.writer(result, delimiter='|')

        for row in reader:
            print(row)
        
            writer.writerow([row[1],row[2]]) # write the row to the new file
