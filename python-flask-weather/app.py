# File: app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

queries = []

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city', 'Unknown')
    queries.append(city)
    return jsonify({"city": city, "forecast": "Sunny (mock data)"})

@app.route('/queries', methods=['GET'])
def get_queries():
    return jsonify(queries)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
