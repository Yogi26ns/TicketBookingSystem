import datetime
class Booking_Task8:
    booking_counter = 1
    def __init__(self, customers, event, num_tickets, total_cost):
        self.booking_id = Booking_Task8.booking_counter
        Booking_Task8.booking_counter += 1
        self.customers = customers
        self.event = event
        self.num_tickets = num_tickets
        self.total_cost = total_cost
        self.booking_date = datetime.datetime.now()

    def display_booking_details(self):
        print(f"Booking ID: {self.booking_id}")
        for customer in self.customers:
            customer.display_customer_details()
        print(f"Event: {self.event.event_name}")
        print(f"Number of Tickets: {self.num_tickets}")
        print(f"Total Cost: {self.total_cost}")
        print(f"Booking Date: {self.booking_date}")
