from db_utils import psg2_query
import pandas as pd

FACT_TABLE = "oblique_throw_fact"


# TODO:: protec from sql injection
def get_all() -> pd.DataFrame:
    """
    select everything from fact table
    :return: rows as pandas dataframe
    """
    query = "select * from oblique_throw_fact;"
    result = psg2_query(query)

    return result


def get_throw_id(throw_id: str) -> pd.DataFrame:
    """
    select everything per throw_id from fact table
    :param throw_id: identifier of throw
    :return: rows as pandas dataframe
    """
    query = f"select * from {FACT_TABLE} where throw_id = {throw_id};"
    result = psg2_query(query)

    return result


def remove_throw(throw_id: str) -> pd.DataFrame:
    """
    remove everything per throw id
    :param throw_id: identifier of throw
    :return: rows as pandas dataframe
    """
    query = f"select * from {FACT_TABLE} where throw_id = {throw_id};"
    result = psg2_query(query)

    query = f"delete from {FACT_TABLE} where throw_id = {throw_id};"
    psg2_query(query, select=False)

    return result


def insert_calc(insert_data: dict) -> dict:
    """
    insert new data into fact table
    :param insert_data: data per fact table structure
    :return: rows as pandas dataframe
    """
    query = f"select max(throw_id) as throw_id from {FACT_TABLE};"
    max_throw_id = psg2_query(query)

    if max_throw_id.loc[0]['throw_id'] is None:
        throw_id = 1
    else:
        throw_id = max_throw_id.loc[0]['throw_id'] + 1

    for record in insert_data:
        x = record["x"]
        y = record["y"]
        t = record["t"]

        query = f"insert into {FACT_TABLE} (x, y, t, throw_id) values ({x}, {y}, {t}, {throw_id});"
        psg2_query(query, select=False)

    # TODO:: should return also id
    return insert_data

