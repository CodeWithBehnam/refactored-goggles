import json

def flatten_json(y):
    """
    Flattens a nested JSON object into a single level dictionary, handling lists by joining elements.
    
    Args:
        y: A JSON object (dict or list) to flatten
        
    Returns:
        dict: A flattened dictionary where:
            - Nested dictionary keys are joined with underscores
            - List values are converted to comma-separated strings
        
    Example:
        Input: {
            "a": 1,
            "b": {
                "c": 2,
                "d": ["x", "y", "z"]
            }
        }
        Output: {
            "a": 1,
            "b_c": 2,
            "b_d": "x, y, z"
        }
    """
    out = {}

    def flatten(x, name=''):
        if isinstance(x, dict):
            for a in x:
                flatten(x[a], f'{name}{a}_')
        elif isinstance(x, list):
            # Concatenate list items into a single string
            out[name[:-1]] = ', '.join(map(str, x))
        else:
            out[name[:-1]] = x

    flatten(y)
    return out

if __name__ == "__main__":
    print(flatten_json(json.loads(json_data)))
    