# Chapter 9: Algorithm Design & Problem-solving - Homework Answers

> Total: 52 marks

---

### Question 1 [6 marks]

**(a)** Pseudocode for finding the largest value in `Numbers[1:100]`: [4]

```
DECLARE Numbers : ARRAY[1:100] OF INTEGER
DECLARE Max : INTEGER

Max ← Numbers[1]                          // ✓ initialise Max to first element
FOR i ← 2 TO 100                          // ✓ loop from second element to end
    IF Numbers[i] > Max THEN              // ✓ compare each element with current Max
        Max ← Numbers[i]                  // ✓ update Max if larger value found
    ENDIF
NEXT i
OUTPUT Max
```

**Mark scheme:**
- ✓ Initialise `Max` to `Numbers[1]` (or a very small value)
- ✓ Loop through all elements (FOR i ← 2 TO 100)
- ✓ Comparison `IF Numbers[i] > Max`
- ✓ Update `Max ← Numbers[i]` and output the result

**(b)** Time complexity: [2]

```
O(n) — Linear time complexity.  ✓
The algorithm visits each element in the array exactly once,  ✓
so the number of comparisons grows in direct proportion to the
number of elements n.
```

**Mark scheme:**
- ✓ State O(n)
- ✓ Justification: every element must be examined exactly once / number of operations proportional to n

---

### Question 2 [6 marks]

**(a)** Trace table for `Data = [5, 3, 8, 1]` after the first complete pass: [4]

| i | Data[1] | Data[2] | Data[3] | Data[4] | Swapped |
|---|---------|---------|---------|---------|---------|
|   |    5    |    3    |    8    |    1    |  FALSE  |
| 1 |    3    |    5    |    8    |    1    |  TRUE   |
| 2 |    3    |    5    |    8    |    1    |  TRUE   |
| 3 |    3    |    5    |    1    |    8    |  TRUE   |

**Mark scheme:**
- ✓ i=1: 5 > 3 is TRUE, swap → [3, 5, 8, 1], Swapped ← TRUE
- ✓ i=2: 5 > 8 is FALSE, no swap → [3, 5, 8, 1]
- ✓ i=3: 8 > 1 is TRUE, swap → [3, 5, 1, 8], Swapped ← TRUE
- ✓ Correct final state and Swapped values throughout

**(b)** Purpose of the `Swapped` variable: [2]

```
The Swapped variable is used to detect when no swaps have occurred
during a complete pass through the array. ✓
If no swaps occur (Swapped remains FALSE), the array is already
sorted and the algorithm can terminate early, avoiding unnecessary
passes. ✓
```

**Mark scheme:**
- ✓ It records/flags whether any swaps were made during a pass
- ✓ If no swaps are made, the data is sorted and the algorithm can stop early (optimisation)

---

### Question 3 [5 marks]

**(a)** Steps of a binary search algorithm: [3]

```
1. Find the middle element of the current search range. ✓
2. Compare the middle element with the target value. ✓
   - If equal, the target is found — return the index.
   - If the target is less than the middle element,
     discard the upper half and repeat on the lower half.
   - If the target is greater than the middle element,
     discard the lower half and repeat on the upper half. ✓
3. Repeat until the target is found or the search range is empty
   (meaning the target is not in the array).
```

**Mark scheme:**
- ✓ Find/calculate the middle element
- ✓ Compare the middle element with the target
- ✓ Discard the half that cannot contain the target and repeat / describe the three cases

**(b)** Binary search for value **23** in `[2, 5, 8, 12, 16, 23, 38, 56, 72, 91]` (indices 1–10): [2]

```
Step 1: Low=1, High=10, Mid=(1+10) DIV 2 = 5
        Array[5] = 16. 23 > 16, so search upper half. ✓
        New: Low=6, High=10

Step 2: Low=6, High=10, Mid=(6+10) DIV 2 = 8
        Array[8] = 56. 23 < 56, so search lower half.
        New: Low=6, High=7

Step 3: Low=6, High=7, Mid=(6+7) DIV 2 = 6
        Array[6] = 23. 23 = 23, found at index 6. ✓
```

**Mark scheme:**
- ✓ Correct first mid calculation and comparison (Mid=5, value 16, search upper half)
- ✓ Correct subsequent steps leading to finding 23 at index 6

---

### Question 4 [5 marks]

```
FUNCTION BinarySearch(Arr : ARRAY, n : INTEGER, Target : INTEGER) RETURNS INTEGER
    DECLARE Low : INTEGER                              // ✓
    DECLARE High : INTEGER
    DECLARE Mid : INTEGER
    Low ← 1                                            // ✓
    High ← n
    WHILE Low <= High DO                               // ✓
        Mid ← (Low + High) DIV 2
        IF Arr[Mid] = Target THEN                      // ✓
            RETURN Mid
        ELSE
            IF Arr[Mid] < Target THEN
                Low ← Mid + 1
            ELSE
                High ← Mid - 1                         // ✓
            ENDIF
        ENDIF
    ENDWHILE
    RETURN -1
ENDFUNCTION
```

**Mark scheme:**
- ✓ Correct declarations and initialisation of Low and High
- ✓ WHILE loop with correct condition `Low <= High`
- ✓ Calculate Mid correctly using integer division
- ✓ Correct three-way comparison (equal / less / greater) with appropriate updates to Low or High
- ✓ Return index when found, return -1 when not found

---

### Question 5 [4 marks]

**(a)** Definition of decomposition: [1]

```
Decomposition is the process of breaking down a complex problem
into smaller, more manageable sub-problems. ✓
```

**(b)** Definition of stepwise refinement: [1]

```
Stepwise refinement is the process of progressively adding
more detail to each sub-problem until each step is detailed
enough to be implemented in code. ✓
```

**(c)** Structure chart for "Borrow a book": [2]

```
                    Borrow a Book                          ✓
                    /     |      \
                   /      |       \
       Check         Update         Issue
    Availability   Book Record    Loan Receipt
                   /        \                              ✓
             Mark Book     Record
            as Borrowed   Due Date
```

**Mark scheme:**
- ✓ At least three sub-tasks shown correctly under "Borrow a Book" (e.g., Check Availability, Update Book Record, Issue Loan Receipt)
- ✓ One sub-task further decomposed into two lower-level sub-tasks with correct hierarchy

---

### Question 6 [6 marks]

**(a)** State-transition diagram: [4]

```
                coin                  coin
          ┌──────────┐          ┌──────────┐
          │          ▼          │          │
     ──►[Idle] ──────────► [Accepting]◄───┘      ✓ ✓
          ▲      coin           │    │
          │                     │    │
          │     dispensed       │    │ cancel
     [Dispensing] ◄─────────────┘    │            ✓
          │         enough           │
          │                          ▼
          └──────────────────────[Idle]            ✓

Transitions:
  Idle     --coin-->      Accepting
  Accepting --coin-->     Accepting
  Accepting --enough-->   Dispensing
  Accepting --cancel-->   Idle
  Dispensing --dispensed--> Idle
```

**Mark scheme:**
- ✓ Three states correctly shown (Idle, Accepting, Dispensing)
- ✓ Correct transitions from Idle and to Accepting
- ✓ Self-loop on Accepting for coin input, and cancel returns to Idle
- ✓ Dispensing → Idle on dispensed event

**(b)** State-transition table: [2]

| Current State | Input | Next State |
|---------------|-------|------------|
| Idle          | coin  | Accepting  |
| Accepting     | coin  | Accepting  |
| Accepting     | enough| Dispensing |
| Accepting     | cancel| Idle       |
| Dispensing    | dispensed | Idle    |

**Mark scheme:**
- ✓ First three transitions correct
- ✓ Last two transitions correct

---

### Question 7 [6 marks]

```
PROCEDURE ClassReport(Scores : ARRAY)
    DECLARE StudentAvg : REAL                           // ✓
    DECLARE HighestAvg : REAL
    DECLARE BestStudent : INTEGER
    DECLARE Total : INTEGER

    HighestAvg ← 0                                      // ✓
    BestStudent ← 1

    FOR i ← 1 TO 30                                     // ✓
        Total ← 0
        FOR j ← 1 TO 5
            Total ← Total + Scores[i, j]                // ✓
        NEXT j
        StudentAvg ← Total / 5
        OUTPUT "Student ", i, " average: ", StudentAvg   // ✓

        IF StudentAvg > HighestAvg THEN
            HighestAvg ← StudentAvg
            BestStudent ← i
        ENDIF
    NEXT i

    OUTPUT "Highest average: ", HighestAvg, " by Student ", BestStudent  // ✓
ENDPROCEDURE
```

**Mark scheme:**
- ✓ Correct variable declarations
- ✓ Initialise tracking variables for highest average
- ✓ Outer loop iterating through 30 students
- ✓ Inner loop summing 5 test scores using 2D array notation `Scores[i, j]`
- ✓ Calculate and output average for each student
- ✓ Track and output the highest average and student number

---

### Question 8 [4 marks]

**(a)** Flowchart: [3]

```
    ┌───────────┐
    │   Start   │                     ✓ (correct symbols)
    └─────┬─────┘
          ▼
    ┌─────────────┐
   /   Input N     /                  ✓ (parallelogram for I/O)
    └─────┬───────┘
          ▼
    ┌─────────────┐
    │ Result ← 1  │                  (rectangle for process)
    └─────┬───────┘
          ▼
      ◇ N <= 1? ◇──── YES ──┐
          │                   │
          NO                  ▼
          ▼            ┌────────────┐
    ┌──────────────┐  /Output Result/  ✓ (loop and output)
    │Result←Result*N│  └──────┬─────┘
    └─────┬────────┘         ▼
          ▼            ┌───────────┐
    ┌──────────┐       │   Stop    │
    │ N ← N-1 │       └───────────┘
    └─────┬────┘
          │
          └──── (back to N <= 1? decision)
```

**Mark scheme:**
- ✓ Correct use of flowchart symbols (oval for start/stop, parallelogram for I/O, rectangle for process, diamond for decision)
- ✓ Correct loop structure (decision leads back from N ← N - 1 to the condition check)
- ✓ Correct flow: Input → Result←1 → decision → multiply/decrement loop → output

**(b)** What the algorithm calculates: [1]

```
The algorithm calculates the factorial of N (N!). ✓
```

---

### Question 9 [5 marks]

**(a)** Four errors identified and corrected: [4]

| Line (approx.) | Error | Corrected Line |
|-----------------|-------|----------------|
| 1 | `DECLAR` is misspelled (missing E) | `DECLARE Count : INTEGER` ✓ |
| 5 | `IF Num > 0` is missing `THEN` keyword | `IF Num > 0 THEN` ✓ |
| 8 | `NEXT Count` should use the loop variable `i` | `NEXT i` ✓ |
| 9 | Concatenation operator `&` missing between string and variable | `OUTPUT "Positive numbers: " & Count` ✓ |

**(b)** Purpose of the algorithm: [1]

```
The algorithm counts how many of 10 input numbers are positive
(greater than zero) and outputs the count. ✓
```

---

### Question 10 [5 marks]

```
FUNCTION FindPrice(Products : ARRAY, Prices : ARRAY, SearchName : STRING) RETURNS REAL
    DECLARE i : INTEGER                                // ✓
    FOR i ← 1 TO 50                                   // ✓
        IF Products[i] = SearchName THEN               // ✓
            RETURN Prices[i]                           // ✓
        ENDIF
    NEXT i
    RETURN -1.0                                        // ✓
ENDFUNCTION
```

**Mark scheme:**
- ✓ Correct declaration of loop variable
- ✓ Loop through all 50 elements
- ✓ Compare each element with `SearchName`
- ✓ Return corresponding price from `Prices` array when found
- ✓ Return `-1.0` if product is not found (after loop ends)

---

**--- End of Answers ---**

**Total: 52 marks**
