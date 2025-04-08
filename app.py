from flask import Flask, jsonify
import redis

app = Flask(__name__)

r = redis.Redis(host='redis', port=6379, db=0)

@app.route('/')
def index():
    return "Welcome to the Flask API!"

@app.route('/ping')
def ping():
    return jsonify({"status": "ok"})

@app.route('/count')
def count():
    visits = r.incr('visits')
    return jsonify({"visits": visits})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
