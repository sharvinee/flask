# Patient Education Portal — Flask Learning Guide

## Purpose of This Exercise

This project is a **learning-focused Flask web application** designed to help you understand how web applications are structured using:

- **Routes** (URLs connected to Python functions)
- **Templates** (HTML files rendered dynamically)
- **Static content** (CSS for styling)

The application presents a **Patient Education Portal** using fictional content. No real patient data is used. The goal is not medical accuracy, but **understanding how Flask applications are built and organized**.

You are encouraged to explore the code, modify it, and experiment.

---

## What This Application Does

When running, the application allows you to:

- Visit a home page that introduces the portal
- View education pages for different health topics
- Submit a simple form to see how query parameters affect output
- Observe how Flask connects Python code to HTML pages

---

## Project Structure

```
patient-education-portal/
│
├── app.py
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── topic.html
│   └── risk.html
│
└── static/
    └── styles.css
```

Each part of this structure demonstrates a core Flask concept.

---

## Routes: Connecting URLs to Python Code

Routes live in **`app.py`**.

A route tells Flask:
> “When a user goes to this URL, run this Python function.”

Routes are defined using decorators that start with `@app.route()`.

### Home Route (`/`)

```python
@app.route("/")
def index():
    return render_template("index.html")
```

Try this:
1. Run the app
2. Open in a browser
3. Notice that Flask returns an HTML page

---

### Dynamic Route (`/topic/<topic_name>`)

```python
@app.route("/topic/<topic_name>")
def topic(topic_name):
    return render_template("topic.html", topic=topic_name)
```

This demonstrates dynamic URLs and passing values from the URL into templates.

---

### Query Parameters (`/risk?age=...`)

```python
@app.route("/risk")
def risk():
    age = request.args.get("age")
    return render_template("risk.html", age=age)
```

Query parameters allow one route to behave differently based on user input.

---

## Templates: Rendering HTML Dynamically

Templates live in the **`templates/`** directory and use **Jinja**.

### Template Inheritance (`base.html`)

`base.html` defines the shared layout and includes the CSS file.

Other templates extend this file using `{% extends "base.html" %}`.

---

### Variables, Loops, and Conditions

Templates demonstrate:
- Variables: `{{ topic }}`
- Loops: `{% for item in list %}`
- Conditions: `{% if condition %}`

These allow HTML to change based on Python data.

---

## Static Content (CSS)

Static files live in the **`static/`** directory.

CSS is linked using:

```html
{{ url_for('static', filename='styles.css') }}
```

Static content controls how the application looks, not how it behaves.

---

## Running the Application

```bash
cd /workspaces/flask-inclass-exercise/patient-portal-exercise
python app.py
```

Then visit the project in a browser.

---

## How to Explore and Learn

To learn the most from this exercise:

- Change route paths and observe errors
- Edit template text and refresh the browser
- Add a new topic page
- Modify the CSS to see layout changes

Learning happens fastest when you experiment.

---

## Key Concepts Demonstrated

| Concept | Where to Look |
|------|--------------|
| Routes | `app.py` |
| Dynamic URLs | `/topic/<topic_name>` |
| Query Parameters | `/risk?age=...` |
| Templates | `templates/` |
| Template Inheritance | `base.html` |
| Static Content | `static/styles.css` |

---

## Academic Note

All content in this application is fictional and used solely for educational purposes.
