
import fnmatch
import pysftp
import stat
import time
import os

#==============================================================================

Hostname = "163.13.137.223" #IP位置
Username = "ding" #使用者名稱
Password = "1211" #使用者密碼

sleep_time = 10 #檢查間隔時間，單位為秒(s)

remote_Path = '/home/ding/test' #下載位置，必須為資料夾
local_Path  = 'C:/Users/user/OneDrive/桌面/ph7' #存檔位置，必須為資料夾

#==============================================================================

def download(remote, local):
	
	for name in sftp.listdir_attr(remote):
		if stat.S_ISDIR(name.st_mode):
			if not os.path.exists(local+"/"+name.filename):
				os.mkdir(local+"/"+name.filename)

			download(remote+"/"+name.filename, local+"/"+name.filename)
			
		else:
			if not os.path.exists(local+"/"+name.filename):
				print("Download\t", name.filename, "\t", name.st_size, "KB")
				sftp.get(remote+"/"+name.filename, local+"/"+name.filename)

#------------------------------------------------------------------------------

def checkpath(path):
    
    if path[-1] != "/":
        path = path + str("/")
        
    return path

#==============================================================================

remote_Path = checkpath(remote_Path)
local_Path  = checkpath(local_Path)

if not os.path.exists(local_Path):
    os.mkdir(local_Path)
    print(local_Path.split("/")[-2],"目錄已建立")

with pysftp.Connection(host = Hostname, username = Username, password = Password) as sftp:

    print("Connection succesfully established ... ")
    
    while True:

    	print(time.ctime())

    	download(remote_Path, local_Path)

    	time.sleep(sleep_time)

print("Disconnect")