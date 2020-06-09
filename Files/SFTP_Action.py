import sys
import os
import paramiko
import linecache
import SSH_Action
import re


def Get_Connect_Config(Server_Number):										# 因为是被自身的函数调用，所以路径要加../返回上级目录
	Config_Path = "../SSH_Config.txt"
	Read_Config = eval(linecache.getline(Config_Path, int(Server_Number) + 2)[11:])
	hostname = Read_Config[0]
	port = int(Read_Config[1])
	username = Read_Config[2]
	password = Read_Config[3]
	return hostname,port,username,password  

def Code_Zip(Server_Number,WWW_Path):														#打包源码
	Command = "tar -zcvf /tmp/Wgpsecbak.tar.gz " + WWW_Path + "/*"
	SSH_Action.Send_Command(Server_Number,Command)

def Get_FileName(Remote_File_Path):
	FileName = str(re.findall(r'[^\\/:*?"<>|\r\n]+$',Remote_File_Path)).strip("[',']")
	return FileName


def File_Upload(Server_Number,FileName,Remote_File_Path):					#上传文件
	try:
		SFTP_Config = Get_Connect_Config(Server_Number)
		SFTP_Connect = paramiko.Transport((SFTP_Config[0],SFTP_Config[1]))
		SFTP_Connect.connect(username = SFTP_Config[2], password = SFTP_Config[3])
	except:
		print("Server Connect Error !")
	
	try:
		SFTP_Get = paramiko.SFTPClient.from_transport(SFTP_Connect)
		SFTP_Get.put('Uploadfiles\\' + FileName,Remote_File_Path + FileName)
		SFTP_Connect.close()
		print("All the Files Uplaod in " + Remote_File_Path + " Successful")
	except:
		print("Upload Error,Maybe u should Check the File exist or limits")


def File_Download(Server_Number,Remote_File_Path):						
	try:
		SFTP_Config = Get_Connect_Config(Server_Number)
		SFTP_Connect = paramiko.Transport((SFTP_Config[0],SFTP_Config[1]))
		SFTP_Connect.connect(username = SFTP_Config[2],password = SFTP_Config[3])
	except:
		print("Server Connect Error !")
	
	try:
		SFTP_Get = paramiko.SFTPClient.from_transport(SFTP_Connect)
		SFTP_Get.get(Remote_File_Path,"Downloads\\"+ str(Server_Number) + "\\" + Get_FileName(Remote_File_Path))
		SFTP_Connect.close()
		print("All the Files Download in /Downloads Successful")
	except:
		print("Download Error,Maybe u should Check the limits")


def Download_Code(Server_Number):											#下载代码
	Default_WWW_Path = "/var/www/html/"
	Remote_File_Path = input("Please Input the WWW Path(Default:[/var/www/html/])")
	if Remote_File_Path == "":
		Remote_File_Path = Default_WWW_Path
	Code_Zip(Server_Number,Remote_File_Path)
	File_Download(Server_Number,"/tmp/Wgpsecbak.tar.gz")


def Get_Logs(Server_Number):												#下载备份
	Default_Log_Path =  "/var/log/apache2/access.log"
	Remote_File_Path = input("Please Input the log Path(Default-Apache:[/var/log/apache2/access.log])")
	if Remote_File_Path == "":
		Remote_File_Path = Default_Log_Path
	File_Download(Server_Number,Remote_File_Path)

