class Book:
    def __init__(self,title,author,pages):
        self.title=title
        self.author=author
        self.pages=pages
    
    def info(self):
        print(f"{self.title} book's author is {self.author} having {self.pages} no. of pages")

b1=Book('Mindset','Carol',265)
b2=Book('Atomic Habit','James',360)

b1.info()
b2.info()