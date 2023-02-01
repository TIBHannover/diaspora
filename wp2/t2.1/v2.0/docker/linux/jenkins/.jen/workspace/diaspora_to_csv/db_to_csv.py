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

log_one = setup_logger('first_logger', 'logwithvalue.log')


""" reading the path from path.properties file,specify the path of path.properties file """

config = configparser.ConfigParser()

''' specify the path of path.properties file here '''

config.readfp(open('./tables.properties'))

''' taking tables name '''

# table1 = config.get('TABLES','materials_dataset')

# ''' taking queries '''

# query1 = config.get('QUERIES','query1')

# print(table1)


# mydb = mysql.connector.connect(
    # host = 'db',
    # # port = '3306',
    # user = 'root',
    # passwd = 'root',
    # database= 'diaspora',
    # auth_plugin='mysql_native_password')
    


mydb = mysql.connector.connect(
    host = 'db',
   # port = '3306',
    user = 'root',
    passwd = 'root',
    database= 'diaspora_v2',
    auth_plugin='mysql_native_password')



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
        results.to_csv(each_key+".csv", index=False)
        
     
        
    
        if each_key == 'strains':

            
            # results['method'].dtype == np.object_
            # results['method'] = results['method'].str.replace('\n','')
          
            results.to_csv(each_key+".csv", index=False)
            # time.sleep(10)
            with open(each_key+".csv",'r',encoding="utf8") as f:
                data = f.read()
                
        
            result =  pd.read_csv(io.StringIO(re.sub('"\s*\n','"',data)), dtype = {'type_strain': str})
                           

            
            
            ids = []   

            
            for col in result.columns:
                # print(col)
               if result[col].dtype == np.object_ or np.int64:
                    
                    
                    
                    # print((result[col]))
                    for h ,g in result[col].iteritems():
                        try:
                            
                            
                            if ("\n" in g):
                                # print(col)
                                # print(h, g)
                                # print(type(g))
                                # print('jjjj')
                                s = (result.loc[result[col]==g, 'ID_strains'].iloc[0])
                                s1 = str(s)
                                # print('kkkkkk')
                                # print(s1)
                                # print('hhhhhh')
                                # print(type(s1))
                                # print('vvvvv')
                                g1 = g.replace('\n', '')
                                print(ids)
                                if s1 not in ids:
                                    ids.append(s1)
                                    print(ids)
                                    log_one.warning('line break problem' + ' , ' + 'table_name:' + each_key + ' , ' + 'col_name:' + col + ' ,' + 'id:' + s1 + ' ' + 'ol_value:' + g + ' ' + 'new_value:' + g1)
                                else:
                                    pass
                                    # log_one.warning('line break problem' + ' , ' + 'table_name:' + each_key + ' , ' + 'col_name:' + col + ' ,' + 'id:' + s1 )

                                # log_one.warning('line break problem' + ' , ' + 'table_name:' + each_key + ' , ' + 'col_name:' + col + ' ,' + 'id:' + s1 + ' ' + 'ol_value:' + g + ' ' + 'new_value:' + g1)
                                
                            # if ("  " in g):
                            #     print('rohit')
                                
                            #     # print(col)
                            #     # print(h, g)
                            #     # print(type(g))
                            #     # print('jjjj')
                            #     s4 = (result.loc[result[col]==g, 'ID_strains'].iloc[0])
                            #     s5 = str(s4)
                            #     print('hhhhhh')
                            #     print('rohit')
                            #     print((s5))
                            #     print('vvvvv')
                            #     g2 = g.replace('  ', '')
                            #     print(ids)
                            #     if s5 not in ids:
                            #         ids.append(s5)
                            #         print(ids)
                          
                            #         log_one.warning('space problem' + ' , ' + 'table_name:' + each_key + ' , ' + 'col_name:' + col + ' ,' + 'id:' +  s5  + ' ' + 'old_value:' + g + ' ' + 'new_value:' + g2)
                            #         # + ' ' + 'old_value:' + g + ' ' + 'new_value:' + g2
                            #     else:
                                    
                            #        pass     
                                   
                            
     
                        except:
                            pass
                        
                    try:
                        
                        
                        
                        result[col] = result[col].str.replace('\n','')   
                        result[col] = result[col].str.replace('  ','')
                    except:
                        pass
                    
 
                    
            result.to_csv(each_key + ".csv", index=False)                    
                                            
                    
            

        
        if each_key == 'colony_morphology':
            
            # results['method'].dtype == np.object_
            # results['method'] = results['method'].str.replace('\n','')
          
            results.to_csv(each_key+".csv", index=False)
            # time.sleep(10)
            with open(each_key+".csv",'r',encoding="utf8") as f:
                data = f.read()
                # print(data)
           
            result =  pd.read_csv(io.StringIO(re.sub('"\s*\n','"',data)))
            
            ids=[]   

            for col in result.columns:
                # print(col)
                # if result[col].dtype == np.object_ or np.int64:
                    
                    
                # print((result[col]))
                for hc ,gc in result[col].iteritems():
                    try:
                        
                        if ("\n" in gc):
                            # print(col)
                            # print(h, g)
                            # print(type(g))
                            # print('jjjj')
                            s2 = (result.loc[result[col]==gc, 'ID_colony_morphology'].iloc[0])
                            s3 = str(s2)
                            print('hhhhhh')
                            print((s3))
                            print('vvvvv')
                            g2 = gc.replace('\n', '')
                            # s
                            print(ids)
                            if s3 not in ids:
                                ids.append(s3)
                                print(ids)
                                log_one.warning('line break problem' + ' , ' + 'table_name:' + each_key + ' , ' + 'col_name:' + col + ' ,' + 'id:' + s3 + ' ' + 'old_value:' + gc + ' ' + 'new_value:' + g2)
                            else:
                                pass
                                # log_one.warning('line break problem' + ' , ' + 'table_name:' + each_key + ' , ' + 'col_name:' + col + ' ,' + 'id:' + s3 )

                            # log_one.warning('line break problem' + ' , ' + 'table_name:' + each_key + ' , ' + 'col_name:' + col + ' ,' + 'id:' +  s3  )
                            # + ' ' + 'ol_value:' + g + ' ' + 'new_value:' + g1
                                # log_one.warning('line break problem' + ' , ' + 'table_name:' + each_key + ' , ' + 'col_name:' + col + ' ,' + 'id_colony_morphology:' + s3 + ' ' + 'old_value:' + gc + ' ' + 'new_value:' + g2 )

                    except:
                        pass
                # (result[col].str.contains(r"\n"))
                try:
                    
                    
                    
                    result[col] = result[col].str.replace('\n','')     
                except:
                    pass

            result.to_csv(each_key+".csv", index=False)                    
                                            
            
            

            
        
        elif each_key == 'culture_medium':
            
            # results['method'].dtype == np.object_
            # results['method'] = results['method'].str.replace('\n','')
          
            results.to_csv(each_key+".csv", index=False)
            # time.sleep(10)
            with open(each_key+".csv",'r',encoding="utf8") as f:
                data = f.read()
                # print(data)
           
            result =  pd.read_csv(io.StringIO(re.sub('"\s*\n','"',data)))
            
            ids=[]  
            
            for col in result.columns:
                # print(col)
                if result[col].dtype == np.object_ or np.int64:
                    
                    
                    
                    # print((result[col]))
                    for h ,g in result[col].iteritems():
                        try:
                            
                            if ("\n" in g):
                                # print(col)
                                # print(h, g)
                                # print(type(g))
                                # print('jjjj')
                                s = (result.loc[result[col]==g, 'ID_culture_medium'].iloc[0])
                                s1 = str(s)
                                print('hhhhhh')
                                print((s1))
                                print('vvvvv')
                                g1 = g.replace('\n', '')
                                print(ids)
                                if s1 not in ids:
                                    ids.append(s1)
                                    print(ids)
                          
                                    log_one.warning('line break problem' + ' , ' + 'table_name:' + each_key + ' , ' + 'col_name:' + col + ' ,' + 'id:' +  s1 + ' ' + 'old_value:' + g + ' ' + 'new_value:' + g1)
                                else:
                                    
                                   pass
                                # + ' ' + 'ol_value:' + g + ' ' + 'new_value:' + g1
                             
                        except:
                            pass
                    # (result[col].str.contains(r"\n"))
                    try:
                        
                        
                        
                        result[col] = result[col].str.replace('\n','')     
                    except:
                        pass

            result.to_csv(each_key +".csv", index=False)   
            

        

        elif each_key == 'origin':
            
            # results['method'].dtype == np.object_
            # results['method'] = results['method'].str.replace('\n','')
          
            results.to_csv(each_key+".csv", index=False)
            # time.sleep(10)
            with open(each_key+".csv",'r',encoding="utf8") as f:
                data = f.read()
                # print(data)
           
            result =  pd.read_csv(io.StringIO(re.sub('"\s*\n','"',data)))
            
            ids=[]  
            
            for col in result.columns:
                # print(col)
                if result[col].dtype == np.object_ or np.int64:
                    
                    
                    
                    # print((result[col]))
                    for h ,g in result[col].iteritems():
                        try:
                            
                            if ("\n" in g):
                                # print(col)
                                # print(h, g)
                                # print(type(g))
                                # print('jjjj')
                                s = (result.loc[result[col]==g, 'ID_origin'].iloc[0])
                                s1 = str(s)
                                print('hhhhhh')
                                print((s1))
                                print('vvvvv')
                                g1 = g.replace('\n', '')
                                print(ids)
                                if s1 not in ids:
                                    ids.append(s1)
                                    print(ids)
                          
                                    log_one.warning('line break problem' + ' , ' + 'table_name:' + each_key + ' , ' + 'col_name:' + col + ' ,' + 'id:' +  s1 + ' ' + 'old_value:' + g + ' ' + 'new_value:' + g1)
                                    # +  s1 + ' ' + 'old_value:' + g + ' ' + 'new_value:' + g1
                                else:
                                    
                                    pass
                                # + ' ' + 'ol_value:' + g + ' ' + 'new_value:' + g1
                            
                            if ("\\" in g):
                                print('rohit')
                                
                                # print(col)
                                # print(h, g)
                                # print(type(g))
                                # print('jjjj')
                                s4 = (result.loc[result[col]==g, 'ID_origin'].iloc[0])
                                s5 = str(s4)
                                print('hhhhhh')
                                print('rohit')
                                print((s5))
                                print('vvvvv')
                                g2 = g.replace('\\', '/')
                                print(ids)
                                if s5 not in ids:
                                    ids.append(s5)
                                    print(ids)
                          
                                    log_one.warning('unescaped backslash' + ' , ' + 'table_name:' + each_key + ' , ' + 'col_name:' + col + ' ,' + 'id:' +  s5  + ' ' + 'old_value:' + g + ' ' + 'new_value:' + g2)
                                    # + ' ' + 'old_value:' + g + ' ' + 'new_value:' + g2
                                else:
                                    
                                   pass    
                            
                            
                        except:
                            pass
                    # (result[col].str.contains(r"\n"))
                    try:
                        
                        
                        
                        result[col] = result[col].str.replace('\n','')     
                        result[col] = result[col].str.replace('\\','/')

                    except:
                        pass

            result.to_csv(each_key+".csv", index=False)   
            
       


        elif each_key == 'strain_history':
            
            # results['method'].dtype == np.object_
            # results['method'] = results['method'].str.replace('\n','')
          
            results.to_csv(each_key+".csv", index=False)
            # time.sleep(10)
            with open(each_key+".csv",'r',encoding="utf8") as f:
                data = f.read()
                # print(data)
           
            result =  pd.read_csv(io.StringIO(re.sub('"\s*\n','"',data)))
            
            ids=[]  
            
            for col in result.columns:
                # print(col)
                if result[col].dtype == np.object_ or np.int64:
                    
                    
                    
                    # print((result[col]))
                    for h ,g in result[col].iteritems():
                        try:
                            
                            if ("\n" in g):
                                # print(col)
                                # print(h, g)
                                # print(type(g))
                                # print('jjjj')
                                s = (result.loc[result[col]==g, 'ID_strain_history'].iloc[0])
                                s1 = str(s)
                                print('hhhhhh')
                                print((s1))
                                print('vvvvv')
                                g1 = g.replace('\n', '')
                                print(ids)
                                if s1 not in ids:
                                    ids.append(s1)
                                    print(ids)
                          
                                    log_one.warning('line break problem' + ' , ' + 'table_name:' + each_key + ' , ' + 'col_name:' + col + ' ,' + 'id:' +  s1 + ' ' + 'old_value:' + g + ' ' + 'new_value:' + g1)
                                    # +  s1 + ' ' + 'old_value:' + g + ' ' + 'new_value:' + g1
                                else:
                                    
                                    pass
                                # + ' ' + 'ol_value:' + g + ' ' + 'new_value:' + g1

                            
                            
                        except:
                            pass
                    # (result[col].str.contains(r"\n"))
                    try:
                        
                        
                        
                        result[col] = result[col].str.replace('\n','')     
                      

                    except:
                        pass

            result.to_csv(each_key +".csv", index=False)  
            
            


        elif each_key == 'sequence':
            
            # results['method'].dtype == np.object_
            # results['method'] = results['method'].str.replace('\n','')
          
            results.to_csv(each_key+".csv", index=False)
            # time.sleep(10)
            with open(each_key+".csv",'r',encoding="utf8") as f:
                data = f.read()
                # print(data)
           
            result =  pd.read_csv(io.StringIO(re.sub('"\s*\n','"',data)))
            
                        
            ids=[]  
            
            for col in result.columns:
                # print(col)
                if result[col].dtype == np.object_ or np.int64:
                    
                    
                    
                    # print((result[col]))
                    for h ,g in result[col].iteritems():
                        try:
                            
                            if ("\n" in g):
                                # print(col)
                                # print(h, g)
                                # print(type(g))
                                # print('jjjj')
                                s = (result.loc[result[col]==g, 'ID_sequence'].iloc[0])
                                s1 = str(s)
                                print('hhhhhh')
                                print((s1))
                                print('vvvvv')
                                g1 = g.replace('\n', '')
                                print(ids)
                                if s1 not in ids:
                                    ids.append(s1)
                                    print(ids)
                          
                                    log_one.warning('line break problem' + ' , ' + 'table_name:' + each_key + ' , ' + 'col_name:' + col + ' ,' + 'id:' +  s1 + ' ' + 'old_value:' + g + ' ' + 'new_value:' + g1)
                                    # +  s1 + ' ' + 'old_value:' + g + ' ' + 'new_value:' + g1
                                else:
                                    
                                    pass
                                # + ' ' + 'ol_value:' + g + ' ' + 'new_value:' + g1

                            
                            
                        except:
                            pass
                    # (result[col].str.contains(r"\n"))
                    try:
                        
                        
                        
                        result[col] = result[col].str.replace('\n','')     
                      

                    except:
                        pass

            result.to_csv(each_key +".csv", index=False) 
            
            


        elif each_key == 'strain_synonyms':
            
            # results['method'].dtype == np.object_
            # results['method'] = results['method'].str.replace('\n','')
          
            results.to_csv(each_key+".csv", index=False)
            # time.sleep(10)
            with open(each_key+".csv",'r',encoding="utf8") as f:
                data = f.read()
                # print(data)
           
            result =  pd.read_csv(io.StringIO(re.sub('"\s*\n','"',data)))
            
                                    
            ids=[]  
            
            for col in result.columns:
                # print(col)
                if result[col].dtype == np.object_ or np.int64:
                    
                    
                    
                    # print((result[col]))
                    for h ,g in result[col].iteritems():
                        try:
                            
                            if ("\n" in g):
                                # print(col)
                                # print(h, g)
                                # print(type(g))
                                # print('jjjj')
                                s = (result.loc[result[col]==g, 'ID_strain_synonyms'].iloc[0])
                                s1 = str(s)
                                print('hhhhhh')
                                print((s1))
                                print('vvvvv')
                                g1 = g.replace('\n', '')
                                print(ids)
                                if s1 not in ids:
                                    ids.append(s1)
                                    print(ids)
                          
                                    log_one.warning('line break problem' + ' , ' + 'table_name:' + each_key + ' , ' + 'col_name:' + col + ' ,' + 'id:' +  s1 + ' ' + 'old_value:' + g + ' ' + 'new_value:' + g1)
                                    # +  s1 + ' ' + 'old_value:' + g + ' ' + 'new_value:' + g1
                                else:
                                    
                                    pass
                                # + ' ' + 'ol_value:' + g + ' ' + 'new_value:' + g1

                            
                            
                        except:
                            pass
                    # (result[col].str.contains(r"\n"))
                    try:
                        
                        
                        
                        result[col] = result[col].str.replace('\n','')     
                      

                    except:
                        pass

            result.to_csv(each_key +".csv", index=False) 
            
            
            


        elif each_key == 'multimedia':
            
            # results['method'].dtype == np.object_
            # results['method'] = results['method'].str.replace('\n','')
          
            results.to_csv(each_key+".csv", index=False)
            # time.sleep(10)
            with open(each_key+".csv",'r',encoding="utf8") as f:
                data = f.read()
                # print(data)
           
            result =  pd.read_csv(io.StringIO(re.sub('"\s*\n','"',data)))
            
            ids=[]  
            
            for col in result.columns:
                # print(col)
                if result[col].dtype == np.object_ or np.int64:
                    
                    
                    
                    # print((result[col]))
                    for h ,g in result[col].iteritems():
                        try:
                            
                            if ("\n" in g):
                                # print(col)
                                # print(h, g)
                                # print(type(g))
                                # print('jjjj')
                                s = (result.loc[result[col]==g, 'ID_multimedia'].iloc[0])
                                s1 = str(s)
                                print('hhhhhh')
                                print((s1))
                                print('vvvvv')
                                g1 = g.replace('\n', '')
                                print(ids)
                                if s1 not in ids:
                                    ids.append(s1)
                                    print(ids)
                          
                                    log_one.warning('line break problem' + ' , ' + 'table_name:' + each_key + ' , ' + 'col_name:' + col + ' ,' + 'id:' +  s1 + ' ' + 'old_value:' + g + ' ' + 'new_value:' + g1)
                                    # +  s1 + ' ' + 'old_value:' + g + ' ' + 'new_value:' + g1
                                else:
                                    
                                    pass
                                # + ' ' + 'ol_value:' + g + ' ' + 'new_value:' + g1
                            
                            if ("\\" in g):
                                print('rohit')
                                
                                # print(col)
                                # print(h, g)
                                # print(type(g))
                                # print('jjjj')
                                s4 = (result.loc[result[col]==g, 'ID_multimedia'].iloc[0])
                                s5 = str(s4)
                                print('hhhhhh')
                                print('rohit')
                                print((s5))
                                print('vvvvv')
                                g2 = g.replace('\\', '/')
                                print(ids)
                                if s5 not in ids:
                                    ids.append(s5)
                                    print(ids)
                          
                                    log_one.warning('unescaped backslash' + ' , ' + 'table_name:' + each_key + ' , ' + 'col_name:' + col + ' ,' + 'id:' +  s5  + ' ' + 'old_value:' + g + ' ' + 'new_value:' + g2)
                                    # + ' ' + 'old_value:' + g + ' ' + 'new_value:' + g2
                                else:
                                    
                                   pass    
                            
                            
                        except:
                            pass
                    # (result[col].str.contains(r"\n"))
                    try:
                        
                        
                        
                        result[col] = result[col].str.replace('\n','')     
                        result[col] = result[col].str.replace('\\','/')

                    except:
                        pass

            result.to_csv(each_key +".csv", index=False) 
            
            
      

        elif each_key == 'biosample':
            
            # results['method'].dtype == np.object_
            # results['method'] = results['method'].str.replace('\n','')
          
            results.to_csv(each_key+".csv", index=False)
            # time.sleep(10)
            with open(each_key+".csv",'r',encoding="utf8") as f:
                data = f.read()
                # print(data)
           
            result =  pd.read_csv(io.StringIO(re.sub('"\s*\n','"',data)))
            ids=[]  
            
            for col in result.columns:
                # print(col)
                if result[col].dtype == np.object_ or np.int64:
                    
                    
                    
                    # print((result[col]))
                    for h ,g in result[col].iteritems():
                        try:
                            
                            if ("\n" in g):
                                # print(col)
                                # print(h, g)
                                # print(type(g))
                                # print('jjjj')
                                s = (result.loc[result[col]==g, 'ID'].iloc[0])
                                s1 = str(s)
                                print('hhhhhh')
                                print((s1))
                                print('vvvvv')
                                g1 = g.replace('\n', '')
                                print(ids)
                                if s1 not in ids:
                                    ids.append(s1)
                                    print(ids)
                          
                                    log_one.warning('line break problem' + ' , ' + 'table_name:' + each_key + ' , ' + 'col_name:' + col + ' ,' + 'id:' +  s1 + ' ' + 'old_value:' + g + ' ' + 'new_value:' + g1)
                                    # +  s1 + ' ' + 'old_value:' + g + ' ' + 'new_value:' + g1
                                else:
                                    
                                    pass
                                # + ' ' + 'ol_value:' + g + ' ' + 'new_value:' + g1
                            
                            if ("\\" in g):
                                print('rohit')
                                
                                # print(col)
                                # print(h, g)
                                # print(type(g))
                                # print('jjjj')
                                s4 = (result.loc[result[col]==g, 'ID'].iloc[0])
                                s5 = str(s4)
                                print('hhhhhh')
                                print('rohit')
                                print((s5))
                                print('vvvvv')
                                g2 = g.replace('\\', '/')
                                print(ids)
                                if s5 not in ids:
                                    ids.append(s5)
                                    print(ids)
                          
                                    log_one.warning('unescaped backslash' + ' , ' + 'table_name:' + each_key + ' , ' + 'col_name:' + col + ' ,' + 'id:' +  s5  + ' ' + 'old_value:' + g + ' ' + 'new_value:' + g2)
                                    # + ' ' + 'old_value:' + g + ' ' + 'new_value:' + g2
                                else:
                                    
                                   pass    
                            
                            
                        except:
                            pass
                    # (result[col].str.contains(r"\n"))
                    try:
                        
                        
                        
                        result[col] = result[col].str.replace('\n','')     
                        result[col] = result[col].str.replace('\\','/')

                    except:
                        pass

            result.to_csv(each_key +".csv", index=False) 
            
            


logging.shutdown()       

            



# import re

# import io

# import os

# import sys

# import pandas as pd 

# from pathlib import Path

# import pickle

# import numpy as np

# import configparser

# import time

# import mysql.connector


# import logging



# formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s',
#                               datefmt='%Y-%m-%d %H:%M:%S')


# def setup_logger(name, log_file, level=logging.DEBUG):
#     """To setup as many loggers as you want"""
#     logger = logging.getLogger(name)
  
#     handler = logging.FileHandler(log_file)        
#     handler.setFormatter(formatter)

  
#     logger.setLevel(level)
#     logger.handlers.clear()
#     logger.addHandler(handler)
       
    
   
#     return logger

# log_one = setup_logger('first_logger', 'log1b.log')


# """ reading the path from path.properties file,specify the path of path.properties file """

# config = configparser.ConfigParser()

# ''' specify the path of path.properties file here '''

# config.readfp(open('./tables.properties'))

# ''' taking tables name '''

# # table1 = config.get('TABLES','materials_dataset')

# # ''' taking queries '''

# # query1 = config.get('QUERIES','query1')

# # print(table1)


# #mydb = pymysql.connect(
#  #   host = 'db',
#    # port = '3306',
#   #  user = 'root',
#    # passwd = 'root',
#   #  database= "b'diaspora",
#    # auth_plugin='mysql_native_password')

# # mydb = mysql.connector.connect(
# #     host = 'db',
# #    # port = '3306',
# #     user = 'root',
# #     passwd = 'root',
# #     database= 'diaspora',
# #     auth_plugin='mysql_native_password')

# mydb = mysql.connector.connect(
#     host = 'localhost',
#     user = 'root',
#     passwd = '8227',
#     database= "b'diaspora'")

# # print(mydb)

# mycursor = mydb.cursor()

# mycursor.execute("select database();")

# database = mycursor.fetchone()

# print(database)


# for each_section in config.sections(): 
#     for each_key, each_val in config.items(each_section):
        
#         query = each_val
    
       
#         print(query)
            
  
#         # query = 'select * from materials_dataset' 
        
#         results = pd.read_sql_query(query, mydb)
#         results.to_csv(each_key+".csv", index=False)
        
     
        
    
            
#         if each_key == 'cell_morphology':
            
#             # results['method'].dtype == np.object_
#             # results['method'] = results['method'].str.replace('\n','')
          
#             results.to_csv(each_key+".csv", index=False)
#             # time.sleep(10)
#             with open(each_key+".csv",'r', encoding="utf8") as f:
#                 data = f.read()
#                 # print(data)
           
#             result =  pd.read_csv(io.StringIO(re.sub('"\s*\n','"',data)))
            
            
#             for col in result.columns:
#                 # result[col].astype(str)
               
           
                
             
#                 if result[col].dtype == np.object_:
#                     # print(type(col))
#                     if result[col].dtype == np.object_:
                        
#                         a = (result[col].str.contains(r"\n"))
                     
                         
#                         if a.any() == True:
#                             print(col,'true')
#                             log_one.warning('line break problem' + ' , ' + 'table_name:' + each_key + ' , ' + 'col_name:' + col)
                    
                  
                     
                  
#                     # if result[col].str.contains(r"\n"):
#                     #     print('hhhhh')
#                     result[col] = result[col].str.replace('\n','')
#             result.to_csv(each_key+".csv", index=False)
    
#         elif each_key == 'strains':

            
#             # results['method'].dtype == np.object_
#             # results['method'] = results['method'].str.replace('\n','')
          
#             results.to_csv(each_key+".csv", index=False)
#             # time.sleep(10)
#             with open(each_key+".csv",'r',encoding="utf8") as f:
#                 data = f.read()
#                 # print(data)
           
#             result =  pd.read_csv(io.StringIO(re.sub('"\s*\n','"',data)), dtype = {'type_strain': str})
            
#             print(result)
    
#             for col in result.columns:
#                 print(col)
#                 if result[col].dtype == np.object_ or np.int64:
                    
                    
#                     print('jjjjj')
                    
                    
#                     # print((result[col]))
#                     for h ,g in result[col].iteritems():
#                         # print(g)
#                         try:
#                             print('ppppppp')
#                             if ("\n" in g):
#                                 print('lllllll')
#                                 print(col)
#                                 # print(h, g)
#                                 # print(type(g))
#                                 # print('jjjj')
#                                 s = (result.loc[result[col]==g, 'ID_strains'].item())
#                                 s1 = str(s)
#                                 print('kkkkkk')
#                                 print(s1)
#                                 print('hhhhhh')
#                                 # print(type(s1))
#                                 # print('vvvvv')
#                                 g1 = g.replace('\n', '')
#                                 # s
#                                 log_one.warning('line break problem' + ' , ' + 'table_name:' + each_key + ' , ' + 'col_name:' + col + ' ,' + 'id:' + s1 + ' ' + 'ol_value:' + g + ' ' + 'new_value:' + g1)
#                                 # log_one.warning('line break problem' + ' , ' + 'table_name:' + each_key + ' , ' + 'col_name:' + col + ' ,' + 'id:' + s1)
                                
                             
                                   
                            
         
#                         except:
#                             pass
                    
#                     try:
                        
#                         print('kkkkkkk')
                        
#                         result[col] = result[col].str.replace('\n','')     
#                     except:
#                         pass
                    
 
                    
#             result.to_csv(each_key + "clean" + ".csv", index=False)  
            
            
#             # for col in result.columns:
#             #     if result[col].dtype == np.object_:
                    
#             #         a = (result[col].str.contains(r"\n"))
#             #         b = (result[col].str.contains(r'  '))
                     
#             #         if a.any() == True:
#             #             print(col,'true')
#             #             log_one.warning('line break problem' + ' , ' + 'table_name:' + each_key + ' , ' + 'col_name:' + col)
                    
#             #         if b.any() == True:
#             #             print(col,'true')
#             #             log_one.warning('space problem' + ' , ' + 'table_name:' + each_key + ' , ' + 'col_name:' + col)
                
            
#             #         result[col] = result[col].str.replace('  ','')
#             #         result[col] = result[col].str.replace('\n','')
                    
#             # result.to_csv(each_key+".csv", index=False)
            
            
#         elif each_key == 'reference':
            
            
           
#             results.to_csv(each_key+".csv", index=False)
#             # time.sleep(10)
#             with open(each_key+".csv",'r', encoding="utf8") as f:
#                 data = f.read()
#                 # print(data)
           
#             result =  pd.read_csv(io.StringIO(re.sub('"\s*\n','"',data)))
            
            
#             for col in result.columns:
#                 if result[col].dtype == np.object_:
#                     a = (result[col].str.contains(r"\n"))
                     
#                     if a.any() == True:
#                         print(col,'true')
#                         log_one.warning('line break problem' + ' , ' + 'table_name:' + each_key + ' , ' + 'col_name:' + col)
                
#                     # result[col] = result[col].str.replace('  ','')
#                     result[col] = result[col].str.replace('\n','')
#             result.to_csv(each_key+".csv", index=False)
        
#         # elif each_key == 'colony_morphology':
            
#         #     # results['method'].dtype == np.object_
#         #     # results['method'] = results['method'].str.replace('\n','')
          
#         #     results.to_csv(each_key+".csv", index=False)
#         #     # time.sleep(10)
#         #     with open(each_key+".csv",'r',encoding="utf8") as f:
#         #         data = f.read()
#         #         # print(data)
           
#         #     result =  pd.read_csv(io.StringIO(re.sub('"\s*\n','"',data)))
            
            
#         #     for col in result.columns:
         
                
#         #         if result[col].dtype == np.object_:
                    
#         #             a = (result[col].str.contains(r"\n"))
                     
#         #             if a.any() == True:
#         #                 print(col,'true')
#         #                 log_one.warning('line break problem' + ' , ' + 'table_name:' + each_key + ' , ' + 'col_name:' + col)	

                        
                        
                        
#         #             result[col] = result[col].str.replace('\n','')
#         #     result.to_csv(each_key+".csv", index=False)
            
        
#         # elif each_key == 'culture_medium':
            
#         #     # results['method'].dtype == np.object_
#         #     # results['method'] = results['method'].str.replace('\n','')
          
#         #     results.to_csv(each_key+".csv", index=False)
#         #     # time.sleep(10)
#         #     with open(each_key+".csv",'r',encoding="utf8") as f:
#         #         data = f.read()
#         #         # print(data)
           
#         #     result =  pd.read_csv(io.StringIO(re.sub('"\s*\n','"',data)))
            
            
#         #     for col in result.columns:
         
                
#         #         if result[col].dtype == np.object_:
                    
#         #             a = (result[col].str.contains(r"\n"))
                     
#         #             if a.any() == True:
#         #                 print(col,'true')
#         #                 log_one.warning('line break problem' + ' , ' + 'table_name:' + each_key + ' , ' + 'col_name:' + col)	

                        
                            
                            
#         #                 result[col] = result[col].str.replace('\n','')
#         #         result.to_csv(each_key+".csv", index=False)
        

#         # elif each_key == 'origin':
            
#         #     # results['method'].dtype == np.object_
#         #     # results['method'] = results['method'].str.replace('\n','')
          
#         #     results.to_csv(each_key+".csv", index=False)
#         #     # time.sleep(10)
#         #     with open(each_key+".csv",'r',encoding="utf8") as f:
#         #         data = f.read()
#         #         # print(data)
           
#         #     result =  pd.read_csv(io.StringIO(re.sub('"\s*\n','"',data)))
            
            
#         #     for col in result.columns:
         
                
#         #         if result[col].dtype == np.object_:
                    
#         #             a = (result[col].str.contains(r"\n"))
                     
#         #             if a.any() == True:
#         #                 # print(col,'true')
#         #                 log_one.warning('line break problem' + ' , ' + 'table_name:' + each_key + ' , ' + 'col_name:' + col)	

#         #             b =  (result[col].str.contains(r'\\'))
                     
#         #             if b.any() == True:
                        
                         
#         #                 log_one.warning('Unescaped backslash' + ' , ' + 'table_name:' + each_key + ' , ' + 'col_name:' + col)
                          
                        
                        
#         #             result[col] = result[col].str.replace('\n','')
#         #             result[col] = result[col].str.replace('\\','/')
#         #             # result[col] = result[col].str.decode('unicode_escape')
#         #     result.to_csv(each_key+".csv", index=False)


#         # elif each_key == 'strain_history':
            
#         #     # results['method'].dtype == np.object_
#         #     # results['method'] = results['method'].str.replace('\n','')
          
#         #     results.to_csv(each_key+".csv", index=False)
#         #     # time.sleep(10)
#         #     with open(each_key+".csv",'r',encoding="utf8") as f:
#         #         data = f.read()
#         #         # print(data)
           
#         #     result =  pd.read_csv(io.StringIO(re.sub('"\s*\n','"',data)))
            
            
#         #     for col in result.columns:
         
                
#         #         if result[col].dtype == np.object_:
                    
#         #             a = (result[col].str.contains(r"\n"))
                     
#         #             if a.any() == True:
#         #                 print(col,'true')
#         #                 log_one.warning('line break problem' + ' , ' + 'table_name:' + each_key + ' , ' + 'col_name:' + col)	

                        
                        
                        
#         #             result[col] = result[col].str.replace('\n','')
#         #     result.to_csv(each_key+".csv", index=False)


#         # elif each_key == 'sequence':
            
#         #     # results['method'].dtype == np.object_
#         #     # results['method'] = results['method'].str.replace('\n','')
          
#         #     results.to_csv(each_key+".csv", index=False)
#         #     # time.sleep(10)
#         #     with open(each_key+".csv",'r',encoding="utf8") as f:
#         #         data = f.read()
#         #         # print(data)
           
#         #     result =  pd.read_csv(io.StringIO(re.sub('"\s*\n','"',data)))
            
            
#         #     for col in result.columns:
         
                
#         #         if result[col].dtype == np.object_:
                    
#         #             a = (result[col].str.contains(r"\n"))
                     
#         #             if a.any() == True:
#         #                 print(col,'true')
#         #                 log_one.warning('line break problem' + ' , ' + 'table_name:' + each_key + ' , ' + 'col_name:' + col)	

                        
                        
                        
#         #             result[col] = result[col].str.replace('\n','')
#         #     result.to_csv(each_key+".csv", index=False)


#         # elif each_key == 'strain_synonyms':
            
#         #     # results['method'].dtype == np.object_
#         #     # results['method'] = results['method'].str.replace('\n','')
          
#         #     results.to_csv(each_key+".csv", index=False)
#         #     # time.sleep(10)
#         #     with open(each_key+".csv",'r',encoding="utf8") as f:
#         #         data = f.read()
#         #         # print(data)
           
#         #     result =  pd.read_csv(io.StringIO(re.sub('"\s*\n','"',data)))
            
            
#         #     for col in result.columns:
         
                
#         #         if result[col].dtype == np.object_:
                    
#         #             a = (result[col].str.contains(r"\n"))
                     
#         #             if a.any() == True:
#         #                 print(col,'true')
#         #                 log_one.warning('line break problem' + ' , ' + 'table_name:' + each_key + ' , ' + 'col_name:' + col)	

                        
                        
                        
#         #             result[col] = result[col].str.replace('\n','')
#         #     result.to_csv(each_key+".csv", index=False)

 
#         # elif each_key == 'culture_condition':
            
#         #     # results['method'].dtype == np.object_
#         #     # results['method'] = results['method'].str.replace('\n','')
          
#         #     results.to_csv(each_key+".csv", index=False)
#         #     # time.sleep(10)
#         #     with open(each_key+".csv",'r',encoding="utf8") as f:
#         #         data = f.read()
#         #         # print(data)
           
#         #     result =  pd.read_csv(io.StringIO(re.sub('"\s*\n','"',data)))
            
            
#         #     for col in result.columns:
         
                
#         #         if result[col].dtype == np.object_:
                    
                 
#         #             a = (result[col].str.contains(r"\n"))
                     
#         #             if a.any() == True:
#         #                 print(col,'true')
#         #                 log_one.warning('line break problem' + ' , ' + 'table_name:' + each_key + ' , ' + 'col_name:' + col)	
 
                        
                       
#         #             result[col] = result[col].str.replace('  ','')    
#         #             result[col] = result[col].str.replace('\n','')
#         #     result.to_csv(each_key+".csv", index=False)


#         # elif each_key == 'field_basic_definition':
            
#         #     # results['method'].dtype == np.object_
#         #     # results['method'] = results['method'].str.replace('\n','')
          
#         #     results.to_csv(each_key+".csv", index=False)
#         #     # time.sleep(10)
#         #     with open(each_key+".csv",'r',encoding="utf8") as f:
#         #         data = f.read()
#         #         # print(data)
           
#         #     result =  pd.read_csv(io.StringIO(re.sub('"\s*\n','"',data)))
            
            
#         #     for col in result.columns:
         
                
#         #         if result[col].dtype == np.object_:
                    
#         #             a = (result[col].str.contains(r"\n"))
                     
#         #             if a.any() == True:
#         #                 print(col,'true')
#         #                 log_one.warning('line break problem' + ' , ' + 'table_name:' + each_key + ' , ' + 'col_name:' + col)	
 
                        
                       
                       
#         #             result[col] = result[col].str.replace('\n','')
#         #     result.to_csv(each_key+".csv", index=False)


#         # elif each_key == 'multimedia':
            
#         #     # results['method'].dtype == np.object_
#         #     # results['method'] = results['method'].str.replace('\n','')
          
#         #     results.to_csv(each_key+".csv", index=False)
#         #     # time.sleep(10)
#         #     with open(each_key+".csv",'r',encoding="utf8") as f:
#         #         data = f.read()
#         #         # print(data)
           
#         #     result =  pd.read_csv(io.StringIO(re.sub('"\s*\n','"',data)))
            
            
#         #     for col in result.columns:
                
                
             
                
#         #         if result[col].dtype == np.object_:
                    
#         #             a = (result[col].str.contains(r"\n"))
                     
#         #             if a.any() == True:
#         #                 # print(col,'true')
#         #                 log_one.warning('line break problem' + ' , ' + 'table_name:' + each_key + ' , ' + 'col_name:' + col)	
 
#         #             b =  (result[col].str.contains(r'\\'))
                    
#         #             if b.any() == True:
                        
#         #                 log_one.warning('Unescaped backslash' + ' , ' + 'table_name:' + each_key + ' , ' + 'col_name:' + col)
                        
                       
                       
#         #             result[col] = result[col].str.replace('\n','')
             
#         #             result[col] = result[col].str.replace('\\','/')
#         #             # result[col] = result[col].str.decode('unicode_escape')
#         #     result.to_csv(each_key+".csv", index=False)


#         # elif each_key == 'biosample':
            
#         #     # results['method'].dtype == np.object_
#         #     # results['method'] = results['method'].str.replace('\n','')
          
#         #     results.to_csv(each_key+".csv", index=False)
#         #     # time.sleep(10)
#         #     with open(each_key+".csv",'r',encoding="utf8") as f:
#         #         data = f.read()
#         #         # print(data)
           
#         #     result =  pd.read_csv(io.StringIO(re.sub('"\s*\n','"',data)))
            
            
#         #     for col in result.columns:
                
                
             
                
#         #         if result[col].dtype == np.object_:
                    
#         #             a = (result[col].str.contains(r"\n"))
                     
#         #             if a.any() == True:
#         #                 # print(col,'true')
#         #                 log_one.warning('line break problem' + ' , ' + 'table_name:' + each_key + ' , ' + 'col_name:' + col)	
 
#         #             b =  (result[col].str.contains(r'\\'))
                    
#         #             if b.any() == True:
                        
#         #                 log_one.warning('Unescaped backslash' + ' , ' + 'table_name:' + each_key + ' , ' + 'col_name:' + col)
                        
                       
                       
#         #             result[col] = result[col].str.replace('\n','')
             
#         #             result[col] = result[col].str.replace('\\','/')
#         #             # result[col] = result[col].str.decode('unicode_escape')
#         #     result.to_csv(each_key+".csv", index=False)
        


# logging.shutdown()       

            
