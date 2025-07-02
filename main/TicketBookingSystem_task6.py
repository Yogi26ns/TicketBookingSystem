from TicketBookingSystem.dao.IBookingSystem_Task6 import IBookingSystem
from TicketBookingSystem.entity.movie_task6 import Movie
from TicketBookingSystem.entity.concert_task6 import Concert
from TicketBookingSystem.entity.sports_task6 import Sports

class TicketBookingSystem(IBookingSystem):
    def __init__(self):
        self.events = []

    def create_event(self, event_name, event_date, event_time, total_seats, ticket_price, event_type, venue_name, **kwargs):
        if event_type == 'Movie':
            event = Movie(event_name, event_date, event_time, total_seats, ticket_price, venue_name, kwargs['genre'], kwargs['actor_name'], kwargs['actress_name'])
        elif event_type == 'Concert':
            event = Concert(event_name, event_date, event_time, total_seats, ticket_price, venue_name, kwargs['artist'], kwargs['concert_type'])
        elif event_type == 'Sports':
            event = Sports(event_name, event_date, event_time, total_seats, ticket_price, venue_name, kwargs['sport_name'], kwargs['teams_name'])
        else:
            print("Invalid event type")
            return None
        self.events.append(event)
        return event

    def display_event_details(self, event):
        event.display_event_details()

    def book_tickets(self, event, num_tickets):
        cost = event.book_tickets(num_tickets)
        if cost == -1:
            print("Insufficient tickets available.")
        else:
            print(f"Successfully booked {num_tickets} tickets. Total cost: {cost}")

    def cancel_tickets(self, event, num_tickets):
        event.cancel_tickets(num_tickets)
        print(f"Cancelled {num_tickets} tickets successfully.")
