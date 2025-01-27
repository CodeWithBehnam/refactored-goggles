import json

def flatten_json(y):
    """
    Flattens a nested JSON object into a single level dictionary.
    
    Args:
        y: A JSON object (dict or list) to flatten
        
    Returns:
        dict: A flattened dictionary where nested keys are joined with underscores
        
    Example:
        Input: {
            "a": 1,
            "b": {
                "c": 2,
                "d": {
                    "e": 3
                }
            }
        }
        Output: {
            "a": 1,
            "b_c": 2, 
            "b_d_e": 3
        }
    """
    out = {}
    
    def flatten(x, name=''):
        """
        Recursive helper function to flatten nested structures
        
        Args:
            x: Current object being processed
            name: Accumulated key name path
        """
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(y)
    return out

if __name__ == "__main__":
    print(flatten_json(json.loads(json_data)))
    