class Sports_Task8:
    def __init__(self, event_name, event_date, event_time, venue, total_seats, ticket_price, sport_name, teams_name):
        self.event_name = event_name
        self.event_date = event_date
        self.event_time = event_time
        self.venue = venue
        self.total_seats = total_seats
        self.available_seats = total_seats
        self.ticket_price = ticket_price
        self.event_type = "Sports"
        self.sport_name = sport_name
        self.teams_name = teams_name

    def display_event_details(self):
        print(f"Sports Event: {self.event_name}, Date: {self.event_date}, Time: {self.event_time}, Venue: {self.venue.venue_name}")
        print(f"Sport: {self.sport_name}, Teams: {self.teams_name}")
        print(f"Available Seats: {self.available_seats}, Ticket Price: {self.ticket_price}")
