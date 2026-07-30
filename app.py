from flask import Flask, render_template, request, redirect, url_for

# Initialize Flask application
app = Flask(__name__)


# ==========================================================================
# CORE PAGES ROUTES
# ==========================================================================


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/game-info")
def game_info():
    return render_template("info.html")


@app.route("/quests")
def quests():
    return render_template("quests.html")


@app.route("/dlc")
def dlc_info():
    return render_template("dlc.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


# ==========================================================================
# QUEST SUBPAGES
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
# GAME INFO SUBPAGES
# ==========================================================================


@app.route("/info/pharloom")
def hornet():
    return render_template("hornet.html")


@app.route("/info/threat-levels")
def threat_levels():
    return render_template("maps.html")


@app.route("/info/primary-tools")
def primary_tools():
    return render_template("bosses.html")


# ==========================================================================
# BOSS PAGES
# ==========================================================================


@app.route("/boss1")
def boss1():
    return render_template("boss1.html")


@app.route("/boss2")
def boss2():
    return render_template("boss2.html")


@app.route("/boss3")
def boss3():
    return render_template("boss3.html")


# ==========================================================================
# CREDITS
# ==========================================================================


@app.route("/credits")
def credits():
    return render_template("credits.html")


# ==========================================================================
# SMART SEARCH ENGINE
# ==========================================================================


@app.route("/search")
def search():

    query = request.args.get("q", "").lower().strip()

    routes_map = {
        "home": "home",
        "hornet": "hornet",
        "character": "hornet",
        "map": "threat_levels",
        "location": "threat_levels",
        "boss": "primary_tools",
        "enemy": "primary_tools",
        "quest": "quests",
        "task": "quests",
        "mission": "quests",
        "skill": "quest_skills",
        "item": "quest_items",
        "reward": "quest_rewards",
        "dlc": "dlc_info",
        "contact": "contact",
    }

    # Redirect exact keyword matches
    for key, endpoint in routes_map.items():

        if key in query:
            return redirect(url_for(endpoint))

    # Search suggestions

    suggestions = []

    if any(x in query for x in ["info", "lore", "game", "phar", "world"]):

        suggestions.append({"label": "Pharloom Overview", "url": "game_info"})

        suggestions.append({"label": "Hornet Specifications", "url": "hornet"})

        suggestions.append({"label": "Maps & Locations", "url": "threat_levels"})

    if any(x in query for x in ["fight", "combat", "boss", "enemy", "weapon"]):

        suggestions.append({"label": "Bosses & Enemies", "url": "primary_tools"})

    if any(x in query for x in ["quest", "task", "mission", "silk"]):

        suggestions.append({"label": "Silk & Bone Tasks", "url": "quests"})

        suggestions.append({"label": "Quest Items", "url": "quest_items"})

    if not suggestions:

        suggestions = [
            {"label": "Pharloom Archive Overview", "url": "game_info"},
            {"label": "Silk & Bone Tasks Overview", "url": "quests"},
            {"label": "Future DLC Information", "url": "dlc_info"},
        ]

    return render_template("search_error.html", query=query, suggestions=suggestions)


# ==========================================================================
# LIVE SEARCH API
# ==========================================================================


@app.route("/api/search")
def live_search():

    query = request.args.get("q", "").lower().strip()

    pages = [
        {
            "name": "Pharloom Archive Overview",
            "url": "game_info",
            "keywords": ["info", "pharloom", "world", "archive"],
        },
        {
            "name": "Hornet Specifications",
            "url": "hornet",
            "keywords": ["hornet", "character", "needle"],
        },
        {
            "name": "Maps & Locations",
            "url": "threat_levels",
            "keywords": ["map", "location", "area"],
        },
        {
            "name": "Bosses & Enemies",
            "url": "primary_tools",
            "keywords": ["boss", "enemy", "fight"],
        },
        {
            "name": "Silk & Bone Tasks",
            "url": "quests",
            "keywords": ["quest", "task", "mission"],
        },
        {
            "name": "Quest Skills",
            "url": "quest_skills",
            "keywords": ["skill", "ability"],
        },
        {
            "name": "Quest Items",
            "url": "quest_items",
            "keywords": ["item", "collect"],
        },
        {
            "name": "Extra Rewards",
            "url": "quest_rewards",
            "keywords": ["reward", "gift"],
        },
        {
            "name": "Future DLC Information",
            "url": "dlc_info",
            "keywords": ["dlc", "update"],
        },
        {
            "name": "Credits",
            "url": "credits",
            "keywords": ["credit", "developer"],
        },
        {
            "name": "Contact",
            "url": "contact",
            "keywords": ["contact", "message"],
        },
    ]

    results = []

    if query:

        for page in pages:

            if query in page["name"].lower() or any(
                query in keyword for keyword in page["keywords"]
            ):

                results.append({"title": page["name"], "url": url_for(page["url"])})

    return {"results": results[:5]}


# ==========================================================================
# CUSTOM 404 ERROR PAGE
# ==========================================================================


@app.errorhandler(404)
def page_not_found(e):

    return render_template("404.html"), 404


# ==========================================================================
# RUN APP
# ==========================================================================


if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000, debug=True)
