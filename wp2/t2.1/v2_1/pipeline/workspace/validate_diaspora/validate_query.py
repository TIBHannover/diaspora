# -*- coding: utf-8 -*-


import os 
import sys

from pathlib import Path

from rdflib import Graph
from rdflib.compare import to_isomorphic, graph_diff


__file__ = 'validate_query.py'

base_path = Path(__file__).parent

print(base_path)

path = (base_path / '../Query_diaspora/expected_result/').resolve()

print(path)

path2 = (base_path / '../Query_diaspora/actual_result/').resolve()

print(path2)

os.chdir(path)
result1 = []
for f in os.listdir():
    print(f)
    a = os.path.join(path,f)
    result1.append(a)
  
# print(result1)
    
os.chdir(path2)
result2 = []
for f1 in os.listdir():
    print(f1)
    a1 = os.path.join(path2,f1)
    result2.append(a1)

# print(result2)

result = [None]*(len(result1)+len(result2))
result[::2] = result1
result[1::2] = result2

print(result)





for (i,k) in zip(result[::2],result[1::2]):
    print('start_validating')
    # print(i)
    # print(k)
    
    g = Graph()
    g.parse(i)
    
    # print(g)
    # print(len(g))
    
    g1 = Graph()
    g1.parse(k)
    
    # print(g)
    # print(len(g1))
    
    iso1 = to_isomorphic(g)
    iso2 = to_isomorphic(g1)

    if iso1 == iso2:
        print('true')
    else:
        print('false')
        break

    

