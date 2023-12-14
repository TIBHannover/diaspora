# Containerized version of the Bacdive Database

This is the containerized version of the RDF counterpart of the Bacdive database produced by TIB in the context of the DIASPora project.

In order to automate the transformation process and control the input tables as well as the intermediate and final outputs, a CI/CD automation pipeline has been employed.

The pipeline is maintained under the same source control and versioning mechanisms to facilitate access, configuration, and re-execution. 
The pipeline is composed of a sequence of steps, each performing a set of related operations e.g., fetching data from the Bacdive database, converting into csv, cleaning, transforming into RDF triples, storing the triples in the triple store of choice, querying and validating the triples. 

# In order to run the pipeline and the steps following have been used:
           1 Python
           2 MySQL workbench
           3 Jenkins 
           4 GraphDB 
  To install the software, docker compose has been used which makes the installation of the software much easier and maintainable. 

# Installation prerequisites:

  ## Installation of docker environment:
     1 Update the apt package index and install packages to allow apt to use a repository over HTTPS:
     
         ```
           sudo apt-get update
           sudo apt-get install \
           ca-certificates \
           curl \
           gnupg \
           lsb-release
          
          ```
      2 Add Docker’s official GPG key:
          ```
          sudo mkdir -p /etc/apt/keyrings
          
          curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
       
          
          ```
      3 Use the following command to set up the repository:
          ```
          echo \
         "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
          $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
       
          
          ```
       4 Install Docker Engine
       
       
          ```
             sudo apt-get update
             sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin
       
          ```
     
 # Deploying the pipeline:
 
 1. Create a local path for the Git repository e.g., in C:\Users\<user>\github\projects. This will be used as `local_repo_path` in the next steps:

 2. Change to `local_repo_path` 

 3. Clone the GitHub repository to `local_repo_path` 
    ```
     git clone -b Diaspora_v2_1 https://github.com/TIBHannover/diaspora.git
    ```

 4. Access repository:

  ```
     cd diaspora/wp2/t2.1/v2_1/docker/linux
     
  ```
 5. Run the command:
     ```
     docker compose up
     
     ```
 6. Executing the jenkins pipeline:
    1. Once all the docker is running, go to folder:
    
     ```
     cd diaspora/wp2/t2.1/v2_1/docker/linux/automate
     
     ```
     2. Run the command:

     ```
     pip3 install python-jenkins
     pip3 install jenkinsapi
     python3 automate.py
     
     ```
     This script contains python file to run all the jobs of jenkins pipeline, this script will take the names of the jobs from the file jobs.properties
     which is alsp present in the automate folder.
  
  7. Accessing GraphDB repository.
     once, all the jobs are executed go to: 
      ```
      http://server_url:7200 (replace server url with the actual url of the server or localhost if the application is deployed on the local)
      ```
      and here in the repository named "Diaspora_v2_1", all the transformed RDF triples are stored:

     ![diaspora](https://github.com/TIBHannover/diaspora/assets/55106484/0f599536-a563-4c8a-8881-c2e553e45bf6)

     Approx. 22 million triples are stored in the repository "Diapora_v2_1" .
     
 
 # Understanding BacDive Knowledge Graph:


   In the BacDive database everything is centered around strains, so the data can be explored by doing the query which explores everything that is linked to strain:

   ![sparql4](https://github.com/TIBHannover/diaspora/assets/55106484/90c30728-b793-4002-b2fd-547c64ad9b34)

   This query will give information about the characteristics related to strain.

   Output looks like this:
   
   ![Capture5](https://github.com/TIBHannover/diaspora/assets/55106484/c1408d80-6638-49d8-a92f-6606c7bece5e)

   Foy visualizing any subject can be copied and put in the easy graph under visual graph section:

   ![st2](https://github.com/TIBHannover/diaspora/assets/55106484/7c880695-dbed-4c96-80ae-0b839695d2cc)

   by doing this, visualization can be done:

   
  ![Capture7](https://github.com/TIBHannover/diaspora/assets/55106484/db8296b5-6027-4748-ab95-1b941aafea50)


  any node can be expanded by double clicking it and all the characteristics that are associated with it can be visualized. 
  By single clicking the node all the information 
  associated with the node can be seen on the right hand side bar.



[Competency questions](https://github.com/TIBHannover/diaspora/blob/Diaspora_v2_1/wp2/t2.1/v2_1/docker/linux/Competency%20questions/queries.txt) contains few queries that can be used to query BacDive knowledge graph. 

# Federated Search

  
SPARQL is a fundamental part of the Semantic Web technology stack. It enables the retrieval and integration of data from various sources that expose RDF data, promoting data interoperability and integration. For example, it can be used to query data from multiple RDF sources.

BacDive knowledge graph can also be linked to other bioinformatics Sparql endpoints such as [Uniprot](https://www.uniprot.org/). 

The information from uniprot can be combined with bacDive database using federated query for better outcomes, which will enhance the overall productivity of the bioinformatics domain.

(Federated query)[https://github.com/TIBHannover/diaspora/blob/Diaspora_v2_1/wp2/t2.1/v2_1/docker/linux/Competency%20questions/federated_query.txt) contains a federated query between (BacDive)[https://bacdive.dsmz.de/] and (Uniprot)[https://www.uniprot.org/].

For example:

![fede](https://github.com/TIBHannover/diaspora/assets/55106484/c3a1884c-23b2-4230-84f8-a8dbf9d8663c)

Outcome of above query looks like this:

![fede1](https://github.com/TIBHannover/diaspora/assets/55106484/e2bb6254-b303-4757-84ab-4750d4faae81)

  
