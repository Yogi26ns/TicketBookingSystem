class Concert_Task8:
    def __init__(self, event_name, event_date, event_time, venue, total_seats, ticket_price, artist, concert_type):
        self.event_name = event_name
        self.event_date = event_date
        self.event_time = event_time
        self.venue = venue
        self.total_seats = total_seats
        self.available_seats = total_seats
        self.ticket_price = ticket_price
        self.event_type = "Concert"
        self.artist = artist
        self.concert_type = concert_type

    def display_event_details(self):
        print(f"Concert: {self.event_name}, Date: {self.event_date}, Time: {self.event_time}, Venue: {self.venue.venue_name}")
        print(f"Artist: {self.artist}, Type: {self.concert_type}")
        print(f"Available Seats: {self.available_seats}, Ticket Price: {self.ticket_price}")
