# Importing necessary classes from entity package
# from entity.movie import Movie
# from entity.concert import Concert
# from entity.sports import Sports
from TicketBookingSystem.entity.movie_task5 import Movie
from TicketBookingSystem.entity.concert_task5 import Concert
from TicketBookingSystem.entity.sports_task5 import Sports
# TicketBookingSystem class for managing events and bookings
class TicketBookingSystem:
    def __init__(self):
        self.events = []

    def create_event(self, event_name, event_date, event_time, total_seats, ticket_price, event_type, venue_name, genre='', actor_name='', actress_name='', artist='', concert_type='', sport_name='', teams_name=''):
        if event_type == 'Movie':
            event = Movie(event_name, event_date, event_time, venue_name, total_seats, total_seats, ticket_price, genre, actor_name, actress_name)
        elif event_type == 'Concert':
            event = Concert(event_name, event_date, event_time, venue_name, total_seats, total_seats, ticket_price, artist, concert_type)
        elif event_type == 'Sports':
            event = Sports(event_name, event_date, event_time, venue_name, total_seats, total_seats, ticket_price, sport_name, teams_name)
        else:
            print("Invalid Event Type")
            return None

        self.events.append(event)
        return event

    def display_event_details(self, event):
        event.display_event_details()

    def book_tickets(self, event, num_tickets):
        if event.available_seats >= num_tickets:
            event.book_tickets(num_tickets)
            total_cost = num_tickets * event.ticket_price
            print(f"Tickets booked successfully! Total cost: {total_cost}")
            return total_cost
        else:
            print("Not enough tickets available. Event is sold out.")
            return 0

    def cancel_tickets(self, event, num_tickets):
        event.cancel_booking(num_tickets)
        print("Tickets cancelled successfully.")