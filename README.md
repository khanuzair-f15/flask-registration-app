# Flask Registration & Blog App

A beginner-friendly Flask web application built to practice routing, Jinja2 templating, and HTML form handling. It includes a registration form, a confirmation page that displays the submitted data, and a small blog-style page.

## Features

- **Home / Registration page** (`/`) — a styled form that collects Full Name, Phone Number, and City
- **Confirmation page** (`/confirmation`) — handles the form's `POST` request and displays the submitted details back to the user
- **Blog page** (`/web`) — a simple static blog-post layout with an image

## Project Structure

```
Flask/
├── new.py                       # Main Flask app and route definitions
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

## Getting Started

### Prerequisites

- Python 3.x installed
- pip

### Installation

```bash
git clone https://github.com/khanuzair-f15/<your-repo-name>.git
cd <your-repo-name>
pip install flask
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

## Author

**Uzair** — [GitHub](https://github.com/khanuzair-f15)
 
