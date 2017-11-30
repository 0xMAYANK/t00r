# -*- coding: utf-8 -*-
from flask import Flask
app = Flask(__name__)

host = os.environ.get('IP', '0.0.0.0')
port = int(os.environ.get('PORT', 8080))
app.run(host=host, port=port)

@app.route('/')
def hello_world():
    return '•¬¬ç'

