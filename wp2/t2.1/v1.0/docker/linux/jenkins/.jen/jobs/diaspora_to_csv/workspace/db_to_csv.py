# -*- coding: utf-8 -*-


import re
import io

import os

import sys

import pandas as pd 


from rdflib import Graph

from pathlib import Path

import pickle

import configparser


import time

import mysql.connector

import logging


formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s',
                              datefmt='%Y-%m-%d %H:%M:%S')


def setup_logger(name, log_file, level=logging.DEBUG):
    """To setup as many loggers as you want"""
    logger = logging.getLogger(name)
  
    handler = logging.FileHandler(log_file)        
    handler.setFormatter(formatter)

  
    logger.setLevel(level)
    logger.handlers.clear()
    logger.addHandler(handler)
       
    
   
    return logger

log_one = setup_logger('first_logger', 'log1.log')


""" reading the path from path.properties file,specify the path of path.properties file """

config = configparser.ConfigParser()

''' specify the path of path.properties file here '''

config.readfp(open('./tables.properties'))

''' taking tables name '''

# table1 = config.get('TABLES','materials_dataset')

# ''' taking queries '''

# query1 = config.get('QUERIES','query1')

# print(table1)


mydb = mysql.connector.connect(
    host = '127.0.0.1',
    port = '42333',
    user = 'root',
    passwd = 'root',
    database= "mydb")

# print(mydb)

mycursor = mydb.cursor()

mycursor.execute("select database();")

database = mycursor.fetchone()

print(database)

    
for each_section in config.sections(): 
    for each_key, each_val in config.items(each_section):
        
        query = each_val
    
       
        print(query)
            
  
        # query = 'select * from materials_dataset' 
        
        results = pd.read_sql_query(query, mydb)
        
        results.to_csv(each_key + ".csv", index=False)
          

logging.shutdown()       

            


