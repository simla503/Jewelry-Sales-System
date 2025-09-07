CREATE DATABASE JewelrySalesSystem;
GO

USE JewelrySalesSystem;
GO

-- 1. User (Nhân viên/Quản lý/Admin)
CREATE TABLE Users (
    user_id INT IDENTITY(1,1) PRIMARY KEY,
    name NVARCHAR(100) NOT NULL,
    email NVARCHAR(100) UNIQUE NOT NULL,
    password_hash NVARCHAR(255) NOT NULL,
    role NVARCHAR(50) CHECK (role IN ('Staff', 'Manager', 'Admin')) NOT NULL,
    created_at DATETIME DEFAULT GETDATE()
);

-- 2. Customer
CREATE TABLE Customers (
    customer_id INT IDENTITY(1,1) PRIMARY KEY,
    name NVARCHAR(100) NOT NULL,
    phone NVARCHAR(20),
    email NVARCHAR(100) UNIQUE,
    loyalty_points INT DEFAULT 0
);

-- 3. Counter (Quầy hàng)
CREATE TABLE Counters (
    counter_id INT IDENTITY(1,1) PRIMARY KEY,
    name NVARCHAR(50) NOT NULL
);

-- 4. GoldPrice (bảng giá vàng theo thời điểm)
CREATE TABLE GoldPrices (
    price_id INT IDENTITY(1,1) PRIMARY KEY,
    effective_date DATETIME DEFAULT GETDATE(),
    price_per_gram DECIMAL(18,2) NOT NULL
);

-- 5. Product
CREATE TABLE Products (
    product_id INT IDENTITY(1,1) PRIMARY KEY,
    name NVARCHAR(200) NOT NULL,
    weight DECIMAL(18,2) NOT NULL,
    gold_price_at_sale DECIMAL(18,2) NOT NULL,
    labor_cost DECIMAL(18,2) NOT NULL,
    stone_cost DECIMAL(18,2) NOT NULL,
    markup_rate DECIMAL(5,2) NOT NULL,
    final_price AS ( (gold_price_at_sale * weight) + labor_cost + stone_cost ) * markup_rate PERSISTED,
    barcode NVARCHAR(50) UNIQUE
);

-- 6. Promotion
CREATE TABLE Promotions (
    promotion_id INT IDENTITY(1,1) PRIMARY KEY,
    description NVARCHAR(255),
    discount_percent DECIMAL(5,2) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL
);

-- 7. Order
CREATE TABLE Orders (
    order_id INT IDENTITY(1,1) PRIMARY KEY,
    customer_id INT FOREIGN KEY REFERENCES Customers(customer_id),
    staff_id INT FOREIGN KEY REFERENCES Users(user_id),
    counter_id INT FOREIGN KEY REFERENCES Counters(counter_id),
    order_date DATETIME DEFAULT GETDATE(),
    total_amount DECIMAL(18,2) NOT NULL,
    discount DECIMAL(18,2) DEFAULT 0,
    final_amount DECIMAL(18,2) NOT NULL,
    promotion_id INT NULL FOREIGN KEY REFERENCES Promotions(promotion_id)
);

-- 8. OrderDetail
CREATE TABLE OrderDetails (
    order_detail_id INT IDENTITY(1,1) PRIMARY KEY,
    order_id INT FOREIGN KEY REFERENCES Orders(order_id),
    product_id INT FOREIGN KEY REFERENCES Products(product_id),
    quantity INT NOT NULL,
    unit_price DECIMAL(18,2) NOT NULL,
    subtotal AS (quantity * unit_price) PERSISTED
);

-- 9. Warranty
CREATE TABLE Warranties (
    warranty_id INT IDENTITY(1,1) PRIMARY KEY,
    product_id INT FOREIGN KEY REFERENCES Products(product_id),
    order_id INT FOREIGN KEY REFERENCES Orders(order_id),
    warranty_period INT NOT NULL, -- số tháng
    issue_date DATETIME DEFAULT GETDATE()
);

-- 10. BuyBack (Mua lại sản phẩm)
CREATE TABLE BuyBacks (
    buyback_id INT IDENTITY(1,1) PRIMARY KEY,
    product_id INT FOREIGN KEY REFERENCES Products(product_id),
    customer_id INT FOREIGN KEY REFERENCES Customers(customer_id),
    staff_id INT FOREIGN KEY REFERENCES Users(user_id),
    buyback_date DATETIME DEFAULT GETDATE(),
    price_paid DECIMAL(18,2) NOT NULL
);

-- 11. Loyalty Transaction
CREATE TABLE LoyaltyTransactions (
    transaction_id INT IDENTITY(1,1) PRIMARY KEY,
    customer_id INT FOREIGN KEY REFERENCES Customers(customer_id),
    points_change INT NOT NULL,
    transaction_date DATETIME DEFAULT GETDATE(),
    note NVARCHAR(255)
);
