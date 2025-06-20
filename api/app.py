from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), '..', 'templates'))

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/sum", methods=["POST"])
def calculate_sum():
    data = request.get_json()
    a = data.get("a")
    b = data.get("b")
    if a is None or b is None:
        return jsonify({"error": "Champs manquants"}), 400
    return jsonify({"result": a + b})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)