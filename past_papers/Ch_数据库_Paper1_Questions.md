# Databases (AS Level) - Paper 1 Past Questions

> Topics: Relational databases, SQL, normalisation, DBMS features, entity-relationship diagrams, DDL/DML
> Note: Database questions appear in every Paper 1 exam and form a significant portion of marks.

---

## 2024 May/June (9618/12)

### Question 4
An assessment board wants to store the marks students achieved in exams in a database named RECORDS.

Part of the database design includes these two tables:
- EXAM(ExamID, Subject, Level, TotalMarks)
- EXAM_QUESTION(ExamQuestionID, ExamID, QuestionNumber, Question, MaxMark)

Sample data for EXAM:

| ExamID | Subject | Level | TotalMarks |
|--------|---------|-------|------------|
| 00956124 | Computer Science | 2 | 75 |
| 00956125 | Computer Science | 3 | 120 |
| 00956126 | Mathematics | 2 | 100 |
| 00956127 | Mathematics | 3 | 150 |
| 00956128 | Physics | 2 | 70 |
| 00956129 | Physics | 3 | 80 |

(a) Identify the relationship between EXAM and EXAM_QUESTION.
[1 mark]

(b) Write a Structured Query Language (SQL) script to define the table EXAM.
[3 marks]

(c) The table EXAM_QUESTION has been created but the foreign key has not been linked.
Write an SQL script to update EXAM_QUESTION and link the foreign key to EXAM.
[2 marks]

(d) The database also needs to store data about the students, the exams the students have taken and the marks the students achieved in each question of each exam.
Describe the additional tables that will need to be included in the database and explain how all the tables in the database will be linked.
[5 marks]

---

## 2024 Oct/Nov (9618/12)

### Question 6
A company uses a relational database to store data about its customers, employees and the individual repair jobs that customers have booked.

(a) Explain the benefits of using a relational database instead of a file-based approach.
[3 marks]

(b) The company decides which employees will work on each repair job. An employee can log into the database to access information about their repair jobs.

The database is normalised and includes these tables:
- CUSTOMER stores personal data about each customer
- EMPLOYEE stores personal data about each employee
- LOGIN_DATA stores the username and password for each employee
- JOB stores the data about each repair job
- JOB_EMPLOYEE stores the employees that are working on each repair job.

(i) Identify each relationship between the database tables and explain how each relationship can be implemented in the normalised database.
[6 marks]

(ii) The database also has the table INVOICE that stores data about each invoice that is sent to a customer.

Example data from the table INVOICE:

| InvoiceID | DateSent | Amount | Paid | JobID |
|-----------|----------|--------|------|-------|
| 29262 | 12/12/2023 | 105.20 | Y | 221 |
| 26765 | 11/11/2023 | 200.00 | Y | 315 |
| 13290 | 02/01/2024 | 50.00 | Y | 315 |
| 34090 | 05/02/2024 | 25.95 | N | 569 |

Write a Structured Query Language (SQL) script to return the total amount of all the invoices sent in the year 2023 that have been paid.
[3 marks]

---

## 2023 May/June (9618/12)

### Question 2
A horse riding school uses a database, Lessons, to store data about lesson bookings. This database is created and managed using a Database Management System (DBMS).

(a) The table contains names and descriptions of DBMS features and tools.
Complete the table by writing down the missing names and descriptions.

| Name | Description |
|------|-------------|
| Data dictionary | .................... |
| Query processor | .................... |
| .................... | A model of a database that is not specific to one DBMS. |
| .................... | A software tool that allows the user to create items such as tables, forms and reports. |

[4 marks]

(b) Explain the reasons why referential integrity is important in a database.
[3 marks]

(c) The database Lessons has the following tables:
- HORSE(HorseID, Name, Height, Age, HorseLevel)
- STUDENT(StudentID, FirstName, LastName, RiderLevel, PreferredHorseID)
- LESSON(LessonID, Date, Time, StudentID, HorseID, LessonContent)

The fields RiderLevel and HorseLevel can only have the values: Beginner, Intermediate or Advanced.

(i) Describe two methods of validating the field RiderLevel.
[2 marks]

(ii) Write a Structured Query Language (SQL) script to return the names of all the horses that have the horse level intermediate or beginner.
[4 marks]

(iii) The following SQL script should return the number of riders that have the rider level beginner and have a lesson booked on 09/09/2023.

```sql
SELECT SUM(STUDENT.RiderLevel) AS NumberOfRiders
FROM STUDENT, LESSON
WHERE StudentID = StudentID
OR Date = #09/09/2023#
AND STUDENT.RiderLevel = Beginner;
```

There are four errors in the script. Identify and correct each error.
[4 marks]

---

## 2023 Oct/Nov (9618/12)

### Question 2
(a) State what is meant by the following terms in a relational database model.
- Entity
- Primary key
- Referential integrity
[3 marks]

(b) Authentication is one method a Database Management System (DBMS) can use to improve the security of a database.
Describe other methods that a DBMS can use to improve the security of a database.
[4 marks]

(c) The following database table is not normalised.

| StudentName | DateOfBirth | TutorGroup | Subject | SubjectCode |
|-------------|-------------|------------|---------|-------------|
| Yuwei Chen | 01/09/2004 | SMH | English, Maths, Computer Science | EN, MA, CS |
| Claudia Raj | 23/02/2005 | JMB | Maths, Physics, Art | MA, PY, AR |
| Aamil Akram | 24/01/2005 | KMB | Art, Design, English language | AR, DE, EN |
| Areeba Faraz | 21/12/2004 | SMH | English language, Chemistry, Design | EN, CH, DE |

Explain how to modify the table to put it into First Normal Form (1NF).
[4 marks]

---

## 2022 Oct/Nov (9618/12)

### Question 5
A relational database, GARDEN, has the following tables:
- OWNER(OwnerID, FirstName, TelephoneNo, TreeID, TreePosition)
- TREE(TreeID, ScientificName, MaxHeight, FastGrowing)

(a) The database is not in Third Normal Form (3NF).
Explain how the database can be normalised to 3NF.
[3 marks]

(b) Write the Structured Query Language (SQL) script to add a new record in the table TREE to store the following data:

| Attribute | Value |
|-----------|-------|
| TreeID | LOW_1276 |
| ScientificName | Salix_Alba |
| MaxHeight | 30.00 |
| FastGrowing | TRUE |

[3 marks]

(c) State what is meant by a candidate key in a relational database.
[1 mark]

(d) (i) Describe, using an example, what is meant by a data dictionary.
[2 marks]

(ii) Describe what is meant by a logical schema.
[2 marks]

---

## 2021 May/June (9618/12)

### Question 1
Raj owns houses that other people rent from him. He has a database, HOUSE_RENTALS, with the following structure:
- CUSTOMER(CustomerID, FirstName, LastName, DateOfBirth, Email)
- HOUSE(HouseID, HouseNumber, Road, Town, Bedrooms, Bathrooms)
- RENTAL(RentalID, CustomerID, HouseID, MonthlyCost, DepositPaid)

(a) Give the definition of the following database terms, using an example from the database HOUSE_RENTALS for each definition.

| Term | Definition and example |
|------|----------------------|
| Field | |
| Entity | |
| Foreign key | |

[6 marks]

(b) Tick one box to identify whether the database HOUSE_RENTALS is in Third Normal Form (3NF) or not in 3NF.
Justify your choice using one or more examples from the database HOUSE_RENTALS.
[2 marks]

(c) Example data from the table RENTAL:

| RentalID | CustomerID | HouseID | MonthlyCost | DepositPaid |
|----------|------------|---------|-------------|-------------|
| 1 | 22 | 15B5L | 1000.00 | Yes |
| 2 | 13 | 3F | 687.00 | No |
| 3 | 1 | 12AB | 550.00 | Yes |
| 4 | 3 | 37 | 444.50 | Yes |

(i) Complete the following Data Definition Language (DDL) statement to define the table RENTAL.

```sql
.................... ....................
CREATE (
    RentalID INTEGER NOT NULL,
    CustomerID INTEGER NOT NULL,
    ....................
    HouseID (5) NOT NULL,
    ....................
    MonthlyCost NOT NULL,
    DepositPaid BOOLEAN NOT NULL,
    ....................
    (RentalID)
);
```
[4 marks]

(ii) Write a Data Manipulation Language (DML) script to return the first name and last name of all customers who have not paid their deposit.
[4 marks]
