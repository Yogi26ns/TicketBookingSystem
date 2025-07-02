# TicketBookingSystem_Task7.py - Task 7

from TicketBookingSystem.entity.movie_task7 import Movie
from TicketBookingSystem.entity.concert_task7 import Concert
from TicketBookingSystem.entity.sports_task7 import Sports
from TicketBookingSystem.entity.venue_task7 import Venue
from TicketBookingSystem.entity.customer_task7 import Customer
from TicketBookingSystem.entity.booking_task7 import Booking

class TicketBookingSystem:
    def __init__(self):
        self.events = []
        self.bookings = []

    def create_event(self, event_obj):
        self.events.append(event_obj)
        print("Event created successfully.")

    def display_event_details(self):
        if not self.events:
            print("No events available.")
        else:
            for event in self.events:
                event.display_event_details()
                print("---")

    def book_tickets(self, event_name, num_tickets, customer_list):
        event = next((e for e in self.events if e.event_name == event_name), None)
        if event:
            cost = event.book_tickets(num_tickets)
            if cost != -1:
                booking = Booking(event, customer_list, num_tickets, cost)
                self.bookings.append(booking)
                print(f"Booking successful. Booking ID: {booking.booking_id}")
            else:
                print("Not enough tickets available.")
        else:
            print("Event not found.")

    def cancel_booking(self, booking_id):
        booking = next((b for b in self.bookings if b.booking_id == booking_id), None)
        if booking:
            booking.event.cancel_booking(booking.num_tickets)
            self.bookings.remove(booking)
            print("Booking cancelled successfully.")
        else:
            print("Booking ID not found.")
