import pandas as pd
from datetime import datetime

# Function to parse the DML file manually
def parse_dml(dml_content):
    """
    Parse the DML file to extract field names, data types, and delimiters.
    """
    fields = []
    lines = dml_content.splitlines()
    for line in lines:
        line = line.strip()
        if line.startswith("string") or line.startswith("decimal") or line.startswith("date"):
            # Extract the data type
            data_type = line.split("(")[0].strip()
            # Extract the delimiter
            delimiter = line.split('"')[1] if '"' in line else line.split("'")[1]
            # Extract the field name
            field_name = line.split()[-1].strip(";")
            fields.append({
                'name': field_name,
                'type': data_type,
                'delimiter': delimiter
            })
    return fields

# Function to convert data types based on the DML description
def convert_data_types(row, fields):
    """
    Convert the data types of a row based on the DML description.
    """
    converted_row = {}
    for i, field in enumerate(fields):
        value = row[i]
        if field['type'] == 'string':
            converted_row[field['name'] = value
        elif field['type'] == 'decimal':
            converted_row[field['name'] = float(value)
        elif field['type'] == 'date':
            converted_row[field['name'] = datetime.strptime(value, '%Y-%m-%d')
    return converted_row

# Read the DML file
with open('schema.dml', 'r') as dml_file:
    dml_content = dml_file.read()

# Parse the DML file
fields = parse_dml(dml_content)

# Read the .dat file into a list of rows
data = []
with open('data.dat', 'r') as dat_file:
    for line in dat_file:
        row = line.strip().split(',')
        data.append(row)

# Convert data types and create a list of dictionaries
converted_data = []
for row in data:
    converted_data.append(convert_data_types(row, fields))

# Convert the list of dictionaries into a DataFrame
df = pd.DataFrame(converted_data)

# Print the DataFrame
print("DataFrame:")
print(df)

# Print the data types of the DataFrame
print("\nData Types:")
print(df.dtypes)