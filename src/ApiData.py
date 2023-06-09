import requests

def get_channel_data(channel_id, read_api_key, num_results=1):
    base_url = f'https://api.thingspeak.com/channels/2146750/feeds.json?api_key=PNOQX59AGZZYNI98&results=2'
    params = {
        'api_key': read_api_key,
        'results': num_results
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if 'feeds' in data:
        return data['feeds']
    else:
        return None

# Replace with your ThingSpeak Channel ID and Read API Key
channel_id = 2146750
read_api_key = 'PNOQX59AGZZYNI98'
num_results = 1

channel_data = get_channel_data(channel_id, read_api_key, num_results)

if channel_data:
    for entry in channel_data:
        print(f"Entry ID: {entry['entry_id']}")
        print(f"Field 1 Value: {entry['field1']}")
        print(f"Field 2 Value: {entry['field2']}")
        print(f"Field 3 Value: {entry['field3']}")
        print(f"Field 4 Value: {entry['field4']}")
        print(f"Field 5 Value: {entry['field5']}")
        print(f"Field 6 Value: {entry['field6']}")
        print(f"Field 7 Value: {entry['field7']}")
        print(f"Timestamp: {entry['created_at']}")
        print(type(entry['field1']))
        print('---')
else:
    print("Error fetching channel data.")
