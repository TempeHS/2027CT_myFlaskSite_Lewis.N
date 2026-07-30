import pytest
from app import app

# ======================================================
# FIXTURE
# ======================================================


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


# ======================================================
# ALL ROUTE STATUS TESTS
# ======================================================


@pytest.mark.parametrize(
    "route",
    [
        "/",
        "/game-info",
        "/quests",
        "/quests/skills",
        "/quests/items",
        "/quests/rewards",
        "/dlc",
        "/contact",
        "/info/pharloom",
        "/info/threat-levels",
        "/info/primary-tools",
        "/boss1",
        "/boss2",
        "/boss3",
        "/credits",
    ],
)
def test_all_routes_exist(client, route):

    response = client.get(route)

    assert response.status_code == 200


# ======================================================
# PAGE CONTENT TESTS
# ======================================================


@pytest.mark.parametrize(
    "route,text",
    [
        ("/", "The Silk Web"),
        ("/game-info", "Pharloom"),
        ("/quests", "Silk"),
        ("/quests/skills", "Skills"),
        ("/quests/items", "Items"),
        ("/quests/rewards", "Rewards"),
        ("/dlc", "DLC"),
        ("/contact", "Contact"),
        ("/info/pharloom", "Hornet"),
        ("/info/threat-levels", "Map"),
        ("/info/primary-tools", "Bosses"),
        ("/credits", "Credits"),
    ],
)
def test_page_contains_expected_content(client, route, text):

    response = client.get(route)

    assert text.encode() in response.data


# ======================================================
# NAVBAR TESTS
# ======================================================


def test_navbar_exists(client):

    response = client.get("/")

    assert b"navbar" in response.data


def test_navbar_links_exist(client):

    response = client.get("/")

    html = response.data

    assert b"Home" in html
    assert b"Bosses" in html
    assert b"Quests" in html
    assert b"Contact" in html


def test_dropdown_exists(client):

    response = client.get("/")

    assert b"dropdown" in response.data


# ======================================================
# BOOTSTRAP + CSS TESTS
# ======================================================


def test_bootstrap_loaded(client):

    response = client.get("/")

    assert b"bootstrap" in response.data


def test_custom_css_loaded(client):

    response = client.get("/")

    assert b"style.css" in response.data


def test_javascript_loaded(client):

    response = client.get("/")

    assert b".js" in response.data


# ======================================================
# DARK MODE SYSTEM
# ======================================================


def test_dark_theme_default(client):

    response = client.get("/")

    assert b'data-theme="dark"' in response.data


def test_theme_toggle_exists(client):

    response = client.get("/")

    assert b"themeToggle" in response.data


def test_theme_icon_exists(client):

    response = client.get("/")

    assert b"themeIcon" in response.data


def test_theme_script_exists(client):

    response = client.get("/")

    assert b"theme.js" in response.data


# ======================================================
# SEARCH ROUTE TESTS
# ======================================================


@pytest.mark.parametrize(
    "query,destination",
    [
        ("boss", "/info/primary-tools"),
        ("enemy", "/info/primary-tools"),
        ("hornet", "/info/pharloom"),
        ("character", "/info/pharloom"),
        ("map", "/info/threat-levels"),
        ("location", "/info/threat-levels"),
        ("quest", "/quests"),
        ("task", "/quests"),
        ("skill", "/quests/skills"),
        ("item", "/quests/items"),
        ("reward", "/quests/rewards"),
        ("dlc", "/dlc"),
        ("contact", "/contact"),
    ],
)
def test_search_redirects(client, query, destination):

    response = client.get(f"/search?q={query}")

    assert response.status_code == 302
    assert destination in response.location


def test_search_case_insensitive(client):

    response = client.get("/search?q=HORNET")

    assert response.status_code == 302
    assert "/info/pharloom" in response.location


def test_search_unknown(client):

    response = client.get("/search?q=randomthing123")

    assert response.status_code == 200
    assert b"Database" in response.data


# ======================================================
# LIVE SEARCH API TESTS
# ======================================================


def test_api_returns_json(client):

    response = client.get("/api/search?q=boss")

    assert response.status_code == 200
    assert response.content_type == "application/json"


def test_api_returns_results(client):

    response = client.get("/api/search?q=hornet")

    data = response.get_json()

    assert "results" in data
    assert len(data["results"]) > 0


def test_api_empty_search(client):

    response = client.get("/api/search?q=")

    data = response.get_json()

    assert data["results"] == []


def test_api_limits_results(client):

    response = client.get("/api/search?q=a")

    data = response.get_json()

    assert len(data["results"]) <= 5


# ======================================================
# 404 ERROR TESTS
# ======================================================


def test_custom_404(client):

    response = client.get("/fake-page")

    assert response.status_code == 404
    assert b"404" in response.data


# ======================================================
# WIKI COMPONENT TESTS
# ======================================================


@pytest.mark.parametrize(
    "page",
    [
        "/info/pharloom",
        "/info/primary-tools",
        "/boss1",
        "/boss2",
        "/boss3",
    ],
)
def test_infobox_exists(client, page):

    response = client.get(page)

    assert b"card" in response.data


def test_cards_exist(client):

    response = client.get("/")

    assert b"card" in response.data


def test_breadcrumb_exists(client):

    response = client.get("/boss1")

    assert b"breadcrumb" in response.data


# ======================================================
# BOSS DATABASE TESTS
# ======================================================


@pytest.mark.parametrize(
    "boss",
    [
        "/boss1",
        "/boss2",
        "/boss3",
    ],
)
def test_boss_pages_have_titles(client, boss):

    response = client.get(boss)

    assert response.status_code == 200
    assert b"Boss" in response.data


def test_boss_images_exist(client):

    for boss in ["/boss1", "/boss2", "/boss3"]:

        response = client.get(boss)

        assert b"img" in response.data


# ======================================================
# SECURITY / HTTP TESTS
# ======================================================


def test_no_server_error(client):

    pages = ["/", "/quests", "/boss1"]

    for page in pages:

        response = client.get(page)

        assert response.status_code != 500


def test_get_only_pages(client):

    response = client.get("/")

    assert response.status_code == 200


# ======================================================
# FOOTER TESTS
# ======================================================


def test_footer_exists(client):

    response = client.get("/")

    assert b"footer" in response.data


# ======================================================
# TEMPLATE RENDER TESTS
# ======================================================


def test_home_template(client):

    response = client.get("/")

    assert response.status_code == 200
    assert b"html" in response.data


def test_all_pages_return_html(client):

    pages = ["/", "/quests", "/boss1", "/credits"]

    for page in pages:

        response = client.get(page)

        assert "text/html" in response.content_type
