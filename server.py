#!/usr/bin/env python3

# Import basic stuff
import os, re
from time import time

# Flask imports
from flask import Flask, Response, request, abort, render_template, jsonify

# Get the word of God
import god_zip

# Web config
WEB_PORT = 80


god = god_zip.GodZip()
app = Flask(__name__)


@app.route("/")
def flask_index():
    context = {
    }
    return render_template('index.html', **context)
    

@app.route("/encode", methods=['GET', 'POST'])
def flask_encode():
    return god.encode(request.form['words'])

@app.route("/decode", methods=['GET', 'POST'])
def flask_decode():
    return 'decoded'


app.run()

#web_server = WSGIServer(('', WEB_PORT), flask_app)
#web_server.start()


# Busy loop
#try:
    # This is gevent.wait()
#    wait()

#except KeyboardInterrupt:
#    pass

# Close it down
#web_server.close()
