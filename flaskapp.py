import os, re, time, memcache
from flask import Flask, render_template, request, redirect, session
from random import randint
from datetime import datetime
import sys, csv
import pymysql


ACCESS_KEY_ID = '######'
ACCESS_SECRET_KEY = '##############'
BUCKET_NAME = '####'

hostname = '####################3'
username = '#####'
password = '#######'
database = '#####'
Conn = pymysql.connect( host=hostname, user=username, passwd=password, db=database, autocommit = True, cursorclass=pymysql.cursors.DictCursor, local_infile=True)

application = Flask(__name__)
app = application



@app.route("/")
def hello():
    return render_template("file1.html")

@app.route('/plotbarchart', methods=['POST'])
def plotbarchart():
    	variable = request.form['limit']

    	query1 = "select count(county),state from USZipcodes group by state having count(distinct county) <"+str(variable)

    	result1 = []
	with Conn.cursor() as curs:
    		curs.execute(query1)
    		for row in curs:
        		result1.append(row)
    	x1 = [x['count(distinct county)'] for x in result1]
    	x2 = [x['state'] for x in result1]
    	result2 = []
    	print x1
    	print x2
    	print result2
    	for p in x2:
        	result2.append(p)
    	print(result2)
    	return render_template("index.html",zipped_data= x1,x2=result2)

@app.route('/plothorizontalchart', methods=['POST'])
def plothorizontalchart():
    	variable = request.form['limit']

    	query1 = "############"

    	result1 = []
	with Conn.cursor() as curs:
    		curs.execute(query1)
    		for row in curs:
        		result1.append(row)
    	x1 = [x['count(distinct county)'] for x in result1]
    	x2 = [x['state'] for x in result1]
    	result2 = []
    	print x1
    	print x2
    	print result2
    	for p in x2:
        	result2.append(p)
    	print(result2)
    	return render_template("multiBarHorizontalChart.html",zipped_data= x1,x2=result2)

@app.route('/plotpiechart', methods=['POST'])
def plotpiechart():
    	variable = request.form['limit']

    	query1 = "##########"

    	result1 = []
	with Conn.cursor() as curs:
    		curs.execute(query1)
    		for row in curs:
        		result1.append(row)
    	x1 = [x['count(distinct county)'] for x in result1]
    	x2 = [x['state'] for x in result1]
    	result2 = []
    	print x1
    	print x2
    	print result2
    	for p in x2:
        result2.append(p)
    	
    	return render_template("PieChart.html",zipped_data= x1,x2=result2)


# Adding extra functions

@app.route('/createtablevoting', methods=['POST'])
def createtablevoting():
	cursor = Conn.cursor()
	file_name2 = 'StateVotingClean.csv'
	# file_name = 'home/ubuntu/flaskapp/data.csv'

	droptbl = "DROP TABLE IF EXISTS vbsdatabase.StateVotingClean;"
	cursor.execute(droptbl)
	with open(file_name2, 'rb') as csvfile:
		reader = csv.reader(csvfile, quotechar='`')
		headers = reader.next()
	print len(headers)
	start_time = time.time()
	print 'ttt'
	sqlcreate = "create table if not exists StateVotingClean("
	for i in range(0, len(headers)):
		sqlcreate += headers[i] + " varchar(100),"
	sqlcreate += "Idautonum int AUTO_INCREMENT PRIMARY KEY)"
	cursor.execute(sqlcreate)
	print sqlcreate
	uploadqry = """LOAD DATA LOCAL INFILE 'StateVotingClean.csv'
          INTO TABLE StateVotingClean FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' LINES TERMINATED BY '\r' IGNORE 1 ROWS;"""
	cursor.execute(uploadqry)
	Conn.commit()
	print uploadqry
	end_time = time.time()
	time_diff = end_time - start_time
	print time_diff
	cursor.close()
	return render_template('file1.html', crteducation=time_diff)


@app.route('/query1', methods=['POST'])
def query1():
	State = request.form['State']
	q1 = "#######"
	qq1 = "#######"
	print (q1)
	print (qq1)
	with Conn.cursor() as curs:
		curs.execute(q1)
		rows = curs.fetchall()
		curs.execute(qq1)
		res = curs.fetchall()
		curs.close()
		return render_template('file1.html', answer1=rows, answer2=res[0]['count(*)'])

@app.route('/query4', methods=['GET', 'POST'])
def query4():
    	
    	logi1 = request.form['val1']
    	logi2 = request.form['val2']
    	lati1 = request.form['val3']
    	lati2 = request.form['val4']

    	locquery = "########"

    	print (locquery)
    	starttime = time.time()
	result1=[]
	with Conn.cursor() as cursor:
		cursor.execute(locquery)
		for row in cursor:
			result1.append(row)
	x1 = [x['count(*)'] for x in result1]
   	x2 = [x['longitude'] for x in result1]
	x3 = [x['latitude'] for x in result1]
	endtime = time.time()

   	totalsqltime = endtime - starttime
	result2=[]
	result3=[]
	for p in x2:
        	result2.append(p)
	for p1 in x3:
		result3.append(p1)

   	return render_template('lineChart.html',zipped_data= x1,x2=result2,x3=result3)


if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)




