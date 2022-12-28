# -*- coding: utf-8 -*-


from SPARQLWrapper import SPARQLWrapper, XML, JSON, TURTLE, CSV
import requests
import time
import pandas as pd
import os
import sys


from SPARQLWrapper import SPARQLWrapper

sparql = SPARQLWrapper("http://graphdb:7200/repositories/Diaspora")

sparql.setQuery("""

 PREFIX hybrid3: <https://materials.hybrid3.duke.edu/materials/> 
 PREFIX matonto: <http://matonto.org/ontology/matonto#> 
 PREFIX owl: <http://www.w3.org/2002/07/owl#> 
 PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
 PREFIX sosa: <http://www.w3.org/ns/sosa/> 
 PREFIX ssn: <http://www.w3.org/ns/ssn/> 
 PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
 PREFIX rml: <http://semweb.mmlab.be/ns/rml#>
 PREFIX ql: <http://semweb.mmlab.be/ns/ql#> 
 PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
 PREFIX bacdive: <http://kg.bacdive.dsmz.de/>

CONSTRUCT {
    ?s bacdive:has_cell_len ?cell_len;
       bacdive:has_cell_shape ?cell_shape.
        
           ?st bacdive:has_domain ?strain_domain.
}


where {
    
    ?s a bacdive:Cell_morphology;
       bacdive:has_cell_len ?cell_len;
       bacdive:has_cell_shape ?cell_shape;
       bacdive:has_strain ?st.
           ?st a bacdive:Strain;
               bacdive:has_domain ?strain_domain.
}


""")


results = sparql.queryAndConvert()
print(results.serialize('./actual_result/query1.ttl'))
