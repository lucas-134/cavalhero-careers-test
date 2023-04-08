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
