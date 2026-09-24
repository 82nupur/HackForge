from flask import Flask, render_template, request, redirect, url_for, jsonify
import os
app = Flask(__name__)

hackathon = {
    "name": "HackForge 2026",
    "tagline": "Build. Innovate. Compete.",
    "date": "15 October 2026",
    "venue": "MIT-WPU, Pune",
    "deadline": "10 October 2026",
    "max_teams": 30
}

teams = []


@app.route("/")
def home():
    slots_remaining = hackathon["max_teams"] - len(teams)
    commit_id = os.getenv("RENDER_GIT_COMMIT", "local-development")

    return render_template(
        "index.html",
        hackathon=hackathon,
        teams=teams,
        slots_remaining=slots_remaining,
        commit_id=commit_id
    )


@app.route("/register", methods=["POST"])
def register():

    team_name = request.form.get("team_name", "").strip()
    leader_name = request.form.get("leader_name", "").strip()
    email = request.form.get("email", "").strip()
    members = request.form.get("members", "").strip()
    project_idea = request.form.get("project_idea", "").strip()

    # Basic validation
    if not team_name or not leader_name or not email:
        return "Please fill in all required fields.", 400

    if not email or "@" not in email:
        return "Please enter a valid email address.", 400

    try:
        members = int(members)
    except ValueError:
        return "Number of members must be a number.", 400

    if members < 2 or members > 4:
        return "A team must have between 2 and 4 members.", 400

    if len(teams) >= hackathon["max_teams"]:
        return "Registration is full.", 400

    new_team = {
        "team_name": team_name,
        "leader_name": leader_name,
        "email": email,
        "members": members,
        "project_idea": project_idea
    }

    teams.append(new_team)

    return redirect(url_for("home"))


@app.route("/api/teams")
def api_teams():
    return jsonify(teams)


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(debug=True)
