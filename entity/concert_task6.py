from TicketBookingSystem.dao.IEvent_Task6 import IEvent
class Concert(IEvent):
    def __init__(self, event_name, event_date, event_time, total_seats, ticket_price, venue_name, artist, concert_type):
        super().__init__(event_name, event_date, event_time, total_seats, ticket_price, 'Concert', venue_name)
        self.artist = artist
        self.concert_type = concert_type

    def display_event_details(self):
        print(f"Concert: {self.event_name}, Artist: {self.artist}, Type: {self.concert_type}")
        print(f"Date: {self.event_date}, Time: {self.event_time}, Venue: {self.venue_name}")
        print(f"Available Seats: {self.available_seats}, Ticket Price: {self.ticket_price}")
