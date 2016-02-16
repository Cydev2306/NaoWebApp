#169.254.66.119

import paramiko
import sys
import time

nbytes = 4096
hostname = '192.168.0.5'
port = 22
username = 'pi' 
password = 'raspberry'
command = str(sys.argv[1],' ',sys.argv[2],' ', sys.argv[3],' ', sys.argv[4])
client = paramiko.SSHClient()
client.load_system_host_keys()
client.connect(hostname,username=username,password=password)
stdin, stdout, stderr = client.exec_command('sudo python app.py'+command)
client.close()