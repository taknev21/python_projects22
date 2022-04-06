###connect_Oracle_TNS
import os 
import cx_Oracle
from pprint import pprint
import csv
import time

#username
USERNAME = "sys"
PASSWORD = input("Pass: ")
TNS = input("TNS_NAME: ")

connection_string = cx_Oracle.connect(USERNAME,PASSWORD,TNS , mode = cx_Oracle.SYSDBA)
cursor1 = cx_Oracle.Cursor (connection_string)
cursor2 = cx_Oracle.Cursor (connection_string)

query_TEXT = "select username, schemaname, osuser,Machine, MOdule, count(*) from GV$session where schemaname not in ('SYS','DBSNMP') group by username,schemaname,osuser,Machine,module order by 3"
query_TEXT2 = "select A.username,b.Machine, b.MOdule,b.Program,count(*) from dba_users A,V$Active_session_History b where B.User_ID=A.user_ID and b.Sample_Time between sysdate-1 and sysdate and A.username not in ('SYS','DBSNMP') gropu by A.username,b.Machine,B.module,b.Program order by 1,2"

cursor1.execute(query_TEXT)
cursor2.execute(query_TEXT2)

#timestamp
timestr = time.strftime("%d-%m-%Y_%H:%M:%S")

#query output1
filename = 'f:\v_session_'+TNS+'.csv'
FILE=open(filename,"w");
output=csv.writer(FILE, dialect='excel')

#connection with Oracle DB
for row in cursor1:
    output.writerow(row)
cursor1.close()
FILE.close()

#query output2
filename='F:\Shell_Script\Create_TNS\active_session_history_'+TNS+'.csv'
FILE=open(filename,"w");
output=csv.writer(FILE, dialect='excel')

#connection with Oracle DB
for row in cursor2:
    output.writerow(row)
cursor2.close()

connection_string.close()
FILE.close()

