import mysql.connector

def database():
    connection =mysql.connector.connect(host='localhost',database='registration',port='8111',user='root',password='')
    cursor=connection.cursor()
    return connection, cursor
