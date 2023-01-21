from flask import Flask, request
from users import get_users
from user import info
from sentiment_analysis import get_sentiment
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})

@app.route('/users', methods = ['POST' , 'GET'])
def users():
    return get_users()

@app.route('/user_info', methods = ['POST', 'GET'])
def user_info():
    user_id = request.json['user_id']
    # print(user_id)
    return info(user_id)

@app.route('/sentiment', methods=['POST', "GET"])
def senti():
    text = request.json['text']
    return get_sentiment(text)

if __name__ == '__main__':
    app.run(debug=True)
