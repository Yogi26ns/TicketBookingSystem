class EventNotFoundException_Task9(Exception):
    def __init__(self, message="Event not found!"):
        super().__init__(message)