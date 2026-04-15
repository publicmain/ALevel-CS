# Databases (AS Level) - Paper 1 Mark Scheme Answers

> Topics: Relational databases, SQL, normalisation, DBMS features, entity-relationship diagrams, DDL/DML

---

## 2024 May/June (9618/12)

### Question 4

(a) Identify the relationship between EXAM and EXAM_QUESTION. [1 mark]

✓ **One-to-many** (one EXAM can have many EXAM_QUESTIONs)

> 提示：一对多关系 - 一个考试(EXAM)包含多个考题(EXAM_QUESTION)

---

(b) Write an SQL script to define the table EXAM. [3 marks]

```sql
CREATE TABLE EXAM
(
    ExamID      VARCHAR(8) NOT NULL,
    Subject     VARCHAR(20) NOT NULL,
    Level       INTEGER NOT NULL,
    TotalMarks  INTEGER NOT NULL,
    PRIMARY KEY (ExamID)
);
```

✓ Correct CREATE TABLE syntax with table name EXAM
✓ Appropriate data types for each field (VARCHAR for ExamID/Subject, INTEGER for Level/TotalMarks)
✓ PRIMARY KEY defined for ExamID

> 提示：CREATE TABLE语法 - 表名、字段名+数据类型+约束、主键定义。注意ExamID是字符串（如00956124带前导零）

---

(c) Write an SQL script to update EXAM_QUESTION and link the foreign key to EXAM. [2 marks]

```sql
ALTER TABLE EXAM_QUESTION
ADD FOREIGN KEY (ExamID) REFERENCES EXAM(ExamID);
```

✓ Correct ALTER TABLE statement with EXAM_QUESTION
✓ Correct FOREIGN KEY ... REFERENCES syntax linking ExamID to EXAM(ExamID)

> 提示：ALTER TABLE添加外键 - ADD FOREIGN KEY (外键字段) REFERENCES 被引用表(主键字段)

---

(d) Describe the additional tables needed and explain how all tables will be linked. [5 marks]

✓ A **STUDENT** table is needed to store data about each student, e.g. STUDENT(StudentID, FirstName, LastName, ...) with StudentID as the primary key

✓ A **STUDENT_EXAM** (or ENROLMENT) table is needed to link students to exams, e.g. STUDENT_EXAM(StudentExamID, StudentID, ExamID) -- this resolves the many-to-many relationship between students and exams

✓ A **STUDENT_ANSWER** (or MARK) table is needed to store the marks each student achieved in each question, e.g. STUDENT_ANSWER(StudentAnswerID, StudentExamID, ExamQuestionID, MarkAwarded)

✓ STUDENT to STUDENT_EXAM is one-to-many (one student can take many exams), linked via StudentID as a foreign key
✓ EXAM to STUDENT_EXAM is one-to-many (one exam can be taken by many students), linked via ExamID as a foreign key
✓ EXAM_QUESTION to STUDENT_ANSWER is one-to-many, linked via ExamQuestionID as a foreign key

> 提示：需要STUDENT表（学生信息）、STUDENT_EXAM表（解决学生和考试的多对多关系）、STUDENT_ANSWER表（存储每个学生每道题的得分）。通过外键连接所有表。

*Any 5 valid points for 5 marks*

---

## 2024 Oct/Nov (9618/12)

### Question 6

(a) Explain the benefits of using a relational database instead of a file-based approach. [3 marks]

✓ **Reduced data redundancy** -- data is stored once and linked via relationships/foreign keys, rather than being duplicated across multiple files
✓ **Data consistency** -- since data is stored in one place, updates only need to be made once, reducing the risk of inconsistencies
✓ **Data integrity** -- referential integrity rules ensure that relationships between tables remain valid (e.g. cannot delete a record that is referenced by another table)
✓ **Easier data access** -- SQL can be used to query data across multiple related tables simultaneously
✓ **Security** -- access rights can be set at table/field level, giving better control over who can see or modify specific data

> 提示：关系数据库优势 - 减少数据冗余、保持数据一致性、维护参照完整性、SQL方便查询、细粒度安全控制

*Any 3 points for 3 marks*

---

(b)(i) Identify each relationship between the database tables and explain how each can be implemented. [6 marks]

✓ **CUSTOMER to JOB** -- one-to-many (one customer can have many repair jobs). Implemented by having CustomerID as a foreign key in the JOB table.

✓ **EMPLOYEE to LOGIN_DATA** -- one-to-one (each employee has one set of login data). Implemented by having EmployeeID as a foreign key in LOGIN_DATA (or the same primary key in both).

✓ **JOB to JOB_EMPLOYEE** -- one-to-many (one job can have many employees assigned). Implemented by having JobID as a foreign key in JOB_EMPLOYEE.

✓ **EMPLOYEE to JOB_EMPLOYEE** -- one-to-many (one employee can work on many jobs). Implemented by having EmployeeID as a foreign key in JOB_EMPLOYEE.

✓ JOB_EMPLOYEE is a **linking/junction table** that resolves the many-to-many relationship between JOB and EMPLOYEE.

> 提示：
> - CUSTOMER → JOB：一对多（CustomerID为JOB外键）
> - EMPLOYEE → LOGIN_DATA：一对一（EmployeeID为外键）
> - JOB → JOB_EMPLOYEE：一对多（JobID为外键）
> - EMPLOYEE → JOB_EMPLOYEE：一对多（EmployeeID为外键）
> - JOB_EMPLOYEE是连接表，解决JOB和EMPLOYEE的多对多关系

*1 mark per relationship identified + 1 mark per implementation explanation. 6 marks total.*

---

(b)(ii) Write an SQL script to return the total amount of all invoices sent in 2023 that have been paid. [3 marks]

```sql
SELECT SUM(Amount) AS TotalAmount
FROM INVOICE
WHERE DateSent >= #01/01/2023# AND DateSent <= #31/12/2023#
AND Paid = 'Y';
```

✓ Correct use of SUM(Amount) aggregate function
✓ Correct WHERE clause filtering for the year 2023 (DateSent between 01/01/2023 and 31/12/2023)
✓ Correct filtering for paid invoices (Paid = 'Y')

> 提示：用SUM聚合函数求总金额，WHERE筛选2023年日期范围且已支付(Paid='Y')

**Working:** Invoices matching: 29262 (105.20, Y, 12/12/2023) + 26765 (200.00, Y, 11/11/2023) = **305.20**

---

## 2023 May/June (9618/12)

### Question 2

(a) Complete the table of DBMS features and tools. [4 marks]

| Name | Description |
|------|-------------|
| Data dictionary | ✓ A file/repository that stores metadata about the database, such as table names, field names, data types, constraints, relationships and validation rules |
| Query processor | ✓ A component that interprets/translates SQL queries and retrieves/manipulates the requested data from the database |
| ✓ **Conceptual data model** (or conceptual schema) | A model of a database that is not specific to one DBMS |
| ✓ **Developer interface** (or DBMS tools / design tools) | A software tool that allows the user to create items such as tables, forms and reports |

> 提示：数据字典=存储数据库元数据；查询处理器=解释执行SQL查询；概念数据模型=不特定于某DBMS的数据库模型；开发者界面/工具=允许创建表、表单、报告

---

(b) Explain the reasons why referential integrity is important in a database. [3 marks]

✓ Referential integrity ensures that relationships between tables remain valid/consistent
✓ It prevents orphan records -- a foreign key value in one table must match an existing primary key value in the related table (or be null)
✓ It prevents the deletion of a record in a primary table if there are related records in another table that reference it
✓ It ensures the database remains accurate and meaningful -- data cannot become inconsistent through invalid references

> 提示：参照完整性 - 确保表间关系有效、防止孤立记录（外键必须对应有效主键）、防止删除被引用的记录、保持数据一致性

*Any 3 points for 3 marks*

---

(c)(i) Describe two methods of validating the field RiderLevel. [2 marks]

✓ **Presence check** -- checks that the RiderLevel field is not left empty / a value has been entered
✓ **Lookup check / list check** -- checks that the value entered is one of the predefined acceptable values: Beginner, Intermediate or Advanced
✓ **Length check** -- checks that the number of characters entered is within an acceptable range

> 提示：验证RiderLevel - 存在性检查（不能为空）、查找检查/列表检查（必须是Beginner/Intermediate/Advanced之一）

*Any 2 for 2 marks*

---

(c)(ii) Write an SQL script to return the names of all horses that have the horse level intermediate or beginner. [4 marks]

```sql
SELECT Name
FROM HORSE
WHERE HorseLevel = 'Intermediate' OR HorseLevel = 'Beginner';
```

✓ Correct SELECT with Name field
✓ Correct FROM HORSE table
✓ Correct WHERE clause with HorseLevel conditions
✓ Correct use of OR to combine conditions / string values in quotes

> 提示：SELECT字段 FROM表 WHERE条件；用OR连接多个条件；字符串值加引号

*Alternative:* `WHERE HorseLevel IN ('Intermediate', 'Beginner')`

---

(c)(iii) There are four errors in the SQL script. Identify and correct each error. [4 marks]

Original:
```sql
SELECT SUM(STUDENT.RiderLevel) AS NumberOfRiders
FROM STUDENT, LESSON
WHERE StudentID = StudentID
OR Date = #09/09/2023#
AND STUDENT.RiderLevel = Beginner;
```

**Error 1:**
✓ `SUM(STUDENT.RiderLevel)` should be `COUNT(STUDENT.RiderLevel)` (or `COUNT(*)`)
-- SUM adds values; COUNT counts the number of records

**Error 2:**
✓ `WHERE StudentID = StudentID` should be `WHERE STUDENT.StudentID = LESSON.StudentID`
-- Must use table prefixes to distinguish which table each StudentID belongs to (ambiguous reference)

**Error 3:**
✓ `OR Date = #09/09/2023#` should be `AND Date = #09/09/2023#`
-- OR would return all beginners regardless of date, or all records on that date regardless of level; AND is needed so both conditions must be true

**Error 4:**
✓ `STUDENT.RiderLevel = Beginner` should be `STUDENT.RiderLevel = 'Beginner'`
-- String/text values must be enclosed in quotation marks

> 提示：四个错误：
> 1. SUM改为COUNT（计数不是求和）
> 2. StudentID需加表名前缀区分（STUDENT.StudentID = LESSON.StudentID）
> 3. OR改为AND（两个条件都必须满足）
> 4. Beginner需加引号（'Beginner'是字符串）

Corrected script:
```sql
SELECT COUNT(STUDENT.RiderLevel) AS NumberOfRiders
FROM STUDENT, LESSON
WHERE STUDENT.StudentID = LESSON.StudentID
AND Date = #09/09/2023#
AND STUDENT.RiderLevel = 'Beginner';
```

---

## 2023 Oct/Nov (9618/12)

### Question 2

(a) State what is meant by the following terms in a relational database model. [3 marks]

✓ **Entity** -- a category/type of object or thing about which data is stored in the database (represented as a table), e.g. a person, product, event

✓ **Primary key** -- a field (or combination of fields) that uniquely identifies each record in a table / no two records can have the same primary key value

✓ **Referential integrity** -- ensures that a foreign key value in one table must match an existing primary key value in the related table, or be null / ensures relationships between tables are valid and consistent

> 提示：实体=存储数据的对象类别（表）；主键=唯一标识每条记录的字段；参照完整性=外键必须对应有效的主键值

---

(b) Describe other methods that a DBMS can use to improve the security of a database. [4 marks]

✓ **Access rights / authorisation levels** -- users are given specific permissions (read, write, delete) for specific tables or fields, restricting what they can access or modify
✓ **Encryption** -- data in the database is encrypted so it is unreadable if accessed without authorisation / without the decryption key
✓ **Database views** -- virtual tables are created to show only specific fields/records to certain users, hiding sensitive data
✓ **Audit trail / transaction log** -- all database operations are logged (who, what, when), enabling detection and investigation of unauthorised access

> 提示：DBMS安全 - 访问权限（读/写/删权限）、加密（未授权无法读取）、视图（隐藏敏感数据）、审计日志（记录所有操作）

*Any 4 points for 4 marks*

---

(c) Explain how to modify the table to put it into First Normal Form (1NF). [4 marks]

✓ The table is not in 1NF because the Subject and SubjectCode fields contain multiple values / repeating groups (e.g. "English, Maths, Computer Science")

✓ To convert to 1NF, remove the repeating groups so that each field contains only a single/atomic value

✓ Create a separate row for each subject-student combination, so each record contains only one subject and one subject code

✓ The resulting table would have more rows, with each row containing a single StudentName, DateOfBirth, TutorGroup, one Subject, and one SubjectCode

Example of 1NF:

| StudentName | DateOfBirth | TutorGroup | Subject | SubjectCode |
|-------------|-------------|------------|---------|-------------|
| Yuwei Chen | 01/09/2004 | SMH | English | EN |
| Yuwei Chen | 01/09/2004 | SMH | Maths | MA |
| Yuwei Chen | 01/09/2004 | SMH | Computer Science | CS |
| Claudia Raj | 23/02/2005 | JMB | Maths | MA |
| ... | ... | ... | ... | ... |

✓ A composite primary key would be needed, e.g. (StudentName, SubjectCode) to uniquely identify each record

> 提示：1NF要求每个字段只包含单一/原子值。原表Subject和SubjectCode含多个值（重复组），需拆分为每行只有一个科目。需要复合主键（如StudentName+SubjectCode）

---

## 2022 Oct/Nov (9618/12)

### Question 5

(a) The database is not in Third Normal Form (3NF). Explain how the database can be normalised to 3NF. [3 marks]

Current tables:
- OWNER(OwnerID, FirstName, TelephoneNo, **TreeID, TreePosition**)
- TREE(TreeID, ScientificName, MaxHeight, FastGrowing)

✓ The OWNER table is not in 1NF / has a problem because an owner could have multiple trees, meaning TreeID and TreePosition would be repeating groups (or there would be redundant owner data)

✓ A new linking table should be created to resolve the one-to-many (or many-to-many) relationship, e.g.:
**OWNER_TREE(OwnerTreeID, OwnerID, TreeID, TreePosition)**

✓ Remove TreeID and TreePosition from the OWNER table, so:
- OWNER(OwnerID, FirstName, TelephoneNo)
- OWNER_TREE(OwnerTreeID, OwnerID, TreeID, TreePosition)
- TREE(TreeID, ScientificName, MaxHeight, FastGrowing)

OwnerID in OWNER_TREE is a foreign key referencing OWNER; TreeID in OWNER_TREE is a foreign key referencing TREE.

> 提示：OWNER表中TreeID和TreePosition是重复组/部分依赖。创建新的连接表OWNER_TREE(OwnerTreeID, OwnerID, TreeID, TreePosition)，从OWNER中移除TreeID和TreePosition

---

(b) Write the SQL script to add a new record in the table TREE. [3 marks]

```sql
INSERT INTO TREE (TreeID, ScientificName, MaxHeight, FastGrowing)
VALUES ('LOW_1276', 'Salix_Alba', 30.00, TRUE);
```

✓ Correct INSERT INTO TREE syntax
✓ Correct field names listed
✓ Correct VALUES with appropriate data types (strings in quotes, numeric without quotes, boolean as TRUE)

> 提示：INSERT INTO 表名 (字段列表) VALUES (值列表)；字符串加引号，数字不加，布尔值用TRUE/FALSE

---

(c) State what is meant by a candidate key in a relational database. [1 mark]

✓ A candidate key is a field (or combination of fields) that could be chosen as the primary key because it uniquely identifies each record in the table / any attribute that could serve as a primary key

> 提示：候选键 = 可以被选为主键的字段，能唯一标识表中每条记录（表可以有多个候选键，选其中一个作为主键）

---

(d)(i) Describe, using an example, what is meant by a data dictionary. [2 marks]

✓ A data dictionary is a file/centralised repository that stores metadata (data about data) about the database structure
✓ For example, it stores information such as the field name (e.g. TreeID), data type (e.g. VARCHAR), field size (e.g. 8 characters), constraints (e.g. NOT NULL, PRIMARY KEY), validation rules, and relationships between tables

> 提示：数据字典 = 存储数据库元数据的文件/仓库，如字段名、数据类型、大小、约束、验证规则、表间关系等

---

(d)(ii) Describe what is meant by a logical schema. [2 marks]

✓ A logical schema is a description/model of the overall structure of the database as seen by the database designer/administrator
✓ It defines the tables, fields, data types, relationships, and constraints without specifying how the data is physically stored on disk / it is independent of the physical implementation

> 提示：逻辑模式 = 数据库整体结构的描述/模型，定义表、字段、关系、约束，不涉及物理存储细节

---

## 2021 May/June (9618/12)

### Question 1

(a) Give the definition of the following database terms, using an example from HOUSE_RENTALS. [6 marks]

| Term | Definition and example |
|------|----------------------|
| Field | ✓ A single item/piece of data / a column in a table / an attribute. ✓ Example: FirstName in the CUSTOMER table (or any other valid field) |
| Entity | ✓ A category of object about which data is stored / represented as a table in the database. ✓ Example: CUSTOMER, HOUSE, or RENTAL |
| Foreign key | ✓ A field in one table that links to / references the primary key of another table, creating a relationship between the tables. ✓ Example: CustomerID in the RENTAL table is a foreign key that references CustomerID (primary key) in the CUSTOMER table |

> 提示：
> - 字段(Field) = 单个数据项/表中的列，如CUSTOMER表中的FirstName
> - 实体(Entity) = 存储数据的对象类别/表，如CUSTOMER、HOUSE、RENTAL
> - 外键(Foreign Key) = 引用另一表主键的字段，如RENTAL中的CustomerID引用CUSTOMER的主键

*1 mark for each definition + 1 mark for each example = 6 marks*

---

(b) Is the database HOUSE_RENTALS in Third Normal Form (3NF)? Justify your choice. [2 marks]

✓ **Yes**, the database is in 3NF.

✓ Justification: All non-key attributes in each table are fully dependent on the primary key and only the primary key (no partial dependencies, no transitive dependencies). For example, in RENTAL, MonthlyCost and DepositPaid depend on RentalID (the primary key), not on CustomerID or HouseID independently. Each table represents a single entity with no repeating groups.

> 提示：是3NF。每个表中所有非键属性完全依赖于主键且仅依赖于主键，无部分依赖或传递依赖。每个表代表单一实体，无重复组。

---

(c)(i) Complete the DDL statement to define the table RENTAL. [4 marks]

```sql
CREATE TABLE RENTAL
(
    RentalID    INTEGER NOT NULL,
    CustomerID  INTEGER NOT NULL,
    HouseID     VARCHAR(5) NOT NULL,
    MonthlyCost REAL NOT NULL,
    DepositPaid BOOLEAN NOT NULL,
    PRIMARY KEY (RentalID)
);
```

The four blanks to fill in:

✓ Line 1: `CREATE TABLE RENTAL` (TABLE and RENTAL)
✓ HouseID line: `VARCHAR` (data type for HouseID -- it contains alphanumeric values like "15B5L")
✓ MonthlyCost line: `REAL` (or `DECIMAL` / `CURRENCY` -- numeric type with decimal places)
✓ Last line: `PRIMARY KEY` (defines the primary key)

> 提示：四个空：
> 1. CREATE TABLE RENTAL
> 2. HouseID的数据类型 = VARCHAR（含字母数字如15B5L）
> 3. MonthlyCost的数据类型 = REAL/DECIMAL（有小数）
> 4. PRIMARY KEY（定义主键）

---

(c)(ii) Write a DML script to return the first name and last name of all customers who have not paid their deposit. [4 marks]

```sql
SELECT CUSTOMER.FirstName, CUSTOMER.LastName
FROM CUSTOMER, RENTAL
WHERE CUSTOMER.CustomerID = RENTAL.CustomerID
AND RENTAL.DepositPaid = FALSE;
```

✓ Correct SELECT with FirstName and LastName fields
✓ Correct FROM with both CUSTOMER and RENTAL tables
✓ Correct JOIN condition: CUSTOMER.CustomerID = RENTAL.CustomerID
✓ Correct WHERE/AND condition: DepositPaid = FALSE (or = 'No')

> 提示：需要连接CUSTOMER和RENTAL两个表（通过CustomerID），筛选DepositPaid=FALSE的记录，返回FirstName和LastName

*Alternative using JOIN syntax:*
```sql
SELECT CUSTOMER.FirstName, CUSTOMER.LastName
FROM CUSTOMER
INNER JOIN RENTAL ON CUSTOMER.CustomerID = RENTAL.CustomerID
WHERE RENTAL.DepositPaid = FALSE;
```
