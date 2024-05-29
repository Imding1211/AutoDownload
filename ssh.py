import paramiko

command = "bash show.sh"

host = "163.13.137.223"
username = "ding"
password = "1211"

client = paramiko.client.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, username=username, password=password)
stdin, stdout, stderr = client.exec_command(command)
print(stdout.read().decode())
client.close()