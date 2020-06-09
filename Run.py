import os
import sys
sys.path.append(r'Files/')
import Print_text        #/Files/Print_text.py
import SSH_Config        #/File/SSH_Config.py
import Defence_Action    #/Files/Defence_Action.py
import paramiko          #SSH相关库 




def Set_Config():
	Site_Nums = int(input("Number of sites:"))   #需要防护加固的服务器总数
	SSH_Config.SSH_Nums_check(Site_Nums)         #检查输入0的问题
	SSH_Config.SSH_Config_Input(Site_Nums)       #配置所有SSH的IP Port 和Pass
	try:
		for i in range(Site_Nums):
			os.system("md Downloads\\" + str(i))
	except Exception as e:
		for i in range(Site_Nums):
			os.system("mkdir Downloads/" +str(i))

	
if __name__ == '__main__': 
	try:
		Print_text.Print_Welcome_Message()           #输出欢迎信息
		#if SSH_Config.Check_Config_Exist():         #检查配置文件是否存在
		choice = input("Start New Game ? [y/n]:")
		if choice == "y":
			Set_Config()
		Print_text.Usage()                           #输出Usage
		ConfigFile = open("SSH_Config.txt","r")
		Site_Nums = int(ConfigFile.readline())
		while True:                                  #内部交互
			Command_Choose = input("Command ==>")
			if Command_Choose == "0" or Command_Choose == "help":
				Print_text.Usage()
			elif Command_Choose == "1" or Command_Choose == "shell":
				Defence_Action.Get_Single_Shell(Site_Nums)
			elif Command_Choose == "2" or Command_Choose == "send":
				Defence_Action.Send_to_All(Site_Nums)
			elif Command_Choose == "3" or Command_Choose == "down":
				Defence_Action.Download_Code(Site_Nums)
			elif Command_Choose == "4" or Command_Choose == "upload":
					Defence_Action.Upload_files(Site_Nums)
			elif Command_Choose == "5" or Command_Choose == "log":
					Defence_Action.Download_log(Site_Nums)
			elif Command_Choose == "6" or Command_Choose == "script":
				Print_text.Scriptlist()
			elif Command_Choose == "exit":
				break
			else:
				print("Wrong type!")
	except:
		print("\nExit!")




