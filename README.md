# Silk Web

| Field                          | Detail                                                  |
| ------------------------------ | ------------------------------------------------------- |
| **Website Title**              | Silk Web                                                |
| **Student Name(s)**            | Lewis N                                                 |
| **Class / Course**             | 9CT1                                                    |
| **Repository**                 | https://github.com/TempeHS/2027CT_myFlaskSite_Lewis.N   |
| **Live Site / Codespaces URL** | https://literate-broccoli-5g6r57v6wppgc7jj5.github.dev/ |
| **Date**                       | 31th July 2026                                          |

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

| Field/Feature            | Detail |
| ---------------- | ------ |
| Homepage |   <img width="766" height="450" alt="Animation" src="https://github.com/user-attachments/assets/264ec2bd-2c0b-48c5-8fbb-9d9f7899453b" />                                     This video showcases the Silk Web homepage, including the hero section, background design, carousel, feature cards, and navigation buttons. It demonstrates the main layout and interactive elements that allow users to explore different sections of the website. |
|  Navbar   |     <img width="550" height="323" alt="Animation2" src="https://github.com/user-attachments/assets/564b60da-e8eb-47a1-9d80-7168dbacefd3" />  This video demonstrates the responsive navigation system, including dropdown menus, dropdown arrows, page links, logo redirection, search bar functionality, and the dark/light mode toggle.  |
| Credits |  <img width="800" height="470" alt="Animation3" src="https://github.com/user-attachments/assets/ca6a62d6-fc94-4274-bbb3-54c2990107ee" /> This video displays the Credits page, showing the resources, references, and external materials used during the development of Silk Web.  |
| Mobile Homepage |  <img width="600" height="878" alt="Animation4" src="https://github.com/user-attachments/assets/f066953a-28ae-4350-b2d9-3615f088c148" />  This video demonstrates Silk Web’s responsive design by resizing the browser window and showing how the layout adapts. It highlights the mobile navbar hamburger menu, stacked content, and adjusted page elements for smaller screens.   |
| Extra Features |    <img width="601" height="354" alt="Animation5" src="https://github.com/user-attachments/assets/2d59572f-1b3d-43fe-a93b-a85a76b42cc6" />  This video highlights additional website features, including animations, hover effects, theme switching, interactive cards, and other design improvements that enhance the overall user experience. |

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

## 3.2 What You Delivered

| Page / Feature | Route | What it delivers |
|----------------|-------|------------------|
| Home | `/` | Landing page featuring a Bootstrap hero carousel, parallax scrolling, welcome section, interactive feature cards, website overview, latest updates, and quick navigation to major sections of the site. |
| Pharloom Archive Overview | `/game-info` | Introduces *Hollow Knight: Silksong*, the kingdom of Pharloom, and provides a spoiler-light overview of the game's setting. |
| Hornet Specifications | `/hornet` | Presents information about Hornet, including her background, abilities, combat style, and equipment. |
| Maps & Locations | `/threat-levels` | Displays important regions of Pharloom and provides guidance to help players explore the game world. |
| Bosses & Enemies | `/primary-tools` | Provides spoiler-light information about enemies, bosses, and combat encounters found throughout the game. |
| Silk & Bone Tasks Overview | `/quests` | Introduces the quest system and explains the different quest categories available within the website. |
| Quest Skills | `/quest-skills` | Explains skills and abilities unlocked through quest progression and their gameplay uses. |
| Quest Items | `/quest-items` | Lists important quest items, their purposes, and how they contribute to progression. |
| Extra Rewards | `/quest-rewards` | Describes optional rewards, collectibles, and bonus content earned from completing quests. |
| Future DLC Information | `/dlc` | Provides information about potential future downloadable content and planned expansions. |
| Credits | `/credits` | Acknowledges Team Cherry, image sources, third-party resources, Bootstrap, Flask, and other project credits. |
| Contact | `/contact` | Provides a contact form allowing visitors to send feedback, questions, or suggestions. |
| Custom 404 Page | Invalid routes | Displays a custom Hollow Knight-themed error page that guides users back to the website when a page cannot be found. |
| Responsive Navigation | Global | Responsive Bootstrap navigation bar with dropdown menus, active page highlighting, hover effects, and a collapsible mobile hamburger menu. |
| Animated Navbar Logo | Global | Animated website logo featuring glow effects, hover animations, and a silk-thread inspired underline. |
| Dark & Light Theme | Global | Allows visitors to switch between dark and light themes using a dedicated theme toggle button. |
| Theme Persistence | Global | Saves the selected theme using Local Storage and automatically detects the user's preferred colour scheme on their first visit. |
| Smart Search | `/search` | Allows users to search the website using keywords and redirects them to the most relevant page. |
| Live Search Suggestions | `/api/search` | Displays live search suggestions while users type to improve navigation speed and usability. |
| Back To Top Button | Global | Floating button appears after scrolling and smoothly returns users to the top of the page. |
| Page Loading Animation | Global | Displays a branded loading screen with an animated spinner while pages load. |
| Page Transition Animation | Global | Smooth fade transition effect between internal pages for a more polished browsing experience. |
| Parallax Scrolling | Global | Selected banners, hero images, and content sections move at different speeds while scrolling to create visual depth. |
| Interactive Feature Cards | Home | Feature cards include hover animations, image zoom effects, elevation animations, and clickable navigation links. |
| Responsive Hero Carousel | Home | Bootstrap carousel featuring three rotating hero images with captions, indicators, and navigation controls. |
| Custom Scrollbar | Global | Themed scrollbar styled to match the website with separate light and dark mode appearances. |
| Responsive Design | Global | Fully responsive layouts built using Bootstrap's grid system to support desktop, tablet, and mobile devices. |
| Reusable Flask Templates | Global | Uses Jinja template inheritance and reusable partials to maintain consistent layouts, navigation, and footers across all pages. |
| Bootstrap Components | Global | Implements Bootstrap components including navigation bars, dropdown menus, cards, forms, buttons, carousel, icons, and responsive grids. |
| Enhanced Footer | Global | Custom footer containing navigation links, project information, framework acknowledgements, and copyright details. |
| Automated Testing | Project | Includes pytest tests to verify website routes and ensure key pages load successfully. |
| Theme System | Global | Complete JavaScript theme management system providing instant theme loading, smooth transitions, keyboard shortcut support, and persistent user preferences. |
| Navbar Scroll Effects | Global | Navbar automatically changes appearance while scrolling with blur effects and dynamic styling. |
| Mobile Optimisation | Global | Navigation, search bar, theme toggle, feature cards, and page layouts automatically adapt to smaller screen sizes for improved usability. |
```

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
