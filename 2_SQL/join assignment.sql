CREATE TABLE Loans_table(
	Deal_id INT PRIMARY KEY,
    Merchant_ID INT NOT NULL,
    Funded  VARCHAR NOT NULL,
    Industry VARCHAR NOT NULL,
    type VARCHAR NOT NULL);
	
SELECT * FROM Loans_table;

INSERT INTO Loans_table VALUES
(1,1,'01/01/2016','Retail','New'),
(100,80,'04/01/2016','Construction','New'),
(130,100,'04/15/2016','Trucking','New'),
(1010,1,'6/23/2017','Retail','Renewal'),
(1051,100,'7/01/2017','Trucking','Renewal'),
(1251,1,'10/01/2017','tail','newal');

CREATE TABLE Submissions(
	Deal_id INT PRIMARY KEY,
    Loan_Amount INT NOT NULL,
    interest_rate DECIMAL NOT NULL,
    rate_type VARCHAR NOT NULL);
	
SELECT * FROM Submissions;

INSERT INTO Submissions VALUES
(1,10000,8.75,'variable'),
(100,10000,11.37,'fixed'),
(1010,15000,8.25,'fixed'),
(1051,20000,4.75,'variable'),
(1251,40000,4.75,'variable'),
(130,10000,3.0,'variable');

SELECT
  l.Merchant_Id,
  l.Deal_id,
  s.Loan_Amount 
FROM Loans_table l
JOIN Submissions s 
ON l.Deal_id = s.Deal_id
WHERE l.Industry = 'Renewal'
AND l.Funded = (
  SELECT MAX(Funded)
  FROM Loans_table
  WHERE Merchant_Id = l.Merchant_Id
  AND Industry = 'Renewal'
);