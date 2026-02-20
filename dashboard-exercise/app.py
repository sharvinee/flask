from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

INITIAL_ENCOUNTERS = [
    {"id": "E001", "age": 72, "hr": 118, "sbp": 86,  "chief_complaint": "chest pain", "arrival_min": 5},
    {"id": "E002", "age": 34, "hr": 92,  "sbp": 122, "chief_complaint": "headache",   "arrival_min": 12},
    {"id": "E003", "age": 58, "hr": 105, "sbp": 99,  "chief_complaint": "shortness of breath", "arrival_min": 30},
    {"id": "E004", "age": 81, "hr": 88,  "sbp": 140, "chief_complaint": "fall",       "arrival_min": 55},
    {"id": "E005", "age": 47, "hr": 131, "sbp": 92,  "chief_complaint": "fever",      "arrival_min": 18},
    {"id": "E006", "age": 29, "hr": 76,  "sbp": 110, "chief_complaint": "abdominal pain", "arrival_min": 40},
]

HIGH_RISK_COMPLAINTS = ["chest pain", "shortness of breath", "stroke symptoms"]

# Working queue (in-memory)
queue = [e.copy() for e in INITIAL_ENCOUNTERS]

# Calculates a triage score for an encounter based on age, vitals, chief complaint, and arrival time
def triage_score(encounter, high_risk_list):
    score = 0
    if encounter['age'] >= 65:
        score += 2
    if encounter['hr'] >= 120:
        score += 2
    if encounter['sbp'] < 90:
        score += 3
    if encounter['chief_complaint'] in high_risk_list:
        score += 2
    if encounter['arrival_min'] <= 10:
        score += 1
    return score

# Maps triage score to priority bucket (RED, YELLOW, GREEN)
def priority_bucket(score):
    if score >= 7:
        return 'RED'
    elif score >= 4:
        return 'YELLOW'
    else:
        return 'GREEN'

# Annotates each encounter with a triage score and priority level
def annotate(encounters):
    annotated = []
    for e in encounters:
        e2 = e.copy()
        s = triage_score(e2, HIGH_RISK_COMPLAINTS)
        e2['score'] = s
        e2['priority'] = priority_bucket(s)
        annotated.append(e2)
    return annotated

# creates a summary dict with counts of each priority level (RED, YELLOW, GREEN)
def priority_summary(annotated):
    summary = {'RED': 0, 'YELLOW': 0, 'GREEN': 0}
    for e in annotated:
        p = e.get('priority')
        if p in summary:
            summary[p] += 1
    return summary

# Finds the encounter with the highest triage score (and earliest arrival time as tiebreaker) and returns its id
def next_up(annotated):
    if not annotated:
        return None
    best = annotated[0]
    for e in annotated[1:]:
        if e['score'] > best['score']:
            best = e
        elif e['score'] == best['score'] and e['arrival_min'] < best['arrival_min']:
            best = e
    return best['id']


@app.get('/')
def dashboard():
    annotated = annotate(queue)
    annotated.sort(key=lambda e: (-e['score'], e['arrival_min']))
    return render_template(
        'index.html',
        encounters=annotated,
        summary=priority_summary(annotated),
        next_id=next_up(annotated)
    )


@app.post('/roomed/<enc_id>')
def roomed(enc_id):
    global queue
    # TODO (STUDENT): Remove the encounter with id == enc_id
    # Hint: list comprehension
    for e in queue:
        if e['id'] == enc_id:
            queue.remove(e)
            break
    return redirect(url_for('dashboard'))

@app.post('/add')
def add_patient():
    global queue

    # TODO (STUDENT): Build a new encounter dict from request.form
    # Required fields: id, age, hr, sbp, chief_complaint, arrival_min
    # Remember: request.form values are strings.
    new_encounter = {
        'id': request.form['id'],
        'age': int(request.form['age']),
        'hr': int(request.form['hr']),
        'sbp': int(request.form['sbp']),
        'chief_complaint': request.form['chief_complaint'],
        'arrival_min': int(request.form['arrival_min'])
    }
    queue.append(new_encounter)

    return redirect(url_for('dashboard'))


@app.post('/reset')
def reset():
    global queue
    queue = [e.copy() for e in INITIAL_ENCOUNTERS]
    return redirect(url_for('dashboard'))


if __name__ == '__main__':
    app.run(debug=True)
