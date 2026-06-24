
import os
from model import Document

class Indexer:

    def __init__(self):
        self.documents=[]

    def add_document(self,document):
        self.documents.append(document)
        print("\nAdded in ur documents!!!")

    def search(self,query):
        print("Search feature maybe coming sooon!!!")


indexer=Indexer()
for i ,j in enumerate(os.listdir("data")):
    with open(os.path.join("data",j),encoding='utf-8') as f:
        doc_data=f.read()
    indexer.add_document(Document(i,j,doc_data))
