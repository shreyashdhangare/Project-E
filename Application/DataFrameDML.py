def parse_dml(dml_content):
    """
    Parse a DML file to extract field names, data types, and delimiters without using `re`.
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

# Example DML content
dml_content = """
record
  string(",") fruit_name;
  string(",") fruitcolour;
  decimal(",") fruitediblity;
  decimal("',") friuttasteblity;
  date("YYYY-MM-DD") fruitseasonstartdate;
end;
"""

# Parse the DML file
fields = parse_dml(dml_content)
print("Parsed Fields:", fields)