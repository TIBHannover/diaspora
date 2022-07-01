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


import numpy as np

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
    host = 'localhost',
    user = 'root',
    passwd = 'knowledge123',
    database= "diaspora")

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
        
    
            
        # if each_key == 'cell_morphology':
            
        #     # results['method'].dtype == np.object_
        #     # results['method'] = results['method'].str.replace('\n','')
          
        #     results.to_csv(each_key+".csv", index=False)
        #     # time.sleep(10)
        #     with open(each_key+".csv",'r', encoding="utf8") as f:
        #         data = f.read()
        #         # print(data)
           
        #     result =  pd.read_csv(io.StringIO(re.sub('"\s*\n','"',data)))
            
            
        #     for col in result.columns:
        #         # result[col].astype(str)
               
           
                
             
        #         if result[col].dtype == np.object_:
        #             # print(type(col))
        #             if result[col].dtype == np.object_:
                        
        #                 a = (result[col].str.contains(r"\n"))
                         
        #                 if a.any() == True:
        #                     print(col,'true')
        #                     log_one.warning('line break problem' + ' , ' + 'table_name:' + each_key + ' , ' + 'col_name:' + col)
                    
                  
                     
                  
        #             # if result[col].str.contains(r"\n"):
        #             #     print('hhhhh')
        #             result[col] = result[col].str.replace('\n','')
        #     result.to_csv(each_key+".csv", index=False)
            
        # # elif each_key == 'culture_condition':
            
        # #     # results['method'].dtype == np.object_
        # #     # results['method'] = results['method'].str.replace('\n','')
          
        # #     results.to_csv(each_key+".csv", index=False)
        # #     # time.sleep(10)
        # #     with open(each_key+".csv",'r') as f:
        # #         data = f.read()
        # #         # print(data)
           
        # #     result =  pd.read_csv(io.StringIO(re.sub('"\s*\n','"',data)))
            
            
        # #     for col in result.columns:
        # #         if result[col].dtype == np.object_:
            
        # #             result[col] = result[col].str.replace('  ','')
        # #             result[col] = result[col].str.replace('\n','')
                    
        # #     result.to_csv(each_key+".csv", index=False)
            
        # elif each_key == 'strains':
            
        #     # results['method'].dtype == np.object_
        #     # results['method'] = results['method'].str.replace('\n','')
          
        #     results.to_csv(each_key+".csv", index=False)
        #     # time.sleep(10)
        #     with open(each_key+".csv",'r',encoding="utf8") as f:
        #         data = f.read()
        #         # print(data)
           
        #     result =  pd.read_csv(each_key+".csv")
            
            
        #     a = (result[col].str.contains(r"\n"))
            
        #     for col in result.columns:
        #         if result[col].dtype == np.object_:
                    
                    
        #             # result = result.replace('\n','', regex=True)
                     
        #             if a.any() == True:
        #                 print(col,'true')
        #                 log_one.warning('line break problem' + ' , ' + 'table_name:' + each_key + ' , ' + 'col_name:' + col)
                
            
        #             result[col] = result[col].str.replace('  ','')
        #             result[col] = result[col].str.replace('\n','')
                    
        #     result.to_csv(each_key+".csv", index=False)
             
        # if each_key == 'reference':
            
            
           
        #     results.to_csv(each_key+".csv", index=False)
        #     # time.sleep(10)
        #     with open(each_key+".csv",'r', encoding="utf8") as f:
        #         data = f.read()
        #         # print(data)
           
        #     result =  pd.read_csv(io.StringIO(re.sub('"\s*\n','"',data)))
            
            
        #     for col in result.columns:
        #         if result[col].dtype == np.object_:
        #             a = (result[col].str.contains(r"\n"))
                     
        #             if a.any() == True:
        #                 print(col,'true')
        #                 log_one.warning('line break problem' + ' , ' + 'table_name:' + each_key + ' , ' + 'col_name:' + col)
                
        #             # result[col] = result[col].str.replace('  ','')
        #             result[col] = result[col].str.replace('\n','')
        #     result.to_csv(each_key+".csv", index=False)
        
        # elif each_key == 'colony_morphology':
            
        #     # results['method'].dtype == np.object_
        #     # results['method'] = results['method'].str.replace('\n','')
          
        #     results.to_csv(each_key+".csv", index=False)
        #     # time.sleep(10)
        #     with open(each_key+".csv",'r',encoding="utf8") as f:
        #         data = f.read()
        #         # print(data)
           
        #     result =  pd.read_csv(io.StringIO(re.sub('"\s*\n','"',data)))
            
            
        #     for col in result.columns:
         
                
        #         if result[col].dtype == np.object_:
                    
        #             a = (result[col].str.contains(r"\n"))
                     
        #             if a.any() == True:
        #                 print(col,'true')
        #                 log_one.warning('line break problem' + ' , ' + 'table_name:' + each_key + ' , ' + 'col_name:' + col)	

                        
                        
                        
        #             result[col] = result[col].str.replace('\n','')
        #     result.to_csv(each_key+".csv", index=False)
            
        
        # elif each_key == 'culture_medium':
            
        #     # results['method'].dtype == np.object_
        #     # results['method'] = results['method'].str.replace('\n','')
          
        #     results.to_csv(each_key+".csv", index=False)
        #     # time.sleep(10)
        #     with open(each_key+".csv",'r',encoding="utf8") as f:
        #         data = f.read()
        #         # print(data)
           
        #     result =  pd.read_csv(io.StringIO(re.sub('"\s*\n','"',data)))
            
            
        #     for col in result.columns:
         
                
        #         if result[col].dtype == np.object_:
                    
        #             a = (result[col].str.contains(r"\n"))
                     
        #             if a.any() == True:
        #                 print(col,'true')
        #                 log_one.warning('line break problem' + ' , ' + 'table_name:' + each_key + ' , ' + 'col_name:' + col)	

                        
                            
                            
        #                 result[col] = result[col].str.replace('\n','')
        #         result.to_csv(each_key+".csv", index=False)
        

        # elif each_key == 'origin':
            
        #     # results['method'].dtype == np.object_
        #     # results['method'] = results['method'].str.replace('\n','')
          
        #     results.to_csv(each_key+".csv", index=False)
        #     # time.sleep(10)
        #     with open(each_key+".csv",'r',encoding="utf8") as f:
        #         data = f.read()
        #         # print(data)
           
        #     result =  pd.read_csv(io.StringIO(re.sub('"\s*\n','"',data)))
            
            
        #     for col in result.columns:
         
                
        #         if result[col].dtype == np.object_:
                    
        #             a = (result[col].str.contains(r"\n"))
                     
        #             if a.any() == True:
        #                 # print(col,'true')
        #                 log_one.warning('line break problem' + ' , ' + 'table_name:' + each_key + ' , ' + 'col_name:' + col)	

        #             b =  (result[col].str.contains(r'\\'))
                     
        #             if b.any() == True:
                        
                         
        #                 log_one.warning('Unescaped backslash' + ' , ' + 'table_name:' + each_key + ' , ' + 'col_name:' + col)
                          
                        
                        
        #             result[col] = result[col].str.replace('\n','')
        #             result[col] = result[col].str.replace('\\','/')
        #             # result[col] = result[col].str.decode('unicode_escape')
        #     result.to_csv(each_key+".csv", index=False)


        # elif each_key == 'strain_history':
            
        #     # results['method'].dtype == np.object_
        #     # results['method'] = results['method'].str.replace('\n','')
          
        #     results.to_csv(each_key+".csv", index=False)
        #     # time.sleep(10)
        #     with open(each_key+".csv",'r',encoding="utf8") as f:
        #         data = f.read()
        #         # print(data)
           
        #     result =  pd.read_csv(io.StringIO(re.sub('"\s*\n','"',data)))
            
            
        #     for col in result.columns:
         
                
        #         if result[col].dtype == np.object_:
                    
        #             a = (result[col].str.contains(r"\n"))
                     
        #             if a.any() == True:
        #                 print(col,'true')
        #                 log_one.warning('line break problem' + ' , ' + 'table_name:' + each_key + ' , ' + 'col_name:' + col)	

                        
                        
                        
        #             result[col] = result[col].str.replace('\n','')
        #     result.to_csv(each_key+".csv", index=False)


        # elif each_key == 'sequence':
            
        #     # results['method'].dtype == np.object_
        #     # results['method'] = results['method'].str.replace('\n','')
          
        #     results.to_csv(each_key+".csv", index=False)
        #     # time.sleep(10)
        #     with open(each_key+".csv",'r',encoding="utf8") as f:
        #         data = f.read()
        #         # print(data)
           
        #     result =  pd.read_csv(io.StringIO(re.sub('"\s*\n','"',data)))
            
            
        #     for col in result.columns:
         
                
        #         if result[col].dtype == np.object_:
                    
        #             a = (result[col].str.contains(r"\n"))
                     
        #             if a.any() == True:
        #                 print(col,'true')
        #                 log_one.warning('line break problem' + ' , ' + 'table_name:' + each_key + ' , ' + 'col_name:' + col)	

                        
                        
                        
        #             result[col] = result[col].str.replace('\n','')
        #     result.to_csv(each_key+".csv", index=False)


        # elif each_key == 'strain_synonyms':
            
        #     # results['method'].dtype == np.object_
        #     # results['method'] = results['method'].str.replace('\n','')
          
        #     results.to_csv(each_key+".csv", index=False)
        #     # time.sleep(10)
        #     with open(each_key+".csv",'r',encoding="utf8") as f:
        #         data = f.read()
        #         # print(data)
           
        #     result =  pd.read_csv(io.StringIO(re.sub('"\s*\n','"',data)))
            
            
        #     for col in result.columns:
         
                
        #         if result[col].dtype == np.object_:
                    
        #             a = (result[col].str.contains(r"\n"))
                     
        #             if a.any() == True:
        #                 print(col,'true')
        #                 log_one.warning('line break problem' + ' , ' + 'table_name:' + each_key + ' , ' + 'col_name:' + col)	

                        
                        
                        
        #             result[col] = result[col].str.replace('\n','')
        #     result.to_csv(each_key+".csv", index=False)

 
        # elif each_key == 'culture_condition':
            
        #     # results['method'].dtype == np.object_
        #     # results['method'] = results['method'].str.replace('\n','')
          
        #     results.to_csv(each_key+".csv", index=False)
        #     # time.sleep(10)
        #     with open(each_key+".csv",'r',encoding="utf8") as f:
        #         data = f.read()
        #         # print(data)
           
        #     result =  pd.read_csv(io.StringIO(re.sub('"\s*\n','"',data)))
            
            
        #     for col in result.columns:
         
                
        #         if result[col].dtype == np.object_:
                    
                 
        #             a = (result[col].str.contains(r"\n"))
                     
        #             if a.any() == True:
        #                 print(col,'true')
        #                 log_one.warning('line break problem' + ' , ' + 'table_name:' + each_key + ' , ' + 'col_name:' + col)	
 
                        
                       
        #             result[col] = result[col].str.replace('  ','')    
        #             result[col] = result[col].str.replace('\n','')
        #     result.to_csv(each_key+".csv", index=False)


        # elif each_key == 'field_basic_definition':
            
        #     # results['method'].dtype == np.object_
        #     # results['method'] = results['method'].str.replace('\n','')
          
        #     results.to_csv(each_key+".csv", index=False)
        #     # time.sleep(10)
        #     with open(each_key+".csv",'r',encoding="utf8") as f:
        #         data = f.read()
        #         # print(data)
           
        #     result =  pd.read_csv(io.StringIO(re.sub('"\s*\n','"',data)))
            
            
        #     for col in result.columns:
         
                
        #         if result[col].dtype == np.object_:
                    
        #             a = (result[col].str.contains(r"\n"))
                     
        #             if a.any() == True:
        #                 print(col,'true')
        #                 log_one.warning('line break problem' + ' , ' + 'table_name:' + each_key + ' , ' + 'col_name:' + col)	
 
                        
                       
                       
        #             result[col] = result[col].str.replace('\n','')
        #     result.to_csv(each_key+".csv", index=False)


        # elif each_key == 'multimedia':
            
        #     # results['method'].dtype == np.object_
        #     # results['method'] = results['method'].str.replace('\n','')
          
        #     results.to_csv(each_key+".csv", index=False)
        #     # time.sleep(10)
        #     with open(each_key+".csv",'r',encoding="utf8") as f:
        #         data = f.read()
        #         # print(data)
           
        #     result =  pd.read_csv(io.StringIO(re.sub('"\s*\n','"',data)))
            
            
        #     for col in result.columns:
                
                
             
                
        #         if result[col].dtype == np.object_:
                    
        #             a = (result[col].str.contains(r"\n"))
                     
        #             if a.any() == True:
        #                 # print(col,'true')
        #                 log_one.warning('line break problem' + ' , ' + 'table_name:' + each_key + ' , ' + 'col_name:' + col)	
 
        #             b =  (result[col].str.contains(r'\\'))
                    
        #             if b.any() == True:
                        
        #                 log_one.warning('Unescaped backslash' + ' , ' + 'table_name:' + each_key + ' , ' + 'col_name:' + col)
                        
                       
                       
        #             result[col] = result[col].str.replace('\n','')
             
        #             result[col] = result[col].str.replace('\\','/')
        #             # result[col] = result[col].str.decode('unicode_escape')
        #     result.to_csv(each_key+".csv", index=False)


        # elif each_key == 'biosample':
            
        #     # results['method'].dtype == np.object_
        #     # results['method'] = results['method'].str.replace('\n','')
          
        #     results.to_csv(each_key+".csv", index=False)
        #     # time.sleep(10)
        #     with open(each_key+".csv",'r',encoding="utf8") as f:
        #         data = f.read()
        #         # print(data)
           
        #     result =  pd.read_csv(io.StringIO(re.sub('"\s*\n','"',data)))
            
            
        #     for col in result.columns:
                
                
             
                
        #         if result[col].dtype == np.object_:
                    
        #             a = (result[col].str.contains(r"\n"))
                     
        #             if a.any() == True:
        #                 # print(col,'true')
        #                 log_one.warning('line break problem' + ' , ' + 'table_name:' + each_key + ' , ' + 'col_name:' + col)	
 
        #             b =  (result[col].str.contains(r'\\'))
                    
        #             if b.any() == True:
                        
        #                 log_one.warning('Unescaped backslash' + ' , ' + 'table_name:' + each_key + ' , ' + 'col_name:' + col)
                        
                       
                       
        #             result[col] = result[col].str.replace('\n','')
             
        #             result[col] = result[col].str.replace('\\','/')
        #             # result[col] = result[col].str.decode('unicode_escape')
        #     result.to_csv(each_key+".csv", index=False)
        
        # elif each_key == 'update_helper':
            
        #     # results['method'].dtype == np.object_
        #     # results['method'] = results['method'].str.replace('\n','')
          
        #     results.to_csv(each_key+".csv", index=False)
        #     # time.sleep(10)
        #     with open(each_key+".csv",'r',encoding="utf8") as f:
        #         data = f.read()
        #         # print(data)
           
        #     result =  pd.read_csv(io.StringIO(re.sub('"\s*\n','"',data)))
            
            
        #     for col in result.columns:
                
                
             
                
        #         if result[col].dtype == np.object_:
                    
        #             a = (result[col].str.contains(r"\n"))
                     
        #             if a.any() == True:
        #                 # print(col,'true')
        #                 log_one.warning('line break problem' + ' , ' + 'table_name:' + each_key + ' , ' + 'col_name:' + col)	
 
        #             b =  (result[col].str.contains(r'\\'))
                    
        #             if b.any() == True:
                        
        #                 log_one.warning('Unescaped backslash' + ' , ' + 'table_name:' + each_key + ' , ' + 'col_name:' + col)
                        
                       
                       
        #             result[col] = result[col].str.replace('\n','')
             
        #             result[col] = result[col].str.replace('\\','/')
        #             # result[col] = result[col].str.decode('unicode_escape')
        #     result.to_csv(each_key+".csv", index=False)

logging.shutdown()       

            


