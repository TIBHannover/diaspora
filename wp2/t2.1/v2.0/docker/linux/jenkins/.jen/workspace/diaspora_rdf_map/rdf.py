# -*- coding: utf-8 -*-






import configparser
import os
import sys

__file__ = 'rdf.py'


absolutepath = os.path.abspath(__file__)
print(absolutepath)

fileDirectory = os.path.dirname(absolutepath)
print(fileDirectory)

config = configparser.ConfigParser()
config1 = configparser.ConfigParser()


## Specifying the location to the directory

config.add_section('default')

main =   fileDirectory 

print(main)

config.set('default','main_directory', main )



## Specifying the dataset details

config.add_section('datasets')

number = str(4)

output_folder = '${default:main_directory}/Mapping/output' 



type(output_folder)

config.set('datasets','number_of_datasets', number)

config.set('datasets','output_folder', output_folder)

config.set('datasets','remove_duplicate', 'yes')


config.set('datasets','all_in_one_file', 'no')

name = 'file'

config.set('datasets','name', name)

config.set('datasets','enrichment', 'yes')

config.set('datasets','large_file', 'false')

config.set('datasets','ordered', 'yes')


## passing the rml mapping files

''' specify the path of path.properties file here '''

config1.readfp(open('../diaspora_to_csv/tables.properties'))


x = 1

for each_section in config1.sections(): 
    for each_key, each_val in config1.items(each_section):
        dataset =  'dataset' + str(x)
        
        config.add_section(dataset)
        
     #   names = 'file' + str(x)
        names = each_key
        
        config.set(dataset,'name', names)
            
        mappings = '${default:main_directory}/Mapping/mappings/' + names + '.ttl'
            
        config.set(dataset,'mapping', mappings)
        x+=1

        


# for x in range(1,int(number)+1):
#     dataset =  'dataset' + str(x)
    
#     config.add_section(dataset)
    
#  #   names = 'file' + str(x)
#     names = 'materials_dataset'
    
#     config.set(dataset,'name', names)
        
#     mappings = '${default:main_directory}/' + 'rml' + str(x) + '.ttl'
        
#     config.set(dataset,'mapping', mappings)


## write the file to the directory

with open('configfile.ini','w') as configfile:
    config.write(configfile)
    





    
    
















