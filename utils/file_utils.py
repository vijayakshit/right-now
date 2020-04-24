#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import os.path
import yaml


def load_yaml_file_as_dict(yaml_path):
	with open(yaml_path, "r") as yaml_file:
		data = yaml.load(yaml_file, Loader=yaml.FullLoader)
	return data


def fetch_json_file_as_dict(filepath):
	with open(filepath) as userData:
		data = json.load(userData)
	return data


def write_dict_to_json_file(filepath, dict):
	with open(filepath, 'w+') as outfile:
		json.dump(dict, outfile, indent=4, sort_keys=True)


def create_file_if_doesnt_exist(filepath):
	if not os.path.exists(filepath):
		print('Started Logging Events For Today:')
		write_dict_to_json_file(filepath, [])
