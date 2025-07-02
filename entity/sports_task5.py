class Sports(Event):
    def __init__(self, event_name='', event_date='', event_time='', venue_name='', total_seats=0, available_seats=0, ticket_price=0.0, event_type='Sports', sport_name='', teams_name=''):
        super().__init__(event_name, event_date, event_time, venue_name, total_seats, available_seats, ticket_price, event_type)
        self.sport_name = sport_name
        self.teams_name = teams_name

    def display_event_details(self):
        super().display_event_details()
        print(f"Sport: {self.sport_name}, Teams: {self.teams_name}")