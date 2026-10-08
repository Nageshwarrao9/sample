from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Student Grade Calculator</h1>
    <p>Use /grade?marks=85</p>
    """

@app.route("/grade")
def grade():
    marks = int(request.args.get("marks"))

    if marks >= 90:
        result = "A+"
    elif marks >= 80:
        result = "A"
    elif marks >= 70:
        result = "B"
    elif marks >= 60:
        result = "C"
    else:
        result = "Fail"

    return "Marks: " + str(marks) + "<br>Grade: " + result

app.run(host="0.0.0.0", port=5000)