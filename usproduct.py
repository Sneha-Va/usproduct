
import requests
import json
import mysql.connector
import sys
try:
    mydb=mysql.connector.connect(host='localhost',user='root',password='',database='usdb')
except mysql.connector.Error as e:
    sys.exit("connection error")
mycursor=mydb.cursor()
data=requests.get("https://datausa.io/api/data?drilldowns=Nation&measures=Population").text
data_info=json.loads(data)

for i in data_info["data"]:
    years = str(i['Year'])
    population= str(i['Population'])
sql = "INSERT INTO `usproduct`(`Nation`, `Year`, `Population`, `Slug Nation`) VALUES ('"+i['Nation']+"','"+years+"','"+population+"','"+i['Slug Nation']+"')"
mycursor.execute(sql)
mydb.commit()
print('Inserted the value succesfully')

