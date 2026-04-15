# Chapter 9: Algorithm Design & Problem-solving - 课后作业 Homework

> 姓名：__________ 日期：__________ 总分：__/52

---

## Pseudocode Syntax Reference (伪代码语法参考)

```
DECLARE x : INTEGER          FOR i ← 1 TO n ... NEXT i
WHILE condition DO ... ENDWHILE     IF condition THEN ... ELSE ... ENDIF
FUNCTION Name(params) RETURNS Type  PROCEDURE Name(params)
INPUT x / OUTPUT x                  CALL ProcedureName()
```

---

### Question 1 [6 marks]

A program needs to find the largest value in an array of 100 integers.

**(a)** Write pseudocode for a **linear search** algorithm that finds and outputs the largest value stored in the array `Numbers[1:100]`. [4]

```
DECLARE Numbers : ARRAY[1:100] OF INTEGER
DECLARE Max : INTEGER

```

**(b)** State the time complexity of this algorithm using Big-O notation. Justify your answer. [2]

```

```

---

### Question 2 [6 marks]

The following pseudocode performs a **bubble sort** on an array `Data[1:n]`.

```
PROCEDURE BubbleSort(Data : ARRAY, n : INTEGER)
    DECLARE Temp : INTEGER
    DECLARE Swapped : BOOLEAN
    REPEAT
        Swapped ← FALSE
        FOR i ← 1 TO n - 1
            IF Data[i] > Data[i + 1] THEN
                Temp ← Data[i]
                Data[i] ← Data[i + 1]
                Data[i + 1] ← Temp
                Swapped ← TRUE
            ENDIF
        NEXT i
        n ← n - 1
    UNTIL NOT Swapped
ENDPROCEDURE
```

**(a)** Complete the **trace table** below for the array `Data = [5, 3, 8, 1]` after the **first complete pass** of the bubble sort (the first full execution of the FOR loop). [4]

| i | Data[1] | Data[2] | Data[3] | Data[4] | Swapped |
|---|---------|---------|---------|---------|---------|
|   |    5    |    3    |    8    |    1    |  FALSE  |
|   |         |         |         |         |         |
|   |         |         |         |         |         |
|   |         |         |         |         |         |

**(b)** Explain why the variable `Swapped` is used in this algorithm. [2]

```

```

---

### Question 3 [5 marks]

A **binary search** is used to find a target value in a sorted array.

**(a)** Describe the steps of a binary search algorithm. [3]

```

```

**(b)** The sorted array contains: `[2, 5, 8, 12, 16, 23, 38, 56, 72, 91]`

Show the steps a binary search would take to find the value **23**. State the index examined at each step and the new search boundaries. [2]

```

```

---

### Question 4 [5 marks]

Write a pseudocode **function** called `BinarySearch` that:
- Takes a sorted array `Arr[1:n]` of integers, the size `n`, and a `Target` value as parameters
- Returns the index position of `Target` if found, or returns `-1` if not found

```
FUNCTION BinarySearch(Arr : ARRAY, n : INTEGER, Target : INTEGER) RETURNS INTEGER

ENDFUNCTION
```

[5]

---

### Question 5 [4 marks]

A program development team uses **stepwise refinement** and **decomposition** when designing a solution.

**(a)** Define the term **decomposition**. [1]

```

```

**(b)** Define the term **stepwise refinement**. [1]

```

```

**(c)** A school library system needs to manage book borrowing. The top-level tasks are identified as:
- Search for a book
- Borrow a book
- Return a book

Draw a **structure chart** showing the decomposition of the "Borrow a book" task into at least **three** sub-tasks, with one sub-task further decomposed into two lower-level sub-tasks. [2]

```

```

---

### Question 6 [6 marks]

A vending machine accepts coins and dispenses drinks. It has three states:
- **Idle** (waiting for coins)
- **Accepting** (receiving coins, total < price)
- **Dispensing** (enough money inserted, dispensing drink)

The possible inputs/events are:
- `coin` (a coin is inserted)
- `enough` (total coins reach the price)
- `dispensed` (drink has been dispensed)
- `cancel` (user cancels the transaction)

**(a)** Draw a **state-transition diagram** for this vending machine. Include all states, transitions, and labels. [4]

```

```

**(b)** Complete the **state-transition table** below. [2]

| Current State | Input | Next State |
|---------------|-------|------------|
| Idle          | coin  |            |
| Accepting     | coin  |            |
| Accepting     | enough|            |
| Accepting     | cancel|            |
| Dispensing    | dispensed |        |

---

### Question 7 [6 marks]

A teacher stores student test scores. Write a pseudocode **procedure** called `ClassReport` that:

- Takes a 2D array `Scores[1:30, 1:5]` as a parameter, where rows represent 30 students and columns represent 5 tests
- Calculates and outputs the **average score** for **each student** (each row)
- Outputs the **highest average** and which student number achieved it

```
PROCEDURE ClassReport(Scores : ARRAY)

ENDPROCEDURE
```

[6]

---

### Question 8 [4 marks]

Study the following flowchart description. A flowchart takes an input number `N` and performs the following steps:

1. Start
2. Input N
3. Set Result ← 1
4. Is N <= 1? If YES, go to step 7. If NO, continue.
5. Result ← Result * N
6. N ← N - 1, go back to step 4
7. Output Result
8. Stop

**(a)** Draw the **flowchart** for the algorithm described above. Use the correct flowchart symbols. [3]

```

```

**(b)** State what this algorithm calculates. [1]

```

```

---

### Question 9 [5 marks]

The pseudocode below contains **errors**. There are **four** errors.

```
DECLAR Count : INTEGER
Count ← 0
FOR i ← 1 TO 10
    INPUT Num
    IF Num > 0
        Count ← Count + 1
    ENDIF
NEXT Count
OUTPUT "Positive numbers: " Count
```

**(a)** Identify each error and write the corrected line. [4]

| Line (approx.) | Error | Corrected Line |
|-----------------|-------|----------------|
|                 |       |                |
|                 |       |                |
|                 |       |                |
|                 |       |                |

**(b)** State the purpose of this algorithm. [1]

```

```

---

### Question 10 [5 marks]

A company stores product names and prices. A linear search is performed to find a product by name.

Write a pseudocode **function** called `FindPrice` that:
- Takes a 1D array `Products[1:50]` of type STRING, a 1D array `Prices[1:50]` of type REAL, and a `SearchName` of type STRING as parameters
- Performs a **linear search** for `SearchName` in the `Products` array
- Returns the corresponding price from the `Prices` array if found
- Returns `-1.0` if the product is not found

```
FUNCTION FindPrice(Products : ARRAY, Prices : ARRAY, SearchName : STRING) RETURNS REAL

ENDFUNCTION
```

[5]

---

**--- End of Homework ---**

**Total: 52 marks**

