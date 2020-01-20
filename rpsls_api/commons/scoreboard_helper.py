from sqlalchemy.sql import text
from rpsls_api.extensions import db

def get_user_stats(username):
    sql = """
        SELECT
            username,
            COALESCE(sum(
                    CASE WHEN win THEN
                        1
                    ELSE
                        0
                    END), 0) AS win,
            COALESCE(sum(
                    CASE WHEN lose THEN
                        1
                    ELSE
                        0
                    END), 0) AS lose,
                        COALESCE(sum(
                    CASE WHEN tie THEN
                        1
                    ELSE
                        0
                    END), 0) AS tie
        FROM
            scoreboard
        WHERE
            username = :username
        GROUP BY
            username
    """
    sql_result = db.engine.execute(text(sql), {"username": username})

    for row in sql_result:
        return {
            "win": row.win,
            "lose": row.lose,
            "tie": row.tie
        }