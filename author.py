#author class creation
class Author:
    #initialization method 
    def __init__ (self, name):
        #author name
        self.name = name
        #empty set for authors books
        self.books = set()
    
    #publish method takes title of book and adds to objects book list
    def publish(self, title):
        #if title already exists, print error
        if title in self.books:
            print('title already exists')
        
        #if not add title to books set
        else:
            self.books.add(title)

    #__str__ method returns a string with authors name & names of all books in book_list
    def __str__(self):
        #adds books to list, or prints 'No published books' if no books exist
        book_list = ', '.join(self.books) or 'No published books'
        #returning formatted string of author and books published
        return f'NAME: {self.name} BOOKS PUBLISHED:  {book_list}'


def main():
    #creating author object and giving it name
    jk = Author ('Jk Rolling')

    #calling publish method to add book titles to book_list
    jk.publish('goblet of fire')

    #adding duplicate titles to trigger error method
    jk.publish('philosphers stone')
    jk.publish('philosphers stone')
    print(jk)

    #testing if author has no books
    kelsey = Author('Kelsey')
    print(kelsey)

#calling main method
main()

