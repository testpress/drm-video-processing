import requests
import json
from get_request_data import get_request_data
from generate_signature import generate_signature

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

def get_key_iv_and_uri():
    config_data = read_config()
    org_code = config_data.get("org_code", "")
    content_id = config_data.get("content_id", "")
    data = {"content_id": content_id}
    data = json.dumps(data, separators=(',', ':'))
    key = config_data.get("widevine_aes_key", "")
    iv = config_data.get("widevine_iv", "")
    request_data = {
        "request": get_request_data().decode('utf-8'),
        "signature": str(generate_signature(data, key, iv))
    }
    response = send_post_request(org_code, request_data)
    print("Response:", response.content)

def send_post_request(org_code, request_data):
    url = f"https://app.tpstreams.com/api/v1/{org_code}/fairplay_key/"
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json=request_data, headers=headers)
    return response

if __name__ == "__main__":
    get_key_iv_and_uri()
