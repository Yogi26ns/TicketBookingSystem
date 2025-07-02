from TicketBookingSystem.dao.BookingSystemRepositoryImpl_Task11 import BookingSystemRepositoryImpl_Task11
from TicketBookingSystem.entity.venue_task4 import Venue
from TicketBookingSystem.entity.customer_task4 import Customer

def ticket_booking_system():
    repository = BookingSystemRepositoryImpl_Task11()

    while True:
        print("\n===== Ticket Booking System =====")
        print("1. Create Event")
        print("2. View Events")
        print("3. Book Tickets")
        print("4. Cancel Booking")
        print("5. View Booking Details")
        print("6. Get Available Seats")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            event_name = input("Enter Event Name: ")
            date = input("Enter Event Date (YYYY-MM-DD): ")
            time = input("Enter Event Time (HH:MM:SS): ")
            total_seats = int(input("Enter Total Seats: "))
            ticket_price = float(input("Enter Ticket Price: "))
            event_type = input("Enter Event Type (Movie, Sports, Concert): ")
            venue_name = input("Enter Venue Name: ")
            venue_address = input("Enter Venue Address: ")

            venue = Venue(venue_name, venue_address)
            repository.create_event(event_name, date, time, total_seats, ticket_price, event_type, venue)
            print("Event created successfully.")

        elif choice == '2':
            events = repository.get_event_details()
            for event in events:
                print(event)

        elif choice == '3':
            event_name = input("Enter Event Name to Book: ")
            num_tickets = int(input("Enter Number of Tickets: "))
            customer_list = []

            for _ in range(num_tickets):
                name = input("Enter Customer Name: ")
                email = input("Enter Customer Email: ")
                phone = input("Enter Customer Phone: ")
                customer = Customer(name, email, phone)
                customer_list.append(customer)

            total_cost = repository.book_tickets(event_name, num_tickets, customer_list)
            if total_cost:
                print(f"Booking successful. Total Cost: {total_cost}")

        elif choice == '4':
            booking_id = int(input("Enter Booking ID to Cancel: "))
            repository.cancel_booking(booking_id)

        elif choice == '5':
            booking_id = int(input("Enter Booking ID: "))
            booking = repository.get_booking_details(booking_id)
            if booking:
                print(booking)
            else:
                print("Invalid Booking ID.")

        elif choice == '6':
            event_id = int(input("Enter Event ID to check available seats: "))
            total_seats = repository.get_available_no_of_tickets(event_id)
            print(f"Total Available Seats: {total_seats}")

        elif choice == '7':
            print("Exiting the system.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    ticket_booking_system()