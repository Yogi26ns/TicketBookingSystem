from abc import ABC, abstractmethod

class IBookingSystem(ABC):

    @abstractmethod
    def create_event(self):
        pass

    @abstractmethod
    def display_event_details(self, event):
        pass

    @abstractmethod
    def book_tickets(self, event, num_tickets):
        pass

    @abstractmethod
    def cancel_tickets(self, event, num_tickets):
        pass