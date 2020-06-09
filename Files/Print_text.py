import os

def Usage():
	print("Commands : ")                                              #输出帮助信息
	print("+----------------------------------------------------+")
	print("|Num|Command |    Describe                           |")
	print("+----------------------------------------------------+")
	print("|0. | help   |    Get Usage(This Page)               |")
	print("|1. | shell  |    Get into the Single Shell          |")
	print("|2. | send   |    Send a Command to All servers      |")
	print("|3. | down   |    Download the Source code           |")
	print("|4. | upload |    Upload a file to the website       |")
	print("|5. | log    |    Download the log of WebServer      |")
	print("|6. | script |    Get the Attack Script list         |")
	print("+----------------------------------------------------+")
	print("You Can type Num or Command to enter the Function which you want,Input 'exit' to break.\n")


def Print_Welcome_Message():                                           #输出欢迎信息
	print("+---------------------------------------+")
	print("|             AWD Framework             |")
	print("+---------------------------------------+")
	print("|            Made By AdianGg            |")
	print("|   AdianGg's Blog:www.e-wolf.top       |")
	print("|         WgpSec:www.wgpsec.org         |")
	print("|               Have Fun                |")
	print("+---------------------------------------+")


def Scriptlist():                                                      #输出Script目录下所有文件列表             
	print("All The Scipts from Internet!")
	for root,dirs,files in os.walk(r"Scripts/"):
		for file in files:
			print(os.path.join(root,file))
