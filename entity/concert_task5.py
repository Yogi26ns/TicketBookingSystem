class Concert(Event):
    def __init__(self, event_name='', event_date='', event_time='', venue_name='', total_seats=0, available_seats=0, ticket_price=0.0, event_type='Concert', artist='', concert_type=''):
        super().__init__(event_name, event_date, event_time, venue_name, total_seats, available_seats, ticket_price, event_type)
        self.artist = artist
        self.concert_type = concert_type

    def display_event_details(self):
        super().display_event_details()
        print(f"Artist: {self.artist}, Concert Type: {self.concert_type}")