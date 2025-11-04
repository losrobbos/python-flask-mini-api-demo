import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# --- GET Route ---
@app.get("/")
def home():
    return """<h1>Da ist eine crazy Überschrift<h1>
    <h2>Pages:</h2>
    <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/info">Info</a></li>
    </ul>

    <p>Send POST data to /echo route</p>
    <form method="POST" action="/echo">
    <button>Submit</button>
    </form>

    """

@app.get("/info")
def info():
    return "Hallo! Dies ist eine einfache Flask-App 🚀"

@app.get("/todos")
def todos():
    # Antwort zurückgeben
    return jsonify(["Wake the dog", "Empty the trash", "Tame some python"]), 200

# --- POST Route ---
@app.post("/echo")
def echo():
    # Erwartet JSON-Daten im Body
    data = request.get_json()
    if not data:
        return jsonify({"error": "Bitte JSON-Daten senden!"}), 400

    # Antwort zurückgeben
    return jsonify({
        "nachricht": "Daten empfangen!",
        "deine_daten": data
    }), 200



port = os.environ.get("PORT", 8000)

# Nur ausführen, wenn Datei direkt (!) gestartet wird (also wenn diese Datei das Entry Script ist)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port, debug=False)

