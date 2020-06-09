import sys
import os
import paramiko
import linecache

def Check_Config_Exist():                                              #检查配置文件SSH_Config.txt是否存在
	state = os.path.exists("SSH_Config.txt")
	return state


def SSH_Nums_check(Site_Nums):
	if Site_Nums == 0:
		print("Are u Kidding me?")                                     #数量为0退出程序
		sys.exit(0)


def SSH_Config_Input(Site_Nums):                                       #写SSH配置文件
	Config_Path = "SSH_Config.txt"
	Save_SSH = open(Config_Path,"w")
	Save_SSH.write(str(Site_Nums) + "\n")
	for i in range(Site_Nums):
		SSH_Config = {}                               
		SSH_Config[0] = input("Server %d IP:====>"%i)                  # 0:IP 
		SSH_Config[1] = input("Server %d Port:==>"%i)                  # 1:Port
		SSH_Config[2] = input("Server %d User:==>"%i)                  # 2:User
		SSH_Config[3] = input("Server %d Pass:==>"%i)                  # 3:Pass
		Save_SSH.write("Server %d : "%i +str(SSH_Config) + "\n")
	print("\nAll The Config Saved in SSH_Config.txt Successful")
	Save_SSH.close()






