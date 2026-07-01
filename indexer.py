from db import get_connection
from tokenizer import tokenize
import math

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

    # Single Search query

    # def search(self,query):
    #     query_token=tokenize(query)
    #     search_result=self.get_term_id(list(query_token.keys())[0])
    #     if search_result is None:
    #         print("No results found")
    #         return None
    #     else:
    #         sorted_items = sorted(search_result, key=lambda item: item[1], reverse=True)
    #         for doc_id,frequency in sorted_items:
    #             title=self.get_document_title(doc_id)
    #             print(f"{query} word is found in {title} {frequency} times")
        # return sorted_result
        
    def get_term_id(self,word):
        conn=get_connection()
        cur=conn.cursor()
        cur.execute("SELECT term_id FROM terms WHERE word = %s",(word,))
        match=cur.fetchone()
        if match is None:
            cur.close()
            conn.close()
            return None
        else:
            cur.execute("select doc_id,term_frequency from postings where term_id=%s",(match[0],))
            fetched_data=cur.fetchall()
            conn.commit()
            cur.close()
            conn.close()
            return (match[0],fetched_data)
        

    def get_document_title(self,doc_id):
        conn=get_connection()
        cur=conn.cursor()
        cur.execute("select title from documents where id=%s",(doc_id,))
        document_title=cur.fetchone()[0]
        cur.close()
        conn.close()
        return document_title
    

        
#TF-IDF value is counted by no. of sentences and word that is repeated in sentences
    def get_document_count(self,doc_id):
        conn=get_connection()
        cur=conn.cursor()
        cur.execute("Select sum(term_frequency) from postings where doc_id=%s",(doc_id,))
        frequency=cur.fetchone()[0]
        cur.close()
        conn.close()
        return frequency
    

    def get_idf(self,term_id):
        return math.log(self.get_total_documents()/self.get_document_frequency(term_id))
    


# MULTIPLE WORD SEARCH handling
# ADDING NEW PART OF FINDING TF IN NEW_SEARCH WHERE K(FREQ) IS DIRECTLY DIVIDED BY TOTAL WORDS

    def new_search(self,query):
        query_tokens=tokenize(query)
        summurised_data={}
        for i in query_tokens.keys():
            result=self.get_term_id(i)
            if result is None:
                    pass
            else:
                term_id,term_id_frequency=result
                for j,k in term_id_frequency:
                    summurised_data[j]=summurised_data.get(j,0)+(k/self.get_document_count(j))*self.get_idf(term_id)
        sorted_summrised_data=sorted(summurised_data.items(),key=lambda i : i[1],reverse=True)
        for i,j in sorted_summrised_data:
            print(f"{self.get_document_title(i)} file has {query} Relevance score : {j}")
        

        
    def get_total_documents(self):
        conn=get_connection()
        cur=conn.cursor()
        cur.execute("select count(id) from documents")
        total_documents=cur.fetchone()[0]
        cur.close()
        conn.close()
        return total_documents
    

    def get_document_frequency(self,term_id):
        conn=get_connection()
        cur=conn.cursor()
        cur.execute("select count(*) from postings where term_id = %s",(term_id,))
        doc_freq=cur.fetchone()[0]
        cur.close()
        conn.close()
        return doc_freq
