# Semantic Transformation of the Bacdive Database 

This is version 1.0.0 of the RDF counterpart of the Bacdive database produced by TIB in the context of the DIASPora project. 
Version 1.0.0 is a direct map of the database, meaning TIB does not annotate the original data with external ontologies, instead, it utilizes the structure of the database as the structure of the transformed RDF graph. Future versions will iteratively add ontologies.
Transformation is done using RML mappings and rules.

In order to automate the transformation process and control the input tables as well as the intermediate and final outputs, a CI/CD automation pipeline has been employed. 
The pipeline is maintained under the same source control and versioning mechanisms to facilitate access, configuration, and re-execution. 
The pipeline is composed of a sequence of steps, each performing a set of related operations e.g., fetching data from the Bacdive database, converting into csv, cleaning, transforming into RDF triples, storing the triples in the triple store of choice, and querying and validating the triples. 
In order to run the pipeline and the steps Python, MySQL workbench, Jenkins, and GraphDB are required.
In the following sections the installation, configuration, and running of the tools as well as the pipeline are described: 

      
# Installation prerequisites:

  ## Install Python and the following dependencies:
  1. For windows: 
     1. Visit [Python](https://www.python.org/downloads/) and choose the python version and follow the steps. 
  2. For Linux:
     1. Install python with commands: 
     
          ```
           sudo apt-get update && sudo apt-get upgrade -y
           sudo apt-get install software-properties-common -y
           sudo add-apt-repository ppa:deadsnakes/ppa
           sudo apt-get install python3.10
     
          
          ```
  3. Once python is installed, install the following dependencies: 
  
       ```
                    1. pip install SPARQLWrapper rdflib pandas requests mysql-connector-python numpy logging configparser natsort Unidecode
       ```
   








 
  ## Install GraphDB (as a desktop installation):
  1. Go to [GraphDB](https://www.ontotext.com/products/graphdb/graphdb-free/) and request a free GraphDB copy. You will receive an email with the download link. 
  2. For windows, follow these steps: 
       1. Download your GraphDB.exe file.
       2. Double-click the application file and follow the on-screen installer prompts.
       3. Locate the GraphDB application in the Windows Start menu and start the database. The GraphDB Server and Workbench open at http://localhost:7200/.
       4. Create a repository in GraphDB with the name `Diaspora` for storing the generated RDF triples, see below:
       ![Graphdb](https://user-images.githubusercontent.com/55106484/176881416-3f39143e-6615-4e83-9f04-80338fc589dc.PNG)
  3. For Linux, follow these steps:
       1. Download the GraphDB .rpm or .deb file.
       2. Install the package with sudo rpm -i or sudo dpkg -i and the name of the downloaded package. Alternatively, you can double-click the package name.
       3. Start the database by clicking the application icon. The GraphDB Server and Workbench open at http://localhost:7200/.

      
  ## Steps to install [Jenkins](https://www.jenkins.io/doc/book/installing/): 
  
  1. For [Windows](https://www.jenkins.io/doc/book/installing/windows/)
       1. Install [Java 8 or 11](https://www.java.com/en/download/help/windows_manual_download.html).
       2. Visit the [Jenkins](https://www.jenkins.io/download/#downloading-jenkins) download page and choose the Windows version. Download the selected file.
       3. Open the installer and follow the steps of the setup wizard. Use all default parameters unless creating the user and the password for Jenkins.
       4. Open http://localhost:8080 in your browser. Login using the initial password (you can find the initial password in C:\Program Files\Jenkins\secrets\initialAdminPassword file)
       5. Select the suggested plugins option and you are done.
       
  2. For [Linux](https://www.jenkins.io/doc/book/installing/linux/)
       1. Install java with commands:

          ```
          sudo apt update
          sudo apt install openjdk-11-jdk
          
          ```
       2. Install Debian packages from [Jenkins Debian Packages](https://pkg.jenkins.io/debian-stable/) or add key and repositories from below:
          - Add key:
          
              ``` 
                      curl -fsSL https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo tee \
                       /usr/share/keyrings/jenkins-keyring.asc > /dev/null
                  
              ```
          - Add repository:
           
             ```
                       echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] \
                       https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
                       /etc/apt/sources.list.d/jenkins.list > /dev/null
  
              ```
           
       4. Update the apt package list and install the latest version of Jenkins:
          ```
             sudo apt-get update
             sudo apt-get install jenkins
          
          ```
       4. Enable and start the Jenkins service by executing:
          ```
            sudo systemctl enable jenkins
          ```
       5. To start the setup process, go to http://localhost:8080/ and it will ask you for a password. To find the password go to: 
            ```
              sudo cat /var/lib/jenkins/secrets/initialAdminPassword
            ```
       6. Now select the suggested plugins option and Jenkins is ready to use.
       
  ## Steps to install MySQL Workbench:
  1. For windows:
        1. The MySQL installer download is available [here](https://dev.mysql.com/downloads/windows/installer/).
        2. After downloading the installer the setup type can be selected, depending upon the requirement. 
        3. Provide username and password and it is ready to use. 
  2. For Linux:
        1. The DEB package can be installed from [here](https://dev.mysql.com/downloads/workbench/).
        2. After downloading the DEB file, go to the terminal and issue these commands:
        
 ```
             sudo apt --fix-broken install
             sudo dpkg -i <path_to_deb_file>
             sudo apt-get update
          
 ```
        

       
# Configuring the automation pipeline (currently working on Windows only): 

1. Create a local path for the Git repository e.g., in C:\Users\<your_user>\github\projects. This will be used as `local_repo_path` in the next steps:

2. Change to `local_repo_path` 

3. Clone the GitHub repository to `local_repo_path` 
```
git clone https://github.com/TIBHannover/diaspora.git
```

4. Access repository:

```
cd diaspora
```
Now, you should be in `C:\Users\<your_user>\github\projects\diaspora`

5. Copy the pipeline job config files into the Jenkins jobs directory

      ```
      xcopy wp2\t2.1\v1.0\pipeline\jobs C:\Users\<your_user>\.jenkins\jobs /I /H /C /E
      xcopy wp2\t2.1\v1.0\pipeline\workspace C:\Users\<your_user>\.jenkins\workspace /I /H /C /E
      ```
      1. Click on Manage Jenkins and then in the bottom part of the page, click "reload configuration from disk"
      2. Once relaod configuration is done, go to dispora_to_csv job in the Jenkins Dashboard and then go to configure and change the path of  "diasp" to your "local_repo_path" in the windows batch command option see below:


      ![ps](https://user-images.githubusercontent.com/55106484/178006003-2c3cfc99-376b-4dc2-b987-4a786b553281.PNG)


      ![p2](https://user-images.githubusercontent.com/55106484/178006016-d8683d12-7ac9-48ee-bce2-e85a62de058e.PNG)

6. Specify the path of the python, Jenkins workspace, xcopy, and the cloned repository in the Jenkins environment variable. For that inside the manage Jenkins option, go to configure the system and then go to global properties and enable environment variables option. Specify the names of the path as mentioned below:


![path5](https://user-images.githubusercontent.com/55106484/177336953-de05409b-45ca-4e6b-87db-6bc22ba7f177.PNG)



![path4](https://user-images.githubusercontent.com/55106484/177315862-af78f503-4673-4525-9100-adb62ca81a9e.PNG)

7. load the database dump into the workbench:

     - Go to the `local_repo_path` folder where the git repo is cloned and then go to the location:
      ```
      diaspora\wp2\t2.1\v1.0\pipeline\database_dump 
      
      ```
     - The dump file is a zip, unzip it before importing it into MySQL workbench. 
     - Go to the server option and click data import. Select import from the self-contained file and import the database dump, see below:




![import](https://user-images.githubusercontent.com/55106484/177316263-edb008f2-947e-4996-8fe7-49b28a440214.PNG)
     - In case if there is import error, then write these commands, see below:
     
       ```
          CREATE DATABASE diaspora;
          USE diaspora
      
      ```

![sql](https://user-images.githubusercontent.com/55106484/177996059-11db1332-c217-4137-b14e-0d8ace8a2ba5.PNG)

8. Cleaning and preparing the workspace:
   1. Go to the `automate` folder" inside local_repo_path:
      
       1. Inside the automate folder, go to jobs.properties file then comment out job3 to job 7 and run the automate.py Python file:

            ```
            cd wp2\t2.1\v1.0\pipeline\automate
            python automate.py
            ```

8. Once the Jenkins workspace is ready and all the jobs are inside the workspace, go to the db_to_csv.py file inside diaspora_to_csv folder and change the host, username, password, and the database name to your recently imported MySQL database.    

   ![db](https://user-images.githubusercontent.com/55106484/176936219-6b697cb6-89d6-41c3-ab88-04f3d5af4057.PNG)
   
   Also to connect to the Jenkins instance, go to automate.py file inside automate folder in your `local_repo_path` and put your Jenkins credentials there.
   
   ![jenkins](https://user-images.githubusercontent.com/55106484/176936641-cbdf7e20-fe02-43e4-81c5-9f7d432b9722.PNG)

# Running the pipeline 

1. Go to the `automate` folder"
   1. Inside the automate folder, go to jobs.properties file then comment out job1 and job 2 and run the automate.py Python file:

      ```
      cd wp2\t2.1\v1.0\pipeline\automate
      python automate.py
      ```
   
# Pipeline details and explanation:
      1. mappings: contains all the mapping files. 
      2. pipeline: contains all the codes, and scripts used to transform the diaspora database into RDF.
         1. Inside the `pipeline` folder, there are four folders `database_dump`, `automate`, `jobs`, and `workspace`.
            - The `workspace` folder contains the jobs that are required for the transformation of Bacdive database into RDF.
              - The diaspora_to_csv folder:
                 1. Contains python script that connects to the MySql database and transforms the Bacdive database into csv format. 
                 2. Contains config file which specify the table names from Bacdive database that needs to be transformed into csv format.

              - The diaspora_rdf_map folder contains:
                 1. [SDM-RDFizer](https://github.com/SDM-TIB/SDM-RDFizer) tool and a python file to create config file that will be used to run the SDM-RDFizer. 
                 2. The `Mapping` folder that contains two folders `mappings`, `output`. 
                 3. The `mappings` folder contains the RML mapping files.
                 4. The `output` folder which is used to store the generated RDF files. 
                 5. An rdf.py file that has a parameter "number_of_datasets". Currently, 68 tables are being transferred.
                 
              - The Diaspora_store_to_graph folder:
                 1. Contains python script to store generated RDF files into the graph database. 

    
              - The Query_diaspora folder:
                 1. Contains script to query the RDF files store in the graph database, and convert in into the RDF triples for the validation. 
    
              - The validate_diaspora folder:
                 1. contains python script for the validation of the query results agianst predefined expected results. 
                 
            - `jobs` folder contains config files of the jobs, these config files have all the steps and configuration that are required to run the job.
            - `automate` folder contains Python code that sequentially runs all the jobs. It also contains a config file to specify which job is needed to run and
               the order.
            - `database_dump` folder contains a zip dump file of the database.  


     3. Before each run of the pipeline the following two jobs are executed to prepare the workspace:
          - clean_workspace: It cleans the complete workspace so that multiple runs of the pipeline do not interfere with each other and always the latest version of the mapping and config files are used.
          - prepare_workspace: It clones the git repository to the `local_repo_path` and then copies the jobs and mapping files into respective folders in the Jenkins workspace. 

    

