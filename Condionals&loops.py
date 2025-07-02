#Task 1 - Conditional statements
#1.Write a program that takes the availableTicket and noOfBookingTicket as input.
#2.Use conditional statements (if-else) to determine if the ticket is available or not.
#3.Display an appropriate message based on ticket availability.
import time
"""
availableTicket = int(input("Enter the number of tickets that are available:"))
time.sleep(0.3)
noOfBookingTicket= int(input("Enter Number of tickets you want:"))
time.sleep(0.5)
if availableTicket>=noOfBookingTicket:
    remaininTicket= availableTicket-noOfBookingTicket
    print(f"Your Booking is Successfully Done, And the Remaining ticket is : {remaininTicket}")
else :
    print("No available tickets")

#Task-2 Nested Conditional Statements
#Create a program that simulates a Ticket booking and calculating cost of tickets. Display tickets options 
#such as "Silver", "Gold", "Dimond". Based on ticket category fix the base ticket price and get the user input 
#for ticket type and no of tickets need and calculate the total cost of tickets booked.

print("===" * 20)
print("Welcome to Our Ticket Booking System")
print("F1: The Movie")
print("We have categories for tickets and each category has different prices. Kindly choose your preference")
print("1. Diamond (Premium Lounges - Balcony)")
print("2. Gold")
print("3. Silver")

categ = int(input("Enter Your Choice of seat to view the prices: "))

if categ == 1:
    print("Ticket Cost is Rs. 250 per seat")
    tckt = int(input("How many tickets? "))
    if tckt > 0:
        print(f"Your Ticket amount for {tckt} tickets is Rs. {tckt * 250}")
        print("Booking Successful! Enjoy the show!")
    else:
        print("Invalid number of tickets.")

elif categ == 2:
    print("Ticket Cost is Rs. 190 per seat")
    tckt = int(input("How many tickets? "))
    if tckt > 0:
        print(f"Your Ticket amount for {tckt} tickets is Rs. {tckt * 190}")
        print("Booking Successful! Enjoy the show!")
    else:
        print("Invalid number of tickets.")

elif categ == 3:
    print("Ticket Cost is Rs. 60 per seat")
    tckt = int(input("How many tickets? "))
    if tckt > 0:
        print(f"Your Ticket amount for {tckt} tickets is Rs. {tckt * 60}")
        print("Booking Successful! Enjoy the show!")
    else:
        print("Invalid number of tickets.")

else:
    print("Choose an appropriate option.")
#Task 3 Looping
# From the above task book the tickets for repeatedly until user type "Exit"
while True:
    print("===" * 20)
    print("Welcome to Our Ticket Booking System")
    print("F1: The Movie")
    print("We have categories for tickets and each category has different prices. Kindly choose your preference")
    print("1. Diamond (Premium Lounges - Balcony)")
    print("2. Gold")
    print("3. Silver")
    print("4.exit")

    categ = int(input("Enter Your Choice of seat to view the prices: "))
    if categ == 4:
        print("You are successfully exited from booking")
        break

    if categ == 1:
        print("Ticket Cost is Rs. 250 per seat")
        tckt = int(input("How many tickets? "))
        if tckt > 0:
            print(f"Your Ticket amount for {tckt} tickets is Rs. {tckt * 250}")
            print("Booking Successful! Enjoy the show!")
        else:
            print("Invalid number of tickets.")

    elif categ == 2:
        print("Ticket Cost is Rs. 190 per seat")
        tckt = int(input("How many tickets? "))
        if tckt > 0:
            print(f"Your Ticket amount for {tckt} tickets is Rs. {tckt * 190}")
            print("Booking Successful! Enjoy the show!")
        else:
            print("Invalid number of tickets.")

    elif categ == 3:
        print("Ticket Cost is Rs. 60 per seat")
        tckt = int(input("How many tickets? "))
        if tckt > 0:
            print(f"Your Ticket amount for {tckt} tickets is Rs. {tckt * 60}")
            print("Booking Successful! Enjoy the show!")
        else:
            print("Invalid number of tickets.")

    else:
        print("Choose an appropriate option.")
"""

from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    def greet(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return 3.14*self.radius*self.radius

circle=Circle(5)
circle.greet()
print("Area:",circle.area())

shape=Shape() #cant be instantiated

