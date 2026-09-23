from flask import Flask, render_template

app = Flask(__name__)

hackathon = {
    "name": "HackForge 2026",
    "tagline": "Build. Innovate. Compete.",
    "date": "15 October 2026",
    "venue": "MIT-WPU, Pune",
    "deadline": "10 October 2026",
    "max_teams": 30
}


@app.route("/")
def home():
    return render_template("index.html", hackathon=hackathon)


if __name__ == "__main__":
    app.run(debug=True)