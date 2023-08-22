from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

def extract_numbers(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException:
        return []

@app.route('/numbers', methods=['GET'])
def get_merged_numbers():
    urls = request.args.getlist('url')

    merged_numbers = set()  # Use a set to avoid repetition
    for url in urls:
        numbers_data = extract_numbers(url)
        merged_numbers.update(numbers_data)

    result = {"numbers": list(merged_numbers)}
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8008)

