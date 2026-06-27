from posting import save_posting
from tokenizer import tokenize
from terms import get_or_create_term_id
from model import Document
from indexer import Indexer
import os


indexer=Indexer()
for i, j in enumerate(os.listdir("data")):
    with open(os.path.join("data", j), encoding='utf-8') as f:
        doc_data = f.read()
        k=Document(i, j, doc_data)
    indexer.add_document(k)
    token_dict=tokenize(k.text)
    save_posting(k,token_dict)

# with open(os.path.join("data","machine_learning.txt"),encoding='utf-8') as f:
#     doc_data=f.read()
# k=Document(2,"machine_learning.txt",doc_data)
# indexer.add_document(k)
# token_dict=tokenize(k.text)
# save_posting(k,token_dict)