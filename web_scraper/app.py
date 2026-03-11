from flask import Flask, render_template, request
import json

app = Flask(__name__)

# Funzione per caricare i dati dal file JSON
def carica_dati():
    try:
        with open("data.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        url = request.form["url"]
        # Qui dovresti aggiungere la funzione per scaricare le news da questo URL
        print(f"URL ricevuto: {url}")

    news = carica_dati()
    return render_template("index.html", news=news)

if __name__ == "__main__":
    app.run(debug=True)
