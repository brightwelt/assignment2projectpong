from flask import Flask, jsonify
from flask_httpauth import HTTPDigestAuth
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret key here'
auth = HTTPDigestAuth()

users = {
    "vcu": "rams"
}

@auth.get_password
def get_pw(username):
        return users.get(username)

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({'message':'Page Not Found'}), 404


@app.errorhandler(500)
def internal_server_error(e):
    return jsonify({'message':'Internal Server Error'}), 500

@app.route('/pong', methods=['GET'])
@auth.login_required
def pong():
    return jsonify({'message': int(random.random()*100)})
