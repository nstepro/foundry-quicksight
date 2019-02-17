#!flask/bin/python
from flask import Flask, redirect, url_for
from flask import Response
from flask_basicauth import BasicAuth
import json, decimal
import psycopg2
from flask_cors import CORS
import simplejson as json
from decimal import Decimal

json.loads('1.1', use_decimal=True) == Decimal('1.1')
json.dumps(Decimal('1.1'), use_decimal=True) == '1.1'

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)
        return super(DecimalEncoder, self).default(o)

def decimal_default(obj):
    if isinstance(obj, decimal.Decimal):
        return float(obj)
    raise TypeError        
        
app = Flask(__name__)
CORS(app)

# app.config['BASIC_AUTH_USERNAME'] = 'arcadia'
# app.config['BASIC_AUTH_PASSWORD'] = 'wehavedata'
# app.config['BASIC_AUTH_FORCE'] = True

# basic_auth = BasicAuth(app)


@app.route('/')
# @basic_auth.required
def home():
  return redirect(url_for('static', filename='index.html'))

@app.route('/<path:path>')
def static_proxy(path):
#   send_static_file will guess the correct MIME type
  return app.send_static_file(path)

if __name__ == '__main__':
    app.run(debug=True)    
