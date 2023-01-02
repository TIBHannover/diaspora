# -*- coding: utf-8 -*-

import yaml
import io


import configparser     

""" reading the path from path.properties file,specify the path of path.properties file"""

config = configparser.ConfigParser()

''' specify the path of path.properties file here '''
config.readfp(open('./names.properties'))



''' reading names from names.properties file '''
database_name = config.get('NAMES', 'db_name' )


data = {
        
        'services':
            
            {
                'jenkins':{
                    
                    'build': './jenkins',
                    'image': 'jenkins',
                    'ports': [
                        "8080:8080",
                        "50000:50000"],
                    'priviledged':True,
                    'user':'root',
                    'volumes':[
                    './jenkins/.jen:/var/jenkins_home']
                    
                    },
                
                
                'graphdb':{
                    
                    'build': './graphdb',
                    'image': 'graphdb',
                    'ports':[
                        "7200:7200"]
                    },
                
                'db':{
                    'build':'./mysql',
                    'image':'mysql',
                    'environment':{
                        
                        'MYSQL_ROOT_PASSWORD':'root',
                        'MYSQL_DATABASE':database_name,
                        'MYSQL_USER':'user',
                        'MYSQL_PASSWORD':'pass'
                        },
                    'ports':[
                        "42333:3306"]
                    }
                
                }
        
        
        }
    

# Write YAML file
with io.open('docker-compose_try.yml', 'w', encoding='utf8') as outfile:
    yaml.dump(data, outfile, default_flow_style=False, allow_unicode=True)