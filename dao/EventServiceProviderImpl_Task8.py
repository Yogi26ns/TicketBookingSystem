from TicketBookingSystem.dao.IIEventServiceProvider_Task8 import IEventServiceProvider_Task8

class EventServiceProviderImpl_Task8(IEventServiceProvider_Task8):
    def __init__(self):
        self.events = []

    def create_event(self, event):
        self.events.append(event)
        print("Event created successfully!")

    def getEventDetails(self):
        return self.events

    def getAvailableNoOfTickets(self):
        return sum(event.available_seats for event in self.events)
