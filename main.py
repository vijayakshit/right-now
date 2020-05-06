#!/usr/bin/python
# -*- coding: utf-8 -*-

import os.path
import sys

from utils.file_utils import load_yaml_file_as_dict, create_file_if_doesnt_exist
from utils.right_now import add_a_stamp, undo_last_stamp, print_all_stamps, print_all_durations_for_a_date, \
	get_exact_db_path_for_date
from utils.time_utils import get_current_stamps

config_yaml_path = str(os.path.join(os.path.dirname(__file__), './config/config.yml'))
json_db_directory_path = str(os.path.join(os.path.dirname(__file__), 'storage/'))

CONFIG = load_yaml_file_as_dict(config_yaml_path)

if __name__ == '__main__':
	(epoch, time_stamp, date_stamp) = get_current_stamps()
	db_path_for_today = get_exact_db_path_for_date(json_db_directory_path, date_stamp)

	create_file_if_doesnt_exist(db_path_for_today)

	PTS_command = sys.argv[1]
	if PTS_command == 'add':
		add_a_stamp(db_path_for_today)
	elif PTS_command == 'undo':
		undo_last_stamp(db_path_for_today)
	elif PTS_command == 'show':
		print_all_stamps(db_path_for_today)
	elif PTS_command == 'report':
		print_all_durations_for_a_date(json_db_directory_path)
	else:
		print(
			'Invalid Command: Try one amongst 1.rnw add <TaskName> (shortened to rnw <Task>), undo, show or report')


