import flask
from flask import Flask, jsonify, Response
import requests as req
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

server = 'https://api-py.vercel.app/@'

@app.route("/<path:URL>", methods=['GET'])
def GetInfo(URL):
    ru = flask.request.url
    if URL[0] == '@': URL = ru[len(server):]
    else: URL = URL.replace('~', '/').replace('$', '?')

    try: data = req.get(URL).json()
    except: return Response('Error', 404)
    return jsonify(data), 200
