import csv
import os

path = os.getcwd()
print (path)
print(os.path.abspath(os.path.join(path, os.pardir)))

def reshape_csv(input_file, output_file, columns=14):
    # Read the data from the input CSV
    with open(input_file, mode='r', newline='') as infile:
        reader = csv.reader(infile)
        #data = [row[0] for row in reader]  # Assume single column
        data = [row[0] if row else '' for row in reader]  # Use an empty string for empty rows
        
    # Create the reshaped data by grouping into rows of 'columns' size
    reshaped_data = [data[i:i + columns] for i in range(0, len(data), columns)]
    
    # Write the reshaped data to the output CSV
    with open(output_file, mode='w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(reshaped_data)

    print(f"Data reshaped into {columns} columns and saved to {output_file}")

input_csv = 'Import.csv'
output_csv = 'Output.csv'

reshape_csv(input_csv, output_csv)
