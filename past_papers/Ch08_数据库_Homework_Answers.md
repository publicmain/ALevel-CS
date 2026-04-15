# Chapter 8: Databases - Homework Answers

> Total: 60 marks

---

## Question 1 [4 marks]

**(a)** Explain what is meant by a **relational database**. [2 marks]

**Answer:**

✓ A relational database is a database that organises data into one or more tables (also called relations), where each table consists of rows (records/tuples) and columns (fields/attributes)
✓ Tables can be linked/related to each other through the use of key fields (primary keys and foreign keys), allowing data to be stored efficiently and relationships between entities to be represented

**(b)** Explain the difference between a **primary key** and a **foreign key**. [2 marks]

**Answer:**

✓ A **primary key** is a field (or combination of fields) that uniquely identifies each record in a table; no two records can have the same primary key value, and it cannot be NULL
✓ A **foreign key** is a field in one table that references the primary key of another table; it is used to create a link/relationship between the two tables and enforce referential integrity

---

## Question 2 [6 marks]

**(a)** Identify the primary key and any foreign keys in the LOAN table. [2 marks]

**Answer:**

✓ Primary key: **LoanID**
✓ Foreign keys: **BookID** (references BOOK.BookID) and **MemberID** (references MEMBER.MemberID)

**(b)** Describe the relationship between BOOK and LOAN. State the type. [2 marks]

**Answer:**

✓ The relationship is **one-to-many (1:M)** — one book can appear in many loan records (it can be borrowed many times), but each loan record relates to only one book
✓ This is implemented by BookID appearing as a foreign key in the LOAN table, referencing the primary key BookID in the BOOK table

**(c)** Entity-relationship diagram. [2 marks]

**Answer:**

```
GENRE 1 ──── M BOOK 1 ──── M LOAN M ──── 1 MEMBER
```

✓ GENRE to BOOK: One-to-many (1:M) — one genre can contain many books; each book belongs to one genre
✓ BOOK to LOAN: One-to-many (1:M) — one book can have many loans; each loan is for one book
✓ MEMBER to LOAN: One-to-many (1:M) — one member can have many loans; each loan belongs to one member

---

## Question 3 [8 marks]

**(a)** Explain why this table is not in a suitable normalised form. Identify two problems. [2 marks]

**Answer:**

✓ **Data redundancy** — customer data (CustomerName, CustomerEmail) is repeated for every order that customer makes (e.g. "Li Wei" and "li@email.com" appear in rows 1001 and 1002); similarly, product data (ProductName, ProductPrice) is duplicated (e.g. "Keyboard, 45.00" appears in rows 1001 and 1003)
✓ **Update anomaly / inconsistency risk** — if a customer's email address changes, it must be updated in every row where that customer appears; if one row is missed, the data becomes inconsistent. Deletion of the last order for a customer would also lose the customer's details entirely (deletion anomaly)

**(b)** Definitions: [3 marks]

✓ **First Normal Form (1NF):** A table is in 1NF if it contains no repeating groups, each column contains only atomic (indivisible) values, and each row is unique (has a primary key)

✓ **Second Normal Form (2NF):** A table is in 2NF if it is already in 1NF and every non-key attribute is fully functionally dependent on the whole primary key (i.e. no partial dependencies — no non-key attribute depends on only part of a composite primary key)

✓ **Third Normal Form (3NF):** A table is in 3NF if it is already in 2NF and there are no transitive dependencies — i.e. no non-key attribute depends on another non-key attribute; all non-key attributes depend directly on the primary key

**(c)** Normalise to 3NF. [3 marks]

**Answer:**

✓ **CUSTOMER** (<u>CustomerID</u>, CustomerName, CustomerEmail)

| CustomerID | CustomerName | CustomerEmail |
|-----------|-------------|---------------|
| C001 | Li Wei | li@email.com |
| C002 | Zhang Min | zhang@email.com |

✓ **PRODUCT** (<u>ProductID</u>, ProductName, ProductPrice)

| ProductID | ProductName | ProductPrice |
|----------|-------------|-------------|
| P001 | Keyboard | 45.00 |
| P002 | Mouse | 25.00 |
| P003 | Monitor | 299.00 |

✓ **ORDER_ITEM** (<u>OrderID</u>, *CustomerID*, *ProductID*, Quantity, OrderDate)

| OrderID | CustomerID | ProductID | Quantity | OrderDate |
|---------|-----------|----------|----------|-----------|
| 1001 | C001 | P001 | 2 | 2025-03-01 |
| 1002 | C001 | P002 | 1 | 2025-03-01 |
| 1003 | C002 | P001 | 1 | 2025-03-02 |
| 1004 | C002 | P003 | 1 | 2025-03-02 |

Primary keys are <u>underlined</u>. Foreign keys are marked with *italics* — CustomerID in ORDER_ITEM references CUSTOMER, and ProductID in ORDER_ITEM references PRODUCT.

---

## Question 4 [6 marks]

**(a)** Display title and author of all books with GenreID = 3, ordered by title. [2 marks]

```sql
SELECT Title, Author
FROM BOOK
WHERE GenreID = 3
ORDER BY Title ASC;
```

✓ Correct SELECT with correct fields (Title, Author)
✓ Correct WHERE clause and ORDER BY clause

**(b)** Insert a new member. [2 marks]

```sql
INSERT INTO MEMBER (MemberID, FirstName, LastName, Email, JoinDate)
VALUES ('M500', 'Chen', 'Yue', 'chenyue@email.com', '2025-09-01');
```

✓ Correct INSERT INTO ... VALUES syntax
✓ All values correctly listed in the correct order

**(c)** Update the email address. [2 marks]

```sql
UPDATE MEMBER
SET Email = 'newemail@email.com'
WHERE MemberID = 'M500';
```

✓ Correct UPDATE ... SET syntax
✓ Correct WHERE clause to identify the specific record

---

## Question 5 [6 marks]

**(a)** Delete all loan records where DateReturned is before '2024-01-01'. [2 marks]

```sql
DELETE FROM LOAN
WHERE DateReturned < '2024-01-01';
```

✓ Correct DELETE FROM syntax
✓ Correct WHERE clause with appropriate comparison operator

**(b)** Display first name, last name, book title, and date borrowed for unreturned loans. [4 marks]

```sql
SELECT m.FirstName, m.LastName, b.Title, l.DateBorrowed
FROM LOAN l
JOIN MEMBER m ON l.MemberID = m.MemberID
JOIN BOOK b ON l.BookID = b.BookID
WHERE l.DateReturned IS NULL;
```

✓ Correct SELECT with fields from multiple tables
✓ Correct JOIN between LOAN and MEMBER on MemberID
✓ Correct JOIN between LOAN and BOOK on BookID
✓ Correct WHERE clause using IS NULL (not = NULL)

---

## Question 6 [4 marks]

Explain the difference between **DDL** and **DML**. Give one example SQL statement for each.

**Answer:**

**DDL (Data Definition Language):**
✓ DDL is used to define or modify the structure of the database — e.g. creating, altering, or deleting tables and specifying data types, keys, and constraints
✓ Example: `CREATE TABLE MEMBER (MemberID VARCHAR(10) PRIMARY KEY, FirstName VARCHAR(50));`

**DML (Data Manipulation Language):**
✓ DML is used to manipulate/work with the data stored in the database — e.g. inserting, selecting, updating, and deleting records
✓ Example: `SELECT * FROM MEMBER WHERE MemberID = 'M500';`

---

## Question 7 [6 marks]

Write SQL to create the LOAN table.

```sql
CREATE TABLE LOAN (
    LoanID VARCHAR(10) PRIMARY KEY,
    BookID VARCHAR(10) NOT NULL,
    MemberID VARCHAR(10) NOT NULL,
    DateBorrowed DATE NOT NULL,
    DateReturned DATE,
    FOREIGN KEY (BookID) REFERENCES BOOK(BookID),
    FOREIGN KEY (MemberID) REFERENCES MEMBER(MemberID)
);
```

✓ Correct CREATE TABLE syntax with table name LOAN
✓ LoanID defined as PRIMARY KEY
✓ BookID defined as FOREIGN KEY referencing BOOK(BookID)
✓ MemberID defined as FOREIGN KEY referencing MEMBER(MemberID)
✓ DateBorrowed specified as NOT NULL
✓ DateReturned allows NULL (no NOT NULL constraint)

---

## Question 8 [6 marks]

**(a)** Explain what is meant by a **DBMS**. [2 marks]

**Answer:**

✓ A DBMS (Database Management System) is software that provides an interface between the user/application programs and the database, enabling users to create, access, manage, and manipulate data
✓ It handles data storage, retrieval, security, and integrity, acting as an intermediary so that users do not need to know how or where data is physically stored

**(b)** Describe **two** features of a DBMS that help maintain data integrity. [2 marks]

**Answer:**

✓ **Referential integrity enforcement** — the DBMS ensures that foreign key values in one table always refer to existing primary key values in the related table; it prevents records from being deleted from a parent table if dependent records exist in a child table
✓ **Validation rules / data type enforcement** — the DBMS enforces data types, constraints (e.g. NOT NULL, UNIQUE, CHECK), and validation rules defined in the schema, preventing invalid data from being entered into the database

**(c)** Explain what a **data dictionary** is and state two items of information it contains. [2 marks]

**Answer:**

✓ A data dictionary is a centralised repository of metadata (data about data) that stores information about the structure and properties of all the data items in the database
✓ It contains: (1) the name and data type of each field/attribute in every table, and (2) any constraints or validation rules applied to each field (e.g. primary key, foreign key, NOT NULL, default values, field size)

---

## Question 9 [6 marks]

**(a)** Explain why a many-to-many relationship cannot be directly implemented. [2 marks]

**Answer:**

✓ A many-to-many relationship cannot be directly represented in a relational database because it would require a field to hold multiple values (e.g. a student record would need to store multiple course IDs), which violates the principle of atomic values in 1NF
✓ It would lead to data redundancy and anomalies — there is no straightforward way to link the two tables using simple foreign keys without creating repeating groups or duplicate data

**(b)** Resolve the many-to-many relationship. [4 marks]

**Answer:**

✓ **STUDENT** (<u>StudentID</u>, FirstName, LastName, Email)

✓ **COURSE** (<u>CourseID</u>, CourseName, Teacher)

✓ **ENROLMENT** (<u>EnrolmentID</u>, *StudentID*, *CourseID*, EnrolmentDate)

Alternatively, using a composite primary key:

✓ **ENROLMENT** (<u>*StudentID*</u>, <u>*CourseID*</u>, EnrolmentDate)

- The ENROLMENT table is the junction/link/intermediate table that resolves the many-to-many relationship
- StudentID is a foreign key referencing STUDENT(StudentID)
- CourseID is a foreign key referencing COURSE(CourseID)
- The primary key can be either a separate EnrolmentID or a composite key of (StudentID, CourseID)
- This creates two one-to-many relationships: STUDENT 1:M ENROLMENT and COURSE 1:M ENROLMENT

---

## Question 10 [8 marks]

**(a)** Describe what the query does, line by line. [5 marks]

```sql
SELECT m.FirstName, m.LastName, COUNT(l.LoanID) AS TotalLoans
```
✓ Selects the first name and last name of each member, and counts the number of loan records for each member, giving the count an alias of "TotalLoans"

```sql
FROM MEMBER m
```
✓ Specifies the MEMBER table as the main table, using "m" as an alias for shorter referencing

```sql
JOIN LOAN l ON m.MemberID = l.MemberID
```
✓ Performs an inner join between MEMBER and LOAN tables on the MemberID field, so only members who have at least one loan are included

```sql
GROUP BY m.MemberID, m.FirstName, m.LastName
```
✓ Groups the results by each member (using MemberID, FirstName, LastName), so that the COUNT function calculates the total number of loans per member

```sql
HAVING COUNT(l.LoanID) > 5
ORDER BY TotalLoans DESC;
```
✓ HAVING filters the grouped results to include only members with more than 5 loans; ORDER BY sorts the final results in descending order of TotalLoans (members with the most loans appear first)

**(b)** Explain the difference between WHERE and HAVING. [3 marks]

**Answer:**

✓ The **WHERE** clause filters individual rows/records before any grouping takes place — it is applied to the raw data and cannot be used with aggregate functions (COUNT, SUM, AVG, etc.)
✓ The **HAVING** clause filters groups of rows after the GROUP BY has been applied — it is used to filter based on the results of aggregate functions
✓ For example, `WHERE GenreID = 3` filters individual book records before grouping, while `HAVING COUNT(l.LoanID) > 5` filters out groups (members) that do not meet the aggregate condition after grouping

---

**--- END OF ANSWERS ---**
