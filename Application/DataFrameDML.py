import re
import pandas as pd

def parse_dml(dml_content):
    """
    Parse a DML file to extract field names, data types, and delimiters.
    """
    fields = []
    pattern = re.compile(r'(\w+)\(["\']([^"\']+)["\']\)\s+(\w+);')
    matches = pattern.findall(dml_content)
    for data_type, delimiter, field_name in matches:
        fields.append({
            'name': field_name,
            'type': data_type,
            'delimiter': delimiter
        })
    return fields

# Example DML content
dml_content = """
record
  decimal(",") field1;
  string(",") field2;
  date("YYYY-MM-DD") field3;
end;
"""

# Parse the DML file
fields = parse_dml(dml_content)

# Path to the .dat file
dat_file_path = 'data.dat'

# Read the .dat file into a DataFrame
df = pd.read_csv(dat_file_path, delimiter=',', header=None)

# Assign column names based on the DML file
column_names = [field['name'] for field in fields]
df.columns = column_names

# Convert columns to appropriate data types
df['field1'] = df['field1'].astype(float)  # Decimal
df['field3'] = pd.to_datetime(df['field3'])  # Date

# Print the DataFrame
print(df)
print(df.dtypes)