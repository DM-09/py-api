import flask
from flask import Flask, jsonify, Response
import requests as req
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/<string:URL>", methods=['GET'])
def OldVersion(URL):
    print(URL)
    URL = URL.replace('~', '/').replace('$', '?')

    try: data = req.get(URL).json()
    except: return Response('Error', 404)
    return jsonify(data), 200

@app.route("/q", methods=['GET'])
def NewVersion():
    URL = flask.request.url
    URL = URL[URL.index('q?')+2:]

    try: data = req.get(URL).json()
    except: return Response('Error', 404)
    return jsonify(data), 200
