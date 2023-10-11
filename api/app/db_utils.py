import psycopg2
import pandas as pd
import os

# TODO:: put as env var
PORT = 5432


def psg2_query(query, select=True):

    # TODO:: move
    host = os.getenv("POSTGRES_HOST")
    db = os.getenv("POSTGRES_DB")
    user = os.getenv("POSTGRES_USER")
    pswd = os.getenv("POSTGRES_PASSWORD")

    with psycopg2.connect(host=host, dbname=db, user=user, password=pswd, port=PORT) as conn:
        with conn.cursor() as cur:
            cur.execute(query)
            if select:
                data = cur.fetchall()
                cols = [col[0] for col in cur.description]
                cols_dot = []
                for col in cols:
                    if "." in col:
                        cols_dot.append(col.split(".")[1])
                    else:
                        cols_dot.append(col)

                data = pd.DataFrame.from_records(data, columns=cols_dot)

                return data
