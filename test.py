# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 13:17:45 2021

@author: maksudul.it
"""

import ast,sys,json

f = open("config.json",'r')

# config =f.read()
# config = ast.literal_eval(str(config))


# Opening JSON file
with open('config.json') as json_file:
    data = json.load(json_file)
  
    # Print the type of data variable
    print("Type:", type(data))
  
    # Print the data of dictionary
    # print("\nPeople1:", data['people1'])
    # print("\nPeople2:", data['people2'])
    print('data: ' ,data)