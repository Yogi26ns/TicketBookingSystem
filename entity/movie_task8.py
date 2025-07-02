class Movie_Task8:
    def __init__(self, event_name, event_date, event_time, venue, total_seats, ticket_price, genre, actor_name, actress_name):
        self.event_name = event_name
        self.event_date = event_date
        self.event_time = event_time
        self.venue = venue
        self.total_seats = total_seats
        self.available_seats = total_seats
        self.ticket_price = ticket_price
        self.event_type = "Movie"
        self.genre = genre
        self.actor_name = actor_name
        self.actress_name = actress_name

    def display_event_details(self):
        print(f"Movie: {self.event_name}, Date: {self.event_date}, Time: {self.event_time}, Venue: {self.venue.venue_name}")
        print(f"Genre: {self.genre}, Actor: {self.actor_name}, Actress: {self.actress_name}")
        print(f"Available Seats: {self.available_seats}, Ticket Price: {self.ticket_price}")
