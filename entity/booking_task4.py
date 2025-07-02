class Booking:
    def __init__(self, event, num_tickets):
        self.event = event
        self.num_tickets = num_tickets
        self.total_cost = 0
        self.calculate_booking_cost(num_tickets)

    def calculate_booking_cost(self, num_tickets):
        self.total_cost = self.event.ticket_price * num_tickets

    def book_tickets(self, num_tickets):
        self.event.book_tickets(num_tickets)
        self.calculate_booking_cost(num_tickets)

    def cancel_booking(self, num_tickets):
        self.event.cancel_booking(num_tickets)

    def getAvailableNoOfTickets(self):
        return self.event.available_seats

    def getEventDetails(self):
        return self.event.display_event_details()