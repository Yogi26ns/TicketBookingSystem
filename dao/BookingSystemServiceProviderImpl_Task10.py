from dao.BookingSystemServiceProviderImpl_Task9 import BookingSystemServiceProviderImpl_Task9
from exception.EventNotFoundException_Task9 import EventNotFoundException
from exception.InvalidBookingIDException_Task9 import InvalidBookingIDException
from TicketBookingSystem.entity.booking_task7 import Booking


class BookingSystemServiceProviderImpl_Task10(BookingSystemServiceProviderImpl_Task9):
    def __init__(self):
        super().__init__()
        self.events = []  # Using list first, will convert to set and map later
        self.bookings = []

    def create_event(self, event):
        self.events.append(event)

    def getEventDetails(self):
        return self.events

    def getAvailableNoOfTickets(self, event_name):
        for event in self.events:
            if event.event_name == event_name:
                return event.available_seats
        raise EventNotFoundException("Event not found.")

    def book_tickets(self, event_name, num_tickets, arrayOfCustomer):
        event_found = False
        for event in self.events:
            if event.event_name == event_name:
                event_found = True
                if event.available_seats >= num_tickets:
                    event.book_tickets(num_tickets)
                    booking = Booking(event, num_tickets, arrayOfCustomer)
                    self.bookings.append(booking)
                    return booking.total_cost
                else:
                    raise Exception("Not enough tickets available.")
        if not event_found:
            raise EventNotFoundException("Event not found.")

    def cancel_booking(self, booking_id):
        for booking in self.bookings:
            if booking.bookingId == booking_id:
                booking.event.cancel_booking(booking.num_tickets)
                self.bookings.remove(booking)
                return
        raise InvalidBookingIDException("Booking ID not found.")

    def get_booking_details(self, booking_id):
        for booking in self.bookings:
            if booking.bookingId == booking_id:
                return booking
        raise InvalidBookingIDException("Booking ID not found.")

    def sort_events(self):
        # Sorting by event name and venue name using a lambda function
        return sorted(self.events, key=lambda e: (e.event_name.lower(), e.venue.venue_name.lower()))

    def switch_to_set_structure(self):
        # Remove duplicates by switching to set
        self.events = set(self.events)
        self.bookings = set(self.bookings)

    def switch_to_map_structure(self):
        # Convert list to map using event name as key
        self.event_map = {event.event_name: event for event in self.events}
        self.booking_map = {booking.bookingId: booking for booking in self.bookings}

    def get_event_by_map(self, event_name):
        if event_name in self.event_map:
            return self.event_map[event_name]
        else:
            raise EventNotFoundException("Event not found in map.")

    def get_booking_by_map(self, booking_id):
        if booking_id in self.booking_map:
            return self.booking_map[booking_id]
        else:
            raise InvalidBookingIDException("Booking ID not found in map.")
