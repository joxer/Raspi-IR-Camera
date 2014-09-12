from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, jsonify

import time

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/take_photo')
def do_photo():
    data = {'filename': "example.jpg"}
    resp = jsonify(data)
    resp.status_code =200
    return resp

if __name__ == '__main__':
    app.run(host="0.0.0.0")
