from fastapi import FastAPI
import psycopg2
import os
app = FastAPI()


@app.get("/")
def read_root():
    host = os.getenv("POSTGRES_HOST")
    db = os.getenv("POSTGRES_DB")
    user = os.getenv("POSTGRES_USER")
    pswd = os.getenv("POSTGRES_PASSWORD")

    conn = psycopg2.connect(host=host, dbname=db, user=user, password=pswd, port=5432)
    cur = conn.cursor()
    cur.execute("select current_date;")

    return {"return": cur.fetchone()}
