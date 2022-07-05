# Semantic Transformation of the Bacdive Database 

This is version 1.0.0 of the RDF counter part of Backdive database produced by TIB in the context of the DIASPora project. Version 1.0.0 is a direct map of the database, meaning tit does not annotate the original data with external ontologies, instead it utilizes the structure of the database as its RDF graph structure. Future versions will iteratively add ontologies.
Transformation is done using RML mappings and rules.

In order to automate teh transformation process and contril over the input tables as well as the intermediate and final outputs, a CI/CD automation pipeline is used. The pipeline is mainatained under the same cource control and versioning mechanisms to facilitate access, configuration, and re-execution. The pipeline is composed of a series of steps, each performing a set of related operations e.g., fetching data from the Bacdive database, converting into csv, cleaning, transformaing into RDF triples, storing the triples into the triple store of choice, and querying and validating the triples. In order to run the pipeline and the steps [Python](https://www.python.org/downloads/), SQL workbench, Jenkins and GraphDB are required, which should be insllaed as follows: 

      
# Installation prerequisites:

 
  ## install GraphDB (as a desktop installation):
  1. Go to [GraphDB](https://www.ontotext.com/products/graphdb/graphdb-free/) Free and request your GraphDB copy. You will receive an email with the download link. 
  2. For windows, follow the steps: 
       1. Download your GraphDB .exe file.
       2. Double-click the application file and follow the on-screen installer prompts.
       3. Locate the GraphDB application in the Windows Start menu and start the database. The GraphDB Server and Workbench open at http://localhost:7200/.
       4. Create a repository in GraphDB with the name `Diaspora` for storing the generated RDF triples, see below:
       ![Graphdb](https://user-images.githubusercontent.com/55106484/176881416-3f39143e-6615-4e83-9f04-80338fc589dc.PNG)
  3. For Linux, follow the steps:
       1. Download the GraphDB .rpm or .deb file.
       2. Install the package with sudo rpm -i or sudo dpkg -i and the name of the downloaded package. Alternatively, you can double click the package name.
       3. Start the database by clicking the application icon. The GraphDB Server and Workbench open at http://localhost:7200/.

      
  ## Steps to install [jenkins](https://www.jenkins.io/doc/book/installing/): 
  1. For [windows](https://www.jenkins.io/doc/book/installing/windows/)
       1. Install [Java 8 or 11](https://www.java.com/en/download/help/windows_manual_download.html).
       2. Visit the [Jenkins](https://www.jenkins.io/download/#downloading-jenkins) download page and choose the Windows version. Download the selected file.
       3. Open the installer and follow the steps of the setup wizard. Use all default parameters unless creating the user and the password for jenkins.
       4. Open http://localhost:8080 in your browser. Login using the initial password (you can find the initial password in C:\Program Files\Jenkins\secrets\initialAdminPassword file)
       5. Select the suggested plugins option and you are done.
  2. For [Linux](https://www.jenkins.io/doc/book/installing/linux/)
       1. Install java with commands:

          ```
          sudo apt update
          sudo apt install default-jdk
          
          ```
       2. Install debian packages from here [Jenkins Debian Packages](https://pkg.jenkins.io/debian-stable/):
       3. Update the apt package list and install the latest version of Jenkins:
          ```
             sudo apt update
             sudo apt install jenkins
          
          ```
       4. Enable and start the Jenkins service by executing:
          ```
            sudo systemctl enable --now jenkins
          ```
       5. To start the setup process, go to http://localhost:8080/ and it will ask you for a password. To find the password go to: 
            ```
              sudo cat /var/lib/jenkins/secrets/initialAdminPassword
            ```
       6. Now select the suggested plugins option and you are done.
       
  ## Steps to install SQL Workbench for windows:
  1. The MySQL  installer download is available [here](https://dev.mysql.com/downloads/windows/installer/).
  2. After downloading the installer we can select the setup type, depending upon the requirement. 
  3. Provide username and password and you are good to go. 
  4. Once everything is setup, load the database dump into the workbench:
     - For that go on the server option and click data import and then import can be done, select import from self-contained file and load the database dump. 
     - copy the database dump into your jenkins workspace:
      ```
      xcopy wp2\t2.1\v1.0\pipeline\jobs C:\Users\<your_user>\.jenkins\database_dump  /I /H /C /E
      ```
     - The dump file is a zip, please unzip it before importing it into SQL workbench. 


  ![i8mport](https://user-images.githubusercontent.com/55106484/177311543-dde6ac6f-1ac8-491e-af20-51d7bad2c23f.PNG)



       
# Configuring the automation pipeline (currently working on Windows only): 

1.Create a local path for the Git repository e.g., in C:\Users\<your_user>\github\projects. This will be used as local_repo_path in next steps:

2. Chnage to local_repo_path 

3. Clone the GitHb repository to local_repo_path 
```
git clone https://github.com/TIBHannover/diaspora.git
```

4. Access repository:

```
cd disapora
```
Now, you should be in `C:\Users\<your_user>\github\projects\diaspora`

5. Copy the files in the jenkins directory

```
xcopy wp2\t2.1\v1.0\pipeline\jobs C:\Users\<your_user>\.jenkins\jobs /I /H /C /E
xcopy wp2\t2.1\v1.0\pipeline\workspace C:\Users\<your_user>\.jenkins\workspace /I /H /C /E
```

6. In jenkins, click on Manage Jenkins and then in the bottom part of the page click "reload configuration from disk"

7. Specify the path of the python, jenkins workspace, xcopy and cloned repository in the jenkins environment variable. For that inside the manage jenkins option, go to configure system and then go to global properties and enable environment variables option. Specify the names of the path as mentioned below:

![path](https://user-images.githubusercontent.com/55106484/176935037-04442cb2-a133-4a08-8125-61df1053c58a.PNG)

![p](https://user-images.githubusercontent.com/55106484/176946958-de23c907-575b-46e4-af55-265a34581ec1.PNG)


8. Once Jenkins workspace is ready and all the jobs are inside the workspace, then go to the db_to_csv.py file inside diaspora_to_csv folder and put the credentials of    your sql workbench in order to connect to the database.    

   ![db](https://user-images.githubusercontent.com/55106484/176936219-6b697cb6-89d6-41c3-ab88-04f3d5af4057.PNG)
   
   Also in order to connect to the jenkins instance, go to automate.py file indise automate folder in your local repo path and put your jenkins credentials.
   
   ![jenkins](https://user-images.githubusercontent.com/55106484/176936641-cbdf7e20-fe02-43e4-81c5-9f7d432b9722.PNG)

# Running the pipeline



Go to the automation file
```
cd wp2\t2.1\v1.0\pipeline\automate
python automate.py
```
# Pipeline details and explanation:
      1. mappings: contains all the mapping files. 
      2. pipeline: contains all the codes, scripts used to transform the diaspora database into RDF.
         1. Inside the `pipeline` folder, there are three folders `automate`, `jobs` and `workspace`.
            - The `workspace` folder contains the jobs that are required for the transformation of Bacdive database into RDF.
              - The diaspora_to_csv folder:
                 1. Contains python script that connects to the MySql database and transforms the Bacdive database into csv format. 

              - The diaspora_rdf_map folder contains:
                 1. [SDM-RDFizer](https://github.com/SDM-TIB/SDM-RDFizer) tool and a python file to create config file that will be used to run the SDM-RDFizer. 
                 2. The `exam` folder that contains the RML mapping files. 
                 3. The `output` folder which is used to store the generated RDF files. 
                 3. An rdf.py file that has a parameter "number_of_datasets". Currently 68 tables are being transferred.
                 
              - The diaspora_store_to_graph folder:
                 1. Contains python script to store generated rdf files into the graph database. 

    
              - The query_diaspora folder:
                 1. Contains script to query the rdf files store in the graph database, and convert in into the rdf triples for the validation. 
    
              - The validate_diaspora folder:
                 1. contains python script for the query validation, here we can validate the query results and the actual results. 
                        - Jobs folder contains config files of the jobs, these config files will have all the steps and configuration that is required to run the job.
                        - automate folders contains python file that run all the jobs one by one it also contains config file to specify which job we need to run and
                          the order.
   

     3. Before each run of the pipeline the following two jobs are executed to prepare the workspace:
          - clean_workspace: It cleans the complete workspace so that multiple runs of the piep;line do not interefer with each other and always the lateset version of the mappaing and config files are used.
          - prepare_workspace: It clones the git repository to the `local_repo_path` and then copies the jobs and mapping files into respecive folders in the jenkins workspace. 

    

