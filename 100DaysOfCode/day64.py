class Library:
    def __init__(self):
       
        self.books=["Python","Java","C++","HTML","CSS","SQL","AI","ML","Git","Linux"]
        self.no_books= len(self.books)
    
    def add(self,book_name):
        self.books.append(book_name)
        self.no_books +=1
        print(f"Name of Books are : {self.books}")
        print(f"No. of Books in Library : {self.no_books}")
        
    def show(self):
        print(f"Name of Books are : {self.books}")
        print(f"No. of Books in Library : {self.no_books}")
        
    def no(self):
        print(f"No. of Books in Library : {self.no_books}")
        
        
        
e=Library ()
e.show()
e.add("Ram")

e.add("Hindu")
e.add("Muslim ")
e.no()
