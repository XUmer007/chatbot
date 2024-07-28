from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Set your OpenAI API key here
openai.api_key = 'your_openai_api_key'

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    
    if not user_message:
        return jsonify({'error': 'Message is required'}), 400
    
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"User: {user_message}\nBot:",
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.9,
        )
        
        bot_message = response.choices[0].text.strip()
        
        return jsonify({'message': bot_message})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
