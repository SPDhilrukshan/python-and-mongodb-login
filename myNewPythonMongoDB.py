# File: myNewPythonMongoDB.py

from pymongo import MongoClient
client=MongoClient()
myDb=client["Users"]

un=str(input("Enter your username"))
pw=str(input("Enter your password"))
queryString1={}
queryString2={}
queryString1["username"]=un
queryString2["password"]=pw
user=myDb.userList.find($and:[queryString1,queryString2]).pretty()

if user:
	print("login successful")
	print("Welcome...!!!")
else:
	print("login failed ,user name or password is incorrect")

	