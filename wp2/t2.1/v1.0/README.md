# Steps to transform Diaspora database into RDF by using [SDM-RDFIzer](https://github.com/SDM-TIB/SDM-RDFizer) and [RML](https://rml.io/specs/rml/#overview-0) mapping rules 
 
# We have two folders here
      1. mappings: contains all the mapping files. 
      2. pipeline: contains all the codes, scripts used to transform the diaspora database into rdf.
 
# pipeline Folder: 
   
## diaspora_to_csv Folder:
     1. Contains python script that will connect to the mysql workbench and then will transform its bacdive database into csv format, there is also a separate config file to add the table names.  
     
## diaspora_rdf_map Folder:
     1. Contains SDM-RDfizer tool and a python file to create config file that will be used to run the SDM-RDFizer. 
     2. There is a folder named exam  and inside this folder, we have some mapping rules files that is used to 
        convert the csv file into rdf transformations. There is one folder output which is used to store the rdf transformed files. 
     3. rdf.py has a parameter "number_of_datasets", currently we are transforming 68 csv files that's why the parameter is set to 68 and can be changed accoring to   the number of csv files.
    
 For detailed information on SDM-RDFizer please visit [SDM-RDFizer](https://github.com/SDM-TIB/SDM-RDFizer)

## Diaspora_store_to_graph Folder
    1. Contains python script to store generated rdf files into the graph database. 
       -> For installing GraphDB, follow the link:
          - [GraphDB](https://graphdb.ontotext.com/documentation/free/free/run-desktop-installation.html)
    
    
## Query_diaspora Folder
    1. Contains script to query the rdf files store in the graph database, and convert in into the rdf triples for the validation. 
    
## validate_diaspora Folder
    1. contains python script for the query validation, here we can validate the query results and the actual results. 
    
## We have used [jenkins_pipeline](https://www.jenkins.io/doc/book/installing/) for the above steps, our pipeline will transform the database tables into csv and then will create rdf transformations of those csv file, will store it into the graph databse and will query the rdf files stored in the database. We have created four jobs for that, one job for each step. 
    1. In the Jobs folder, there are config files for each job. 
    2. copy these config files to your job folder inside your jenkins directory respectively.
    3. Go to your jenkins local instance and click on manage jenkins there we have "reload configuration from disk" option, click on this option. 
    
## Steps to create jenkins jobs: 
     1. Install jenkins and create six freestyle jobs:
            - clean_workspace
            - prepare_workspace
            - diaspora_to_csv
            - diaspora_rdf_map
            - Diaspora_store_to_graph
            - Query_diaspora
            - validate_diaspora
         
           
     2. After installing jenkins; go the .jenkins folder in your directory where jenkins has been installed, now go the workspace folder inside the .jenkins folder, there you will see workspace has already been created for the 4 freestyle projects that you have created. 
     
     3. Copy the contents of the above folders ( prepare_workspace, diaspora_to_csv, diaspora_rdf_map, Diaspora_store_to_graph, Query_diaspora, validate_diaspora, clean_workspace ) respectively. 
 
 ## Inside the automate folder there are two files:
     1. automate.py, is a python script to run our jenkins pipeline from any IDE'S or terminal.  
     2. jobs.properties is a config file, where we can specify the jobs and their order of execution. 
     
 ## Steps to run complete jenkins pipeline
     1. create a folder "automate" on your pc and copy automate.py and jobs.properties into it, please change the username and password of your jenkins instance inside the automate.py file 
On the terminal run <mark> "python automate.py" </mark> and you can see the results whether the job is success or failure on your terminal. Go to the jenkins workspace to check the outputs
