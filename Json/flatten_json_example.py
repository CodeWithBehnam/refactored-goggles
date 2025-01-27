from flatten_json import flatten_json
import json

# Example usage:

# JSON string provided
json_data = '''
{
    "value": [
        {
            "id": "cfafbeb1-8037-4d0c-896e-a46fb27ff229",
            "name": "SalesMarketing",
            "kind": "Dataset",
            "startTime": "2017-06-13T09:25:43.153Z",
            "endTime": "2017-06-19T11:22:32.445Z",
            "refreshCount": 22,
            "refreshFailures": 0,
            "averageDuration": 289.3814,
            "medianDuration": 268.6245,
            "refreshesPerDay": 11,
            "lastRefresh": {
                "refreshType": "ViaApi",
                "startTime": "2017-06-13T09:25:43.153Z",
                "endTime": "2017-06-13T09:31:43.153Z",
                "status": "Completed",
                "requestId": "9399bb89-25d1-44f8-8576-136d7e9014b1"
            },
            "refreshSchedule": {
                "days": ["Sunday", "Friday", "Saturday"],
                "times": ["05:00", "11:30", "17:30", "23:00"],
                "enabled": true,
                "localTimeZoneId": "UTC",
                "notifyOption": "MailOnFailure"
            },
            "configuredBy": ["john@contoso.com"],
            "capacity": {
                "id": "0f084df7-c13d-451b-af5f-ed0c466403b2",
                "displayName": "MyCapacity",
                "sku": "A1"
            },
            "group": {
                "id": "cfafbeb1-8037-4d0c-896e-a46fb27ff229",
                "name": "SalesMarketing"
            }
        }
    ]
}
'''

# Parse JSON
data = json.loads(json_data)

# Since 'value' is a list, we'll flatten each dictionary in the list
flattened_data = []
for item in data['value']:
    flattened_item = flatten_json(item)
    flattened_data.append(flattened_item)

# Convert the list of flattened dictionaries back to a single dictionary if needed
# Here, we keep it as a list since you might want to process each item individually or keep the structure

import pandas as pd
df = pd.DataFrame(flattened_data)

# Display the DataFrame (you won't see this output, but it's here for reference)
#print(df.to_string())

df.head() 