import flask
from flask import Flask, jsonify, Response
import requests as req
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/<string:URL>", methods=['GET'])
@app.route('/', defaults={'URL': 'a'})
def V0(URL):
    a = flask.request.args.get('r')

    if a: URL = a
    else: URL = URL.replace('~', '/').replace('$', '?')

    try: data = req.get(URL).json()
    except: return Response('Error', 404)
    return jsonify(data), 200
