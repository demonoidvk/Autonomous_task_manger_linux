#!/usr/bin/python
import mysql.connector as msc
hostname = 'localhost'
user = ' '          #input the username for database access, for saving logs and users
pwd = ' '           #input password to access the db

def dbcon():
  cnx = msc.connect( host=hostname, user=user, passwd=pwd)
  global cursor
  cursor=cnx.cursor()
  return cnx
