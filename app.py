from flask import Flask, render_template, request, redirect, url_for

# Initialize the Flask application block at the absolute top
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
# SIDEBAR ROW ROUTES (Quests Subpage Links)
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
# UPDATED SIDEBAR ROUTES (Main Game Info Subpage & Dropdown Links)
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
# SMART SEARCH ROUTE ENGINE (For Fixed Navigation Bar Search Input)
# ==========================================================================


@app.route("/search")
def search():
    query = request.args.get("q", "").lower().strip()

    # Core database keyword routing map matching search terms to functions
    routes_map = {
        "home": "home",
        "hornet": "hornet",
        "character": "hornet",
        "map": "threat_levels",
        "location": "threat_levels",
        "boss": "primary_tools",
        "enemy": "primary_tools",
        "skill": "quest_skills",
        "item": "quest_items",
        "reward": "quest_rewards",
        "dlc": "dlc_info",
        "contact": "contact",
    }

    # 1. Exact or partial matched keyword redirect checks
    for key, endpoint in routes_map.items():
        if key in query:
            return redirect(url_for(endpoint))

    # 2. Contextual dynamic page suggestion builders
    suggestions = []

    if any(x in query for x in ["info", "lore", "game", "phar", "world"]):
        suggestions.append({"label": "Pharloom Overview", "url": "game_info"})
        suggestions.append({"label": "Hornet Specifications", "url": "hornet"})
        suggestions.append({"label": "Maps & Locations", "url": "threat_levels"})

    if any(
        x in query for x in ["fight", "kill", "combat", "bos", "ene", "tool", "weapon"]
    ):
        suggestions.append({"label": "Bosses & Enemies", "url": "primary_tools"})
        suggestions.append({"label": "Quest Skills", "url": "quest_skills"})

    if any(
        x in query for x in ["quest", "task", "mission", "side", "bone", "silk", "gift"]
    ):
        suggestions.append({"label": "Silk & Bone Tasks", "url": "quests"})
        suggestions.append({"label": "Quest Items", "url": "quest_items"})
        suggestions.append({"label": "Extra Rewards", "url": "quest_rewards"})

    # Default fallback array if input is completely random text strings
    if not suggestions:
        suggestions = [
            {"label": "Pharloom Archive Overview", "url": "game_info"},
            {"label": "Silk & Bone Tasks Overview", "url": "quests"},
            {"label": "Future DLCs Info", "url": "dlc_info"},
        ]

    return render_template(
        "search_error.html", query=request.args.get("q", ""), suggestions=suggestions
    )


# ==========================================================================
# CREDITS PAGE ROUTE
# ==========================================================================


@app.route("/credits")
def credits():
    return render_template("credits.html")


# ======================================================
# LIVE SEARCH SUGGESTIONS API
# ======================================================


# ======================================================
# LIVE SEARCH SUGGESTIONS API
# ======================================================


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
# GLOBAL 404 EXCEPTION ROUTE ENGINE
# ==========================================================================


@app.errorhandler(404)
def page_not_found(e):
    """Catch broken or unregistered paths gracefully with a styled template."""
    return render_template("404.html"), 404


# Keep execution code block down at the absolute bottom
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
