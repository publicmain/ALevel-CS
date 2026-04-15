# Chapter 10: Data Types & Structures - Homework Answers

> Total: 54 marks

---

### Question 1 [5 marks]

**(a)** Data types: [5]

| Value | Data Type |
|-------|-----------|
| The number of students in a class (e.g. 32) | INTEGER ✓ |
| A student's grade letter (e.g. 'A') | CHAR ✓ |
| Whether a user has logged in (e.g. TRUE) | BOOLEAN ✓ |
| The price of an item (e.g. 19.99) | REAL ✓ |
| A customer's full name (e.g. "Zhang Wei") | STRING ✓ |

**Mark scheme:** ✓ 1 mark for each correct data type

---

### Question 2 [6 marks]

**(a)** Record type definition and array declaration: [3]

```
TYPE StudentRecord                                     // ✓
    DECLARE StudentID : STRING
    DECLARE Name : STRING
    DECLARE Age : INTEGER                              // ✓
    DECLARE AverageScore : REAL
    DECLARE IsActive : BOOLEAN
ENDTYPE

DECLARE Students : ARRAY[1:200] OF StudentRecord       // ✓
```

**Mark scheme:**
- ✓ Correct TYPE ... ENDTYPE structure
- ✓ All five fields declared with correct data types
- ✓ Array declaration with correct size and type

**(b)** Assigning values to the first student: [2]

```
Students[1].StudentID ← "S00001"                       // ✓
Students[1].Name ← "Li Ming"
Students[1].Age ← 16
Students[1].AverageScore ← 85.5                        // ✓
Students[1].IsActive ← TRUE
```

**Mark scheme:**
- ✓ Correct dot notation to access record fields (e.g. `Students[1].Name`)
- ✓ All five fields assigned with correct values and types

**(c)** Output names of active students with average above 90: [1]

```
FOR i ← 1 TO 200                                      // ✓
    IF Students[i].IsActive = TRUE AND Students[i].AverageScore > 90 THEN
        OUTPUT Students[i].Name
    ENDIF
NEXT i
```

**Mark scheme:**
- ✓ Loop through array with correct condition checking both IsActive and AverageScore > 90, and outputting the Name

---

### Question 3 [6 marks]

**(a)** Two key characteristics of a stack: [2]

```
1. A stack is a Last-In, First-Out (LIFO) data structure — the last
   item added is the first item removed. ✓
2. Items can only be added (pushed) or removed (popped) from
   the top of the stack. ✓
```

**Mark scheme:**
- ✓ LIFO (Last In First Out) principle
- ✓ Access restricted to the top only / operations are push and pop

**(b)** Current value of `TopOfStack`: [1]

```
TopOfStack = 3 ✓
```

(Three items in the stack: 10 at index 1, 25 at index 2, 7 at index 3)

**(c)** Stack operations trace: [3]

| Operation | Stack contents (bottom → top) | TopOfStack |
|-----------|-------------------------------|------------|
| Initial   | 10, 25, 7                     | 3          |
| PUSH(15)  | 10, 25, 7, 15                 | 4  ✓       |
| POP()     | 10, 25, 7                     | 3  ✓       |
| POP()     | 10, 25                        | 2          |
| PUSH(42)  | 10, 25, 42                    | 3  ✓       |

**Mark scheme:**
- ✓ PUSH(15): correctly adds 15, TopOfStack = 4
- ✓ Two POP operations correctly remove items in LIFO order
- ✓ PUSH(42): correctly adds 42 on top, TopOfStack = 3

---

### Question 4 [6 marks]

**(a)** Push procedure: [3]

```
PROCEDURE Push(Value : INTEGER)
    IF Top >= 100 THEN                                 // ✓
        OUTPUT "Error: Stack overflow - stack is full"  // ✓
    ELSE
        Top ← Top + 1                                  // ✓
        Stack[Top] ← Value
    ENDIF
ENDPROCEDURE
```

**Mark scheme:**
- ✓ Check for stack overflow (Top >= 100)
- ✓ Output error message when full
- ✓ Increment Top then store value at Stack[Top]

**(b)** Pop function: [3]

```
FUNCTION Pop() RETURNS INTEGER
    DECLARE Value : INTEGER
    IF Top = 0 THEN                                    // ✓
        OUTPUT "Error: Stack underflow - stack is empty" // ✓
        RETURN -1
    ELSE
        Value ← Stack[Top]                              // ✓
        Top ← Top - 1
        RETURN Value
    ENDIF
ENDFUNCTION
```

**Mark scheme:**
- ✓ Check for stack underflow (Top = 0)
- ✓ Output error / return -1 when empty
- ✓ Store top value, decrement Top, return the value

---

### Question 5 [5 marks]

**(a)** Difference between stack and queue: [2]

```
A stack uses LIFO (Last In First Out) — items are added and removed
from the same end (the top). ✓
A queue uses FIFO (First In First Out) — items are added at the rear
and removed from the front. ✓
```

**Mark scheme:**
- ✓ Stack: LIFO — added and removed from the same end
- ✓ Queue: FIFO — added at rear, removed from front

**(b)** Circular queue operations: [3]

| Operation | Front | Rear | Size | Queue[0] | Queue[1] | Queue[2] | Queue[3] | Queue[4] | Queue[5] |
|-----------|-------|------|------|----------|----------|----------|----------|----------|----------|
| Initial   | 2     | 4    | 3    |          |          | A        | B        | C        |          |
| Enqueue('D') | 2  | 5    | 4    |          |          | A        | B        | C        | D   ✓    |
| Dequeue() | 3     | 5    | 3    |          |          |          | B        | C        | D   ✓    |
| Enqueue('E') | 3  | 0    | 4    | E        |          |          | B        | C        | D   ✓    |

**Mark scheme:**
- ✓ Enqueue('D'): Rear = (4+1) MOD 6 = 5, D placed at index 5, Size = 4
- ✓ Dequeue(): removes A from index 2, Front = (2+1) MOD 6 = 3, Size = 3
- ✓ Enqueue('E'): Rear = (5+1) MOD 6 = 0 (wraps around), E placed at index 0, Size = 4

---

### Question 6 [5 marks]

**(a)** Linked list diagram: [2]

```
Start
  │
  ▼
┌──────┬───┐    ┌──────┬───┐    ┌──────┬──────┐
│ "Cat"│  ─┼───►│ "Dog"│  ─┼───►│"Fish"│ NULL │    ✓ ✓
└──────┴───┘    └──────┴───┘    └──────┴──────┘
```

**Mark scheme:**
- ✓ Each node shown with data field and pointer field, linked in correct order
- ✓ Start pointer pointing to first node, and NULL pointer at the end of the list

**(b)** Steps to insert "Bird" at the beginning: [3]

```
1. Create a new node and store "Bird" in its data field. ✓
2. Set the pointer of the new node to point to the current
   first node ("Cat") — i.e., the address that Start currently
   holds. ✓
3. Update the Start pointer to point to the new node ("Bird"). ✓
```

**Mark scheme:**
- ✓ Create a new node with data "Bird"
- ✓ Set the new node's pointer to the current Start (first node)
- ✓ Update Start pointer to point to the new node

---

### Question 7 [6 marks]

**(a)** Read names from file into array: [4]

```
DECLARE Names : ARRAY[1:500] OF STRING
DECLARE Count : INTEGER
Count ← 0

OPENFILE "students.txt" FOR READ                       // ✓
WHILE NOT EOF("students.txt") DO                       // ✓
    Count ← Count + 1                                  // ✓
    READFILE "students.txt", Names[Count]               // ✓
ENDWHILE
CLOSEFILE "students.txt"
```

**Mark scheme:**
- ✓ Open file for reading
- ✓ Loop until end of file (EOF)
- ✓ Increment Count for each name read
- ✓ Read each line into the array at the correct index, then close file

**(b)** Append three new names to the file: [2]

```
OPENFILE "students.txt" FOR APPEND                     // ✓
FOR i ← 1 TO 3
    DECLARE NewName : STRING
    INPUT NewName
    WRITEFILE "students.txt", NewName                   // ✓
NEXT i
CLOSEFILE "students.txt"
```

**Mark scheme:**
- ✓ Open file in APPEND mode
- ✓ Loop 3 times, input a name and write it to the file, then close

---

### Question 8 [5 marks]

**(a)** Definition of abstract data type (ADT): [2]

```
An abstract data type is a data type defined by the user/programmer  ✓
that describes a collection of data and the operations that can be
performed on that data, without specifying how the data is stored
or how the operations are implemented.  ✓
```

**Mark scheme:**
- ✓ A data type described in terms of the data it stores and the operations on that data
- ✓ Implementation details are hidden / independent of implementation

**(b)** Real-world applications: [3]

| ADT | Application | Justification |
|-----|-------------|---------------|
| Stack | Browser back button / Undo feature in a text editor | The most recently visited page / most recent action needs to be accessed first (LIFO behaviour). ✓ |
| Queue | Print queue / customer service call queue | Documents / customers are processed in the order they arrive (FIFO behaviour). ✓ |
| Linked List | Music playlist / image viewer | Items can be easily inserted or removed at any position without shifting other elements, and the list can grow dynamically. ✓ |

**Mark scheme:** ✓ 1 mark for each valid application with correct justification that relates to the ADT's characteristics

---

### Question 9 [4 marks]

**(a)** Contents of `Grid` after the nested loops: [2]

|       | Col 1 | Col 2 | Col 3 |
|-------|-------|-------|-------|
| Row 1 |   1   |   2   |   3   |
| Row 2 |   2   |   4   |   6   |
| Row 3 |   3   |   6   |   9   |
| Row 4 |   4   |   8   |  12   |

✓ ✓

(Each cell = Row * Col)

**Mark scheme:**
- ✓ First two rows correct
- ✓ Last two rows correct

**(b)** Value of `Total` output: [2]

```
The second loop sums Grid[Row, 2] for Row = 1 to 4:  ✓
Total = Grid[1,2] + Grid[2,2] + Grid[3,2] + Grid[4,2]
Total = 2 + 4 + 6 + 8
Total = 20  ✓
```

**Mark scheme:**
- ✓ Correct identification that column 2 is being summed (show working)
- ✓ Correct final answer: 20

---

### Question 10 [6 marks]

```
PROCEDURE Enqueue(Name : STRING)
    IF QueueSize >= 50 THEN                            // ✓
        OUTPUT "Error: Queue is full"                   // ✓
    ELSE
        Rear ← Rear + 1                                // ✓
        PatientQueue[Rear] ← Name
        QueueSize ← QueueSize + 1
    ENDIF
ENDPROCEDURE

FUNCTION Dequeue() RETURNS STRING
    DECLARE Value : STRING
    IF QueueSize = 0 THEN                              // ✓
        OUTPUT "Error: Queue is empty"                  // ✓
        RETURN ""
    ELSE
        Value ← PatientQueue[Front]
        Front ← Front + 1                              // ✓
        QueueSize ← QueueSize - 1
        RETURN Value
    ENDIF
ENDFUNCTION
```

**Mark scheme:**
- ✓ Enqueue: check if queue is full (QueueSize >= 50)
- ✓ Enqueue: output error message when full
- ✓ Enqueue: increment Rear and store Name, increment QueueSize
- ✓ Dequeue: check if queue is empty (QueueSize = 0)
- ✓ Dequeue: output error / return empty when empty
- ✓ Dequeue: retrieve value from Front, increment Front, decrement QueueSize, return value

---

**--- End of Answers ---**

**Total: 54 marks**
