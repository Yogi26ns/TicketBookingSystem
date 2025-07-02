from abc import ABC, abstractmethod

class IBookingSystemRepository_Task11(ABC):

    @abstractmethod
    def create_event(self, event_name, date, time, total_seats, ticket_price, event_type, venue_id):
        pass

    @abstractmethod
    def get_event_details(self):
        pass

    @abstractmethod
    def get_available_no_of_tickets(self, event_id):
        pass

    @abstractmethod
    def calculate_booking_cost(self, num_tickets, event_id):
        pass

    @abstractmethod
    def book_tickets(self, event_name, num_tickets, list_of_customers):
        pass

    @abstractmethod
    def cancel_booking(self, booking_id):
        pass

    @abstractmethod
    def get_booking_details(self, booking_id):
        pass