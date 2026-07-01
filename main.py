from indexer import Indexer
indexer=Indexer()

while True:
    search=input("Search: ")

    if search in ["exit","quit"]:
        print("Goodbye👋")
        break

    elif search.strip() == "":
        continue

    else:
        indexer.new_search(search)