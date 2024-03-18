import pyodbc
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

server = os.environ.get("server")
database = os.environ.get("database")
username = os.environ.get("username")
password = os.environ.get("password")

# Connection to database.
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)


# Function to check data on SQL server
def get_schema(p_cnxn):

    try:

        cursor = p_cnxn.cursor()
        # Select table names and schema from SQL Server
        query = """SELECT 
                    t.name as TableName
                FROM
                    sys.tables t
                    INNER JOIN sys.schemas s ON t.schema_id = s.schema_id
                WHERE s.name =  'dbo'"""


        # Execute query.
        cursor.execute(query)

        # Fetch the tables from sql server.
        schema_tables = cursor.fetchall()

        cursor.close()
        
        return schema_tables

    except pyodbc.Error as e:

        # Message stating export unsuccessful.
        print("Data fetch unsuccessful.")
        quit() 


# Funtion to do the data completenes check
def data_completenes(p_schema_tables, p_cnxn):
    # Select data from table
    querydata = "SELECT * FROM "

    for table in p_schema_tables:        
        df = pd.read_sql(querydata + table[0], p_cnxn)
        #print(df.head)
        #df.describe()
        # Check for missing values in the DataFrame
        missing_values = df.isnull().sum()
        print(table[0]+ " Missing Values:")
        print(missing_values)
        print("----")
        # Check for duplicate rows in the DataFrame
        duplicate_rows = df[df.duplicated()]
        print(table[0]+ " Duplicate Rows:")
        print(duplicate_rows)
        print("----")
        # Check data types of each column in the DataFrame
        data_types = df.dtypes
        print(table[0]+ " Data Types:")
        print(data_types)
        print("---------------------------")

    p_cnxn.close()
 

# Run pipeline
schema_tables = get_schema(cnxn)
data_completenes(schema_tables, cnxn)


