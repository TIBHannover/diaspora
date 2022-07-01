# Transformation of Bacdive database into RDF by using one to one [RML](https://rml.io/specs/rml/#overview-0) mapping rules and [SDM-RDFIzer](https://github.com/SDM-TIB/SDM-RDFizer) 

For creating one to one rml mapping rules, CI/CD automation pipeline is used that will run all the steps from fetching the bacdive database, converting it into csv, cleaning it, transformaing it into rdf triples, storing the triples into the triple store, querying and validating the triples. For this automation, [Python](https://www.python.org/downloads/) , Jenkins and GraphDB is required. Follow the below steps in order to install GraphDB and jenkins on windows. 

      
# Install prerequisites:

  

  ## steps to install GraphDB as a desktop installation:
  1. Go to [GraphDB](https://www.ontotext.com/products/graphdb/graphdb-free/) Free and request your GraphDB copy. You will receive an email with the download link. 
  2. For windows, follow the steps: 
       1. Download your GraphDB .exe file.
       2. Double-click the application file and follow the on-screen installer prompts.
       3. Locate the GraphDB application in the Windows Start menu and start the database. The GraphDB Server and Workbench open at http://localhost:7200/.
       4. Create a repository in GraphDB with the name "Diaspora" for storing the generated rdf triples, see below:
       ![Graphdb](https://user-images.githubusercontent.com/55106484/176881416-3f39143e-6615-4e83-9f04-80338fc589dc.PNG)
  
  ## Steps to install [jenkins](https://www.jenkins.io/doc/book/installing/windows/) on windows: 
   1. First of all, we need [Java 8 or 11](https://www.java.com/en/download/help/windows_manual_download.html) to run Jenkins .
   2. Go [here](https://www.jenkins.io/download/#downloading-jenkins) and install the Windows version
   3. Open the installer and follow the steps of the setup wizard. Use all default parameters unless creating the user and the password for jenkins.
   4. Go to http://localhost:8080 and it will ask you for a password. To find it go to C:\Program Files\Jenkins\secrets and open the file initialAdminPassword, it contains the password.
   5. Now selecct the suggested plugins option and you will be done.
 
# Configuring the automation pipeline, currently working with windows environment. 

1.Create a local path for the Git repository e.g., in C:\Users\<your_user>\Desktop\diasp. This will be used as local_repo_path in next steps:
```
git clone https://github.com/TIBHannover/diaspora.git
```

2. Access repository:

```
cd disapora
```

3. Copy the files in the jenkins directory

```
xcopy wp2\t2.1\v1.0\pipeline\jobs C:\Users\<your_user>\.jenkins\jobs /I /H /C /E
xcopy wp2\t2.1\v1.0\pipeline\workspace C:\Users\<your_user>\.jenkins\workspace /I /H /C /E
```

4. In jenkins, click on Manage Jenkins and then in the bottom part of the page click "reload configuration from disk"

5. Specify the path of the python, jenkins workspace, xcopy and cloned repository in the jenkins environment variable, for that inside the manage jenkins option, go to configure system and then go to global properties and enable environment variables option. specify the names of the path as mentioned below:

![path1](https://user-images.githubusercontent.com/55106484/176921715-b0aa112e-3798-4a5d-89ba-a69a4866c69e.PNG)

![path2](https://user-images.githubusercontent.com/55106484/176921732-c61b989e-9c2a-49ed-8f4b-6e7229004eae.PNG)

# Running the pipeline

Go to the automation file
```
cd wp2\t2.1\v1.0\pipeline\automate
python automate.py
```
# Pipeline details and explanation:
      1. mappings: contains all the mapping files. 
      2. pipeline: contains all the codes, scripts used to transform the diaspora database into rdf.
         1. Inside pipeline folder, there are three folder automate, jobs and workspace.
            - Workspace folder contains the jobs that are required for the transformation of bacdive database into rdf.
              - diaspora_to_csv Folder:
                 1. Contains python script that will connect to the mysql workbench and then will transform its bacdive database into csv format, there is also a                           separate config file to add the table names.  
                 2. This script will take bacdive database as an input and will convert its tables into csv for the rdf transformation. 


              - diaspora_rdf_map Folder:
                 1. Contains SDM-RDfizer tool and a python file to create config file that will be used to run the SDM-RDFizer. 
                 2. There is a folder named exam and inside this folder, we have some mapping rules files that is used to 
                    convert the csv file into rdf transformations. There is one folder output which is used to store the rdf transformed files. 
                 3. rdf.py has a parameter "number_of_datasets", currently we are transforming 68 csv files that's why the parameter is set to 68 and can be changed                       according to the number of csv files.

                 For detailed information on SDM-RDFizer please visit [SDM-RDFizer](https://github.com/SDM-TIB/SDM-RDFizer)

              - Diaspora_store_to_graph Folder
                 1. Contains python script to store generated rdf files into the graph database. 


    
              - Query_diaspora Folder
                 1. Contains script to query the rdf files store in the graph database, and convert in into the rdf triples for the validation. 
    
              - validate_diaspora Folder
                 1. contains python script for the query validation, here we can validate the query results and the actual results. 
                        - Jobs folder contains config files of the jobs, these config files will have all the steps and configuration that is required to run the job.
                        - automate folders contains python file that run all the jobs one by one it also contains config file to specify which job we need to run and
                          the order.


   

    

