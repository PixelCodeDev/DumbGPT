from flask import Flask, render_template, request, jsonify
import random
import google.generativeai as genai

api_key = "AIzaSyCOQ7lBaZb5iV_Ycvil9xqQC26-Vb_KHmg"
genai.configure(api_key=api_key)

msg_type = {
    'dumb': "your the dumb AI, talk in a human way, give off the weirdest answers to the questions, should probably be even unrelated to the question's topic, and be creative with it AND DONT MAKE THE ANSWERS LONG!!!",
    'brainrot': "your the brainrot AI, talk in a human way, talk only in brainrot using 2024-2025 tiktok/instagram brainrot words, try to make the answer somewhat short and less 'slay' and less words"
}

def gemini(messages, temperature=0.7, max_tokens=250):
    model = genai.GenerativeModel("gemini-1.5-pro")

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
    mode = data.get("mode")
    answer = ''
    
    if num:
        if question in empty_questions:
            answer = random.choice(empty_answers) 
        elif question:
            messages = [
                {"content": f"{msg_type['dumb']}: {question}"}
            ]
            answer = gemini(messages)
    
    print('Answer: ' + answer)
    return jsonify(success=True, answers=answer)

if __name__ == '__main__':
    app.run(debug=True)
