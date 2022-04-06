#connect MSSQL server and run the SQL query
import pyodbc
import csv

server = 'hostname.com:port'
database = 'dbname'
username = 'username'
password = 'pass'

cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cnxn1 = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

sql_cursor = cnxn.cursor()
sql_cursor1 = cnxn1.cursor()

### SQL Disk Storage data
### SQL1
sql_cursor.execute(""" select
ServerName
, Environment
, LOB
, DiskType
, Drive
, DriveType
, Total_InGB = ROUND(ISNULL([Free_InGB] / NULLIF ([FreeSpace_Percentage], 0), 0)*100,0)
, Free_InGB
, FreeSpace_Percentage
, DiskStatus
, DateTime
from [dbname].[tablename]
where DriveType ='others'
;""")

#SQL Database level storage data
### SQL2
sql_cursor1.execute("select * from [EDS02].[DS_MasterInv].[dbo].[vw_SQLSever_DBSize_details] order by servername;")

sql_disk_data = sql_cursor.fetchall()

with open('/dfs/external_data/sqlserver_disk_storage.csv','w', newline='') as f_handle:
    writer = csv.writer(f_handle)

    for rowin sql_disk_data:
        writer.writerow(row)

sql_db_data = sql_cursor1.fetchall()

with open('/dfs/external_data/sqlserver_db_storage.csv','w', newline='') as f_handle:
    writer = csv.writer(f_handle)

    for row in sql_db_data:
        writer.writerow(row)

#--------------- END ------------------#        

