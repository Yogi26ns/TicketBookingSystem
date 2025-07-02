from TicketBookingSystem.dao.IBookingSystemRepository_Task11 import IBookingSystemRepository_Task11
from TicketBookingSystem.util.DBUtil_task11 import DBUtil_Task11

class BookingSystemRepositoryImpl_Task11(IBookingSystemRepository_Task11):

    def __init__(self):
        self.conn = DBUtil_Task11.get_connection()
        self.cursor = self.conn.cursor(dictionary=True)

    def create_event(self, event_name, date, time, total_seats, ticket_price, event_type, venue_id):
        sql = """
            INSERT INTO event (event_name, event_date, event_time, venue_id, total_seats, available_seats, ticket_price, event_type)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (event_name, date, time, venue_id, total_seats, total_seats, ticket_price, event_type)
        self.cursor.execute(sql, values)
        self.conn.commit()
        print("Event created successfully.")

    def get_event_details(self):
        self.cursor.execute("SELECT * FROM event")
        return self.cursor.fetchall()

    def get_available_no_of_tickets(self, event_id):
        self.cursor.execute("SELECT available_seats FROM event WHERE event_id = %s", (event_id,))
        result = self.cursor.fetchone()
        return result['available_seats'] if result else 0

    def calculate_booking_cost(self, num_tickets, event_id):
        self.cursor.execute("SELECT ticket_price FROM event WHERE event_id = %s", (event_id,))
        price = self.cursor.fetchone()['ticket_price']
        return price * num_tickets

    def book_tickets(self, event_name, num_tickets, list_of_customers):
        self.cursor.execute("SELECT * FROM event WHERE event_name = %s", (event_name,))
        event = self.cursor.fetchone()
        if event:
            available_seats = event['available_seats']
            if available_seats >= num_tickets:
                total_cost = event['ticket_price'] * num_tickets

                for customer in list_of_customers:
                    # Insert customer into DB first
                    self.cursor.execute(
                        "INSERT INTO customer (customer_name, email, phone_number) VALUES (%s, %s, %s)",
                        (customer.customer_name, customer.email, customer.phone)
                    )
                    customer_id = self.cursor.lastrowid  # Get auto-generated customer_id

                    # Insert booking with num_tickets for this customer
                    self.cursor.execute(
                        "INSERT INTO booking (customer_id, event_id, num_tickets, total_cost, booking_date) VALUES (%s, %s, %s, %s, CURDATE())",
                        (customer_id, event['event_id'], num_tickets, total_cost)
                    )

                # Update available seats
                self.cursor.execute(
                    "UPDATE event SET available_seats = available_seats - %s WHERE event_id = %s",
                    (num_tickets, event['event_id'])
                )
                self.conn.commit()
                print("Tickets booked successfully.")
                return total_cost
            else:
                print("Not enough tickets available.")
                return None
        else:
            print("Event not found.")
            return None

    def cancel_booking(self, booking_id):
        self.cursor.execute("SELECT event_id, num_tickets FROM booking WHERE booking_id = %s", (booking_id,))
        booking = self.cursor.fetchone()
        if booking:
            self.cursor.execute("DELETE FROM booking WHERE booking_id = %s", (booking_id,))
            self.cursor.execute("UPDATE event SET available_seats = available_seats + %s WHERE event_id = %s",
                                (booking['num_tickets'], booking['event_id']))
            self.conn.commit()
            print("Booking cancelled successfully.")
        else:
            print("Booking ID not found.")

    def get_booking_details(self, booking_id):
        self.cursor.execute("SELECT * FROM booking WHERE booking_id = %s", (booking_id,))
        return self.cursor.fetchone()

    def close_connection(self):
        self.cursor.close()
        self.conn.close()
