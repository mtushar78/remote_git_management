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
import socket

current_time = datetime.now()
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
        status = 0
        msg = ""
        try: 
            self.client.set_missing_host_key_policy(pm.AutoAddPolicy())
            self.client.connect(cred[0],cred[1],cred[2],cred[3], timeout=30)
            msg = "Connected successfully!"
            status = 1
            logging.info("%s: Successfully Connected to %s",current_time, cred[0])
        except AuthenticationException:
            msg = "Authentication Error!"
            print ("Authentication failed, please verify your credentials")
            logging.error("%s: Authentication failed, please verify your credentials", current_time)
        except SSHException as sshException:
            msg = "Unable to establish SSH connection!"
            print ("Unable to establish SSH connection: %s" % sshException)
            logging.error(f"{current_time}: Unable to establish SSH connection: {sshException}")
        except (pm.SSHException, socket.error) as se:
            msg = "Connection timeout!"
        except:
            msg = "Connection timeout!"
        
        return [status,msg]
    def execute_commands(self, commands: List[str]):
        for cmd in commands:
            try: 
                stdin, stdout, stderr = self.client.exec_command(cmd,timeout=30)
                
            except socket.timeout:
                print('socket Timeout')
                response = "Socket Timeout"
            stdout.channel.recv_exit_status()
            response = stdout.readlines()
            # print("response:", response)
            for line in response:
                logging.info(f"{current_time} INPUT: {cmd} | OUTPUT: {line}")
            
            return response
    def __del__(self):
        self.client.close()
    def disconnect(self):
        self.client.close()
    def check_connection_status(self):
        status = False
        if self.client.get_transport() is not None:
           status =  self.client.get_transport().is_active()   
        return status;






