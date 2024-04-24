from psycopg2 import * #pg connection module 
server = connect(host='localhost',database='firstedatabase',password='3104',user='postgres') #connection
cursor = server.cursor()#command writer
name = input('enter your name')
email = input('enter your email')
password = input('enter your password')
phone = int(input('enter your phone'))
cursor.execute(f"insert into s_details(id,cuser,paswd,email,phone) values(4,'{name}','{password}','{email}','{phone}')")

cursor.close()
