"""
# ----------------------
# Created : 05-12-2021 13:28
# Licencing : (C) 2021 Dalimol Abraham, LYIT
#             Available under GNU public licence
# Description: 
# Author : Dalimol Abraham
# ----------------------
"""
import time
import re
import paramiko


def create_directory(ip):
    """Create folder in remote server"""
    try:
        print("Establishing a connection...")
        session = paramiko.SSHClient()
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        session.connect(ip, username='l00169942', password='dalimol123')
        connection = session.invoke_shell()
        connection.send("mkdir Lab\n")  # unix command to list
        connection.send('mkdir Lab/Lab1\n')
        connection.send('mkdir Lab/Lab2\n')
        time.sleep(1)
        vm_output = connection.recv(65535)
        print(vm_output)
        if re.search(b"% Invalid input", vm_output):
            print("There was an error on vm {}".format(ip))
        else:
            print("Commands successfully executed on {}".format(ip))
        session.close()
    except paramiko.AuthenticationException:
        print("Authentication Error")
        create_directory()
    except Exception as err:
        print(err)


if __name__ == '__main__':
    ip = '192.168.85.128'
    create_directory(ip)
