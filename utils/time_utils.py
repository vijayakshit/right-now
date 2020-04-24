#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
import time


def unicode_to_ts(time_in_unicode):
	return datetime.datetime.strptime(time_in_unicode, '%Y-%m-%d %H:%M:%S')


def get_current_stamps():
	epoch_stamp = time.time()
	timestamp = datetime.datetime.fromtimestamp(epoch_stamp).strftime('%Y-%m-%d %H:%M:%S')
	date_stamp = datetime.datetime.fromtimestamp(epoch_stamp).strftime('%Y-%m-%d')
	return epoch_stamp, timestamp, date_stamp
