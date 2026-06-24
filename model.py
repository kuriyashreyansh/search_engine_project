class Document:
    def __init__(self,Id,title,text):
        self.Id=Id
        self.title=title
        self.text=text

    def __repr__(self):
        return f'{self.Id}. {self.title}\n\n{self.text}\n'

import os
docs=[]
for i,j in enumerate(os.listdir("data")):
    with open(os.path.join("data",j),encoding='utf-8') as f:
        content=f.read()
    docs.append(Document(i+1,j,content))

for d in docs:
    print(d)