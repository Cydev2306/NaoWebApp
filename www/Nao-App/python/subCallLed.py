#169.254.66.119

import paramiko
import sys
import time

nbytes = 4096
hostname = '192.168.0.5'
port = 22
username = 'pi' 
password = 'raspberry'
client = paramiko.SSHClient()
client.load_system_host_keys()
client.connect(hostname,username=username,password=password)
time.sleep(12)
stdin, stdout, stderr = client.exec_command('sudo python app.py 255 0 0 8')#rouge
time.sleep(13)# Timer - secondes passes en param
stdin, stdout, stderr = client.exec_command('sudo python app.py 0 255 0 8')#Vert
time.sleep(10)
stdin, stdout, stderr = client.exec_command('sudo python app.py 0 0 255 8')#bleu
time.sleep(10)
stdin, stdout, stderr = client.exec_command('sudo python app.py 122 50 0 8')#Faux violet
time.sleep(27)
stdin, stdout, stderr = client.exec_command('sudo python app.py 255 50 0 5')# Orange
client.close()