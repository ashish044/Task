""" 
    @author Ashish patel
    @This code defines the connection form oracle server
    @since 15-09-2020
"""
import cx_Oracle
import configparser
import os
from main import app
def connection(sql,variable):
    
    #Taking Username and password
    UserName=app.config['Username']
    Password=app.config['Password']
    #Connection String
    dsn = cx_Oracle.makedsn("developmentb.cbzwztcxfluc.eu-west-1.rds.amazonaws.com", 1521, service_name="devsuite")
    connection = cx_Oracle.connect(UserName, Password, dsn, encoding="UTF-8")
    cursor = cx_Oracle.Cursor(connection)
    #SQL query without any input paramenter
    if variable==None:
        cursor.execute(sql)
        data={"columns":cursor.description,"data":cursor.fetchall()}
        cursor.close()
        connection.close()
        return data
    #Sql query with Input Parameter
    else:
        cursor.execute(sql,variable)
        #cursor.description provides the column names
        data={"columns":cursor.description,"data":cursor.fetchall()}
        cursor.close()
        connection.close()

        return data







