class InvalidBookingIDException_Task9(Exception):
    def __init__(self, message="Invalid Booking ID!"):
        super().__init__(message)