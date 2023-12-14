import flask
from flask import Flask, jsonify, Response
import requests as req
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

server = 'https://api-py.vercel.app/@'

@app.route("/<string:URL>", methods=['GET'])
def V0(URL):
    URL = URL.replace('~', '/').replace('$', '?')

    try: data = req.get(URL).json()
    except: return Response('Error', 404)
    return jsonify(data), 200

@app.route('/@<path:URL>', methods=['GET'])
def V1(URL):
    URL = flask.request.url[len(server):].replace('https:/', 'https://')

    try: data = req.get(URL).json()
    except: return Response('Error', 404)
    return jsonify(data), 200
