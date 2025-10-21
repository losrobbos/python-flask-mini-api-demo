from flask import Flask, request, jsonify

app = Flask(__name__)

# --- GET Route ---
@app.get("/")
def home():
    return "Hallo! Dies ist eine einfache Flask-App 🚀"

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


# Nur ausführen, wenn Datei direkt gestartet wird
if __name__ == "__main__":
    app.run(debug=True)

