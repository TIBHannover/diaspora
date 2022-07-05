# -*- coding: utf-8 -*-


import jenkins 
import time
from jenkinsapi.jenkins import Jenkins
# It comes with pip module python-jenkins
# use pip to install python-jenkins

# Jenkins Authentication URL

JENKINS_URL = 'http://localhost:8080'
JENKINS_USERNAME = "rohit"
JENKINS_PASSWORD = "krishnamaa9$R"


import configparser


""" reading the path from path.properties file,specify the path of path.properties file """

config = configparser.ConfigParser()

''' specify the path of path.properties file here '''

config.readfp(open('./jobs.properties'))


server = Jenkins(JENKINS_URL, username = JENKINS_USERNAME , password = JENKINS_PASSWORD)


server_build = jenkins.Jenkins(JENKINS_URL, username=JENKINS_USERNAME, password=JENKINS_PASSWORD)


    
for each_section in config.sections(): 
    for each_key, each_val in config.items(each_section):
        
        print(each_key, each_val)
        
        print(each_val)
        
        # build_number = server_build.get_job_info(each_val)['nextBuildNumber']['lastCompletedBuild']['number']
        build_number = server_build.get_job_info(each_val)['lastCompletedBuild']['number']

        job_instance = server.get_job(each_val)
    
        server_build.build_job(each_val)
        build_info = server_build.get_build_info(each_val,build_number)
        
        
        duration = build_info['duration']
        print(duration)
        
            
       
        print((duration/1000))
        time.sleep((duration/1000) + 10)
        
        latestBuild = job_instance.get_last_build()
                    
       
        # time.sleep(20)
        
        if (latestBuild.get_status()) == 'SUCCESS':
            print('job is success', build_number)
        else:
            print('job is failure')
        
        print(server_build.get_build_console_output(each_val,build_number))
        
        
        










    