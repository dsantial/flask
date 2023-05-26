import os
from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

openai.api_key = "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"

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()

    if 'prompt' not in data:
        return jsonify({'error': 'No prompt provided'}), 400

    prompt = data['prompt']

    # Call GPT-4 API
    response = openai.Completion.create(
      engine="text-davinci-004",
      prompt=prompt,
      max_tokens=100
    )

    return jsonify({'response': response.choices[0].text.strip()})

if __name__ == '__main__':
    app.run(debug=True)
