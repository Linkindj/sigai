import mysql.connector

database = mysql.connector.connect(
    host='127.0.0.1',
    port='3306',
    user='root',
    password='',
    database='bd_nueva'
)