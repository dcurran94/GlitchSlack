#!/usr/bin/env python
# -*- coding: utf-8 -*-

#       _                              
#      | |                             
#    __| |_ __ ___  __ _ _ __ ___  ___ 
#   / _` | '__/ _ \/ _` | '_ ` _ \/ __|
#  | (_| | | |  __/ (_| | | | | | \__ \
#   \__,_|_|  \___|\__,_|_| |_| |_|___/ .
#
# A 'Fog Creek'–inspired demo by Kenneth Reitz™

import os
from flask import Flask, request, jsonify, render_template, Response
app = Flask(__name__)



# Support for gomix's 'front-end' and 'back-end' UI.
app = Flask(__name__, static_folder='public', template_folder='views')

# Set the app secret key from the secret environment variables.
app.secret = os.environ.get('SECRET')

# Dream database. Store dreams in memory for now. 
DREAMS = ['Python. Python, everywhere.']


@app.after_request
def apply_kr_hello(response):
    """Adds some headers to all responses."""
  
    # Made by Kenneth Reitz. 
    if 'MADE_BY' in os.environ:
        response.headers["X-Was-Here"] = os.environ.get('MADE_BY')
    
    # Powered by Flask. 
    response.headers["X-Powered-By"] = os.environ.get('POWERED_BY')
    return response


@app.route('/')
def homepage():
    """Displays the homepage."""
    return render_template('index.html')
  
@app.route('/slashcommand', methods=['POST'])  # Changed to POST as this method only handles post requests
def slash():
    #'if request.form['token'] == "":
        payload = {'text': 'Success'}
        return jsonify(payload)
      
@app.route('/events', methods=['POST'])  # Changed to POST as this method only handles post requests
def events_handler():
    request_body_json = request.get_json()

    if "challenge" in request_body_json:
        # Respond to the challenge
        return Response(request_body_json["challenge"]), 200


if __name__ == '__main__':
    app.run()