from abc import ABC, abstractmethod

#defining the class
class Resource(ABC):
    @abstractmethod
    def get_reference(self):
        return ("Resource")
    
    def __init__(self, author, title, publication_year, place_of_publication=None, publisher=None):
        self.author = author
        self.title = title
        self.publication_year = publication_year
        self.place_of_publication = place_of_publication
        self.publisher = publisher
        
resource1 = Resource (["author1"], "title", 2002)
print (resource1.get_reference())
resource2 = Resource (["author1", "author2"], "title", 2002, "place", "publisher")


class PrintedBook(Resource):
    def __init__(self, author, title, publication_year, place_of_publication=None, publisher=None, edition_Number=None):
        super().__init__(author, title, publication_year, place_of_publication, publisher)
        self.edition_Number = edition_Number
    
    def get_reference(self):
        ref = super().get_reference()
        return (f"{ref} PrintedBook. ")

resource1 = PrintedBook (["author1"], "title", 2002)

print (resource1.get_reference())

authors = ["Erich Gamma", "Richard Helm", "Ralph Johnson", "John Vlissides"]

book = PrintedBook(authors, "Design Patterns", 1994, "United States", "Pearson Education")


print(book.get_reference())