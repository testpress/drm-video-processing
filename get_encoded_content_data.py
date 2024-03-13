import json
import base64

def get_encoded_content_data():
    try:
        with open('config.json', 'r') as config_file:
            config_data = json.load(config_file)
            content_id = config_data.get('content_id', '')

            data = {
                "content_id": content_id
            }

            data_str = json.dumps(data, separators=(',', ':'))
            encoded_content_data = base64.urlsafe_b64encode(data_str.encode()).decode()

            return encoded_content_data
    except FileNotFoundError:
        print("Error: config.json not found.")
        return None
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in config.json.")
        return None

if __name__ == "__main__":
    encoded_content_data = get_encoded_content_data()

    if encoded_content_data:
        print("content_data :",encoded_content_data)

