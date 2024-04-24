from psycopg2 import * #pg connection module 
server = connect(host='localhost',database='firstedatabase',password='3104',user='postgres') #connection
cursor = server.cursor()#command writer
command="select * from s_details"
cursor.execute(command)#command exicuter
#inserting data
data = cursor.fetchall()#fetching data from cursor
for i in data:
    print(i)
cursor.close()
