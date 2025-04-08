from flask import Flask, jsonify
import redis

app = Flask(__name__)

# Подключение к Redis (контейнер Redis будет доступен по имени "redis" в Docker Compose)
r = redis.Redis(host='redis', port=6379, db=0)

@app.route('/')
def index():
    return "Welcome to the Flask API!"

@app.route('/ping')
def ping():
    return jsonify({"status": "ok"})

@app.route('/count')
def count():
    # Увеличиваем счетчик посещений
    visits = r.incr('visits')  # Redis будет хранить количество посещений по ключу 'visits'
    return jsonify({"visits": visits})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
