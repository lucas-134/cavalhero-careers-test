from flask import Flask, render_template, jsonify

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
    return render_template('home.html',
                          jobs=jobs_lst,
                          company_name='Cavalhero Importadora')

@app.route("/api/jo")
def job_lst():
    return jsonify(jobs_lst)

print(__name__)
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)