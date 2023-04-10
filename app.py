from flask import Flask, render_template, jsonify, request
from database import load_jobs_from_db, load_job_from_db, add_application_to_db, add_note_data


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

@app.route("/job/<id>/apply", methods=['post'])
def apply_to_job(id):
  data = request.form
  chosen_job = load_job_from_db(id)
  add_application_to_db(id, data)
  return render_template('application_submitted.html',
                        application = data,
                        company = 'Cavalhero Express',
                        job = chosen_job)

@app.route("/notepad", methods=['get', 'post'])
def notepad():
    if request.method == "POST":
      text_data = request.form['texto_inserido']
      print(text_data)
      add_note_data(text_data)
      return render_template('test.html',
                            note_inserted = text_data)
    else:
      return render_template('notepad.html')

@app.route("/test")
def test():
    return render_template('test.html')

print(__name__)
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)