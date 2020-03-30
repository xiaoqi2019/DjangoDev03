# -*- coding: utf-8 -*-
from utils.format_time import format_time

def modify_output(datas):
	"""
	1:对时间格式化
	:param datas:
	:return:
	"""
	datas_list = []
	for item in datas:
		# if item['create_time']:
		item['create_time'] = format_time(item['create_time'])
		# if item['update_time']:
		item['update_time'] = format_time(item['update_time'])
		datas_list.append(item)
	return datas_list
