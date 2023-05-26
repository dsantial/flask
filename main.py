from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()

    if 'prompt' not in data:
        return jsonify({'error': 'No prompt provided'}), 400

    prompt = data['prompt']

    # TODO: Call GPT-4 API and count tokens

    return jsonify({'prompt': prompt})

if __name__ == '__main__':
    app.run(debug=True)
