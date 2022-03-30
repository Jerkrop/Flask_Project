#  this is all of the needed parts for the data base all that needs done is makeing it work
# And don't forget to download this so that it works
# pip install Flask psycopg2-binary
import os
import psycopg2

conn = psycopg2.connect(
    host = 'localhost',
    database = 'flask_db',
    # dont forget to use your password for pgadmin
    password = 'Meegee12',
    user = 'postgres'
)
cur = conn.cursor()

# This below will make the table

cur.execute("CREATE TABLE bicycle (id serial PRIMARY KEY, name text NOT NULL, email varchar (150) NOT NULL,username varchar (150) NOT NULL,password varchar (150) NOT NULL,bicycleName text NOT NULL,bicyclePrice int NOT NULL);")
# cur.execute('CREATE TABLE bicycle (id varchar (10) NOT NULL',
#                                  'name text NOT NULL',
#                                  'email varchar (150) NOT NULL',
#                                  'username varchar (150) NOT NULL',
#                                  'password varchar (150) NOT NULL',
#                                  'bicycleName text NOT NULL',
#                                  'bicyclePrice int (10) NOT NULL)')

# # all the values still need to be added but i put in an example for you 
cur.execute('INSERT INTO bicycle (id, name, email, username, password, bicycleName, bicyclePrice)'
'VALUES(%s, %s, %s, %s, %s, %s, %s)',
('10001', 'Jeremy', 'Testemail@gmail.com', 'Jerkrop' , 'Yes' , 'Brookes' , '50'))


cur.execute('INSERT INTO bicycle (id, name, email, username, password, bicycleName, bicyclePrice)'
'VALUES(%s, %s, %s, %s, %s, %s, %s)',
('10002', 'Ezra', 'Ezra@gmail.com', 'EzraB' , 'Yes' , 'BlackBicycle' , '150'))


cur.execute('INSERT INTO bicycle (id, name, email, username, password, bicycleName, bicyclePrice)'
'VALUES(%s, %s, %s, %s, %s, %s, %s)',
('10003', 'Zach', 'Zach@gmail.com', 'ZachD' , 'Yes' , 'OrangeBicycle' , '170'))

cur.execute('INSERT INTO bicycle (id, name, email, username, password, bicycleName, bicyclePrice)'
'VALUES(%s, %s, %s, %s, %s, %s, %s)',
('10004', 'Ashton', 'Ashton@gmail.com', 'Ashtonw' , 'Yes' , 'BlueBicycle' , '100'))

cur.execute('INSERT INTO bicycle (id, name, email, username, password, bicycleName, bicyclePrice)'
'VALUES(%s, %s, %s, %s, %s, %s, %s)',
('10005', 'Justice', 'Finn@gmail.com', 'Justicev' , 'Yes' , 'GreenBicycle' , '170'))



cur.execute('INSERT INTO bicycle (id, name, email, username, password, bicycleName, bicyclePrice)'
'VALUES(%s, %s, %s, %s, %s, %s, %s)',
('10006', 'Gabriel', 'Gabe@gmail.com', 'GabeD' , 'Yes' , 'RedBroonieBicycle' , '200'))



cur.execute('INSERT INTO bicycle (id, name, email, username, password, bicycleName, bicyclePrice)'
'VALUES(%s, %s, %s, %s, %s, %s, %s)',
('10007', 'Finn', 'Finn@gmail.com', 'FinnM' , 'Yes' , 'QuintonBicycle' , '250'))


cur.execute('INSERT INTO bicycle (id, name, email, username, password, bicycleName, bicyclePrice)'
'VALUES(%s, %s, %s, %s, %s, %s, %s)',
('10008', 'Carlos', 'CarlosA@gmail.com', 'CarlosA' , 'Yes' , 'HarleyDavidsonBicycles' , '260'))


cur.execute('INSERT INTO bicycle (id, name, email, username, password, bicycleName, bicyclePrice)'
'VALUES(%s, %s, %s, %s, %s, %s, %s)',
('10009', 'William', 'Will@gmail.com', 'WillB' , 'Yes' , 'FordBicycles' , '270'))


cur.execute('INSERT INTO bicycle (id, name, email, username, password, bicycleName, bicyclePrice)'
'VALUES(%s, %s, %s, %s, %s, %s, %s)',
('10010', 'Dinnese', 'Dinnese@gmail.com', 'DinneseH' , 'Yes' , 'TopSubaruBicycles' , '280'))



conn.commit()
cur.close()
conn.close()