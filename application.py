from flask import Flask, render_template
from data import session, Job
from flask import jsonify


application = Flask(__name__)

jobs = session.query(Job)

def load_data(session,jobs):
    defined_jobs = []
    for job in jobs:
        defined_jobs.append(job.__dict__)
    return defined_jobs


@application.route("/")
def hello_world():
    return render_template("home.html", jobs=load_data(session,jobs), company_name = "Amit")

@application.route("/app/data")
def hello_world_api_data():
    return jsonify(results = load_data(session,jobs))


@application.route("/job/<id>")
def specific_job_api_data(id):
    result = list(filter(lambda x: (x["id"]==int(id)), load_data(session,jobs)))
    if not result:
        return "Not Found", 404
    return render_template("job.html", result=result, company_name = "Amit")


if __name__ == "__main__":
    application.run(host="0.0.0.0", debug=True)
