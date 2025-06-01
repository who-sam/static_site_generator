# Static Site Generator

This is a simple static site generator built in Python. It converts Markdown files from the `content/` directory into styled HTML files using a provided template, then outputs everything into the `docs/` directory—ready for deployment with GitHub Pages.

---

## Prerequisites

Make sure you have the following tools installed:

| Tool              | Description                                           |
| ----------------- | ----------------------------------------------------- |
| Python 3          | Required to run the site generator                    |
| Git               | Required for version control                          |
| Bash              | To run the shell scripts                              |
| GitHub CLI (`gh`) | Optional, for automation (repo creation, Pages setup) |

---

## Features

* Converts Markdown to HTML with styling
* Recursively processes folders
* Uses a common HTML template
* Copies static assets (CSS, images, favicon, etc.)
* Compatible with GitHub Pages (uses `docs/` as the output folder)

---

## Directory Structure

```text
.
├── build.sh       -------------------> # Builds the site (runs the Python generator)
├── main.sh       --------------------> # Builds & starts local preview server on port 8888
├── test.sh       --------------------> # Runs unit tests
├── template.html       --------------> # Template HTML file for every page
├── content/       -------------------> # Markdown source files
│   └── blog/       ------------------> # Nested structure supported
│       └── .../index.md
├── static/       --------------------> # Static files (CSS, images, favicon, etc.)
│   └── index.css       --------------> # Global stylesheet
├── docs/       ----------------------> # Output directory (auto-generated)
│   └── ...       --------------------> # Final HTML pages and assets
├── src/       -----------------------> # Python source code
│   ├── main.py       ----------------> # Entry point of the generator
│   ├── copystatic.py       ----------> # Copies static assets to docs/
│   ├── generating_html.py              # Markdown-to-HTML rendering logic
│   ├── markdown_blocks.py
│   ├── markdown_to_html.py
│   ├── htmlnode.py
│   ├── textnode.py
│   ├── inline_markdown.py
│   └── test_*.py       --------------> # Unit tests for individual components
```

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/static-site-generator.git
cd static-site-generator
```

### 2. Build the Site

```bash
./build.sh
```

This builds the final HTML files into the `docs/` directory.

### 3. Preview Locally

```bash
./main.sh
```

This starts a local web server at `http://localhost:8888`.

### 4. Run Tests

```bash
./test.sh
```

Runs all the unit tests using Python's `unittest`.

---

## Deploy to GitHub Pages

1. create a new GitHub repo
2. Push your project directory to GitHub.
3. On the GitHub repo page, go to **Settings > Pages**.
4. Under **Source**, choose:

   * Branch: `main`
   * Folder: `/docs`
5. Save the settings.

Your site will be live at:
`https://<your-username>.github.io/<repo-name>/`

---

## Optional: Automate GitHub Setup

```bash
#!/bin/bash
REPO="my-static-site"
USERNAME="your-username"

gh repo create "$REPO" --public --source=. --remote=origin --push
./build.sh
git add .
git commit -m "Initial build"
git push origin main

echo "Enable GitHub Pages at:"
echo "https://github.com/$USERNAME/$REPO/settings/pages"
```
