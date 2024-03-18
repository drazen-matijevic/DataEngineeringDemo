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
cnxn = pyodbc.connect(f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}')
# cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

# Function to create Landing Zone folder structure
def create_landing_zone():
    if os.name == 'nt':
        if not os.path.exists('c:\\demo'):
            os.makedirs('c:\\demo')

        if not os.path.exists('c:\\demo\\landing_zone'):
            os.makedirs('c:\\demo\\landing_zone')

        # Sink path
        output_path = 'c:\\demo\\landing_zone\\'

    else:
        # Define the path to the folder you want to create
        folder_path = '/app/demo/landing_zone/'

        # Create the folder if it doesn't already exist
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        print("Folder created successfully at:", folder_path)
        # Sink path
        output_path = folder_path

    return output_path


# Function to load data from SQL server
def load_data(p_cnxn):

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
        print("Data export unsuccessful.")
        quit() 


# Funtion to save the data to defined location (c:\demo\landing_zone)
def save_data(p_schema_tables, p_cnxn, p_sink):
    # Select data from table
    querydata = "SELECT * FROM "

    for table in p_schema_tables:        
        df = pd.read_sql(querydata + table[0], p_cnxn)
        #print(df.head)
        # Write dataframe to csv files
        try:
            df.to_csv ((p_sink + table[0] + '.csv'), index = None, header=True, mode='x')            
            print('The csv file for table ' +table[0]+ ' has been created in landing zone!')
        except FileExistsError:
            print('WARNING: This file ' +table[0]+ ' already exists!')
            
    p_cnxn.close()
 

# Run pipeline
sink = create_landing_zone()
schema_tables = load_data(cnxn)
save_data(schema_tables, cnxn, sink)


