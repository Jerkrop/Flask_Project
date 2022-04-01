import os
import psycopg2
conn = psycopg2.connect(
    host = 'localhost',
    database = 'flask_db',
    password = 'Meegee12',
    user = 'postgres'
)
cur = conn.cursor()


#cur.execute("CREATE TABLE bicycle (id int, name text NOT NULL, email varchar (150) NOT NULL,username varchar (150) NOT NULL,password varchar (150) NOT NULL,bicycleName text NOT NULL,bicyclePrice varchar (150) NOT NULL);")
def function_(var1,var2, var3, var4, var5, var6, var7):
    cur.execute('INSERT INTO bicycle (id, name, email, username, password, bicycleName, bicyclePrice)'
    'VALUES(%s, %s, %s, %s, %s, %s, %s)',
    (var1, var2, var3, var4, var5, var6, var7))



function_('10001', 'Jeremy', 'Jeremy@gmail.com', 'Jerkrop' , 'Yes' , 'Bike1' , '$12,000')
function_('10002', 'Ezra', 'Ezra@gmail.com', 'EzraB' , 'Yes' , 'Bike2' , '$400')
function_('10003', 'Zach', 'Zach@gmail.com', 'ZachD' , 'Yes' , 'Bike3' , '$700')
function_('10004', 'Ashton', 'Ashton@gmail.com', 'Ashtonw' , 'Yes' , 'Bike4' , '$250')
function_('10005', 'Justice', 'Finn@gmail.com', 'Justicev' , 'Yes' , 'Bike5' , '$50')
function_('10006', 'Gabriel', 'Gabe@gmail.com', 'GabeD' , 'Yes' , 'Bike6' , '₽448,049.79')
function_('10007', 'Finn', 'Finn@gmail.com', 'FinnM' , 'Yes' , 'Bike7' , '$500')
function_('10008', 'Carlos', 'CarlosA@gmail.com', 'CarlosA' , 'Yes' , 'Bike8' , '$1,000')
function_('10009', 'William', 'Will@gmail.com', 'WillB' , 'Yes' , 'Bike9' , '$1,500')
function_('10010', 'Dinnese', 'Dinnese@gmail.com', 'DinneseH' , 'Yes' , 'Bike10' , '$5,000')

cur.execute("SELECT * FROM bicycle")
bicycle = cur.fetchall()
conn.commit()
cur.close()
conn.close()