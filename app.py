from flask import Flask, render_template, jsonify
from database import load_jobs_from_db, load_job_from_db


app = Flask(__name__)

jobs_lst = [
  {
    'id': 1,
    'title': 'data analyst',
    'location': 'Sao Paulo',
    'salary': '3000'
  },
  {
    'id': 2,
    'title': 'data analyst',
    'location': 'Remote',
    'salary': '2500'
  },
  {
    'id': 3,
    'title': 'sales specialist',
    'location': 'Remote',
    'salary': '2000'
  },
  {
    'id': 4,
    'title': 'product developer',
    'location': 'Sao Paulo',
    'salary': '2500'
  }
]

@app.route("/")
def hello_world():
  db_job_lst = load_jobs_from_db()
  return render_template('home.html',
                        jobs=db_job_lst,
                        company_name='Cavalhero Importadora')

@app.route("/api/jobs")
def job_lst():
    job_lst = load_jobs_from_db()
    print(job_lst)
    print(type(job_lst))
    return jsonify(job_lst)

@app.route("/job/<id>")
def show_job(id):
  chosen_job = load_job_from_db(id)
  if not chosen_job:
    return "Job wasn't found", 404
  return render_template('jobpage.html',
                        job = chosen_job,
                        company_name='Cavalhero Importadora')

print(__name__)
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)