from flask import Flask, jsonify, Response
import requests as req

app = Flask(__name__)

@app.route("/<string:URL>", methods=['GET'])
def GetInfo(URL):
    URL = URL.replace('~', '/').replace('$', '?')

    try:
        data = req.get(URL).json()
    except:
        return Response('Error', 404)
    return jsonify(data), 200
