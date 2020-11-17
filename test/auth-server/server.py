# Auth Server
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

def encrypt(key,mess):
   f = Fernet(key)
   encrypted = f.encrypt(mess)
   return encrypted

@app.route('/')
def index():
    return 'Please Authenticate Yourself'

@app.route('/authenticate', methods=['POST'])
def authenticate():
   username = request.form['username']
   password = request.form['password']
   authen = requests.auth.HTTPBasicAuth(username,password)
   data = {'grant_type':'client-credentials'}
#   req = requests.post('http://192.168.202.45:8080/token.php', data=data, auth=authen)
   req = ''
   if req == '':
      return jsonify(auth='fail',token='')
   if req.status_code == 400:
      return jsonify(auth='fail', token='')
   res = req.json()
   if 'access_token' in res:
      encryptToken = encrypt(secret_key, req.text)
      newRes = json.dumps({'auth':'sucess','token':encryptToken})
      passw = hashlib.sha256()
      passw.update(bytes(password, 'utf-8'))
      passKey = passw.digest()
      encryptPassw = encrypt(newRes, passKey)
      return jsonify(res=encryptPassw)
   else:
      return false

if __name__ == '__main__':
   app.config['TEMPLATES_AUTO_RELOAD'] = True
   app.run('192.168.206.35',port=5000,debug=True)
