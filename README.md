# Website Name

| Field                          | Detail                                                  |
| ------------------------------ | ------------------------------------------------------- |
| **Website Title**              | Silk Web                                                |
| **Student Name(s)**            | Lewis N                                                 |
| **Class / Course**             | 9CT1                                                    |
| **Repository**                 | https://github.com/TempeHS/2027CT_myFlaskSite_Lewis.N   |
| **Live Site / Codespaces URL** | https://literate-broccoli-5g6r57v6wppgc7jj5.github.dev/ |
| **Date**                       | 30th July 2026                                          |

> Your website is the main piece of work. This README is short on purpose — it
> points a reader to your **2-minute walkthrough** and gives an honest
> **evaluation of what you delivered**.

---

## 1. Overview

**Purpose:** <!-- One or two sentences: what the site is and why it exists (from your Statement of Intent). -->
Silk Web is a fan-made information website for Hollow Knight: Silksong. It provides players with information about the game world, quests, bosses, maps, and future downloadable content through a modern, easy-to-navigate website.
**Target audience:** <!-- One sentence: who the site is for (from your personas). -->
The website is designed for Hollow Knight: Silksong players, especially new and returning players looking for guides, game information, and quest assistance without needing to search multiple websites.
**Technology stack:** Python Flask · Jinja2 templates · Bootstrap (CDN) · custom CSS · pytest

---

## 2. Walkthrough Video (2 minutes)

This is the most important part of your documentation — it shows your website running.

<!--
  Embed a ~2 minute walkthrough. Replace VIDEO_ID with your YouTube video ID:
  [![Website Walkthrough](https://img.youtube.com/vi/VIDEO_ID/0.jpg)](https://www.youtube.com/watch?v=VIDEO_ID)

  OR link a screen recording stored in the repository:
  [Watch the Walkthrough](./docs/walkthrough.mp4)
-->

| Field            | Detail |
| ---------------- | ------ |
| **Link / Embed** |        |
| **Duration**     |        |

**Your walkthrough should show:**

- A tour of each page (Home and Contact)
- Your key Bootstrap components working (navbar, carousel, cards, map, form)
- The layout responding when the window is resized (navbar collapsing to a hamburger)

---

## 3. Evaluation — Did You Deliver Your Statement of Intent?

This is the most important written part of your documentation. Evaluate the
website you **delivered** against the **Statement of Intent** you wrote during
planning. Be honest and use evidence — point to a page, a feature or a test.

### 3.1 Your Statement of Intent

The purpose of Silk Web was to create a professional, responsive fan website for Hollow Knight: Silksong that allows players to quickly access information about Pharloom, bosses, quests, maps, and future DLC content. The website aimed to provide an attractive interface, simple navigation, responsive design, and useful search functionality while remaining easy for both new and experienced players to use.

<!-- Paste the Statement of Intent you wrote during planning so the reader can judge your site against it. -->

### 3.2 What You Delivered

| Page / Feature | Route | What it delivers |
| Home | `/` | Landing page featuring a Bootstrap carousel, parallax scrolling, welcome section, and feature cards linking to key areas of the website. |
| Pharloom Archive Overview | `/game-info` | Provides an overview of Hollow Knight: Silksong and introduces the world of Pharloom. |
| Hornet Specifications | `/info/pharloom` | Contains information about Hornet, including her abilities and role in the game. |
| Maps & Locations | `/info/threat-levels` | Displays important locations and maps to help players explore Pharloom. |
| Bosses & Enemies | `/info/primary-tools` | Provides information about bosses and enemies throughout the game. |
| Silk & Bone Tasks | `/quests` | Main quests page providing an overview of available quest content. |
| Quest Skills | `/quests/skills` | Describes skills and abilities gained during quests. |
| Quest Items | `/quests/items` | Lists important quest items and explains their uses. |
| Extra Rewards | `/quests/rewards` | Shows optional quest rewards and collectibles. |
| Future DLC Information | `/dlc` | Provides information about planned or future downloadable content. |
| Credits | `/credits` | Acknowledges Team Cherry, third-party resources, and project contributors. |
| Contact | `/contact` | Contact page allowing users to submit feedback or enquiries. |
| Custom 404 Page | Invalid routes | Displays a custom Hollow Knight themed error page when users visit a page that does not exist. |
| Responsive Navigation | Global | Bootstrap navigation bar with dropdown menus that automatically collapse into a hamburger menu on tablets and mobile devices. |
| Dark & Light Mode | Global | Toggle button allows users to switch between light and dark themes, with preferences saved using Local Storage. |
| Smart Search | `/search` | Keyword-based search redirects users to the most relevant page or displays suggested pages when no exact match is found. |
| Live Search Suggestions | `/api/search` | Displays suggested pages beneath the search bar while users type. |
| Responsive Design | Global | Website layout automatically adapts to desktop, tablet, and mobile screen sizes using Bootstrap's responsive grid system. |
| Parallax Scrolling | Global | Hero images move at a different speed while scrolling to create a modern visual effect. |
| Reusable Flask Templates | Global | Uses Jinja templates and partials so the navigation bar, footer, and overall layout remain consistent across every page. |
| Theme Persistence | Global | The selected theme is remembered between visits using browser Local Storage. |
| Bootstrap Components | Global | Uses a responsive navbar, dropdown menus, carousel, cards, forms, buttons, icons, and grid layout throughout the website. |
| Automated Testing | Project | Includes pytest tests to verify website routes and ensure important pages load correctly. |

### 3.3 Evaluation Against Your Intent (2–3 paragraphs)

> Take each aim in your Statement of Intent and evaluate **how well the
> delivered site meets it**. Where did you meet your intent? Where did you fall
> short, and why? Support every judgement with evidence from your site.

<!-- Write 2–3 paragraphs. -->

The finished website successfully achieves most of the goals outlined in my Statement of Intent. It provides visitors with organised information about Hollow Knight: Silksong using multiple linked pages, dropdown navigation, and a consistent visual design. The use of Flask templates and reusable navigation means every page shares the same layout, making the website easy to navigate. The responsive Bootstrap navigation bar works on both desktop and mobile devices, while the custom CSS creates a unique appearance suited to the game's atmosphere.

Additional features improved the overall user experience beyond the original plan. These include a dark and light mode theme system that remembers the user's preference using local storage, a custom search feature that redirects users to relevant pages based on keywords, and automated pytest tests to verify routes and major website features. These additions improve usability and demonstrate the functionality of the website.

Although the website meets most of its intended goals, there are still areas that could be expanded. More detailed game information, additional boss guides, interactive maps, and user accounts could be added in future versions. Because Hollow Knight: Silksong continues to receive updates, the website would also benefit from regular content updates to keep information current.

### 3.4 Overall Effectiveness (1–2 paragraphs)

> Step back from the detail. Overall, **how effective** is the website at
> achieving its purpose for its target audience? Weigh what works against what
> falls short, and state what you would improve to better meet your intent.

<!-- Write 1–2 paragraphs. -->

Overall, Silk Web is an effective fan website that achieves its purpose of providing players with an organised source of Hollow Knight: Silksong information. The responsive layout, clean navigation, dropdown menus, search function, and dark/light theme create a professional user experience that is easy to use across different devices.

## If I continued developing the project, I would add a database for user accounts, favourites, and saved progress, improve the search system with more advanced filtering, and include more detailed guides with interactive maps and images. These improvements would make the website even more useful for players while further meeting the goals of my original Statement of Intent.

## 4. Acknowledgements

> List anything you did not make yourself — tutorials, images, fonts, icons and
> libraries. Using content without acknowledgement may constitute academic
> misconduct.

| What you used           | Source / Creator | Licence   | What you used it for             |
| ----------------------- | ---------------- | --------- | -------------------------------- |
| Bootstrap               | Bootstrap team   | MIT       | Layout and components            |
| Flask                   | Pallets Projects | BSD       | Web server and routing           |
| Bootstrap Icons         | Bootstrap team   | MIT       | Navigation and interface icons   |
| Hollow Knight: Silksong | Team Cherry      | Copyright | Game information and inspiration |

---

> **Student Declaration:** All work submitted is my own except where explicitly acknowledged above.
