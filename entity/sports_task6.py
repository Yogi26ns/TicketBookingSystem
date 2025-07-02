from TicketBookingSystem.dao.IEvent_Task6 import IEvent
class Sports(IEvent):
    def __init__(self, event_name, event_date, event_time, total_seats, ticket_price, venue_name, sport_name, teams_name):
        super().__init__(event_name, event_date, event_time, total_seats, ticket_price, 'Sports', venue_name)
        self.sport_name = sport_name
        self.teams_name = teams_name

    def display_event_details(self):
        print(f"Sports Event: {self.event_name}, Sport: {self.sport_name}, Teams: {self.teams_name}")
        print(f"Date: {self.event_date}, Time: {self.event_time}, Venue: {self.venue_name}")
        print(f"Available Seats: {self.available_seats}, Ticket Price: {self.ticket_price}")
