import mysql.connector

class DBUtil_Task11:
    @staticmethod
    def get_connection():
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="yogeshwar@#2003",
            database="TicketBookingSystem"
        )
