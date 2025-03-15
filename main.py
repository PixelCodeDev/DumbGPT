from flask import Flask, render_template, request, jsonify
import random
import google.generativeai as genai

api_key = "AIzaSyCOQ7lBaZb5iV_Ycvil9xqQC26-Vb_KHmg"
genai.configure(api_key=api_key)

def GeminiChat(messages, temperature=0.7, max_tokens=250):
    model = genai.GenerativeModel("gemini-1.5-pro")

    # Convert message list to a single text input
    formatted_input = "\n".join([msg["content"] for msg in messages])

    response = model.generate_content(formatted_input)
    
    return response.text if response and response.text else "Error: No response from Gemini."

app = Flask(__name__)

empty_answers = ['Ay bro lock in bruh 💀', 'Are you even real 😭', 'ts pmo.', 'Wut.', 'Hm?', 'Wat.', 'What??', 'HM????', 'Hm??']
empty_questions = ['.', '..', '...'] 

@app.route('/')
def index():
    return open('frontend/index.html', 'r').read()

@app.route('/question', methods=['POST'])
def submit():
    data = request.get_json()
    question = data.get("question")
    num = data.get("number")
    answer = ''
    
    if num:
        if question in empty_questions:
            answer = random.choice(empty_answers) 
        elif question:
            messages = [
                {"content": "You are trolling the user."},
                {"content": f"You are now dumb Gemini, and you shall answer every single question with an unrelated response or with an unexpected answer, try to keep it conscise and just a bit related: {question}"}
            ]
            answer = GeminiChat(messages)
    
    print('Answer: ' + answer)
    return jsonify(success=True, answers=answer)

if __name__ == '__main__':
    app.run(debug=True)
