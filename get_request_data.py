import json
import base64


def read_config():
    try:
        with open('config.json', 'r') as config_file:
            config_data = json.load(config_file)
            return config_data
    except FileNotFoundError:
        print("Error: config.json not found.")
        return None
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in config.json.")
        return None
    
def get_request_data():
    config_data = read_config()
    content_id = config_data.get("content_id", "")
    data = json.dumps({"content_id": content_id}, separators=(',', ':'))
    result = base64.urlsafe_b64encode(data.encode())
    print("request : ", result)
    return result


if __name__ == "__main__":
    request_data = get_request_data()