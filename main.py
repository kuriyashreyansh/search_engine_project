from indexer import Indexer
from model import Document
from tokenizer import tokenize
from posting import save_posting
indexer=Indexer()

doc=indexer.get_total_documents()
if doc==0:
    import os
    docs=[]
    for i,j in enumerate(os.listdir("data")):
        with open(os.path.join("data",j),encoding='utf-8') as f:
            content=f.read()
        docs.append(Document(i+1,j,content))
    for i in docs:
        indexer.add_document(i)
        tokens=tokenize(i.text)
        save_posting(i,tokens)
while True:
        search=input("Search: ")

        if search in ["exit","quit"]:
            print("Goodbye👋")
            break

        elif search.strip() == "":
            continue

        else:
            indexer.new_search(search)