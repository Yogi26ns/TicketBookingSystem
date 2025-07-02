from TicketBookingSystem.dao.IEvent_Task6 import IEvent

class Movie(IEvent):
    def __init__(self, event_name, event_date, event_time, total_seats, ticket_price, venue_name, genre, actor_name, actress_name):
        super().__init__(event_name, event_date, event_time, total_seats, ticket_price, 'Movie', venue_name)
        self.genre = genre
        self.actor_name = actor_name
        self.actress_name = actress_name

    def display_event_details(self):
        print(f"Movie: {self.event_name}, Genre: {self.genre}, Actor: {self.actor_name}, Actress: {self.actress_name}")
        print(f"Date: {self.event_date}, Time: {self.event_time}, Venue: {self.venue_name}")
        print(f"Available Seats: {self.available_seats}, Ticket Price: {self.ticket_price}")
