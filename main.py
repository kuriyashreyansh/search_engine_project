from indexer import Indexer
from model import Document
from tokenizer import tokenize
from posting import save_posting
from trie import Trie


indexer=Indexer()
trie=Trie()


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

for i in indexer.get_all_terms():
     trie.insert(i)

while True:
        search=input("Search: ")
    
        if search in ["exit","quit"]:
            print("Goodbye👋")
            break

        elif search.strip() == "":
            continue

        else:
            print(trie.search_prefix(search))
            indexer.new_search(search)
