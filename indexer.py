from db import get_connection
from tokenizer import tokenize

class Indexer:

    def __init__(self):
        self.documents=[]


    def add_document(self,document):
        conn=get_connection()
        self.documents.append(document)
        cur=conn.cursor()
        cur.execute("insert into documents(title,content) values(%s,%s) returning Id",(document.title,document.text))
        new_id=cur.fetchone()[0]
        document.Id=new_id
        conn.commit()
        cur.close()
        conn.close()
        print("\nAdded in ur documents!!!")


    def search(self,query):
        query_token=tokenize(query)
        print("Search feature maybe coming sooon!!!")
        
    def get_term_id(self,word):
        conn=get_connection()
        cur=conn.cursor()
        cur.execute("SELECT term_id FROM terms WHERE word = %s",(word,))
        match=cur.fetchone()
        if match is None:
            cur.close()
            conn.close()
            return "Query word not found"
        else:
            cur.execute("select doc_id,term_frequency from postings where term_id=%s",(match[0],))
            fetched_data=cur.fetchall()
            conn.commit()
            cur.close()
            conn.close()
            return fetched_data
        
indexer=Indexer()
print(indexer.get_term_id("learning"))
print(indexer.get_term_id("xyzabc"))



# import os
# from model import Document
# indexer=Indexer()
# for i ,j in enumerate(os.listdir("data")):
#     with open(os.path.join("data",j),encoding='utf-8') as f:
#         doc_data=f.read()
#     indexer.add_document(Document(i,j,doc_data))
