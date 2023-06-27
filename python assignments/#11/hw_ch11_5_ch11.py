class Flight_ticket:
    def __init__(self, start, destination, date, Class, fare, name,ticket_no):
        self.date = date
        self.ticket_no = ticket_no
        self.name = name
        self.start = start
        self.destination = destination
        self.Class = Class
        self.fare = fare

    def printAirlineTicket(self):
        print("Date of travel: " + str(self.date))
        print("Destination: " + str(self.destination))
        print("Class: " + str(self.Class))
        print("Fare of the ticket: $" + str(self.fare))
        print("Ticket number: " + self.ticket_no)
        print("Name of traveller: " + str(self.name))
        print("Travelling from: " + str(self.start))

ticket = Flight_ticket("Boston, MA", "Dallas, TX", "08-21-2022", "Business", 450, "Raphael","ABC123")
ticket.printAirlineTicket()