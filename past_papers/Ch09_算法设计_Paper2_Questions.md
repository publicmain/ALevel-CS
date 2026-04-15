# Chapter 9: Algorithm Design & Problem-solving - Paper 2 Past Questions

This file covers: pseudocode, flowcharts, algorithm design, trace tables, state-transition diagrams, structure charts.

---

## 2024 May/June (9618/22)

### Question 2
A program is being developed.

**(a)** An algorithm for part of the program will:
- input three numeric values and assign them to identifiers Num1, Num2 and Num3
- assign the largest value to variable Ans
- output a message giving the largest value and the average of the three numeric values.

Assume the values are all different and are input in no particular order.

Complete the program flowchart on page 5 to represent the algorithm.

(The flowchart shows: START -> INPUT Num1, Num2, Num3 -> [decision boxes] -> END)

**[5 marks]**

**(b)** A different part of the program contains an algorithm represented by the following program flowchart:

START -> Set Flag to GetStat() -> Is Flag = TRUE? (Yes -> END) (No -> Set Port to 1) -> Is Port = 4? (No -> CALL Reset(Port) -> Set Port to Port + 1 [loop back]) (Yes -> [end loop])

Write pseudocode for the algorithm.

**[5 marks]**

### Question 7 (b)
A different part of the program is represented by the following state-transition diagram.

Input-B | Output-W; Input-B; Input-B
START -> S1 -> S3 -> S2 -> S5
Input-A; Input-A; Input-A | Output-W
Input-B | Output-Y; Input-A | Output-X
S4

**(i)** Complete the table to show the inputs, outputs and next states.
Assume that the current state for each row is given by the 'Next state' on the previous row. For example, the first Input-A is made when in state S1.
If there is no output for a given transition, then the output cell should contain 'none'.

The first two rows have been completed:
| Input | Output | Next state |
|-------|--------|------------|
| S1 | | |
| Input-A | none | S3 |
| Input-B | Output-W | none |
| Input-A | | |
| | | S4 |

**[5 marks]**

**(ii)** Identify the input sequence that will cause the minimum number of state changes in the transition from S1 to S4.

**[1 mark]**

---

## 2024 Oct/Nov (9618/22)

### Question 4
A global integer variable Tick is always incremented every millisecond (1000 times per second) regardless of the other programs running.

The value of Tick can be read by any program but the value should not be changed. Assume that the value of Tick does not overflow.

As an example, the following pseudocode algorithm would output "Goodbye" 40 seconds after outputting "Hello".

```
DECLARE Start : INTEGER
OUTPUT "Hello"
Start <- Tick
REPEAT
  //do nothing
UNTIL Tick = Start + 40000
OUTPUT "Goodbye"
```

A program is needed to help a user to time an event such as boiling an egg. The time taken for the event is known as the elapsed time.

The program contains a procedure Timer() which will:
- take two integer values representing an elapsed time in minutes and seconds
- use the value of variable Tick to calculate the elapsed time
- output a warning message 30 seconds before the elapsed time is up
- output a final message when the total time has elapsed.

For example, to set an alarm for 5 minutes and 45 seconds the program makes the following call:
`CALL Timer(5, 45)`

When 5 minutes and 15 seconds have elapsed, the program will output: "30 seconds to go"
When 5 minutes and 45 seconds have elapsed, the program will output: "The time is up!"

Write pseudocode for the procedure Timer().

**[6 marks]**

---

## 2023 May/June (9618/22)

### Question 2
A program stores a user's date of birth using a variable of type DATE: MyDOB

**(a)** Write a pseudocode statement, using a function from the insert, to assign the value corresponding to 17/11/2007 to MyDOB.

**[1 mark]**

**(b)** MyDOB has been assigned a valid value representing the user's date of birth. Write a pseudocode statement to calculate the number of months from the month of the user's birth until the end of the year and to assign this to the variable NumMonths.

For example, if MyDOB contains a value representing 02/07/2008, the value 5 would be assigned to NumMonths.

**[2 marks]**

**(c)** The program will output the day of the week corresponding to MyDOB. For example, given the date 22/06/2023, the program will output "Thursday".

An algorithm is required. An array will be used to store the names of the days of the week.
Define the array and describe the algorithm in four steps. Do not use pseudocode statements in your answer.

Array definition: ...
Step 1: ...
Step 2: ...
Step 3: ...
Step 4: ...

**[6 marks]**

---

## 2023 Oct/Nov (9618/22)

### Question 2
An algorithm will:
1. input a sequence of integer values, one at a time
2. ignore all values until the value 27 is input, then sum the remaining values in the sequence
3. stop summing values when the value 0 is input and then output the sum of the values.

**(a)** Draw a program flowchart to represent the algorithm.

(Space provided with START and END)

**[5 marks]**

**(b)** The solution to the algorithm includes iteration.
Give the name of a suitable loop structure that could be used. Justify your answer.

**[2 marks]**

### Question 5
A global 1D array of integers contains four elements, which are assigned values as shown:

```
Mix[1] <- 1
Mix[2] <- 3
Mix[3] <- 4
Mix[4] <- 2
```

A procedure manipulates the values in the array: Process()

The procedure is written in pseudocode:

```
PROCEDURE Process(Start : INTEGER)
  DECLARE Value, Index, Count : INTEGER
  Index <- Start
  Count <- 0
  REPEAT
    Value <- Mix[Index]
    Mix[Index] <- Mix[Index] - 1
    Index <- Value
    Count <- Count + 1
  UNTIL Count = 5
  Mix[4] <- Count * Index
ENDPROCEDURE
```

Complete the trace table by dry running the procedure when it is called as follows:
`CALL Process(3)`

| Index | Value | Count | Mix[1] | Mix[2] | Mix[3] | Mix[4] |
|-------|-------|-------|--------|--------|--------|--------|

**[6 marks]**

### Question 7
A program contains six modules:

```
Pseudocode module headers:
PROCEDURE Module-A()
PROCEDURE Module-X(T1 : INTEGER, S2 : REAL)
PROCEDURE Reset(BYREF Code : INTEGER)
FUNCTION Restore(OldCode : INTEGER) RETURNS BOOLEAN
FUNCTION Module-Y(RA : INTEGER, RB : BOOLEAN) RETURNS BOOLEAN
FUNCTION Module-Z(SA : INTEGER) RETURNS INTEGER
```

Module-X() calls Reset()
Module-Y() calls Restore()

**(a)** Complete the structure chart for these modules.

(Top-level: Module-A())

**[4 marks]**

**(b)** Explain the meaning of the diamond symbol as used in the diagram in part (a).

**[2 marks]**

---

## 2022 Oct/Nov (9618/22)

### Question 2 (a)
An algorithm will process data from a test taken by a group of students. The algorithm will prompt and input the name and test mark for each of the 35 students.

The algorithm will add the names of all the students with a test mark of less than 20 to an existing text file Support_List.txt, which already contains data from other group tests.

**(i)** Describe the steps that the algorithm should perform. Do not include pseudocode statements in your answer.

**[5 marks]**

**(ii)** Explain why it may be better to store the names of the students in a file rather than in an array.

**[1 mark]**

**(iii)** Explain why WRITE mode cannot be used in the answer to part 2(a)(i).

**[1 mark]**

### Question 2 (b)
Examine the following state-transition diagram.

Input-A Output-X; Input-B Output-W; Input-B
START -> S1 -> S2 -> S3
Input-A; Input-A; Input-B
S4; Input-A Output-W

Complete the table to show the inputs, outputs and next states.

| Input | Output | Next state |
|-------|--------|------------|
| S1 | | |
| Input-A | | |
| | | S2 |
| | Output-W | |
| | Output-W | |

**[4 marks]**

### Question 4
The program flowchart represents a simple algorithm.

START -> INPUT UserID -> Set Average to GetAverage(UserID) -> Set Total to 0 -> Set Index to 4 -> Add 1 to Index -> Is Index < 7? (YES -> Set Last to SameMonth[Index] -> Is Average > Last? (YES -> Add Average to Total) (NO -> Add Last to Total) [loop back]) (NO -> Update(UserID, Total)) -> END

**(a)** Write the equivalent pseudocode for the algorithm represented by the flowchart.

**[6 marks]**

**(b)** Give the name of the iterative construct in the flowchart.

**[1 mark]**

---

## 2021 May/June (9618/22)

### Question 2 (a)
Examine the following state-transition diagram.

Low level detected | Activate pump; Low level detected
X -> S2 -> S1
Normal level detected | Deactivate pump; Normal level detected -> S3

**(i)** Complete the table with reference to the diagram.

| | Answer |
|---|--------|
| The number of transitions that result in a different state | |
| The number of transitions with associated outputs | |
| The label that should replace 'X' | |
| The final or halting state | |

**[4 marks]**

**(ii)** The current state is S1. The following inputs occur:
1. Low level detected
2. Low level detected
3. Low level detected
4. Low level detected

Give the number of outputs and the current state.

Number of outputs: ...
Current state: ...

**[2 marks]**

### Question 2 (b)
A system is being developed to help manage book loans in a library. Registered users may borrow books from the library for a period of time.

**(i)** State three items of data that must be stored for each loan.

**[2 marks]**

**(ii)** State one item of data that will be required in the library system but does not need to be stored for each loan.

**[1 mark]**

**(iii)** One operation that manipulates the data stored for each loan, would produce a list of all overdue books. Identify two other operations.

**[2 marks]**

### Question 4
A teacher uses a paper-based system to store marks for a class test. The teacher requires a program to assign grades based on these results.

The program will output the grades together with the average mark.

Write a detailed description of the algorithm that will be needed.

**[6 marks]**
