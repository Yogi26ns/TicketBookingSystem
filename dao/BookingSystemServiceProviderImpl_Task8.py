# Task 8: Booking System Service Implementation

from dao.EventServiceProviderImpl_Task8 import EventServiceProviderImpl_Task8
from dao.IBookingSystemServiceProvider_Task8 import IBookingSystemServiceProvider_Task8
from TicketBookingSystem.entity.booking_task8 import Booking_Task8

class BookingSystemServiceProviderImpl_Task8(EventServiceProviderImpl_Task8, IBookingSystemServiceProvider_Task8):
    def __init__(self):
        super().__init__()
        self.bookings = []

    def calculate_booking_cost(self, event, num_tickets):
        return event.ticket_price * num_tickets

    def book_tickets(self, event_name, num_tickets, array_of_customers):
        event = next((e for e in self.events if e.event_name == event_name), None)
        if event is None:
            print("Event not found!")
            return

        if event.available_seats >= num_tickets:
            total_cost = self.calculate_booking_cost(event, num_tickets)
            booking = Booking_Task8(array_of_customers, event, num_tickets, total_cost)
            self.bookings.append(booking)
            event.available_seats -= num_tickets
            print(f"Tickets booked successfully! Booking ID: {booking.booking_id}")
        else:
            print("Not enough seats available!")

    def cancel_booking(self, booking_id):
        booking = next((b for b in self.bookings if b.booking_id == booking_id), None)
        if booking:
            booking.event.available_seats += booking.num_tickets
            self.bookings.remove(booking)
            print("Booking cancelled successfully!")
        else:
            print("Booking ID not found!")

    def get_booking_details(self, booking_id):
        booking = next((b for b in self.bookings if b.booking_id == booking_id), None)
        if booking:
            booking.display_booking_details()
        else:
            print("Booking ID not found!")
