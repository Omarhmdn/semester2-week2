-- Enable readable output format
.mode columns
.headers on

-- Instructions for students:
-- 1. Open SQLite in terminal: sqlite3 library.db
-- 2. Load this script: .read code.sql
-- 3. Exit SQLite: .exit


-- write your sql code here
--QUESTION 1
SELECT Books.title, Members.name, DATE(Loans.loan_date) AS Loan_Date 
FROM Books JOIN Loans ON Books.id=Loans.book_id JOIN Members ON Loans.member_id=Members.id 
GROUP BY Loan_Date;

--QUESTION 2
SELECT Books.title, Loans.id 
FROM Books LEFT JOIN Loans ON Books.id=Loans.book_id 
GROUP BY Books.title;

--QUESTION 6
SELECT Members.name, COUNT(Loans.id) AS Num_of_Loans
FROM Members LEFT JOIN Loans ON Members.id=Loans.member_id
GROUP BY Members.id;

--QUESTION 7
SELECT Members.name, COUNT(Loans.id) AS Num_of_Loans
FROM Members LEFT JOIN Loans ON Members.id=Loans.member_id
GROUP BY Members.id HAVING Num_of_Loans = 0;
