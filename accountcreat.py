from psycopg2 import * #pg connection module 
server = connect(host='localhost',database='firstedatabase',password='3104',user='postgres') #connection
cursor = server.cursor()#command writer
command=cursor.execute('''create table study_data(
                        name varchar(13) not null,
                        email varchar(17) not null,
                        password varchar(17) not null,
                        phone int not null                        
                       )''')
cursor.close()
