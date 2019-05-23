import json
import csv
import numpy as np

def csv_to_json(csv_file_path):

    csvfile = open(csv_file_path, 'r')
    jsonfile = open('emails.json', 'w')

    fieldnames = ("file", "message")
    reader = csv.DictReader(csvfile, fieldnames)
    for row in reader:
        json.dump(row, jsonfile)
        jsonfile.write('\n')


