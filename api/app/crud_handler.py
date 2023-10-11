from db_utils import psg2_query
import pandas as pd


# TODO:: define fact table const
# TODO:: protec from sql injection
# TODO:: check if id does not exists
def get_all() -> pd.DataFrame:
    query = "select * from oblique_thow_fact;"
    result = psg2_query(query)

    return result


def get_throw_id(throw_id: str) -> pd.DataFrame:
    query = f"select * from oblique_thow_fact where throw_id = {throw_id};"
    result = psg2_query(query)

    return result


def remove_throw(throw_id: str) -> pd.DataFrame:
    query = f"select * from oblique_thow_fact where throw_id = {throw_id};"
    result = psg2_query(query)

    query = f"delete from oblique_thow_fact where throw_id = {throw_id};"
    psg2_query(query, select=False)

    return result


def insert_calc(insert_data: dict) -> dict:

    query = f"select max(throw_id) as throw_id from oblique_thow_fact;"
    max_throw_id = psg2_query(query)

    if max_throw_id.loc[0]['throw_id'] is None:
        throw_id = 1
    else:
        throw_id = max_throw_id.loc[0]['throw_id'] + 1

    for record in insert_data:
        x = record["x"]
        y = record["y"]
        t = record["t"]

        query = f"insert into oblique_thow_fact (x, y, t, throw_id) values ({x}, {y}, {t}, {throw_id});"
        psg2_query(query, select=False)

    return insert_data

