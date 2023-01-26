# import requests
# import json


# response = requests.get('https://api.stackexchange.com/2.3/collectives?order=desc&sort=name&site=stackoverflow')
# print(response)
import os
import psycopg2
import pandas as pd
from psycopg2.extras import RealDictCursor 
import traceback
from flask import Flask
app = Flask(__name__)

def get_db_connection():
    try:
        conn = psycopg2.connect(host='pgprod.cmgd0fjjmi5g.ap-northeast-1.rds.amazonaws.com',
                            database='res_api',
                            user='postgres',
                            password='nandymaya',
                            cursor_factory=RealDictCursor
                             )
        cur =conn.cursor()
        print("Db connected Successfull!!")
        return cur
    except Exception as error:
        print("connecting database failed **********")
        print("Error :", error)
        traceback.print_exc()

@app.route('/')
def test():
    return 'hello hi hw r u          !!!!!!!!!!!!!'

@app.route('/home',methods=['GET','POST'])
def home():
    return {'name':'nandhini'}

@app.route('/students',methods=['GET','POST'])
def student():
    cur = get_db_connection()
    student_data=cur.execute("""SELECT * FROM public.student""")
    student_data= cur.fetchall()
    print(student_data)
    return student_data


# @app.post('/add_students')
# def add_student():
#     cur = get_db_connection()
#     print("---------1-------")
#     student_data=cur.execute("""INSERT INTO  public.student(name,age,class,gender)
#                               VALUES(Hari, 8, 2,M)""")
#     student_data= cur.fetchall()
#     print(student_data)
#     print('---------2--------')
#     return student_data
        
   


if __name__ == '__main__':
    app.run(debug=True)