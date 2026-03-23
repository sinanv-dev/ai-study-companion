from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# 🔑 
genai.configure(api_key="AIzaSyBkqaagLrbtQfUfboRIXop899X7ugQGUHI")

model = genai.GenerativeModel("gemini-1.5-flash")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    try:
        user_input = request.json["message"]
        response = model.generate_content(user_input)
        return jsonify({"reply": response.text})
    except Exception as e:
        return jsonify({"reply": f"Error: {str(e)}"})

@app.route("/notes", methods=["POST"])
def notes():
    try:
        topic = request.json["topic"]
        prompt = f"Generate short notes with key points on {topic}"
        response = model.generate_content(prompt)
        return jsonify({"notes": response.text})
    except Exception as e:
        return jsonify({"notes": f"Error: {str(e)}"})

@app.route("/quiz", methods=["POST"])
def quiz():
    try:
        topic = request.json["topic"]
        prompt = f"Generate 5 MCQ questions with answers on {topic}"
        response = model.generate_content(prompt)
        return jsonify({"quiz": response.text})
    except Exception as e:
        return jsonify({"quiz": f"Error: {str(e)}"})

@app.route("/planner", methods=["POST"])
def planner():
    try:
        data = request.json
        subjects = data["subjects"]
        days = data["days"]
        prompt = f"Create a {days}-day study plan for: {subjects}"
        response = model.generate_content(prompt)
        return jsonify({"plan": response.text})
    except Exception as e:
        return jsonify({"plan": f"Error: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)