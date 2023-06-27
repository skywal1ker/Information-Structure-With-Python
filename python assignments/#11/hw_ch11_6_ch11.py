class Book:
    def __init__(self, name="N/A", publishername="N/A", publicationYear="2022", type="Paperback", price=0, author="N/A",
                 isbn="N/A"):
        self.name = name
        self.publishername = publishername
        self.price = price
        self.type = type
        self.publicationYear = publicationYear
        self.author = author
        self.isbn = isbn

    def getName(self):
        return self.name

    def getPrice(self):
        return self.price

    def getType(self):
        return self.type

    def getAuthor(self):
        return self.author

    def getPublisher(self):
        return self.publishername

    def getPublicationYear(self):
        return self.publicationYear

    def getISBN(self):
        return self.isbn


howtoSaveYourFourthMarriage = Book("How to Save Your Fourth Marriage: One Person Can Transform a Relationship",
                                   "Balboa Press", "2022", "Paperback", 19.99, "Terri Crosby", "1982278358")
print("Details of your favourite book")
print("Name: " + str(howtoSaveYourFourthMarriage.getName()))
print("Price: $" + str(howtoSaveYourFourthMarriage.getPrice()))
print("Type: " + str(howtoSaveYourFourthMarriage.getType()))
print("Author: " + str(howtoSaveYourFourthMarriage.getAuthor()))
print("Publisher: " + str(howtoSaveYourFourthMarriage.getPublisher()))
print("Publication Year: " + str(howtoSaveYourFourthMarriage.getPublicationYear()))
print("ISBN: " + str(howtoSaveYourFourthMarriage.getISBN()))