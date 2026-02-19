from flask import Flask, render_template, request

app = Flask(__name__)

TOPICS = {
    "diabetes": [
        "Monitor blood glucose as recommended.",
        "Focus on balanced meals and activity.",
        "Keep follow-up appointments."
    ],
    "hypertension": [
        "Track blood pressure regularly.",
        "Limit sodium and follow a heart-healthy diet.",
        "Take medications as prescribed."
    ],
    "vaccines": [
        "Vaccines reduce risk of serious illness.",
        "Keep an up-to-date immunization record.",
        "Ask a clinician about recommended schedules."
    ],
}

@app.route("/")
def index():
    return render_template("index.html", topics=sorted(TOPICS.keys()))

@app.route("/topic/<topic_name>")
def topic(topic_name):
    points = TOPICS[topic_name.lower()]
    #points = TOPICS.get(topic_name.lower())
    return render_template("topic.html", topic=topic_name, points=points)

@app.route("/risk")
def risk():
    age_raw = request.args.get("age", "") 
    try:
        age = int(age_raw)
    except:
        age = None

    if age is None:
        bucket = "unknown"
        message = "Enter an age to see a demo message (not medical advice)."
    elif age < 18:
        bucket = "pediatric"
        message = "Demo: Pediatric education resources may differ by age group."
    elif age < 65:
        bucket = "adult"
        message = "Demo: Adult education resources often focus on prevention and screening."
    else:
        bucket = "older_adult"
        message = "Demo: Older adult resources may include fall prevention and medication review."

    return render_template("risk.html", age=age, bucket=bucket, message=message)

if __name__ == "__main__":
    app.run(debug=True)