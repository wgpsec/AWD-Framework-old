import sys
import os
import paramiko
import threading 
import linecache
import threading

def UseShell(Server_Number):                                           # 连接SSH
	Config_Path = "SSH_Config.txt"
	Read_Config = eval(linecache.getline(Config_Path , int(Server_Number) + 2)[11:])
	hostname = Read_Config[0]                                          #配置SSH连接信息
	port = int(Read_Config[1])
	username = Read_Config[2]
	password = Read_Config[3]
	try:
		client = paramiko.SSHClient()                                  # 绑定实例
		client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		client.connect(hostname, port, username, password, timeout = 10)
		while True:
			Command_Input = input(username + "@" + hostname + ": ")
			if Command_Input == "exit":
				break
			stdin, stdout, stderr = client.exec_command(Command_Input) # 执行bash命令
			result = stdout.read()
			error = stderr.read()
			if not error:
		   		print (result.decode('utf-8'))
			else:
		   		print (error.decode('utf-8'))
	except:
		print("Connect Closed or Something Error !")


def Send_Command(Server_Number,Command):                               #发送单条指令
	Config_Path = "../SSH_Config.txt"
	Read_Config = eval(linecache.getline(Config_Path, int(Server_Number) + 2)[11:])
	hostname = Read_Config[0]                                          #配置SSH连接信息
	port = int(Read_Config[1])
	username = Read_Config[2]
	password = Read_Config[3]
	try:
		client = paramiko.SSHClient()                                  # 新建实例
		client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		client.connect(hostname, port, username, password, timeout = 10)
		stdin, stdout, stderr = client.exec_command(Command)    	   # 执行bash命令
		result = stdout.read()
		error = stderr.read()
		if not error:
		   	return result.decode('utf-8')
		else:
		   	return error.decode('utf-8')
	except:
		return "Connect Server Error ! "
