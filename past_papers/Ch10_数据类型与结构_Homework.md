# Chapter 10: Data Types & Structures - 课后作业 Homework

> 姓名：__________ 日期：__________ 总分：__/54

---

## Pseudocode Syntax Reference (伪代码语法参考)

```
DECLARE x : INTEGER / REAL / CHAR / STRING / BOOLEAN
DECLARE Arr : ARRAY[1:n] OF DataType
DECLARE Arr2D : ARRAY[1:r, 1:c] OF DataType
TYPE RecordName
    DECLARE field1 : DataType
    DECLARE field2 : DataType
ENDTYPE
```

---

### Question 1 [5 marks]

**(a)** State the most appropriate data type for each of the following values. Choose from: `INTEGER`, `REAL`, `CHAR`, `STRING`, `BOOLEAN`. [5]

> 中文提示：选择最合适的数据类型。INTEGER=整数，REAL=小数，CHAR=单个字符，STRING=字符串，BOOLEAN=真/假。

| Value | Data Type |
|-------|-----------|
| The number of students in a class (e.g. 32) | |
| A student's grade letter (e.g. 'A') | |
| Whether a user has logged in (e.g. TRUE) | |
| The price of an item (e.g. 19.99) | |
| A customer's full name (e.g. "Zhang Wei") | |

---

### Question 2 [6 marks]

A school stores data about 200 students using a **record** structure. Each student record contains:
- `StudentID` (a 6-character string, e.g. "S00142")
- `Name` (a string)
- `Age` (an integer)
- `AverageScore` (a real number)
- `IsActive` (a Boolean)

**(a)** Write pseudocode to define the record type `StudentRecord` and declare an array `Students` of 200 such records. [3]

> 中文提示：先用TYPE...ENDTYPE定义记录类型，再用DECLARE声明一个包含200个记录的数组。

```
TYPE StudentRecord




ENDTYPE

DECLARE Students : ___________________________________
```

**(b)** Write pseudocode to assign the following values to the first student in the array: StudentID = "S00001", Name = "Li Ming", Age = 16, AverageScore = 85.5, IsActive = TRUE. [2]

> 中文提示：用点号(.)访问记录的字段，例如 Students[1].Name

```





```

**(c)** Write pseudocode to output the names of all active students whose average score is above 90. [1]

```




```

---

### Question 3 [6 marks]

A **stack** is an abstract data type (ADT).

**(a)** Describe two key characteristics of a stack. [2]

> 中文提示：栈的特点——后进先出(LIFO)，只能从顶部操作。

```



```

**(b)** A stack is implemented using an array `Stack[1:8]` and a variable `TopOfStack` that points to the top element. The stack currently contains the following data (bottom to top): `10, 25, 7`

State the current value of `TopOfStack`. [1]

```

```

**(c)** Show the state of the stack and the value of `TopOfStack` after each of the following operations are performed **in sequence**: [3]

1. `PUSH(15)`
2. `POP()`
3. `POP()`
4. `PUSH(42)`

> 中文提示：PUSH=入栈（放到顶部），POP=出栈（从顶部移除）。逐步画出每次操作后栈的状态。

| Operation | Stack contents (bottom → top) | TopOfStack |
|-----------|-------------------------------|------------|
| Initial   | 10, 25, 7                     |            |
| PUSH(15)  |                               |            |
| POP()     |                               |            |
| POP()     |                               |            |
| PUSH(42)  |                               |            |

---

### Question 4 [6 marks]

Write pseudocode for a **stack** implementation using a global array `Stack[1:100]` of type INTEGER and a global variable `Top` of type INTEGER (initially 0).

**(a)** Write a **procedure** `Push(Value : INTEGER)` that adds a value to the stack. The procedure should check for stack overflow (stack full) and output an error message if the stack is full. [3]

> 中文提示：入栈操作——先检查Top是否等于100（满了），如果没满则Top加1，然后把值放在Stack[Top]。

```
PROCEDURE Push(Value : INTEGER)





ENDPROCEDURE
```

**(b)** Write a **function** `Pop()` that removes and returns the top value from the stack. The function should check for stack underflow (stack empty) and return `-1` if the stack is empty. [3]

> 中文提示：出栈操作——先检查Top是否等于0（空了），如果不为空则取出Stack[Top]的值，Top减1，返回取出的值。

```
FUNCTION Pop() RETURNS INTEGER






ENDFUNCTION
```

---

### Question 5 [5 marks]

A **queue** is another abstract data type.

**(a)** State the difference between how items are added and removed in a stack compared to a queue. [2]

> 中文提示：栈是LIFO（后进先出），队列是FIFO（先进先出）。栈从同一端进出，队列从一端进、另一端出。

```



```

**(b)** A circular queue is implemented using an array `Queue[0:5]` (6 elements), with `Front = 2`, `Rear = 4`, and `Size = 3`. The current queue contents are:

| Index | 0 | 1 | 2 | 3 | 4 | 5 |
|-------|---|---|---|---|---|---|
| Value |   |   | A | B | C |   |

Show the state of the queue (including `Front`, `Rear`, and `Size`) after each of the following operations performed **in sequence**: [3]

1. `Enqueue('D')`
2. `Dequeue()`
3. `Enqueue('E')`

> 中文提示：环形队列——Rear指向下一个插入位置的前一个（或当前最后元素），Front指向第一个元素。入队时Rear移动，出队时Front移动。注意取模运算实现循环。

| Operation | Front | Rear | Size | Queue[0] | Queue[1] | Queue[2] | Queue[3] | Queue[4] | Queue[5] |
|-----------|-------|------|------|----------|----------|----------|----------|----------|----------|
| Initial   | 2     | 4    | 3    |          |          | A        | B        | C        |          |
| Enqueue('D') |    |      |      |          |          |          |          |          |          |
| Dequeue() |       |      |      |          |          |          |          |          |          |
| Enqueue('E') |    |      |      |          |          |          |          |          |          |

---

### Question 6 [5 marks]

A **linked list** stores data items where each node contains a data value and a pointer to the next node.

**(a)** Draw a diagram of a linked list containing the values `"Cat"`, `"Dog"`, `"Fish"` in that order. Include a `Start` pointer and show the null pointer at the end. [2]

> 中文提示：链表图——每个节点画成两格（数据|指针），用箭头指向下一个节点，最后一个节点指针为null。

```




```

**(b)** Describe the steps needed to insert a new node with value `"Bird"` at the **beginning** of the linked list from part (a). [3]

> 中文提示：在链表头部插入——创建新节点，将新节点的指针指向当前第一个节点，然后更新Start指针指向新节点。

```





```

---

### Question 7 [6 marks]

A program needs to read data from a text file and store it.

The file `students.txt` contains one student name per line. There are no more than 500 students.

**(a)** Write pseudocode to read all names from the file `students.txt` into a 1D array `Names[1:500]`, counting how many names were read into a variable `Count`. [4]

> 中文提示：文件读取——用OPENFILE打开，用WHILE NOT EOF循环读取每一行（READFILE），存入数组并计数，最后CLOSEFILE。

```
DECLARE Names : ARRAY[1:500] OF STRING
DECLARE Count : INTEGER
Count ← 0








```

**(b)** Write pseudocode to **append** three new names entered by the user to the end of the file `students.txt`. [2]

> 中文提示：追加写入——用OPENFILE("students.txt", APPEND)打开文件，用循环INPUT三个名字并WRITEFILE写入，最后CLOSEFILE。

```






```

---

### Question 8 [5 marks]

**(a)** Define the term **abstract data type (ADT)**. [2]

> 中文提示：抽象数据类型——描述数据的逻辑结构和可以执行的操作，不涉及具体实现方式。

```



```

**(b)** A stack, a queue, and a linked list are all examples of ADTs. For each one, give **one** real-world application where it would be the most appropriate data structure to use. Justify each choice. [3]

> 中文提示：每种数据结构举一个实际应用场景，并解释为什么这种结构最合适。

| ADT | Application | Justification |
|-----|-------------|---------------|
| Stack | | |
| Queue | | |
| Linked List | | |

---

### Question 9 [4 marks]

Study the following pseudocode:

```
DECLARE Grid : ARRAY[1:4, 1:3] OF INTEGER
DECLARE Total : INTEGER
Total ← 0

FOR Row ← 1 TO 4
    FOR Col ← 1 TO 3
        Grid[Row, Col] ← Row * Col
    NEXT Col
NEXT Row

FOR Row ← 1 TO 4
    Total ← Total + Grid[Row, 2]
NEXT Row

OUTPUT Total
```

**(a)** Complete the table below showing the contents of `Grid` after the first pair of nested loops has executed. [2]

> 中文提示：二维数组——Grid[Row, Col] = Row * Col。填入每个位置的计算结果。

|       | Col 1 | Col 2 | Col 3 |
|-------|-------|-------|-------|
| Row 1 |       |       |       |
| Row 2 |       |       |       |
| Row 3 |       |       |       |
| Row 4 |       |       |       |

**(b)** State the value of `Total` that is output. Show your working. [2]

```



```

---

### Question 10 [6 marks]

A hospital maintains a patient queue system. Patients are added to the queue when they arrive, and the next patient is called from the front of the queue.

Write pseudocode for a queue implementation using:
- A global array `PatientQueue[1:50]` of type STRING
- Global variables `Front`, `Rear`, and `QueueSize`, all of type INTEGER

Write a **procedure** `Enqueue(Name : STRING)` and a **function** `Dequeue() RETURNS STRING`.

- `Enqueue` should check if the queue is full before adding
- `Dequeue` should check if the queue is empty before removing
- Implement as a **linear queue** (not circular)

> 中文提示：入队——检查Rear是否等于50，没满则Rear+1并把Name放在PatientQueue[Rear]，QueueSize+1。出队——检查QueueSize是否为0，不为空则取出PatientQueue[Front]，Front+1，QueueSize-1。

```
PROCEDURE Enqueue(Name : STRING)






ENDPROCEDURE

FUNCTION Dequeue() RETURNS STRING







ENDFUNCTION
```

[6]

---

**--- End of Homework ---**

**Total: 54 marks**

> 提交提醒：请确保所有伪代码使用Cambridge 9618规范的语法格式。记录类型用TYPE...ENDTYPE定义，文件操作用OPENFILE/READFILE/WRITEFILE/CLOSEFILE。
