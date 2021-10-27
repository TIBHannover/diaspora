# How to run the motivating example?
To run the motivating example, install docker in your machine and then:

`docker run -d -p 4000:4000 -v /../SDM-RDFizer-Experiments/cikm2020/motivating-example:/data sdmtib/sdmrdfizer-server:3.2`

`curl http://localhost:4000/graph_creation/data/config.ini`
 		

Your results will be in the output folder (automatically created in this folder from the docker image)


