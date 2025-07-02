from abc import ABC, abstractmethod

class IEvent(ABC):
    def __init__(self, event_name, event_date, event_time, total_seats, ticket_price, event_type, venue_name):
        self.event_name = event_name
        self.event_date = event_date
        self.event_time = event_time
        self.total_seats = total_seats
        self.available_seats = total_seats
        self.ticket_price = ticket_price
        self.event_type = event_type
        self.venue_name = venue_name

    @abstractmethod
    def display_event_details(self):
        pass

    def book_tickets(self, num_tickets):
        if num_tickets <= self.available_seats:
            self.available_seats -= num_tickets
            return num_tickets * self.ticket_price
        else:
            return -1

    def cancel_tickets(self, num_tickets):
        self.available_seats += num_tickets

    def get_available_tickets(self):
        return self.available_seats