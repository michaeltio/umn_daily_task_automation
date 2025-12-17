from flask import Flask, request, jsonify, send_from_directory
import json
from flask_cors import CORS


app = Flask(__name__, static_folder='.', static_url_path='')

CORS(app)  
DATA_FILE = 'data.json'

@app.route('/save', methods=['POST'])
def save():
    try:
        data = request.get_json()
        for item in data:
            text = item["task_description"]

            if text.startswith('"') and text.endswith('"'):
                text = text[1:-1]

            item["task_description"] = text
      
        print(data)
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        return jsonify({"status": "success", "message": "Data saved!"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

if __name__ == '__main__':
    app.run(debug=True)
