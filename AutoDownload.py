
import fnmatch
import pysftp
import time
import os

Hostname = "163.13.137.223" #IP位置
Username = "ding" #使用者名稱
Password = "1211" #使用者密碼

get_name = "*" #要下載的檔案名稱

sleep_time = 10 #檢查間隔時間，單位為秒(s)

remote_Path = '/home/ding/test/' #下載位置，必須為資料夾
local_Path = 'C:/Users/user/Desktop/download/' #存檔位置，必須為資料夾

with pysftp.Connection(host = Hostname, username = Username, password = Password) as sftp:

    print("Connection succesfully established ... ")

    while True:

        print(time.ctime())

        newfile_exist = False

        for name in sftp.listdir_attr(remote_Path):
            if fnmatch.fnmatch(name.filename, get_name) and name.filename not in os.listdir(local_Path):
                print("Download\t", name.filename, "\t", name.st_size, "KB")
                sftp.get(remote_Path+name.filename, local_Path+name.filename)
                newfile_exist = True

        time.sleep(sleep_time)

        if newfile_exist:
            print("The download is complete ... ")
        else:
            print("Nothing new files to Download ... ")

print("Disconnect")

