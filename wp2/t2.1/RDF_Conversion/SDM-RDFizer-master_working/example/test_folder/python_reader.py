#https://pynative.com/python-mysql-database-connection/

import mysql.connector
from mysql.connector import Error
import pandas as pd
import os

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='tib_bacdive',
                                         user='root',
                                         password='gautam')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        
        sql1="""SELECT ID_strains, cell_len, cell_len_unit, cell_width, cell_width_unit FROM tib_bacdive.cell_morphology; """
        df = pd.read_sql(sql1, connection)
        print(df.head(2))
        print(df.shape)
        df.to_csv("cell_morphology.csv")
        
        #os.system('cmd /k "python rdfizer/run_rdfizer.py C:\Gautam\Gautam_Working\diaspora_Github\wp2\t2.1\RDF_Conversion\SDM-RDFizer-master_working\example\test_folder\cell_morphology_config_test.ini" ')
        
        

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
