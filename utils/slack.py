#!/usr/bin/python
# -*- coding: utf-8 -*-

import json,os
import requests

from utils.file_utils import load_yaml_file_as_dict
from utils.emoji import get_random_emoji

secrets_yaml_path = "/config/secrets.yml"
#TODO: Generalise Paths
secrets_yaml_path = str(os.path.join(os.path.dirname(__file__))).split("/utils")[0] + secrets_yaml_path
SECRETS = load_yaml_file_as_dict(secrets_yaml_path)
BEARER_TOKEN = SECRETS["slack"]["bearer_token"]


def publish_status_to_slack(message):

	emoji, a, b = get_random_emoji()
	url = 'https://api.slack.com/api/users.profile.set'
	headers = {'Content-Type': 'application/json; charset=utf-8', 'Authorization': 'Bearer ' + BEARER_TOKEN}
	body = {'profile': {'status_text': message + " " +str(emoji), 'status_emoji' : ":snow_capped_mountain:",
	                    'status_expiration': 0}}
	if len(BEARER_TOKEN) > 0 :
		requests.post(url, data=json.dumps(body), headers=headers)
	