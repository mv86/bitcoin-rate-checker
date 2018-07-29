"""Handle connections to the PostgreSQL database."""
import psycopg2
# from logger import LOG
from .config import db_config

# TODO Add insert for multiple records withouth opening/closing connection every time

def insert(sql, data):
    """Wrapper to insert sql into db. Tuple of data paramaters required"""
    conn = None
    try:
        params = db_config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, data)
        cur.close()
        conn.commit()
    except psycopg2.Error as db_exception:
        print(f'Database error: {db_exception}')
    finally:
        if conn is not None:
            conn.close()


def select(sql, data=()):
    """Wrapper to select sql from db. Tuple of data paramaters optional"""
    conn = None
    try:
        params = db_config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        if data:
            cur.execute(sql, data)
        else:
            cur.execute(sql)
        select_data = cur.fetchall()
        cur.close()
        return select_data
    except psycopg2.DatabaseError as db_exception:
        print(f'Database error: {db_exception}')
    finally:
        if conn is not None:
            conn.close()
