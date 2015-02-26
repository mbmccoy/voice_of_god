#!/usr/bin/env python3

# Import basic stuff
import os


# Flask imports
from flask import Flask, request, render_template

# Get the word of God
import god_zip

# Web config
WEB_PORT = 80


god = god_zip.GodZip()
app = Flask(__name__)
app.debug = True


@app.route("/")
def flask_index():
    context = {
    }
    return render_template('index.html', **context)
    

@app.route("/praise", methods=['GET', 'POST'])
def flask_encode():
    words = request.form['words']
    if len(words) > 10000:
        words = words[:10000]

    try:
        return god.praise(words)

    except god_zip.Heresy as h:
        return "Heresy! " + str(h)

@app.route("/reveal", methods=['GET', 'POST'])
def flask_decode():
    words = request.form['words']
    if len(words) > 10000:
        words = words[:10000]

    try:
        return god.reveal(words)

    except god_zip.Heresy as h:
        return "Heresy! " + str(h)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', '5000')))
