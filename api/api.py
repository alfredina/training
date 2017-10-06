from flask import Flask
from flask_httpauth import HTTPBasicAuth
import pymysql.cursors
import json
import pymssql
from flask_jsonpify import jsonify
from flask import request
import os


CMS_URL = os.environ['CMS_URL']
CMS_USER = os.environ['CMS_USER']
CMS_PASSWORD = os.environ['CMS_PASSWORD']
CMS_DB = os.environ['CMS_DB']

app = Flask(__name__)
auth=HTTPBasicAuth()

users={
       "john":"hello1",
       "susan":"bye"
}


@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None



connection = pymssql.connect(CMS_URL, CMS_USER, CMS_PASSWORD, CMS_DB)
@app.route("/")
def hello():
    return "Hello world,WASAC1"

@app.route('/about-us')
def about_us():
  return "About Us"

@app.route('/taha')
def taha():
  return "taha:"

@app.route('/poc/<customerid>')
def show_user_profile(customerid):
 return 'POC: %s' % customerid

@app.route('/customer', methods=['POST'])
@app.route('/customer/<poc>', methods=['GET'])
@auth.login_required
def show_user_profiles(poc=None):
	if request.method == 'GET':
		try:
			with connection.cursor(as_dict=True) as cursor:
				sql = "SELECT *  FROM customer2 WHERE customerid='%s'" % poc
				cursor.execute(sql)
				customer = cursor.fetchone()
				print(customer)
				return jsonify(dict(customer))
		finally:
			pass
	elif request.method == 'POST':
		try:
			data = request.get_json(force=True)
			with connection.cursor(as_dict=True) as cursor:
				sql = "insert into api_table (customerid,name,cbal) values ('%s', '%s', '%i')" % (data['customerid'], data['name'], data['cbal']) 
				cursor.execute(sql)
                                connection.commit()
				return "OK" 
		except:
				return "Error", 500
		finally:
			pass


if __name__=="__main__":
    app.run(debug=True, port=5001, host="0.0.0.0")
#reka ndebe ra!
