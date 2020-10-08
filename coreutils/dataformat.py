#!/usr/bin/python3

"""
This is Class for ycn agent libvirt Guest Monitoring

Author : Dhanasekara Pandian
Email  : sekar5in@gmail.com
CopyRights : All Rights are Reserved
"""

# Global Import
import json


def dict_to_json(data):
    json_data = json.dumps(data, indent=4)
    return json_data
