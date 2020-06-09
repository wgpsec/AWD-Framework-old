import SSH_Config
import SSH_Action
import SFTP_Action


def Show_Server_List(Site_Nums):                                             #展示服务器列表
	Server_list = open("SSH_Config.txt","r")
	next(Server_list)
	print("\n\n")
	for i in range(Site_Nums):
		Config_list = eval(Server_list.readline()[11:])                      #处理字符串，读取为dict
		print( "Server[%d]  ==> "%i + "IP : " + Config_list[0] + "   Username : "+ Config_list[2] + "   Password : " + Config_list[3])
	print("\n")



def Get_Single_Shell(Site_Nums):                                             #进入单个Linux交互环境
	Show_Server_List(Site_Nums)
	try:
		Server_Number = input("Input Which Server you want  : ") 
		if int(Server_Number) > Site_Nums:
			print("Wrong Choice")
			return "Wrong"
		SSH_Action.UseShell(Server_Number)
	except:
		pass
	


def Send_to_All(Site_Nums):                                                  #向所有服务器发送指令
	Command = input("Command:")
	for i in range(Site_Nums):
		Command_Result = SSH_Action.Send_Command(i,Command)
		print("Server [%d] With Result:\n\n"%i,Command_Result,"\n\n")


def Download_Code(Site_Nums):                                           #下载所有的源码和数据文件
	Show_Server_List(Site_Nums)
	try:
		Server_Number = int(input("Input Which Server you want  : "))
		if int(Server_Number) > Site_Nums:
			print("Wrong Choice")
			return "Wrong"
		SFTP_Action.Download_Code(Server_Number)
	except:
	 	pass


def Upload_files(Site_Nums):                                                 #上传文件
	Show_Server_List(Site_Nums)
	try:
		Server_Number = int(input("Input Which Server you want  : "))
		if int(Server_Number) > Site_Nums:
			print("Wrong Choice")
			return "Wrong" 
		FileName = input("Input The FileName in /Uploadfils : ")
		Default_WWW_Path = "/var/www/html/"
		Remote_Path = input("Input The RemotePath(Default:[/var/www/html/]) : ")
		if Remote_Path == "":
			Remote_Path = Default_WWW_Path
		SFTP_Action.File_Upload(Server_Number,FileName,Remote_Path)
	except:
		pass

def Download_log(Site_Nums):                                                 #下载日志
	Show_Server_List(Site_Nums)
	try:
		Server_Number = input("Input Which Server you want  : ") 
		if int(Server_Number) > Site_Nums:
			print("Wrong Choice")
			return "Wrong"
		SFTP_Action.Get_Logs(Server_Number)
	except:
		pass
		