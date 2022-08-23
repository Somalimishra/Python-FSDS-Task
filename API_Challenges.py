#1 . Write a program to insert a record in sql table via api database
#2 . Write a program to update a record via api
#3 . Write a program to delete a record via api
#4 . Write a program to fetch a record via api
#5 . All the above questions you have to answer for mongo db as well .
from flask import Flask, request, jsonify

import mysql.connector as connection

app = Flask(__name__)

mydb = connection.connect(host='localhost', user='root',passwd='1234')
cursor = mydb.cursor()
cursor.execute("create database if not exists api_task")
cursor.execute("create table if not exists api_task.tasktable (name varchar(30) , number int)")


#1 . Write a program to insert a record in sql table via api database
@app.route('/insert',methods = ['POST'])
def insert():
    if request.method=='POST':
        name = request.json['name']
        number = request.json['number']
        cursor.execute("insert into api_task.tasktable  values(%s , %s)",(name ,number))
        mydb.commit()
        return jsonify(str('succesfully inserted'))
'''
use this link: 127.0.0.1:5000/insert
In postman try passing this
{
    "name":"shyamli",
    "number":5565678
}
output: "succesfully inserted"
'''

#2 . Write a program to update a record via api
@app.route("/update" , methods= ['POST'])
def update():
    if request.method=='POST':
         get_name = request.json['get_name']
         cursor.execute("update api_task.tasktable set number = number + 500 where name = %s ",(get_name,))
         mydb.commit()
         return jsonify(str("updated successfully"))

'''
use this link: 127.0.0.1:5000/update
In postman try passing this
{
    "get_name":"rojali"
}
output: "updated successfully"
'''

#3 . Write a program to delete a record via api
@app.route("/delete" , methods= ['POST'])
def delete():
    if request.method == 'POST':
        name_del = request.json['name_del']
        cursor.execute("delete from api_task.tasktable where name = %s",(name_del,))
        mydb.commit()
        return jsonify(str("deleted successfully"))

'''
use this link: 127.0.0.1:5000/delete
In postman try passing this
{
    "name_del":"rojali"
}
output: "deleted successfully"
'''

#4 . Write a program to fetch a record via api
@app.route("/fetch",methods = ['POST','GET'])
def fetch_data():
    cursor.execute("select * from api_task.tasktable")
    l = []
    for i in cursor.fetchall():
        l.append(i)
    return jsonify(str(l))

'''
use this link: 127.0.0.1:5000/fetch

output: "[('somali', 456789), ('rupali', 667347), ('shyamli', 5565678)]"
'''

if __name__=='__main__':
    app.run()

