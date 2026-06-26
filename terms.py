
from db import get_connection
def get_or_create_term_id(word):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT term_id FROM terms WHERE word = %s", (word,))
    result = cur.fetchone()
    
    # now: check if result is None or not, and act accordingly
    if result is None:
        cur.execute("insert into terms(word) values(%s) returning term_id",(word,))
        result=cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()
        return result
    else:
        conn.commit()
        cur.close()
        conn.close()
        return result[0]