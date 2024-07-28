import os
from dotenv import load_dotenv
from flask import Flask, render_template, request
import openai

app = Flask(__name__)
load_dotenv()

# Get the OpenAI API key from environment variables
openai_api_key = os.getenv('OPENAI_API_KEY')
print(openai_api_key)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['POST'])

def search():
    query = request.form['query']
    response = get_response_from_gpt(query)
    return render_template('index.html', query=query, response=response)

def get_response_from_gpt(query):
    try:
        # Make a request to the v1/chat/completions endpoint
        response = openai.ChatCompletion.create(
        model="gpt-4",  # Replace with the specific model you are using
        messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": query}
                ]
        )
        return response.choices[0].message['content']
    except Exception as e:
        return str(e)
if __name__ == '__main__':
    app.run(debug=True)
