import re

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