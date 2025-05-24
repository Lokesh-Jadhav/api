import json
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load student data from the provided JSON file
with open('q-vercel-python.json') as f:
    students = json.load(f)

@app.get("/")
def home():
    return {"marks": []}

@app.route('/api', methods=['GET'])
def get_marks():
    names = request.args.getlist('name')
    response = {"marks": []}
    
    # Create a dictionary for fast lookup of student marks by name
    student_marks = {student['name']: student['marks'] for student in students}

    # Append marks in the order of names in the query
    for name in names:
        if name in student_marks:
            response["marks"].append(student_marks[name])

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
