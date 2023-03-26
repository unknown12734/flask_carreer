from flask import Flask, render_template

app = Flask(__name__)

defined_jobs = [
    {
        "id":1,
        "title":"Data Science",
        "location": "Hyderabad",
        "Salary": 1000.00,
        "Work Type": "Remote"
    },
    {
            "id":2,
            "title":"Data Analyst",
            "location": "Bengaluru",
            "Salary": 900.00
    },
    {
            "id":3,
            "title":"Frontend Developer",
            "location": "Bhubaneswar",
            "Salary": 1100.00,
            "Work Type": "Hybrid"
    },
    {
            "id":4,
            "title":"Data Engineer",
            "location": "Hyderabad",
            "Salary": 1500.00,
            "Work Type": "Office"
    }

]
@app.route("/")
def hello_world():
    return render_template("home.html", jobs=defined_jobs, company_name = "Amit")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
