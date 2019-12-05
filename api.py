from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
from datetime import datetime
import requests
import json
from os import environ

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
	return "Hello."

@app.route('/mp3/<path:path>')
def send_mp3(path):
	return send_from_directory('mp3', path)

simpleData = {
	"status": "OK",
	"requested_at": datetime.now()
}

api_r = requests.get('https://pastebin.com/raw/b16W5Nu3')
api = {'api': api_r.text}
base_domain = 'sandbox5b325091bd334c5792decfea9d1f14c2.mailgun.org'

emailData = {
	"from": "Zenmark Mail <sandbox5b325091bd334c5792decfea9d1f14c2@mailgun.org>",
	"to": "tcsion@mail.com",
	"subject": "New Survivio+ JS Error Report!",
}

@app.route("/api/report", methods=["GET", "POST"])
def report():
	if request.method == "GET":
		errorData = request.args.get('body')
		if errorData:
			return jsonify({"status": "OK", "errors": errorData})
		else:
			return jsonify(simpleData)
	if request.method == "POST":
		errorData = request.form
		errorData = errorData.to_dict()
		# print(errorData)
		emailData["text"] = "New message! \n " + json.dumps(errorData, indent=4)
		r = requests.post('https://api.mailgun.net/v3/{}/messages'.format(base_domain), auth=('api', api['api']), data=emailData)
		# print(r.status_code)
		return jsonify({"status": "OK"})

@app.after_request
def after_request_stuff(resp):

	# Support CORS
    resp.headers['Access-Control-Allow-Origin'] = "*"
    resp.headers['Access-Control-Allow-Methods'] = "POST, GET, OPTIONS, PUT, DELETE, PATCH"
    resp.headers['Access-Control-Allow-Headers'] = "origin, content-type, accept, x-requested-with"

    return resp


if __name__ == "__main__":
	# convention to run on Heroku
	port = int(environ.get("PORT", 5000))
	# run the app available anywhere on the network, on debug mode
	app.run(host="0.0.0.0", port=port, debug=True)
