#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
import sys
import time

from utils.file_utils import fetch_json_file_as_dict, write_dict_to_json_file
from utils.slack import publish_status_to_slack
from utils.time_utils import unicode_to_ts, get_current_stamps


def add_a_stamp(filepath):
	if len(sys.argv) < 3:
		print('No Event Provided')
		exit()

	work_text = sys.argv[2]
	(epochstamp, timestamp, datestamp) = get_current_stamps()
	if len(sys.argv) == 5:
		if sys.argv[3] == 'm':
			minus = sys.argv[4]
			timestamp = edit_time(minus)

	work_data = fetch_json_file_as_dict(filepath)
	work_data = add_event_to_dict(work_data, timestamp, work_text)
	write_dict_to_json_file(filepath, work_data)
	publish_status_to_slack(work_text)


def undo_last_stamp(filepath):
	work_data = fetch_json_file_as_dict(filepath)
	work_data = work_data[:-1]
	write_dict_to_json_file(filepath, work_data)


def print_all_stamps(filepath):
	for event in fetch_json_file_as_dict(filepath):
		print(event['starttime'], ':', event['eventname'])


def edit_time(minusVal):
	epoch = time.time()
	dt = datetime
	dt_dt = dt.datetime

	ts = dt_dt.fromtimestamp(epoch).strftime('%Y-%m-%d %H:%M:%S')
	new_timestamp = dt_dt.strptime(ts, '%Y-%m-%d %H:%M:%S') - dt.timedelta(minutes=int(minusVal))
	return str(new_timestamp)


def print_all_durations_for_a_date(db_directory):
	(epoch, ts, ds) = get_current_stamps()
	date_to_check = ds

	if len(sys.argv) > 2:
		date_to_check = sys.argv[2]

	filepath = get_exact_db_path_for_date(db_directory, date_to_check)

	try:
		events = fetch_json_file_as_dict(filepath)
	except:
		print('Sorry, It seems you have no records for ', date_to_check)
		exit()

	last_event = {}
	print('Report For', date_to_check)
	for event in events:
		if last_event == {}:
			last_event = event
			continue
		time_difference = unicode_to_ts(event['starttime']) - unicode_to_ts(last_event['starttime'])

		print(str(last_event['eventname']), ':', str(time_difference))
		last_event = event


def get_exact_db_path_for_date(db_directory, date_stamp):
	return db_directory + str(date_stamp) + '.json'


def add_event_to_dict(day_events, timestamp, work_text):
	day_events.append({'starttime': timestamp, 'eventname': work_text})
	return day_events
