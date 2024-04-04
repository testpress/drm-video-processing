import base64
import json

import requests
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.parsers import BaseParser
from rest_framework.views import APIView


class OctetStreamParser(BaseParser):
    charset = None
    format = None
    media_type = "application/octet-stream"
    render_style = "binary"

    def parse(self, stream, media_type=None, parser_context=None):
        return stream.read()


    
class DRMProxyView(APIView):
    parser_classes = [OctetStreamParser]

    def post(self, request, *args, **kwargs):
        config_data = self.read_config()
        body = {
            "player_payload": base64.b64encode(self.request.data).decode('utf-8'),
            "widevine": {
                "content_key_specs": [
                    {'track_type': 'SD', 'security_level': 1, 'required_output_protection': {'hdcp': 'HDCP_V1'}},
                    {'track_type': 'HD', 'security_level': 1, 'required_output_protection': {'hdcp': 'HDCP_V1'}},
                    {'track_type': 'UHD1', 'security_level': 1, 'required_output_protection': {'hdcp': 'HDCP_V1'}},
                    {'track_type': 'UHD2', 'security_level': 1, 'required_output_protection': {'hdcp': 'HDCP_V1'}},
                    {'track_type': 'AUDIO', 'security_level': 1, 'required_output_protection': {'hdcp': 'HDCP_V1'}}],
            }
        }
        license_url = config_data.get("license_url","")
        license_response = requests.post(license_url, data=json.dumps(body),
                                         headers={"content-type": "application/json"})
        license_data = license_response.content
        license_response.raise_for_status()

        return HttpResponse(
            license_data,
            status=status.HTTP_200_OK,
            content_type="application/octet-stream",
        )

    def read_config(self):
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

def index_view(request):
    return render(request, template_name="index.html")