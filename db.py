#!/usr/bin/python
import mysql.connector as msc
hostname = 'localhost'
user = 'demonoid'
pwd = 'password'

def dbcon():
  cnx = msc.connect( host=hostname, user=user, passwd=pwd)
  global cursor
  cursor=cnx.cursor()
  return cnx
