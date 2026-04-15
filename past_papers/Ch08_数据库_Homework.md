# Chapter 8: Databases - 课后作业 Homework

> 姓名：__________ 日期：__________ 总分：__/60

---

## Question 1 [4 marks]

A school stores data about students, courses, and enrolments in a relational database.

(a) Explain what is meant by a **relational database**. [2 marks]

(b) Explain the difference between a **primary key** and a **foreign key**. [2 marks]

---

## Question 2 [6 marks]

A library database has the following tables:

**BOOK** (BookID, Title, Author, ISBN, GenreID)

**GENRE** (GenreID, GenreName, Description)

**MEMBER** (MemberID, FirstName, LastName, Email, JoinDate)

**LOAN** (LoanID, BookID, MemberID, DateBorrowed, DateReturned)

(a) Identify the **primary key** and any **foreign keys** in the LOAN table. [2 marks]

(b) Describe the relationship between the BOOK table and the LOAN table. State the type of relationship. [2 marks]

(c) Draw an **entity-relationship (E-R) diagram** showing the relationships between all four tables. Use appropriate notation to show the type of each relationship. [2 marks]

---

## Question 3 [8 marks]

The following table stores data about orders in a small business:

| OrderID | CustomerName | CustomerEmail | ProductName | ProductPrice | Quantity | OrderDate |
|---------|-------------|---------------|-------------|-------------|----------|-----------|
| 1001 | Li Wei | li@email.com | Keyboard | 45.00 | 2 | 2025-03-01 |
| 1002 | Li Wei | li@email.com | Mouse | 25.00 | 1 | 2025-03-01 |
| 1003 | Zhang Min | zhang@email.com | Keyboard | 45.00 | 1 | 2025-03-02 |
| 1004 | Zhang Min | zhang@email.com | Monitor | 299.00 | 1 | 2025-03-02 |

(a) Explain why this table is **not** in a suitable normalised form. Identify **two** problems with this design. [2 marks]

(b) Define what is meant by:
- **First Normal Form (1NF)** [1 mark]
- **Second Normal Form (2NF)** [1 mark]
- **Third Normal Form (3NF)** [1 mark]

(c) Normalise the table above to **Third Normal Form (3NF)**. Show the resulting tables clearly, underlining primary keys and indicating foreign keys. [3 marks]

和外键。）

---

## Question 4 [6 marks]

Using the library database from Question 2, write SQL statements for each of the following:

(a) Display the title and author of all books with GenreID = 3, ordered alphabetically by title. [2 marks]

```sql

```

(b) Insert a new member with the following details: MemberID: 'M500', FirstName: 'Chen', LastName: 'Yue', Email: 'chenyue@email.com', JoinDate: '2025-09-01'. [2 marks]

```sql

```

(c) Update the email address of the member with MemberID 'M500' to 'newemail@email.com'. [2 marks]

```sql

```

---

## Question 5 [6 marks]

Using the library database from Question 2, write SQL statements for each of the following:

(a) Delete all loan records where the DateReturned is before '2024-01-01'. [2 marks]

```sql

```

(b) Display the first name, last name, book title, and date borrowed for all loans that have not yet been returned (DateReturned IS NULL). The results should show data from multiple tables. [4 marks]

```sql

```

---

## Question 6 [4 marks]

(a) Explain the difference between **DDL (Data Definition Language)** and **DML (Data Manipulation Language)**. Give one example SQL statement for each. [4 marks]

，DML用于操作数据（如SELECT, INSERT）。）

---

## Question 7 [6 marks]

Write an SQL statement to **create** the LOAN table from Question 2 with appropriate data types. The table should have:
- LoanID as a primary key
- BookID as a foreign key referencing the BOOK table
- MemberID as a foreign key referencing the MEMBER table
- DateBorrowed must not be NULL
- DateReturned can be NULL

```sql

```

[6 marks]

---

## Question 8 [6 marks]

A Database Management System (DBMS) is used to manage the library database.

(a) Explain what is meant by a **DBMS**. [2 marks]

(b) Describe **two** features of a DBMS that help maintain data integrity. [2 marks]

(c) Explain what a **data dictionary** is and state **two** items of information it contains. [2 marks]

---

## Question 9 [6 marks]

A many-to-many relationship exists between students and courses — a student can take many courses, and a course can have many students.

(a) Explain why a many-to-many relationship cannot be directly implemented in a relational database. [2 marks]

(b) Show how you would resolve the many-to-many relationship between STUDENT and COURSE by creating a suitable intermediate table. Write out the table structures, showing primary keys and foreign keys. [4 marks]

---

## Question 10 [8 marks]

The following SQL query is written to produce a report:

```sql
SELECT m.FirstName, m.LastName, COUNT(l.LoanID) AS TotalLoans
FROM MEMBER m
JOIN LOAN l ON m.MemberID = l.MemberID
GROUP BY m.MemberID, m.FirstName, m.LastName
HAVING COUNT(l.LoanID) > 5
ORDER BY TotalLoans DESC;
```

(a) Describe what this query does, line by line. [5 marks]

(b) Explain the difference between the **WHERE** clause and the **HAVING** clause in SQL. [3 marks]

---

**--- END OF HOMEWORK ---**

Total: 60 marks
