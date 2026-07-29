# The Silk Web - Spoilers-Free Silksong Database

A simple, fast, and secure Python Flask web application designed for VS Code in GitHub Codespaces using a dark atmospheric *Hollow Knight: Silksong* wiki aesthetic.

## Description

**The Silk Web** serves as a structured, multi-page web archive that delivers gameplay records and progression hints with zero to minimal narrative spoilers. Built using the **Python Flask** micro-framework and styled with **Bootstrap 5**, this repository houses comprehensive database modules tracking core campaign elements, side objectives, and expansion content. The user interface features custom-engineered interactive styles, such as responsive scroll-fading navigation elements, white needle-tip hover indicators, wiki-style infobox tablets, and a dynamic contextual search engine designed to intercept user entries and route them cleanly across the kingdom parameters.

## Getting Started

### Dependencies

Before launching the web system, verify your workspace environment satisfies the following baseline prerequisites:
* **Operating System:** Linux (Ubuntu/Debian environment inside GitHub Codespaces), Windows 10/11, or macOS.
* **Runtime Environment:** Python 3.8 or higher.
* **Core Framework:** Flask 2.0+ (and its corresponding template engine dependency, Jinja2).
* **Testing Engine:** Pytest 7.0+ for running the automated unit test matrix.

### Installing

1. Open your terminal shell layout at the bottom of VS Code.
2. Ensure you have activated your local Python virtual environment container (`venv` or `env` folder). If not initialized, execute:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Upgrade your package manager installer tool and deploy the core micro-framework dependencies:
   ```bash
   pip install --upgrade pip
   pip install flask pytest
   ```
4. Place your custom wallpaper image file inside your project structure as `static/images/bg.jpg`. Ensure the name is completely lowercase to match the CSS routing directives.

### Executing program

To launch the server instance local loop and test out your features:

1. Start up your backend python application server file:
   ```bash
   python app.py
   ```
   *Alternatively, use the native Flask execution utility:*
   ```bash
   flask run --host=0.0.0.0 --port=5000
   ```
2. Click the open browser pop-up link exposed by your GitHub Codespace environment to access your active rendering view dashboard.
3. To trigger the comprehensive automated quality assurance test runner matrix, run:
   ```bash
   pytest
   ```

## Help

### Common Issues & Troubleshooting

* **Problem:** `NameError: name 'app' is not defined` inside `app.py`.
  * *Solution:* Python scripts interpret statements from top to bottom. Ensure `app = Flask(__name__)` is initialized at the absolute top of your script block before any `@app.route` wrapper modules try to tap into it.
* **Problem:** Changes to the background image layout boundaries or navbar colors are not displaying.
  * *Solution:* Browsers hold onto layout style sheets heavily. Force an instantaneous cache rewrite by entering **Ctrl + F5** (Windows) or **Cmd + Shift + R** (Mac) inside your web view browser window.
* **Problem:** Clicking a navigation dropdown line returns a `TemplateNotFound` failure crash screen.
  * *Solution:* Check your folder layout naming. If your code renders `"maps.html"` but your file is saved as `"Maps.html"` or `"threat_levels.html"`, Flask will crash due to character casing discrepancies.

To review available background command help summaries and framework details, invoke:
```bash
flask --help
```

## Authors

* **Lewis N.** - Lead Full-Stack Application Architect - [@MrSushi2](https://github.com)
* **TempeHS Framework Template** - Project Blueprint Foundation and Contextual Parameters.

## Version History

* **0.2**
  * Integrated multi-level drop-down navbar frameworks.
  * Added white glowing Silksong needle link hovers and vertical indicator triangles.
  * Added smart search logic mapping with custom suggestion error templates.
  * Added universal fixed background min-height stabilization overrides.
  * Configured dynamic global custom `404 Page Not Found` pulse exception modules.
  * Extended automated Pytest integration matrices to match active endpoints.
* **0.1**
  * Initial Release.
  * Established baseline Flask blueprint mappings and standard Bootstrap container card carousels.

## License

This project is licensed under the MIT License - see the `LICENSE.md` file for details.

## Acknowledgments

* **Team Cherry** - For crafting the gorgeous art direction and environmental atmosphere of *Hollow Knight: Silksong*.
* **Hollow Knight Wiki Contributors** - For inspiring the structural layout guidelines utilized in our infobox parameters grids.
