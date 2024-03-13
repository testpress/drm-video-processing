import base64
import binascii
import hashlib
import json

from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad

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

def generate_signature(data, key, iv):
    hash_value = hashlib.sha1(base64.b64encode(data.encode())).digest()
    cipher = AES.new(
        binascii.unhexlify(key),
        AES.MODE_CBC,
        binascii.unhexlify(iv),
    )
    padded_hash = pad(hash_value, AES.block_size, style="pkcs7")
    signature = cipher.encrypt(padded_hash)
    return base64.b64encode(signature).decode()

if __name__ == "__main__":
    config_data = read_config()

    if config_data:
        key = config_data.get("widevine_aes_key", "")
        iv = config_data.get("widevine_iv", "")
        
        data = {
            "content_id": config_data.get("content_id", "")
        }
        data_str = json.dumps(data, separators=(',', ':'))
        
        signature = generate_signature(data_str, key, iv)
        print("Signature:", signature)

