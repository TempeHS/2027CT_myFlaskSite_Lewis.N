from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/game-info")
def game_info():
    return render_template("info.html")


# NEW DROPDOWN PAGE ROUTE
@app.route("/quests")
def quests():
    return render_template("quests.html")


# NEW FUTURE DLC ROUTE (For Card 3)
@app.route("/dlc")
def dlc_info():
    return render_template("dlc.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


# ==========================================================================
# NEW SIDEBAR ROW ROUTES (Quests Sidebar Links)
# ==========================================================================


@app.route("/quests/skills")
def quest_skills():
    return render_template("quest_skills.html")


@app.route("/quests/items")
def quest_items():
    return render_template("quest_items.html")


@app.route("/quests/rewards")
def quest_rewards():
    return render_template("quest_rewards.html")


# ==========================================================================
# UPDATED ROUTES (Main Game Info Sidebar & Dropdown Links)
# ==========================================================================


@app.route("/info/pharloom")
def hornet():
    # UPDATED: Now looks specifically for templates/hornet.html
    return render_template("hornet.html")


@app.route("/info/threat-levels")
def threat_levels():
    # UPDATED: Now looks specifically for templates/maps.html
    return render_template("maps.html")


@app.route("/info/primary-tools")
def primary_tools():
    # UPDATED: Now looks specifically for templates/bosses.html
    return render_template("bosses.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
