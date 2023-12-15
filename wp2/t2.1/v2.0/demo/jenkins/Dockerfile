
FROM jenkins/jenkins:latest

USER root

RUN apt-get update && apt-get install -y lsb-release

RUN apt-get install -y python3-pip

#RUN apt-get update && apt-get install default-mysql-server
RUN apt update
RUN apt install wget

#RUN apt-get install default-mysql-client -y

RUN apt install mariadb-server -y


RUN pip install --upgrade pip

RUN pip3 install requests 

RUN pip3 install pandas

RUN pip3 install numpy

RUN pip3 install rdflib

RUN pip3 install natsort

RUN pip3 install configparser

RUN pip3 install psycopg2-binary

RUN pip3 install sparqlwrapper

RUN pip3 uninstall mysql-connector
RUN pip3 install mysql-connector-python

RUN pip3 install PyMySQL

RUN pip3 install PyMySQL[rsa]

RUN pip3 install cryptography






USER jenkins

RUN jenkins-plugin-cli --plugins "blueocean:1.25.5 docker-workflow:1.28"





