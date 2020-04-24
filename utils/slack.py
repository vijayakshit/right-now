#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import requests

from utils.file_utils import load_yaml_file_as_dict

secrets_yaml_path = "./config/secrets.yml"
SECRETS = load_yaml_file_as_dict(secrets_yaml_path)
BEARER_TOKEN = SECRETS["slack"]["bearer_token"]


def publish_status_to_slack(message):
	url = 'https://api.slack.com/api/users.profile.set'
	headers = {'Content-Type': 'application/json; charset=utf-8', 'Authorization': 'Bearer ' + BEARER_TOKEN}
	body = dict(profile={'status_text': message, 'status_emoji': ':mountain_railway:',
	                     'status_expiration': 0})
	requests.post(url, data=json.dumps(body), headers=headers)
