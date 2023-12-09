from flask import Flask, jsonify, Response
import requests as req
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/<string:URL>", methods=['GET'])
def GetInfo(URL):
    URL = URL.replace('~', '/').replace('$', '?')
    URL = URL.replace('|', '/')

    try:
        data = req.get(URL).json()
    except:
        return Response('Error', 404)
    return jsonify(data), 200
