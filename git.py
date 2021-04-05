"""
Created on Mon Mar 29 16:16:09 2021

@author: maksudul.it
"""

from os import system
from paramiko import SSHClient, AutoAddPolicy, SSHException
import paramiko as pm
from typing import List
from datetime import date
from datetime import datetime
from paramiko.auth_handler import AuthenticationException
import logging
import sys
import os
from config import configs

time = datetime.now()
today = date.today()
today = today.strftime("%d-%m-%Y")
# file_location = ["D:\\projects\\remote git management\\",
#                  "F:\\Maksudul_Hasan\\New folder\\"
#                  ]
file_location = os.getcwd()+"\\logs\\"

if not os.path.exists(file_location):
    os.mkdir(file_location)

file_name = file_location+today+".log"

if not os.path.exists(file_name):
    f = open(file_name,"w")


logging.basicConfig(filename=file_name,
                    style="{",
                    level=logging.INFO)


class RemoteCon:
    client=pm.SSHClient()
    
    def connect(self, cred):
        try: 
            self.client.set_missing_host_key_policy(pm.AutoAddPolicy())
            self.client.connect(cred[0],cred[1],cred[2],cred[3])
            print ("Connected Successfully!")
        except AuthenticationException:
            print ("Authentication failed, please verify your credentials")
            logging.ERROR(f"{time}: Authentication failed, please verify your credentials")
        except SSHException as sshException:
            print ("Unable to establish SSH connection: %s" % sshException)
            logging.ERROR(f"{time}: Unable to establish SSH connection: {sshException}")
            
    def execute_commands(self, commands: List[str]):
        for cmd in commands:
            stdin, stdout, stderr = self.client.exec_command(cmd)
            stdout.channel.recv_exit_status()
            response = stdout.readlines()
            print("response:", response)
            for line in response:
                logging.info(f"{time} INPUT: {cmd} | OUTPUT: {line}")
            
            return response
    def __del__(self):
        self.client.close()
    def disconnect(self):
        self.client.close()
        







