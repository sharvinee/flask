# Flask Triage Dashboard — In‑Class Exercise

This exercise builds a **minimal Flask web application** that displays an Emergency Department (ED) triage dashboard.

You are starting from a **working prototype** that:
- Loads a list of patient encounters (a list of Python dictionaries)
- Calculates a triage score and priority
- Displays the queue in a web dashboard

Your job is to complete the missing pieces so the dashboard becomes **interactive**:
- Patients can be **roomed** (removed from the queue)
- New patients can be **added** via a form

This is an **in‑memory application** (no database). Restarting the server resets the data.

---

## Project Structure

After running the notebook cell that generates the project, you should see:

```
flask_triage_dashboard/
├── app.py
├── requirements.txt
└── templates/
    └── index.html
```

- **app.py** — the Flask application (you will edit this)
- **templates/index.html** — the dashboard UI (already complete)
- **requirements.txt** — Python dependencies (`flask`)

---

## How to Run the App

From a terminal (not from inside Jupyter):

```bash
cd /workspaces/flask-inclass-exercise/dashboard-exercise
python app.py
```


Open the application in your browser.

---

## What Already Works (Do Not Change)

These parts are **already complete** and should not be modified for the exercise:

### ✅ Triage logic
- `triage_score()`
- `priority_bucket()`
- `annotate()`
- `priority_summary()`
- `next_up()`

These functions:
- Compute a triage score
- Assign RED / YELLOW / GREEN
- Sort and summarize the queue

### ✅ Dashboard rendering

The `/` route:

```python
@app.get('/')
def dashboard():
```

- Annotates the queue
- Sorts patients by priority and arrival time
- Renders `index.html`

The HTML template already:
- Displays the table
- Shows summary counts
- Provides buttons and forms that submit POST requests

---

## What You Need to Complete (TODOs)

There are **two required TODO sections** in `app.py`.

---

### ✅ TODO 1 — Room a patient (remove from queue)

**Route:**
```python
@app.post('/roomed/<enc_id>')
def roomed(enc_id):
```

**Goal:**
When a user clicks **“Roomed (Remove)”**, remove that patient from the queue.

**What Flask gives you:**
- `enc_id` → the encounter ID from the URL (e.g., `"E001"`)

**What you must do:**
- Remove the matching dictionary from `queue`

**Recommended solution pattern:**
You will need to alter `queue` so that it contains every dictionary item except for the one with an `id` equal to `enc_id`

✅ After this works:
- Clicking “Roomed (Remove)” should make that row disappear

---

### ✅ TODO 2 — Add a new patient (append to queue)

**Route:**
```python
@app.post('/add')
def add_patient():
```

**Goal:**
When a user submits the **Add New Arrival** form, create a new encounter and add it to the queue.

**What Flask gives you:**
- `request.form` → a dictionary of form values (all **strings**)

**Required fields:**
- `id`
- `age`
- `hr`
- `sbp`
- `chief_complaint`
- `arrival_min`

**What you must do:**
1. Read values from `request.form`
2. Convert numeric fields using `int(...)`
3. Build a dictionary that matches the existing encounter format
4. Append it to `queue`

**Hints:**
create a new encounter dictionary
Add it (append) it to queue

✅ After this works:
- Submitting the form should immediately add a new row to the table
- The new patient should receive a score and priority automatically

---

## How to Tell If Your Code Is Working

### Quick manual tests
1. Click **Roomed (Remove)** on a patient → the row disappears
2. Add a new patient using the form → a new row appears
3. Click **Reset** → the original sample data returns

### If nothing happens
- Watch the **terminal output**
- Flask prints errors there (not in the browser)
- A route mismatch or exception will always appear in the terminal

---

## Common Pitfalls

### 1. `request.form` values are strings

❌ Incorrect:
```python
'age': request.form['age'] + 1
```

✅ Correct:
```python
'age': int(request.form['age'])
```

---

### 2. This app does NOT save data permanently

- Restarting Flask resets the queue
- This is intentional for the exercise

---

## Stretch Goals (Optional)

If you finish early, try one:
- Prevent duplicate encounter IDs
- Add basic validation with `try/except`
- Persist the queue to a JSON file
- Filter the dashboard to show only RED patients
- Keep roomed patients in a separate list instead of deleting them

---

## Learning Takeaway

This exercise demonstrates:
- How backend state (Python lists) changes in response to HTTP requests
- How Flask routes connect UI actions to Python logic
- Why real applications need databases for persistence
- How small Python functions scale into web applications
