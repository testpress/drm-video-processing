import base64
import json
from generate_signature import generate_signature
from get_encoded_content_data import get_encoded_content_data

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

def get_license_url():
    config_data = read_config()
    if config_data:
        widevine_aes_key = config_data.get("widevine_aes_key", "")
        widevine_iv = config_data.get("widevine_iv", "")
        org_code = config_data.get("org_code", "")
        
        encoded_content_data = get_encoded_content_data()
        signature = generate_signature(encoded_content_data, widevine_aes_key, widevine_iv)

        data = {
            "content_data": encoded_content_data,
            "signature": signature
        }
        data_str = json.dumps(data, separators=(',', ':'))
        encoded_data = base64.urlsafe_b64encode(data_str.encode()).decode()

        print("Encoded Data:", encoded_data)
        LICENSE_URL = f"https://license.tpstreams.com/api/v1/{org_code}/drm_license/?data={encoded_data}"
        print("License URL:", LICENSE_URL)



if __name__ == "__main__":
    get_license_url()
