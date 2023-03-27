from flask import Flask, render_template
from data import defined_jobs
from flask import jsonify

application = Flask(__name__)

@application.route("/")
def hello_world():
    return render_template("home.html", jobs=defined_jobs, company_name = "Amit")

@application.route("/app/data")
def hello_world_api_data():
    return jsonify(results = defined_jobs)


@application.route("/job/<id>")
def specific_job_api_data(id):
    result = list(filter(lambda x: (x["id"]==int(id)), defined_jobs))
    if not result:
        return "Not Found", 404
    return render_template("job.html", result=result, company_name = "Amit")


if __name__ == "__main__":
    application.run(host="0.0.0.0", debug=True)
