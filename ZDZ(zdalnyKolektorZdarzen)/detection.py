import sqlite3

def select_logs(conn, rule=None, description=None, time=None):
    sql = 'SELECT * FROM logs'
    conditions = []
    params = []
    if rule is not None:
        conditions.append('rule = ?')
        params.append(rule)
    if description is not None:
        conditions.append('description = ?')
        params.append(description)
    if time is not None:
        conditions.append('time = ?')
        params.append(time)
    if conditions:
        sql += ' WHERE ' + ' AND '.join(conditions)
    cur = conn.cursor()
    cur.execute(sql, params)

    # Fetch and return results
    return cur.fetchall()
