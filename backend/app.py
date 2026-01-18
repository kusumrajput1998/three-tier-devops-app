from flask import Flask, jsonify
import mysql.connector
import os

app = Flask(__name__)

db = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user="root",
    password="root",
    database="devops"
)

@app.route("/health")
def health():
    return jsonify({"status": "UP"})

@app.route("/users")
def users():
    cursor = db.cursor()
    cursor.execute("SELECT name FROM users")
    result = cursor.fetchall()
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
