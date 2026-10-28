USE ai_learning;
CREATE TABLE used_cars(
    id INT AUTO_INCREMENT PRIMARY KEY ,
    car_name VARCHAR(100),
    fuel_type VARCHAR(20),
    transmission VARCHAR(20),
    mileage FLOAT,
    engine FLOAT,
    power FLOAT,
    seats FLOAT,
    new_price FLOAT
);
SHOW TABLES;
SELECT * FROM used_cars LIMIT 10;
SELECT car_name, new_price FROM used_cars WHERE new_price > 100000 AND fuel_type = 'Diesel';
SELECT car_name, power FROM used_cars ORDER BY power  DESC LIMIT 5;
SELECT used_cars.transmission,AVG(new_price) AS avg_price FROM used_cars GROUP BY transmission;
SELECT * FROM used_cars WHERE car_name LIKE '%Toyota%';
ALTER TABLE used_cars add(gender char(1),tel char(11));   #添加列
ALTER TABLE used_cars drop tel; #删除
DESC used_cars;
ALTER TABLE used_cars drop gender;
ALTER TABLE used_cars MODIFY COLUMN new_price DECIMAL(10,2);   #改变数据类型
ALTER TABLE used_cars CHANGE tel  phone char(11);   #  更改列名，change必须带上数据类型
ALTER TABLE used_cars RENAME COLUMN gender TO sex;

CREATE TABLE sellers (
    seller_id INT AUTO_INCREMENT PRIMARY KEY,
    seller_name VARCHAR(50),
    city VARCHAR(50)
);
INSERT INTO sellers (seller_name,city) VALUES
('张三','北京'),
('李四','上海'),
('王五','广州');
ALTER TABLE used_cars ADD COLUMN seller_id INT;
UPDATE used_cars SET seller_id = 1 WHERE id IN (1,2);
UPDATE used_cars SET seller_id = 2 WHERE id IN (3,4);

 SELECT c.car_name, c.new_price, s.seller_name, s.city   #内连接
 FROM used_cars AS c
 INNER JOIN sellers AS s ON c.seller_id = s.seller_id;


SELECT c.car_name, s.seller_name   #  左连接
FROM used_cars AS c
LEFT JOIN sellers AS s ON c.seller_id = s.seller_id;


CREATE INDEX idx_car_name ON used_cars(car_name);   # 给车名建个索引

EXPLAIN SELECT * FROM used_cars WHERE fuel_type = 'Diesel';   # 检测索引到底有没有生效
EXPLAIN SELECT * FROM used_cars WHERE car_name = 'Toyota';


START TRANSACTION;    #  价格打9折
UPDATE used_cars SET new_price = new_price * 0.9;
COMMIT;

SELECT car_name, new_price FROM used_cars LIMIT 5;