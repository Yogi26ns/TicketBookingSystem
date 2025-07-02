import datetime
class Booking:
    booking_counter = 1

    def __init__(self, event, customers, num_tickets, total_cost):
        self.booking_id = Booking.booking_counter
        Booking.booking_counter += 1
        self.event = event
        self.customers = customers
        self.num_tickets = num_tickets
        self.total_cost = total_cost
        self.booking_date = datetime.datetime.now()

    def display_booking_details(self):
        print(f"Booking ID: {self.booking_id}")
        print(f"Booking Date: {self.booking_date}")
        print(f"Event: {self.event.event_name}")
        print(f"Number of Tickets: {self.num_tickets}")
        print(f"Total Cost: {self.total_cost}")
        print("Customer Details:")
        for customer in self.customers:
            customer.display_customer_details()
            print("---")
