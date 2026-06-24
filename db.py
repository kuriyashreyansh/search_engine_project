import psycopg

def get_connection():
    connection=psycopg.connect("dbname=searchdb user=postgres password=sdkndk2dbk host=localhost")
    return connection