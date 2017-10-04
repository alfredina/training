import requests
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Welcome to NYANZA"

@app.route('/about-us')
def about_us():
  return "About Us"

@app.route('/taha')
def taha():
  return "taha:"

@app.route('/customer/<customerid>')
def show_user_profile(customerid):
 r= requests.get('http://api:5001/customer/%s'%customerid)
 print r
 data = r.json()
 return 'POC: %s' % data['customerid']

@app.route('/poc/<customerid>/<name>')
def show_user_profiles(customerid,name):
  return 'All: %s %s'  % (customerid,name)

if __name__=="__main__":
    app.run(debug=True, port=5001, host="0.0.0.0")
