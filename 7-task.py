class library():
    def __init__ (self, book):
        self.book=book

    def add(self,book):
        f=open("Books.txt", "a")
        f.write(book)
        f.close()
    def read(self):
        f=open("Books.txt", "r")
        contents=f.read()
        print(contents)
        f.close()
my_ob=library("")
print(my_ob.add("Akrom Malik. Halqa"))
print(my_ob.read())
