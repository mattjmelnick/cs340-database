-- Amity Hill, Matthew Melnick
-- Eastern Beavers (Group 15)
-- Updated Data Manipulation Queries for Step 6
-- Variables that are used to pass data from the backend are denoted with '~' in front of them

-- SELECT Queries to Populate Tables on Initial GET Requests
-- get customer attributes from the Customers table
select *
from Customers;

-- get sneaker attributes from the Sneakers table
select *
from Sneakers;

-- get drawings attributes from the Drawings table
-- get raffle description from Raffles table
SELECT *, raffle_description FROM Drawings
INNER JOIN Raffles
ON Drawings.raffle_id = Raffles.raffle_id;

-- get the raffle id and raffle description from Raffles table
-- used for adding and updating a Raffle in Drawings table
SELECT raffle_id, raffle_description FROM Raffles

-- get raffle attributes from the Raffles table
-- get brand and model name from Sneakers table
SELECT *, brand, model_name FROM Raffles
INNER JOIN Sneakers
ON Raffles.sneaker_id = Sneakers.sneaker_id;

-- get the sneaker ids, brands, and model names from the Sneakers table
-- used for adding and updating a Sneaker in the Raffles table
SELECT sneaker_id, brand, model_name FROM Sneakers

-- get order attributes from the Orders table
-- get customer name from Customers table
SELECT *, name FROM Orders
INNER JOIN Customers
ON Orders.customer_id = Customers.customer_id;

-- get customer ids and names from the Customers table
-- used for adding and updating a Customer in the Orders table
SELECT customer_id, name FROM Customers

-- get raffle order attributes from the RaffleOrders table
-- get customer name from Customers table
-- get raffle description from Raffles table
SELECT *, name, raffle_description FROM RaffleOrders
INNER JOIN Raffles
ON RaffleOrders.raffle_id = Raffles.raffle_id
INNER JOIN Orders
ON RaffleOrders.order_id = Orders.order_id
INNER JOIN Customers
ON Orders.customer_id = Customers.customer_id;

-- get the order id and customer names from the Orders and Customers tables
-- used for adding and updating an Order in the RaffleOrders table
SELECT order_id, name FROM Orders
INNER JOIN Customers
ON Orders.customer_id = Customers.customer_id

-- get the raffle ids and raffle descriptions from the Raffles table
-- used for adding and updating a Raffle in the RaffleOrders table
SELECT raffle_id, raffle_description FROM Raffles

-- get sneaker order attributes from the SneakerOrders table
-- get brands and model names from Sneakers table
-- get customer names from Customers table
SELECT *, brand, model_name, name FROM SneakerOrders
LEFT JOIN Sneakers
ON SneakerOrders.sneaker_id = Sneakers.sneaker_id
INNER JOIN Orders
ON SneakerOrders.order_id = Orders.order_id
INNER JOIN Customers
ON Orders.customer_id = Customers.customer_id;

-- get the sneaker ids, brands, model name from the Sneakers table
-- used for adding and updating a Sneaker in the SneakerOrders table
SELECT sneaker_id, brand, model_name FROM Sneakers

-- get the order ids and customer names from the Orders and Customers table
-- used for adding and updating an Order in the SneakerOrders table
SELECT order_id, name FROM Orders
INNER JOIN Customers
ON Orders.customer_id = Customers.customer_id

-- get customer raffle attributes from the CustomerRaffles table
-- get customer name from Customers table
-- get raffle description from Raffles table
SELECT *, name, raffle_description FROM CustomerRaffles
INNER JOIN Customers
ON CustomerRaffles.customer_id = Customers.customer_id
INNER JOIN Raffles
ON CustomerRaffles.raffle_id = Raffles.raffle_id;

-- get customer attributes from the Customers table
-- used for adding and updating a Customer in the CustomerRaffles table
SELECT * FROM Customers

-- get the raffle attributes from the Raffles table
-- used for adding and updating a Raffle in the CustomerRaffles table
SELECT * FROM Customers

-- INSERT Queries to Create a New Table Entry Based on User Input
-- add a new customer entry
insert into Customers (name, email, phone_number)
values (~name_input, ~email_input, ~phone_number_input);

-- add a new sneaker entry
insert into Sneakers (brand, model_name, size, colorway, price, stock_count)
values (~brand_input, ~model_name_input, ~size_input, ~colorway_input, ~price_input, ~stock_count_input);

-- add a new order entry
insert into Orders (customer_id, purchase_date, total_price, entered_raffle)
values (~customer_id_from_dropdown_input, ~purchase_date_calendar_input, ~total_price_input, ~entered_raffle_input);

-- add a new raffle entry
insert into Raffles (sneaker_id, raffle_description, entry_cost)
values (~sneaker_id_from_dropdown_input, ~raffle_description_input, ~entry_cost_input);

-- add a new drawing entry
insert into Drawings (raffle_id, draw_date, draw_day)
values (~raffle_id_from_dropdown_input, ~draw_date_calendar_input, ~draw_day_input);

-- add a new sneaker order entry
insert into SneakerOrders (order_id, sneaker_id, quantity)
values (~order_id_from_dropdown_input, ~sneaker_id_from_dropdown_input, ~quantity_input);

-- add a new raffle order entry 
insert into RaffleOrders (order_id, raffle_id)
values (~order_id_from_dropdown_input, ~raffle_id_from_dropdown_input);

-- add a new customer raffle entry 
insert into CustomerRaffles (raffle_id, customer_id, won_raffle)
values (~raffle_id_from_dropdown_input, ~customer_id_from_dropdown_input, ~won_raffle_input);

-- UPDATE Queries to Update a Table Entry Based on User Input
-- update a customer entry
update Customers
set name = ~name_input, email = ~email_input, phone_number = ~phone_number_input
where customer_id = ~customer_id_from_browse_customers_page;

-- update a sneaker entry
update Sneakers
set brand = ~brand_input, model_name = ~model_name_input, size = ~size_input, colorway = ~colorway_input, price = ~price_input, stock_count = ~stock_count_input
where sneaker_id = ~sneaker_id_from_browse_sneakers_page;

-- update an order entry
update Orders
set customer_id = ~customer_id_from_dropdown_input, purchase_date = ~purchase_date_calendar_input, total_price = ~total_price_input, entered_raffle = ~entered_raffle_input
where order_id = ~order_id_from_browse_orders_page;

-- update a raffle entry
update Raffles
set sneaker_id = ~sneaker_id_from_dropdown_input, raffle_description = ~raffle_description_input, entry_cost = ~entry_cost_input
where raffle_id = ~raffle_id_from_browse_raffles_page;

-- update a drawing entry
update Drawings
set raffle_id = ~raffle_id_from_dropdown_input, draw_date = ~draw_date_calendar_input, draw_day = ~draw_day_input
where drawing_id = ~draw_id_from_browse_drawings_page;

-- update a sneaker order entry
update SneakerOrders
set order_id = ~order_id_from_dropdown_input, sneaker_id = ~sneaker_id_from_dropdown_input, quantity = ~quantity_input
where sneaker_order_id = ~sneaker_order_id_from_browse_sneaker_orders_page;

-- update a raffle order entry 
update RaffleOrders
set order_id = ~order_id_from_dropdown_input, raffle_id = ~raffle_id_from_dropdown_input
where raffle_order_id = ~raffle_order_id_from_browse_raffle_orders_page;

-- update a customer raffle entry 
update CustomerRaffles 
set raffle_id = ~raffle_id_from_dropdown_input, customer_id = ~customer_id_from_dropdown_input, won_raffle = ~won_raffle_input
where custoemr_raffle_id = ~customer_raffle_id_from_browse_customer_raffles_page;

-- DELETE Queries to Delete a Table Entry Based on Table ID
-- delete a customer entry
delete from Customers
where customer_id = ~customer_id_from_browse_customers_page;

-- delete a sneaker entry
delete from Sneakers
where sneaker_id = ~sneaker_id_from_browse_sneakers_page;

-- delete an order entry
delete from Orders
where order_id = ~order_id_from_browse_orders_page;

-- delete a raffle entry
delete from Raffles
where raffle_id = ~raffle_id_from_browse_raffles_page;

-- delete a drawing entry
delete from Drawings
where drawing_id = ~drawing_id_from_browse_drawings_page;

-- delete a sneaker order entry 
delete from SneakerOrders
where sneaker_order_id = ~sneaker_order_id_from_browse_sneaker_orders_page;

-- delete a raffle order entry
delete from RaffleOrders
where raffle_order_id = ~raffle_order_id_from_browse_raffle_orders_page;

-- delete a customer raffle entry
delete from CustomerRaffles
where customer_raffle_id = ~customer_raffle_id_from_browse_customer_raffles_page;

-- Example Queries
-- get the sneaker name, raffle description, and draw date from the Sneakers, Raffles, and Drawings tables
select Sneakers.name, Raffles.raffle_description, Drawings.draw_date
from Sneakers
inner join Raffles on Sneakers.sneaker_id = Raffles.sneaker_id
inner join Drawings on Raffles.raffle_id = Drawings.raffle_id
order by Drawings.draw_date desc;

-- get the customer name, purchase date, and total price from the Customers and Orders tables
select Customers.name, Orders.purchase_date, Orders.total_price
from Customers
inner join Orders on Customers.customer_id = Orders.customer_id
order by Customers.name asc;

-- get the sneaker name, customer name, entry cost, and raffle outcome from the Sneakers, Customers, Raffles, and CustomerRaffles tables
select Sneakers.model_name, Customers.name, Raffles.entry_cost, CustomerRaffles.won_raffle
from Sneakers
inner join Raffles on Sneakers.sneaker_id = Raffles.sneaker_id
inner join CustomerRaffles on Raffles.raffle_id = CustomerRaffles.raffle_id
inner join Customers on CustomerRaffles.customer_id = Customers.customer_id
order by Sneakers.model_name asc;

-- get order ID, sneaker name, and quantity purchased from Sneakers and SneakerOrders tables
select SneakerOrders.order_id, Sneakers.model_name, SneakerOrders.quantity
from SneakerOrders
inner join Sneakers on SneakerOrders.sneaker_id = Sneaker.sneaker_id
order by SneakerOrders.order_id asc;

-- get order ID, raffle ID, and sneaker name from RaffleOrders, Raffles, and Sneakers tables
select RaffleOrders.order_id, RaffleOrders.raffle_id, Sneakers.model_name
from RaffleOrders
inner join Raffles on RaffleOrders.raffle_id = Raffles.raffle_id
inner join Sneakers on Raffles.sneaker_id = Sneakers.sneaker_id
order by RaffleOrders.order_id asc;
