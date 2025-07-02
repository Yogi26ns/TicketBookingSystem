class Concert:
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
        print(f"Event: {self.event_name} | Date: {self.event_date} | Time: {self.event_time}")
        print(f"Venue: {self.venue.venue_name} | Available Seats: {self.available_seats}")
        print(f"Type: {self.event_type} | Artist: {self.artist} | Concert Type: {self.concert_type}")

    def book_tickets(self, num_tickets):
        if num_tickets <= self.available_seats:
            self.available_seats -= num_tickets
            return num_tickets * self.ticket_price
        else:
            return -1

    def cancel_booking(self, num_tickets):
        self.available_seats += num_tickets
