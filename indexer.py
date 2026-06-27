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
        #as it is single word earlier hence i am not adding tuple format
        cur.execute("SELECT term_id FROM terms WHERE word = %s",(word,))
        match=cur.fetchone()
        if match is None:
            print("Query word not found")
            conn.commit()
            cur.close()
            conn.close()
            return None
        else:
            cur.execute("select (doc_id,term_frequency) from postings where word=%s",(match))
            conn.commit()
            cur.close()
            conn.close()
            return match



# import os
# from model import Document
# indexer=Indexer()
# for i ,j in enumerate(os.listdir("data")):
#     with open(os.path.join("data",j),encoding='utf-8') as f:
#         doc_data=f.read()
#     indexer.add_document(Document(i,j,doc_data))
