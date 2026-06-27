from db import get_connection
from terms import get_or_create_term_id
def save_posting(document,token_dict):
    conn=get_connection()
    cur=conn.cursor()
    for word,count in token_dict.items():
        cur.execute("insert into postings(term_id,doc_id,term_frequency) values(%s,%s,%s)",(get_or_create_term_id(word),document.Id,count))
        
    conn.commit()
    cur.close()
    conn.close()