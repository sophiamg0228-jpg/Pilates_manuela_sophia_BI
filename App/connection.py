import oracledb

oracledb.init_oracle_client(lib_dir=r"C:\oracle\instantclient_23_26")


def get_connection():
    conn = oracledb.connect(
        user="G06_E01",
        password="Bi!2026-06-01",
        dsn="adbg06_low"
    )
    return conn


def run_query(query, params=None):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        columns = [col[0] for col in cursor.description]
        rows = cursor.fetchall()
        return [dict(zip(columns, row)) for row in rows]
    finally:
        cursor.close()
        conn.close()


def run_dml(query, params=None):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        conn.commit()
        return True
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cursor.close()
        conn.close()