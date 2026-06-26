import re

def tokenize(text):
    tokens=re.findall(r'\w+',text.lower())
    return tokens

text='My name is Shreyansh , and i love to talk, also my motive is to love u'
tokens=tokenize(text)
print((tokens))

token_dict={}

for token in tokens:
    token_dict[token]=token_dict.get(token,0)+1
print(token_dict)