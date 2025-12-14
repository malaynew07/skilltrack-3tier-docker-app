from flask import Flask, request, jsonify
from flask_cors import CORS
from db import get_db_connection

app = Flask(__name__)
CORS(app)

@app.route("/add", methods=["POST"])
def add_skill():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO skills (name, email, skill, progress)
        VALUES (%s, %s, %s, %s)
    """, (data["name"], data["email"], data["skill"], data["progress"]))

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Skill saved successfully"})

@app.route("/")
def home():
    return "SkillTrack Backend Running"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

