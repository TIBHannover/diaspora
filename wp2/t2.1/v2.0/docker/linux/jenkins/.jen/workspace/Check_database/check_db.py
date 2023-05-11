# -*- coding: utf-8 -*-




import re

import io

import os

import sys

import pandas as pd 

from pathlib import Path

import pickle

import numpy as np

import configparser

import time

import mysql.connector


import logging



formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s',
                              datefmt='%Y-%m-%d %H:%M:%S')


def setup_logger(name, log_file, level=logging.DEBUG):
    """To setup as many loggers as you want"""
    logger = logging.getLogger(name)
  
    handler = logging.FileHandler(log_file,mode='w')        
    handler.setFormatter(formatter)

  
    logger.setLevel(level)
       
    
    logger.handlers.clear()
    logger.addHandler(handler)
       
    
   
    return logger

log_one = setup_logger('first_logger', 'log.log')


""" reading the path from path.properties file,specify the path of path.properties file"""

config = configparser.ConfigParser()

''' specify the path of db.properties file here '''
config.readfp(open('./db.properties'))



''' reading names from db.properties file '''
db_name = config.get('DATABASE', 'db' )


print(db_name)


mydb = mysql.connector.connect(
    host = 'db',
    user = 'root',
    passwd = 'root',
    auth_plugin='mysql_native_password')

    
# mydb = mysql.connector.connect (
    # host = 'localhost',
    # user = 'root',
    # passwd = '8227')

# log_one.warning("database doesn't exixts " + ' , ' + 'mydb:' + mydb )


# print(mydb)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

print(mycursor)

database = mycursor.fetchall()

print(database)

databases = []

for d in database:
    print((d[0]))
    databases.append(d[0])

print(databases)

if db_name in databases:
    print(db_name)
    
else:    
    log_one.warning("database doesn't exixts ")

    sys.exit("doesn't exit")
    








logging.shutdown()       

            
