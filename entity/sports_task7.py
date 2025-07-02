class Sports:
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
        print(f"Event: {self.event_name} | Date: {self.event_date} | Time: {self.event_time}")
        print(f"Venue: {self.venue.venue_name} | Available Seats: {self.available_seats}")
        print(f"Type: {self.event_type} | Sport: {self.sport_name} | Teams: {self.teams_name}")

    def book_tickets(self, num_tickets):
        if num_tickets <= self.available_seats:
            self.available_seats -= num_tickets
            return num_tickets * self.ticket_price
        else:
            return -1

    def cancel_booking(self, num_tickets):
        self.available_seats += num_tickets
