# Chapter 8: Databases - 课后作业 Homework

> 姓名：__________ 日期：__________ 总分：__/60

---

## Question 1 [4 marks]

A school stores data about students, courses, and enrolments in a relational database.

(a) Explain what is meant by a **relational database**. [2 marks]

（中文提示：解释什么是关系数据库。数据以表格形式存储，表之间通过关系连接。）

(b) Explain the difference between a **primary key** and a **foreign key**. [2 marks]

（中文提示：解释主键和外键的区别。主键唯一标识表中的记录，外键是另一个表中的主键，用于建立表之间的关系。）

---

## Question 2 [6 marks]

A library database has the following tables:

**BOOK** (BookID, Title, Author, ISBN, GenreID)

**GENRE** (GenreID, GenreName, Description)

**MEMBER** (MemberID, FirstName, LastName, Email, JoinDate)

**LOAN** (LoanID, BookID, MemberID, DateBorrowed, DateReturned)

(a) Identify the **primary key** and any **foreign keys** in the LOAN table. [2 marks]

（中文提示：识别LOAN表中的主键和外键。）

(b) Describe the relationship between the BOOK table and the LOAN table. State the type of relationship. [2 marks]

（中文提示：描述BOOK表和LOAN表之间的关系并说明关系类型。一本书可以被多次借出。）

(c) Draw an **entity-relationship (E-R) diagram** showing the relationships between all four tables. Use appropriate notation to show the type of each relationship. [2 marks]

（中文提示：画出四个表之间的实体关系图，使用适当的标记表示每种关系类型。）

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

（中文提示：解释为什么这个表没有被合适地规范化。识别两个设计问题。考虑数据冗余和更新异常。）

(b) Define what is meant by:
- **First Normal Form (1NF)** [1 mark]
- **Second Normal Form (2NF)** [1 mark]
- **Third Normal Form (3NF)** [1 mark]

（中文提示：定义第一范式、第二范式和第三范式。1NF：无重复组；2NF：满足1NF且无部分依赖；3NF：满足2NF且无传递依赖。）

(c) Normalise the table above to **Third Normal Form (3NF)**. Show the resulting tables clearly, underlining primary keys and indicating foreign keys. [3 marks]

（中文提示：将上表规范化到第三范式。写出结果表，标明主键（下划线）和外键。）

---

## Question 4 [6 marks]

Using the library database from Question 2, write SQL statements for each of the following:

(a) Display the title and author of all books with GenreID = 3, ordered alphabetically by title. [2 marks]

```sql


```

（中文提示：查询GenreID为3的所有书籍的标题和作者，按标题字母顺序排列。使用SELECT...FROM...WHERE...ORDER BY。）

(b) Insert a new member with the following details: MemberID: 'M500', FirstName: 'Chen', LastName: 'Yue', Email: 'chenyue@email.com', JoinDate: '2025-09-01'. [2 marks]

```sql


```

（中文提示：插入新会员记录。使用INSERT INTO...VALUES。）

(c) Update the email address of the member with MemberID 'M500' to 'newemail@email.com'. [2 marks]

```sql


```

（中文提示：更新会员M500的电子邮件地址。使用UPDATE...SET...WHERE。）

---

## Question 5 [6 marks]

Using the library database from Question 2, write SQL statements for each of the following:

(a) Delete all loan records where the DateReturned is before '2024-01-01'. [2 marks]

```sql


```

（中文提示：删除所有归还日期在2024年1月1日之前的借阅记录。使用DELETE FROM...WHERE。）

(b) Display the first name, last name, book title, and date borrowed for all loans that have not yet been returned (DateReturned IS NULL). The results should show data from multiple tables. [4 marks]

```sql


```

（中文提示：查询所有尚未归还的借阅记录，显示借阅者姓名、书名和借阅日期。需要使用JOIN连接多个表。DateReturned为NULL表示未归还。）

---

## Question 6 [4 marks]

(a) Explain the difference between **DDL (Data Definition Language)** and **DML (Data Manipulation Language)**. Give one example SQL statement for each. [4 marks]

（中文提示：解释DDL和DML的区别并各举一个SQL语句示例。DDL用于定义数据库结构（如CREATE TABLE），DML用于操作数据（如SELECT, INSERT）。）

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

（中文提示：编写CREATE TABLE语句创建LOAN表。需要指定数据类型、主键、外键约束和NOT NULL约束。常用数据类型：VARCHAR, INT, DATE等。）

---

## Question 8 [6 marks]

A Database Management System (DBMS) is used to manage the library database.

(a) Explain what is meant by a **DBMS**. [2 marks]

（中文提示：解释什么是数据库管理系统。DBMS是管理数据库的软件，提供创建、查询和管理数据的工具。）

(b) Describe **two** features of a DBMS that help maintain data integrity. [2 marks]

（中文提示：描述DBMS帮助维护数据完整性的两个功能。例如：引用完整性、数据验证规则等。）

(c) Explain what a **data dictionary** is and state **two** items of information it contains. [2 marks]

（中文提示：解释什么是数据字典并说明它包含的两项信息。数据字典存储关于数据库结构的元数据。）

---

## Question 9 [6 marks]

A many-to-many relationship exists between students and courses — a student can take many courses, and a course can have many students.

(a) Explain why a many-to-many relationship cannot be directly implemented in a relational database. [2 marks]

（中文提示：解释为什么多对多关系不能直接在关系数据库中实现。）

(b) Show how you would resolve the many-to-many relationship between STUDENT and COURSE by creating a suitable intermediate table. Write out the table structures, showing primary keys and foreign keys. [4 marks]

（中文提示：通过创建中间表来解决STUDENT和COURSE之间的多对多关系。写出表结构，标明主键和外键。中间表通常包含两个外键，组成复合主键。）

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

（中文提示：逐行描述这个查询的功能。SELECT选择列，FROM指定表，JOIN连接表，GROUP BY分组，HAVING过滤分组，ORDER BY排序。）

(b) Explain the difference between the **WHERE** clause and the **HAVING** clause in SQL. [3 marks]

（中文提示：解释SQL中WHERE子句和HAVING子句的区别。WHERE在分组前过滤行，HAVING在分组后过滤组。）

---

**--- END OF HOMEWORK ---**

Total: 60 marks
