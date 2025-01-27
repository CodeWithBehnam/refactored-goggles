# JSON Flattening Utilities

A Python utility library for flattening nested JSON structures into pandas DataFrames.

## Features

- Two main flattening approaches:
  - `flatten_json_with_list_to_string`: Converts lists to comma-separated strings
  - `flatten_json_with_list_to_columns`: Parses lists into separate columns
- Handles deeply nested JSON structures
- Preserves data types
- Built on pandas for efficient data manipulation

## Getting Started

1. Clone the repository
2. Ensure you have the required dependencies:
   - pandas
   - json (built-in)
3. Import the desired function:
   ```python
   from json_helpers import flatten_json_with_list_to_string
   # or
   from json_helpers import flatten_json_with_list_to_columns
   ```
