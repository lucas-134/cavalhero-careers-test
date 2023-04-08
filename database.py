from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ["DB_CONNECTION_STRING"]

engine = create_engine(
  db_connection_string,
  connect_args={
    "ssl": {
      "ssl_ca":"etc/ssl/cert.pem"
    }
  })

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs2"))
    result_all = result.all()
    dict_lst = []
    for row in result_all:
      dict_lst.append(row._mapping)
    return dict_lst

#print(load_jobs_from_db())

def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs2 where id =" + str(id)))
    job_data = result.all()
    if len(job_data) == 0:
      return None
    else:
      return job_data[0]._mapping

#print(load_job_from_db(2))

def add_application_to_db(id, application):
  with engine.connect() as conn:
    query = text("INSERT INTO applications (job_id, full_name, email, phone) VALUES (:job_id, :name, :email, :phone)")
    
    conn.execute(query, {"job_id": id, "name": application['name'], "email": application['email'], "phone": application['phone']})