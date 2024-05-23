import csv

def find_repeated_data(filename):
    repeated_data = []
    encountered_values = set()

    with open(filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        # Skip the header row
        next(csv_reader)

        # Iterate over each row in the CSV file
        for row in csv_reader:
            name = row[0]
            sample_id = row[2]
            identifier = (name, sample_id)

            # Check if the identifier has been encountered before
            if identifier in encountered_values:
                repeated_data.append(identifier)
            else:
                encountered_values.add(identifier)

    return repeated_data

# Usage example
file_path = 'mineral_data.csv'
repeated_values = find_repeated_data(file_path)

for entry in repeated_values:
    print(entry)
#print("Repeated Data (name, sampleID):", repeated_values)
