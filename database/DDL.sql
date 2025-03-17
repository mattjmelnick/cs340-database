-- Amity Hill, Matthew Melnick
-- Eastern Beavers (Group 15)
-- Data Definition Queries with sample data to initialize database for Step 6

SET FOREIGN_KEY_CHECKS=0;
SET AUTOCOMMIT = 0;

-- Drops existing tables to prevent issues loading 
DROP TABLE IF EXISTS Customers, Sneakers, Raffles, Drawings, CustomerRaffles, Orders, RaffleOrders, SneakerOrders;

-- Creates Customers Table
CREATE TABLE Customers(
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(100) NOT NULL,
    phone_number CHAR(12) NOT NULL
);

-- Creates Sneakers Table 
CREATE TABLE Sneakers(
    sneaker_id INT AUTO_INCREMENT PRIMARY KEY,
    brand VARCHAR(100) NOT NULL,
    model_name VARCHAR(100) NOT NULL,
    size DECIMAL(3,1) NOT NULL,
    colorway VARCHAR(100) NOT NULL,
    price DECIMAL(9,2) NOT NULL,
    stock_count INT NOT NULL
);

-- Creates Raffles Table
CREATE TABLE Raffles(
    raffle_id INT AUTO_INCREMENT PRIMARY KEY,
    sneaker_id INT NOT NULL,
    raffle_description TEXT NOT NULL UNIQUE,
    entry_cost DECIMAL(5,2) NOT NULL,
    FOREIGN KEY (sneaker_id) REFERENCES Sneakers(sneaker_id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Creates Drawings Table
CREATE TABLE Drawings(
    drawing_id INT AUTO_INCREMENT PRIMARY KEY,
    raffle_id INT NOT NULL,
    draw_date DATE NOT NULL,
    draw_day VARCHAR(9) NOT NULL,
    FOREIGN KEY (raffle_id) REFERENCES Raffles(raffle_id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Creates CustomerRaffles Intersection Table
CREATE TABLE CustomerRaffles(
    customer_raffle_id INT AUTO_INCREMENT PRIMARY KEY,
    raffle_id INT NOT NULL,
    customer_id INT NOT NULL,
    won_raffle TINYINT(1) NOT NULL,
    FOREIGN KEY (raffle_id) REFERENCES Raffles(raffle_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (customer_id) REFERENCES Customers (customer_id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Creates Orders Table
CREATE TABLE Orders(
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    purchase_date DATE NOT NULL,
    total_price DECIMAL(9,2) NOT NULL,
    entered_raffle TINYINT(1) NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Creates SneakerOrders Intersection Table
CREATE TABLE SneakerOrders(
    sneaker_order_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    sneaker_id INT NULL,
    quantity INT NOT NULL,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (sneaker_id) REFERENCES Sneakers (sneaker_id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Creates RaffleOrders Intersection Table
CREATE TABLE RaffleOrders(
    raffle_order_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    raffle_id INT NULL,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (raffle_id) REFERENCES Raffles(raffle_id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Insert Data into Customers Table 
INSERT INTO Customers(name, email, phone_number)
VALUES
('Jonah Hill', '21JumpStreet@blockbuster.com', '323-999-9999'),
('Will Ferrell', 'THEAnchorman@blockbuster.com', '949-999-9999'),
('Dave Chappelle', 'HalfBaked@blockbuster.com', '202-999-9999');

-- Insert Data into Sneakers Table 
INSERT INTO Sneakers(brand, model_name, size, colorway, price, stock_count)
VALUES
('Nike', 'Nike Air Yeezy 2 "Red October"', 10, 'Red', 250.00, 1),
('Nike', 'Nike SB Dunk Low "Ben & Jerry Chunky Dunky"', 8, 'White/Lagoon Pulse/Black/University Gold', 100.00, 1),
('Jordan', 'Off-White x Jordan Retro 4 Sail', 7, 'Sail/Muslin/White/Black', 200, 1),
('Adidas', 'Y-3 Superstar', 9, 'Core White/Talc/Black', 350.00, 10),
('Adidas', 'Y-3 Stan Smith', 11, 'Off White/ Off White/ Off White', 350.00, 10);

-- Insert Data into Raffles Table 
INSERT INTO Raffles(sneaker_id, raffle_description, entry_cost)
VALUES
(1, 'The Nike Air Yeezy 2 "Red October" is the latest collaboration with musician and fashion designer Kanye West.', 20.00),
(2, 'Drawing inspiration from Ben & Jerry’s colorful ice cream pint packaging, this release goes beyond a simple new colorway and features unique detailing that has never been used on the Dunk Low silhouette.', 20.00),
(3, 'After teasing the release of the Off-White 4 with samples in his MCA exhibit and presenting them in his Off-White FW2020 Women’s Show, Jordan finally delivered what might be the most anticipated re-release of 2025', 20.00);

-- Insert Data into Drawings Table 
INSERT INTO Drawings(raffle_id, draw_date, draw_day)
VALUES 
((SELECT raffle_id from Raffles where sneaker_id = 1), '2025-04-12', 'Saturday'),
((SELECT raffle_id from Raffles where sneaker_id = 2), '2025-05-17', 'Saturday'),
((SELECT raffle_id from Raffles where sneaker_id = 3), '2025-06-13', 'Friday');

-- Insert Data into CustomerRaffles Table 
INSERT INTO CustomerRaffles(raffle_id, customer_id, won_raffle)
VALUES
((SELECT raffle_id from Raffles where sneaker_id = 1), 3, 1),
((SELECT raffle_id from Raffles where sneaker_id = 2), 2, 1),
((SELECT raffle_id from Raffles where sneaker_id = 3), 1, 1);

-- Insert Data into Orders Table 
INSERT INTO Orders(customer_id, purchase_date, total_price, entered_raffle)
VALUES
(1, '2025-06-13', 620.00, 1),
(2, '2025-06-13', 350.00, 0),
(2, '2025-05-17', 970.00, 1),
(3, '2025-04-12', 270.00, 1);

-- Insert Data into SneakerOrders Table 
INSERT INTO SneakerOrders(order_id, sneaker_id, quantity)
VALUES
((SELECT order_id from Orders where customer_id = 1 and purchase_date = '2025-06-13'), (SELECT sneaker_id from Sneakers where sneaker_id = 4), 1),
((SELECT order_id from Orders where customer_id = 2 and purchase_date = '2025-06-13'), (SELECT sneaker_id from Sneakers where sneaker_id = 4), 1),
((SELECT order_id from Orders where customer_id = 2 and purchase_date = '2025-05-17'), (SELECT sneaker_id from Sneakers where sneaker_id = 5), 2);

-- Insert Data into RaffleOrders Table 
INSERT INTO RaffleOrders(order_id, raffle_id)
VALUES
((SELECT order_id from Orders where customer_id = 3 and purchase_date = '2025-04-12'), (SELECT raffle_id from CustomerRaffles where customer_id = 3)),
((SELECT order_id from Orders where customer_id = 2 and purchase_date = '2025-05-17'), (SELECT raffle_id from CustomerRaffles where customer_id = 2)),
((SELECT order_id from Orders where customer_id = 1 and purchase_date = '2025-06-13'), (SELECT raffle_id from CustomerRaffles where customer_id = 1));

SET FOREIGN_KEY_CHECKS=1;
COMMIT;