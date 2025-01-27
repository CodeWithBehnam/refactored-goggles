# Import json module for JSON parsing
import json
# Import pandas for DataFrame operations
import pandas as pd

# Main function to flatten JSON and convert to DataFrame
def flatten_json_with_list_to_columns(json_data):
    """
    Flattens a nested JSON object and converts it to a pandas DataFrame.
    this function parse list values as separate columns.
    Args:
        json_data: JSON string to process
        
    Returns:
        pandas.DataFrame: DataFrame containing flattened JSON data
    """
    # Helper function to flatten nested dictionaries
    def flatten_dict(y):
        # Initialize empty output dictionary
        out = {}
        
        # Inner recursive function to do the flattening
        def flatten(x, name=''):
            # If value is a dictionary, recursively flatten it
            if type(x) is dict:
                # Iterate through dictionary items
                for a in x:
                    # Recursively call flatten with updated name
                    flatten(x[a], name + a + '_')
            # If value is a list, process each element
            elif type(x) is list:
                # Initialize counter
                i = 0
                # Iterate through list elements
                for a in x:
                    # Recursively flatten each element with index in name
                    flatten(a, name + str(i) + '_')
                    # Increment counter
                    i += 1
            # For primitive values, add directly to output
            else:
                # Store value with flattened key name
                out[name[:-1]] = x

        # Call inner flatten function
        flatten(y)
        # Return flattened dictionary
        return out

    # Parse JSON string into Python object
    data = json.loads(json_data)
    
    # Process each dictionary in the 'value' list using list comprehension
    flattened_data = [flatten_dict(item) for item in data['value']]
    
    # Convert flattened data to DataFrame and return
    return pd.DataFrame(flattened_data)

# Main function to flatten and process JSON data
def flatten_json_with_list_to_string(json_data):
    """
    Flattens a nested JSON object and converts it to a pandas DataFrame.
    This function parts list values as a comma separated string.
    Args:
        json_data: JSON string to process
        
    Returns:
        pandas.DataFrame: DataFrame containing flattened JSON data
    """
    # Helper function to flatten nested dictionaries
    def flatten_dict(y):
        # Initialize empty output dictionary
        out = {}
        
        # Inner recursive function to do the flattening
        def flatten(x, name=''):
            # If value is a dictionary, recursively flatten it
            if isinstance(x, dict):
                # Iterate through dictionary items
                for a in x:
                    # Recursively call flatten with updated name
                    flatten(x[a], f'{name}{a}_')
            # If value is a list, join elements with commas
            elif isinstance(x, list):
                # Convert list to comma-separated string
                out[name[:-1]] = ', '.join(map(str, x))
            # For primitive values, add directly to output
            else:
                # Store value with flattened key name
                out[name[:-1]] = x

        # Call inner flatten function
        flatten(y)
        # Return flattened dictionary
        return out

    # Parse JSON and flatten data
    data = json.loads(json_data)
    # Process each item in the 'value' list
    flattened_data = [flatten_dict(item) for item in data['value']]
    
# Execute only if run as a script
if __name__ == "__main__":
    # Print description of what the script does
    print('Flattens a nested JSON object and converts it to a pandas DataFrame.')


