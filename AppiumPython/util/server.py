#coding=utf-8
import sys
sys.path.append('/Users/cloudin/Desktop/project/AMTest/AppiumPython')

from util.dos_cmd import DosCmd
from util.port import Port
import threading
import time
from util.write_user_command import WriteUserCommand
from util.tools import Tools

tool = Tools()
rootPath = tool.getRootPath()

class Server:
	'''
		几个手机创建几个appium用来连接手机使用
	'''
	def __init__(self):
		#执行控制台的命令使用
		self.dos = DosCmd()
		#获取设备devices的集合
		self.device_list = self.get_devices()
		#yaml的操作类
		self.write_file = WriteUserCommand()

	def get_devices(self):
		'''
		#获取设备devices的集合
		'''
		devices_list = []
		#执行adb devices命令来获取 devices list
		result_list = self.dos.excute_cmd_result('adb devices')
		print(result_list)
		#取出devicees存入devices_list中
		if len(result_list)>=2:
			for i in result_list:
				if 'List' in i:
					continue
				devices_info = i.split('\t')
				if devices_info[1] == 'device':
					devices_list.append(devices_info[0])
			return devices_list
		else:
			return None

	def create_port_list(self,start_port):
		'''
		创建可用端口
		'''
		port = Port()
		port_list = []
		port_list = port.create_port_list(start_port,self.device_list)
		return port_list

	def create_command_list(self,i):
		'''
		生成命令
		'''
		#appium -p 4700 -bp 4701 -U 127.0.0.1:21503
		command_list = []
		appium_port_list = self.create_port_list(4700)
		bootstrap_port_list = self.create_port_list(4900)
		device_list = self.device_list
		command = "appium -p "+str(appium_port_list[i])+" -bp "+str(bootstrap_port_list[i])+" -U "+device_list[i]+" --no-reset --session-override --log "+rootPath+"/log/test0"+str(i)+".log"
		#appium -p 4723 -bp 4726 -U 127.0.0.1:62001 --no-reset --session-override --log /log/test01.log
		command_list.append(command)
		self.write_file.write_data(i,device_list[i],str(bootstrap_port_list[i]),str(appium_port_list[i]))

		return command_list

	def start_server(self,i):
		'''
		启动服务
		'''
		self.start_list = self.create_command_list(i)
		print(self.start_list)
		self.dos.excute_cmd(self.start_list[0])

	def kill_server(self):
		# 这里是windows 命令行 linux 使用命令 ps ef | grep node
		server_list = self.dos.excute_cmd_result('tasklist | find "node.exe"')
		if len(server_list)>0:
			self.dos.excute_cmd('taskkill -F -PID node.exe')
	def write_data(self):
		self.write_file.write_data('0','device','dp','port')
	def main(self):
		thread_list = []
		self.kill_server()
		#清除上一次userconfig1.yaml里面的数据
		self.write_file.clear_data()
		#写入dervices到userconfig1.yaml里
		for i in range(len(self.device_list)):
			#有几个drivaer创建几个线程
			appium_start = threading.Thread(target=self.start_server,args=(i,))
			#加入到线程组里面
			thread_list.append(appium_start)
		for j in thread_list:
			#启动线程组
			j.start()

		time.sleep(25)


if __name__ == '__main__':
	server = Server()
	print(server.get_devices());
