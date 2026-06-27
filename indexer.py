from db import get_connection

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
        print("Search feature maybe coming sooon!!!")

# import os
# from model import Document
# indexer=Indexer()
# for i ,j in enumerate(os.listdir("data")):
#     with open(os.path.join("data",j),encoding='utf-8') as f:
#         doc_data=f.read()
#     indexer.add_document(Document(i,j,doc_data))
