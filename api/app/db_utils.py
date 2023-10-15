import psycopg2
import pandas as pd
import os

host = os.getenv("POSTGRES_HOST")
db = os.getenv("POSTGRES_DB")
user = os.getenv("POSTGRES_USER")
pswd = os.getenv("POSTGRES_PASSWORD")
port = os.getenv("POSTGRES_PORT")


def psg2_query(query: str, select=True) -> pd.DataFrame:
    """
    executes query via psycopg2, connection and cursor are closed at the end
    :param query: query string which should be executed
    :param select: if the query should return selected rows
    :return: selected rows if select set to True in pandas dataframe
    """
    with psycopg2.connect(host=host, dbname=db, user=user, password=pswd, port=port) as conn:
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
