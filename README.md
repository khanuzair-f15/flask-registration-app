# Flask Registration & Blog App

A beginner-friendly Flask web application built to practice routing, Jinja2 templating, and HTML form handling. It includes a registration form, a confirmation page that displays the submitted data, and a small blog-style page.

## Live Demo

🔗 [https://flask-registration-app-8oqj.onrender.com/](https://flask-registration-app-8oqj.onrender.com/)

## Features

- **Home / Registration page** (`/`) — a styled form that collects Full Name, Phone Number, and City
- **Confirmation page** (`/confirmation`) — handles the form's `POST` request and displays the submitted details back to the user
- **Blog page** (`/web`) — a simple static blog-post layout with an image

## Project Structure

```
Flask/
├── new.py                       # Main Flask app and route definitions
├── requirements.txt              # Python dependencies
├── Procfile                       # Start command for deployment
├── static/
│   └── images/
│       └── xyz.jpeg              # Image used on the blog page
└── templates/
    ├── base.html                 # Base template (shared layout/blocks)
    ├── home_page.html             # Registration form (extends base.html)
    ├── confirmation_page.html     # Post-submission confirmation view
    └── web.html                   # Blog-style page
```

## Tech Stack

- Python 3
- Flask
- Jinja2 (templating)
- HTML / CSS
- Gunicorn (production server)
- Render (hosting)

## Getting Started

### Prerequisites

- Python 3.x installed
- pip

### Installation

```bash
git clone https://github.com/khanuzair-f15/<your-repo-name>.git
cd <your-repo-name>
pip install -r requirements.txt
```

### Run the app

```bash
python new.py
```

Then open **http://127.0.0.1:5000/** in your browser.

## Routes

| Route            | Method     | Description                                   |
|-------------------|------------|------------------------------------------------|
| `/`               | GET        | Renders the registration home page             |
| `/web`            | GET        | Renders a simple blog page                      |
| `/confirmation`   | GET, POST  | Processes the form and shows confirmation data  |

## Deployment

This app is deployed for free on [Render](https://render.com).

To deploy your own copy:

1. Fork or clone this repo, and make sure `requirements.txt` and `Procfile` are present in the root.
2. Sign up on [Render](https://render.com) using your GitHub account.
3. Click **New +** → **Web Service** and connect this repository.
4. Set the following:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn new:web`
   - **Instance Type:** Free
5. Click **Create Web Service** — Render will build and deploy automatically, giving you a live URL in a few minutes.

## Author

**Uzair** — [GitHub](https://github.com/khanuzair-f15)