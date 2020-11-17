# Client Server
# CSEC 472 - Lab 5
# Alex Rosse

from flask import *
import json
import requests
import hashlib
import sys
from cryptography.fernet import Fernet

app = Flask(__name__)
secret_key = b'@uth3nt!c@t!0n_L@b_5 _S3cr3t_K3y'

def decrypt(key,mess):
   f = Fernet(key)
   decrypted = f.decrypt(mess)
   return decrypted

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/authenticate', methods=['POST'])
def authenticate():
   username = request.form['username']
   password = request.form['password']
   data = {'username': username, 'password': password}
   req = requests.post('http://192.168.206.35:5000/authenticate', data=data)
   return req

if __name__ == '__main__':
   app.config['TEMPLATES_AUTO_RELOAD'] = True
   app.run('192.168.206.35',port=80,debug=True)
