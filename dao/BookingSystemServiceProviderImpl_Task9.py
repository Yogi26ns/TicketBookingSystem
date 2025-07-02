from dao.BookingSystemServiceProviderImpl_Task8 import BookingSystemServiceProviderImpl_Task8
from exception.EventNotFoundException_Task9 import EventNotFoundException_Task9
from exception.InvalidBookingIDException_Task9 import InvalidBookingIDException_Task9

class BookingSystemServiceProviderImpl_Task9(BookingSystemServiceProviderImpl_Task8):

    def book_tickets(self, event_name, num_tickets, array_of_customers):
        try:
            event = next((e for e in self.events if e.event_name == event_name), None)
            if event is None:
                raise EventNotFoundException_Task9(f"Event '{event_name}' not found!")

            if event.available_seats >= num_tickets:
                total_cost = self.calculate_booking_cost(event, num_tickets)
                from TicketBookingSystem.entity.booking_task8 import Booking_Task8
                booking = Booking_Task8(array_of_customers, event, num_tickets, total_cost)
                self.bookings.append(booking)
                event.available_seats -= num_tickets
                print(f"Tickets booked successfully! Booking ID: {booking.booking_id}")
            else:
                print("Not enough seats available!")

        except EventNotFoundException_Task9 as e:
            print(e)

        except Exception as e:
            print(f"Unexpected error: {e}")

    def cancel_booking(self, booking_id):
        try:
            booking = next((b for b in self.bookings if b.booking_id == booking_id), None)
            if booking:
                booking.event.available_seats += booking.num_tickets
                self.bookings.remove(booking)
                print("Booking cancelled successfully!")
            else:
                raise InvalidBookingIDException_Task9(f"Booking ID '{booking_id}' not found!")

        except InvalidBookingIDException_Task9 as e:
            print(e)

        except Exception as e:
            print(f"Unexpected error: {e}")

    def get_booking_details(self, booking_id):
        try:
            booking = next((b for b in self.bookings if b.booking_id == booking_id), None)
            if booking:
                booking.display_booking_details()
            else:
                raise InvalidBookingIDException_Task9(f"Booking ID '{booking_id}' not found!")

        except InvalidBookingIDException_Task9 as e:
            print(e)

        except Exception as e:
            print(f"Unexpected error: {e}")