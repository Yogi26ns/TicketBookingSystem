-- ========================================
-- TASK 1: Database Design
-- ========================================

-- Question 1: Create database
create database TicketBookingSystem;

-- Question 2: Use the created database
use TicketBookingSystem;

-- Question 3: Create tables with PKs, FKs, and proper datatypes

-- Table 1: Venue
create table venue (
  venue_id int auto_increment primary key,
  venue_name varchar(100),
  address varchar(100)
);

-- Table 2: Booking
create table booking (
  booking_id int auto_increment primary key,
  customer_id int,
  event_id int,
  num_tickets int,
  total_cost decimal(10,2),
  booking_date date
);

-- Table 3: Event
create table event (
  event_id int auto_increment primary key,
  event_name varchar(100),
  event_date date,
  event_time time,
  venue_id int,
  total_seats int,
  available_seats int,
  ticket_price decimal(6,2),
  event_type enum('Movie', 'Sports', 'Concert'),
  booking_id int,
  foreign key (venue_id) references venue(venue_id),
  foreign key (booking_id) references booking(booking_id)
);

-- Table 4: Customer
create table customer (
  customer_id int auto_increment primary key,
  customer_name varchar(100),
  email varchar(100),
  phone_number varchar(15),
  booking_id int,
  foreign key (booking_id) references booking(booking_id)
);

-- ========================================
-- Task 2 Question 1
-- Insert Values into All Tables (At least 10 each)

-- Venue Table Inserts
insert into venue (venue_name, address) values 
('M A Chidambaram Stadium', 'Chepauk'),
('Kamarajar Arangam', 'Kodambakkam'),
('DY Patil Stadium', 'Mumbai'),
('YMCA Ground', 'Nandanam'),
('Luxe Cinemas', 'Velachery'),
('Music Academy', 'Alwarpet'),
('Narada Gana Sabha', 'Mylapore'),
('Sathyam', 'Royapettah'),
('Wankhede Stadium', 'Mumbai'),
('Eden Gardens', 'Kolkata');

-- Booking Table Inserts
insert into booking (customer_id, event_id, num_tickets, total_cost, booking_date) values
(1, 1, 2, 1999.98, '2025-06-10'),
(2, 2, 3, 3600.00, '2025-06-11'),
(3, 3, 4, 1200.00, '2025-06-12'),
(4, 4, 1, 450.00, '2025-06-12'),
(5, 5, 5, 700.00, '2025-06-12'),
(6, 6, 1, 500.00, '2025-06-13'),
(7, 7, 3, 2400.00, '2025-06-14'),
(8, 8, 2, 700.00, '2025-06-15'),
(9, 9, 1, 1500.00, '2025-06-16'),
(10, 10, 2, 2000.00, '2025-06-17');

-- Event Table Inserts
insert into event (event_name, event_date, event_time, venue_id, total_seats, available_seats, ticket_price, event_type, booking_id) values
('IPL Match CSK vs MI', '2025-07-01', '19:00:00', 1, 50000, 43000, 999.99, 'Sports', 1),
('Music Night with AR Rahman', '2025-07-02', '18:00:00', 6, 2000, 1400, 1200.00, 'Concert', 2),
('Vijay’s Leo - Special Screening', '2025-07-03', '16:30:00', 5, 350, 100, 300.00, 'Movie', 3),
('Stand-up Comedy by Zakir Khan', '2025-07-04', '20:00:00', 7, 1000, 600, 450.00, 'Concert', 4),
('Dance Festival', '2025-07-05', '17:00:00', 8, 800, 600, 350.00, 'Concert', 5),
('Science Expo 2025', '2025-07-06', '10:00:00', 3, 1000, 950, 500.00, 'Concert', 6),
('Vijay Awards', '2025-07-07', '18:30:00', 4, 1500, 1100, 800.00, 'Concert', 7),
('Kantara Special Screening', '2025-07-08', '15:00:00', 5, 400, 120, 350.00, 'Movie', 8),
('India vs Australia Test', '2025-07-09', '10:30:00', 9, 60000, 50000, 1500.00, 'Sports', 9),
('Ilayaraja Live', '2025-07-10', '19:30:00', 6, 2500, 1700, 1000.00, 'Concert', 10);

-- Customer Table Inserts
insert into customer (customer_name, email, phone_number, booking_id) values
('Yogeshwar', 'yogesh@gmail.com', '9876543210', 1),
('Ashwin', 'ashwin@gmail.com', '9123456780', 2),
('Sofia', 'sofia@gmail.com', '9988776655', 3),
('Arjun', 'arjunr@gmail.com', '9001122233', 4),
('Geeta', 'geeta88@gmail.com', '7894561230', 5),
('Nandhini', 'nandhini@gmail.com', '9876012345', 6),
('Rahul', 'rahul.d@gmail.com', '9844012345', 7),
('Priya', 'priyapriya@gmail.com', '9797012345', 8),
('Varun', 'varunv@gmail.com', '9823012345', 9),
('Deepika', 'deepika@gmail.com', '9833012345', 10);
-- ========================================

-- ========================================
-- Task 2 Question 2
-- List all events
select * from event;
-- ========================================

-- ========================================
-- Task 2 - Question 3
-- SQL query to select events with available tickets
select * from event 
where available_seats>0;
-- ========================================

-- ========================================
-- Task 2 - Question 4
-- SQL query to select events name partial match with ‘cup’
select event_name from event 
where event_name like "%awards%";
-- ========================================

-- ========================================
-- Task 2 - Question 5
-- SQL query to select events with ticket price range is between 1000 to 2500
select * from event 
where ticket_price between 1000 and 2500;
-- ========================================

-- ========================================
-- Task 2 - Question 6
-- SQL query to retrieve events with dates falling within a specific range
select * from event 
where event_date between '2025-07-05' and '2025-07-15';
-- ========================================

-- ========================================
-- Task 2 - Question 7
-- SQL query to retrieve events with available tickets that also have "Concert" in their name
select * from event 
where available_seats > 0 and event_type like '%Concert%';
-- ========================================

-- ========================================
-- Task 2 - Question 8
-- SQL query to retrieve users in batches of 5, starting from the 6th user
select * from customer 
limit 5 offset 5;
-- ========================================

-- ========================================
-- Task 2 - Question 9
-- SQL query to retrieve bookings details contains booked no of ticket more than 4.
select * from booking 
where num_tickets>4;
-- ========================================

-- ========================================
-- Task 2 - Question 10
-- SQL query to retrieve customer information whose phone number end with ‘000’
select * from customer 
where phone_number like '%000%';
-- ========================================

-- ========================================
-- Task 2 - Question 11
-- SQL query to retrieve the events in order whose seat capacity more than 15000
select * from event 
where total_seats > 1500 
order by total_seats;
-- ========================================

-- ========================================
-- Task 2 - Question 12
-- SQL query to select events name not start with ‘x’, ‘y’, ‘z’
select event_name from event 
where event_name not like 'x%'
and event_name not like 'y%'
and event_name not like 'z%';
-- ========================================

-- ========================================
-- Task 3 - Question 1
-- SQL query to List Events and Their Average Ticket Prices
select event_name, avg(ticket_price) as 'average' 
from event 
group by event_name;
-- ========================================

-- ========================================
-- Task 3 - Question 2
-- SQL query to Calculate the Total Revenue Generated by Events
select event_name,sum(total_cost) as revenue
from event 
join booking using(event_id)
group by 1
order by revenue desc ;
-- ========================================

-- ========================================
-- Task 3 - Question 3
-- SQL query to find the event with the highest ticket sales
select event_name,sum(total_cost) as revenue
from event 
join booking using(event_id)
group by 1
order by revenue desc 
limit 1;
-- ========================================

-- ========================================
-- Task 3 - Question 4
-- SQL query to Calculate the Total Number of Tickets Sold for Each Event
select event_name,sum(num_tickets) as total_tickets_sold
from event
join booking using (event_id)
group by event_name
order by 2 desc;
-- ========================================

-- ========================================
-- Task 3 - Question 5
-- SQL query to Find Events with No Ticket Sales
select event_name,num_tickets from event
left join booking using(event_id)
where num_tickets is null;
-- ========================================

-- ========================================
-- Task 3 - Question 6
-- SQL query to Find the User Who Has Booked the Most Tickets
select customer_name,sum(num_tickets) 
from customer 
join booking using (customer_id)
group by customer_name
order by 2 desc
limit 1;
-- ========================================

-- ========================================
-- Task 3 - Question 7
-- SQL query to List Events and the total number of tickets sold for each month
/*create view list_of_events as
select event_name,num_tickets from event
join booking using(event_id)*/
select event_name,month(booking_date) as month ,sum(num_tickets) as total_sold
from booking
join event using(event_id)
group by month(booking_date),event_name
order by 3 desc;
-- ========================================

-- ========================================
-- Task 3 - Question 8
--  SQL query to calculate the average Ticket Price for Events in Each Venue
select event_name,avg(ticket_price),venue_name 
from event join venue using(venue_id)
group by event_name,venue_name;
-- ========================================

-- ========================================
-- Task 3 - Question 9
-- SQL query to calculate the total Number of Tickets Sold for Each Event Type
select event_type,sum(num_tickets) as tickets_sold
from event join booking using(event_id)
group by event_type
order by 2 desc;
-- ========================================

-- ========================================
-- Task 3 - Question 10
-- SQL query to calculate the total Revenue Generated by Events in Each Year
select event_name,sum(total_cost) as Total_revenue,year(booking_date) as Year
from event join booking using(event_id)
group by event_name,year(booking_date);
-- ========================================

-- ========================================
-- Task 3 - Question 11
-- SQL query to list users who have booked tickets for multiple events
select customer_name,sum(num_tickets) as total_tickets,count(distinct event_id)
from customer join booking using(customer_id)
group by customer_name;
-- ========================================

-- ========================================
-- Task 3 - Question 12
-- SQL query to calculate the Total Revenue Generated by Events for Each User
select customer_name,event_name,sum(total_cost) as total_revenue
from customer join booking using(customer_id) join event using(event_id)
group by customer_name,event_name;
-- ========================================

-- ========================================
-- Task 3 - Question 13
-- SQL query to calculate the Average Ticket Price for Events in Each Category and Venue
select venue_name,event_type,avg(ticket_price) as average_ticket_price
from event join venue using(venue_id)
group by event_type,venue_name;
-- ========================================

-- ========================================
-- Task 3 - Question 14
-- SQL query to list Users and the Total Number of Tickets They've Purchased in the Last 30 Days
select customer_name,sum(num_tickets) as total_tickets_boughtin30days
from customer join booking using(customer_id)
where booking_date >= curdate() - interval 30 day 
group by customer_name
order by 2 desc;
-- ========================================

-- ========================================
-- Task 4 - Question 1
-- Calculate the Average Ticket Price for Events in Each Venue Using a Subquery. 
select venue_name,(select avg(ticket_price) from event where event.venue_id = venue.venue_id)
as avg_ticket_price 
from venue
group by venue_name,venue_id;
-- ========================================

-- ========================================
-- Task 4 - Question 2
-- Find Events with More Than 50% of Tickets Sold using subquery. 
select event_name,(total_seats - available_seats) as sold_tickets
from event where event_id in (select event_id from event
    where (total_seats - available_seats) > (total_seats / 2));
-- ========================================

-- ========================================
-- Task 4 - Question 3
-- Calculate the Total Number of Tickets Sold for Each Event. 
select event_name, 
(select sum(num_tickets) from booking where booking.event_id = event.event_id) 
as total_no_tickets_sold 
from event 
group by event_id;
-- ========================================

-- ========================================
-- Task 4 - Question 4
-- Find Users Who Have Not Booked Any Tickets Using a NOT EXISTS Subquery.
select customer_name from customer 
where not exists 
( select customer_id from booking where booking.customer_id = customer.customer_id); 
-- ========================================

-- ========================================
-- Task 4 - Question 5
-- List Events with No Ticket Sales Using a NOT IN Subquery. 
select event_name from event where event_id not in (select event_id from booking group by event_id);
-- ========================================

-- ========================================
-- Task 4 - Question 6
-- Calculate the Total Number of Tickets Sold for Each Event Type Using a Subquery in the FROM Clause. 
select event_type,sum(tickets_sold) as num_tickets_sold 
from ( select event_type,(total_seats-available_seats) as tickets_sold from event) 
as d 
group by event_type;
-- ========================================

-- ========================================
-- Task 4 - Question 7
-- Find Events with Ticket Prices Higher Than the Average Ticket Price Using a Subquery in the WHERE Clause. 
select event_name,ticket_price 
from event 
where ticket_price > (select avg(ticket_price) from event);
-- ========================================

-- ========================================
-- Task 4 - Question 8
-- Calculate the Total Revenue Generated by Events for Each User Using a Correlated Subquery. 
select customer_name, 
(select sum(total_cost) from booking where booking.customer_id = customer.customer_id) as total_revenue
from customer; 
-- ========================================

-- ========================================
-- Task 4 - Question 9
-- List Users Who Have Booked Tickets for Events in a Given Venue Using a Subquery in the WHERE Clause. 
select customer_name from customer 
where customer_id in ( select customer_id from booking 
						join event using(event_id) 
                        where venue_id = 5); 
-- ========================================

-- ========================================
-- Task 4 - Question 10
-- Calculate the Total Number of Tickets Sold for Each Event Category Using a Subquery with GROUP BY. 
select event_type,total_tickets_sold 
from (select event_type,sum(total_seats-available_seats) as total_tickets_sold 
	  from event group by event_type) as temp;
-- ========================================

-- ========================================
-- Task 4 - Question 11
-- Find Users Who Have Booked Tickets for Events in each Month Using a Subquery with DATE_FORMAT.
select customer_name,booking_month 
from ( select customer_id,date_format(booking_date,'%m') as booking_month from booking) as temp
join customer using(customer_id);
-- ========================================

-- ========================================
-- Task 4 - Question 12
-- Calculate the Average Ticket Price for Events in Each Venue Using a Subquery
select venue_name,avg_tckt_price 
from ( select avg(ticket_price) as avg_tckt_price,venue_id 
	from event group by venue_id) as t 
join venue using(venue_id);
-- ========================================