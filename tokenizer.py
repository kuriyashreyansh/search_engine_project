import re

def tokenize(text):
    tokens=re.findall(r'\w+',text.lower())


    token_dict={}
    # here we had done the change of value means at 1st coming it is coming value 1 then after another same token value changes to 2 and also it is 0 for token not present
    for token in tokens:
        token_dict[token]=token_dict.get(token,0)+1
    return token_dict