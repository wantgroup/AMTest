#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
class DosCmd:
	"封装在控制台执行命令的方法"
	def excute_cmd_result(self,command):
		'''
		执行命令返回结果
		:param command: shell命令
		:return: 在控制台执行的结果
		'''
		result_list = []
		result = os.popen(command).readlines()
		for i in result:
			if i =='\n':
				continue
			result_list.append(i.strip('\n'))
		return result_list

	def excute_cmd(self,command):
		'''
		执行控制台命令
		:param command: shell命令
		:return: null
		'''
		os.system(command)

if __name__ == '__main__':
	dos = DosCmd()
	print(dos.excute_cmd_result('adb devices'))