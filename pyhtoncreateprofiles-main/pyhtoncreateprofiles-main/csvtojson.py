import csv
import json

def csv_to_json(csv_file, json_file):
    # Open the CSV file and read its contents
    with open(csv_file, 'r') as csvfile:
        # Parse the CSV file
        csvreader = csv.DictReader(csvfile)
        
        # Convert CSV data to a list of dictionaries
        data = []
        for row in csvreader:
            data.append(row)
    
    # Write the JSON data to a file
    with open(json_file, 'w') as jsonfile:
        json.dump(data, jsonfile, indent=4)

# Example usage
csv_to_json('profiles1.csv', 'nydata.json')