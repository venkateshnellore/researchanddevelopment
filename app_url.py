import json
from flask import Flask,request, jsonify
from flask_cors import CORS
from otp_send import sendotp

app = Flask(__name__)
CORS(app)

@app.route('/',methods=['GET'])
def hello():
   return ("Application is working Fine")

@app.route('/sendotp',methods=['POST'])
def sendotp():
   return sendotp(request)

if __name__ == "__main__":
  app.run(debug=True)
  #app.run(host="192.168.56.1",port=5000)
