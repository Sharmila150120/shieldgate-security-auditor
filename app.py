from flask import Flask, render_template, request
import re

app = Flask(__name__)

def audit_strength(text):
    score = 0
    feedback = []

   
    if len(text) >= 12:
        score += 2
    elif len(text) >= 8:
        score += 1
    else:
        feedback.append("❌ Too short (Minimum 8-12 characters recommended).")

    
    if re.search(r"[A-Z]", text): score += 1
    else: feedback.append("⚠️ Missing uppercase letters.")

    if re.search(r"[a-z]", text): score += 1
    else: feedback.append("⚠️ Missing lowercase letters.")

    if re.search(r"\d", text): score += 1
    else: feedback.append("⚠️ Missing numbers.")

    if re.search(r"[ !@#$%^&*(),.?\":{}|<>]", text): score += 1
    else: feedback.append("⚠️ Missing special characters.")

   
    if score >= 5: rating = "STRONG"
    elif score >= 3: rating = "MODERATE"
    else: rating = "WEAK"

    return rating, feedback, score

@app.route('/', methods=['GET', 'POST'])
def index():
    results = None
    if request.method == 'POST':
        user_input = request.form.get('target')
        rating, feedback, score = audit_strength(user_input)
        results = {'rating': rating, 'feedback': feedback, 'score': score}
    
    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)