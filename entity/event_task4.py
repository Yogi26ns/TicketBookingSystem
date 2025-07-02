class Event:
    def __init__(self,event_name,event_date,event_time,venue_name,total_seats,available_seats,ticket_price,event_type):
        self.event_name = event_name
        self.event_date = event_date
        self.event_time = event_time
        self.venue_name = venue_name
        self.total_seats = total_seats
        self.available_seats = available_seats
        self.ticket_price = ticket_price
        self.event_type = event_type

    def getEventName(self):
        return self.event_name

    def getEventDate(self):
        return self.event_date

    def getEventTime(self):
        return self.event_time

    def getVenueName(self):
        return self.venue_name

    def getTotalSeats(self):
        return self.total_seats

    def getAvailableSeats(self):
        return self.available_seats

    def getTicketPrice(self):
        return self.ticket_price

    def getEventType(self):
        return self.event_type

    def setEventName(self,event_name):
        self.event_name = event_name

    def setEventDate(self,event_date):
        self.event_date = event_date

    def setEventTime(self,event_time):
        self.event_time = event_time

    def setVenueName(self,venue_name):
        self.venue_name = venue_name

    def setTotalSeats(self,total_seats):
        self.total_seats = total_seats

    def setAvailableSeats(self,available_seats):
        self.available_seats = available_seats

    def setTicketPrice(self,ticket_price):
        self.ticket_price = ticket_price

    def setEventType(self,event_type):
        self.event_type = event_type

    def calculate_total_revenue(self):
        booked_tickets = self.total_seats - self.available_seats
        return booked_tickets * self.ticket_price

    def getBookedNoOfTickets(self):
        return self.total_seats - self.available_seats

    def book_tickets(self, num_tickets):
        if num_tickets <= self.available_seats:
            self.available_seats -= num_tickets
            print(f"Successfully booked {num_tickets} tickets.")
        else:
            print("Not enough seats available.")

    def cancel_booking(self, num_tickets):
        if num_tickets <= (self.total_seats - self.available_seats):
            self.available_seats += num_tickets
            print(f"Successfully cancelled {num_tickets} tickets.")
        else:
            print("Invalid cancellation request.")

    def display_event_details(self):
        print(
            f"Event Name: {self.event_name}\nDate: {self.event_date}\nTime: {self.event_time}\nVenue: {self.venue_name}\nTotal Seats: {self.total_seats}\nAvailable Seats: {self.available_seats}\nTicket Price: {self.ticket_price}\nEvent Type: {self.event_type}")

