# Chapter 11: Programming - 课后作业 Homework

> 姓名：__________ 日期：__________ 总分：__/56

---

## Pseudocode Syntax Reference (伪代码语法参考)

```
String functions:    LENGTH(s), SUBSTRING(s, start, length), UCASE(s), LCASE(s)
                     s1 & s2 (concatenation)
File handling:       OPENFILE(name, mode)    // modes: READ, WRITE, APPEND
                     READFILE(name, variable)
                     WRITEFILE(name, data)
                     CLOSEFILE(name)
                     EOF(name)
Subprograms:         FUNCTION Name(x : Type) RETURNS Type ... RETURN value ... ENDFUNCTION
                     PROCEDURE Name(BYVAL x : Type) / PROCEDURE Name(BYREF x : Type)
                     CALL ProcedureName(args)
```

---

### Question 1 [6 marks]

**(a)** Study the following pseudocode expressions. State the output of each expression. [4]

| Expression | Output |
|------------|--------|
| `LENGTH("Computer")` | |
| `SUBSTRING("Cambridge", 4, 3)` | |
| `UCASE("hello")` | |
| `LCASE("WORLD") & " " & UCASE("cup")` | |

**(b)** Write a single pseudocode expression that extracts the **last 3 characters** of a string variable `Word`. Your expression should work for any string length. [2]

```

```

---

### Question 2 [6 marks]

Write a pseudocode **function** called `CountChar` that:
- Takes a `Text` parameter of type STRING and a `Target` parameter of type CHAR
- Returns the number of times `Target` appears in `Text`

```
FUNCTION CountChar(Text : STRING, Target : CHAR) RETURNS INTEGER

ENDFUNCTION
```

[6]

---

### Question 3 [5 marks]

Explain the differences between a **function** and a **procedure** in pseudocode.

**(a)** State **two** differences between a function and a procedure. [2]

| | Function | Procedure |
|---|----------|-----------|
| Difference 1 | | |
| Difference 2 | | |

**(b)** The following pseudocode uses a function. Rewrite it as a **procedure** that achieves the same result, using a parameter passed **by reference** to return the result. [3]

Original function:
```
FUNCTION Double(x : INTEGER) RETURNS INTEGER
    RETURN x * 2
ENDFUNCTION

// Called as:
Result ← Double(5)
OUTPUT Result
```

Rewrite as procedure:
```
PROCEDURE Double(________________________)

ENDPROCEDURE

// Rewrite the calling code:

```

---

### Question 4 [6 marks]

**(a)** Explain the difference between passing a parameter **by value** (`BYVAL`) and passing a parameter **by reference** (`BYREF`). [2]

```

```

**(b)** Study the following pseudocode. Trace through it and state the output. [4]

```
DECLARE a : INTEGER
DECLARE b : INTEGER

PROCEDURE Modify(BYVAL x : INTEGER, BYREF y : INTEGER)
    x ← x + 10
    y ← y + 10
    OUTPUT x, " ", y
ENDPROCEDURE

a ← 5
b ← 5
CALL Modify(a, b)
OUTPUT a, " ", b
```

| Step | x | y | a | b | Output |
|------|---|---|---|---|--------|
| Before CALL | - | - | | | |
| After x ← x + 10 | | | | | |
| After y ← y + 10 | | | | | |
| OUTPUT in procedure | | | | | |
| OUTPUT after CALL | - | - | | | |

---

### Question 5 [6 marks]

A text file `marks.txt` contains student marks, one integer per line. Write pseudocode to:

**(a)** Read all marks from `marks.txt`, calculate and output the **average mark** and the **number of marks** that are above the average. [6]

```
DECLARE Marks : ARRAY[1:1000] OF INTEGER
DECLARE Count : INTEGER
DECLARE Total : INTEGER
DECLARE Average : REAL
DECLARE AboveCount : INTEGER

Count ← 0
Total ← 0

OUTPUT "Average: ", Average
OUTPUT "Above average: ", AboveCount
```

---

### Question 6 [5 marks]

Write a pseudocode **procedure** called `SaveReport` that:
- Takes a 1D array `Names[1:n]` of type STRING, a 1D array `Scores[1:n]` of type INTEGER, and `n` of type INTEGER as parameters
- Creates a new file called `report.txt`
- Writes each student's name and score on a single line in the format: `"Name: [name], Score: [score]"`
- At the end, writes a line `"Total students: [n]"`

```
PROCEDURE SaveReport(Names : ARRAY, Scores : ARRAY, n : INTEGER)

ENDPROCEDURE
```

[5]

---

### Question 7 [6 marks]

**(a)** Define the term **recursion**. [1]

```

```

**(b)** State **two** essential components that every recursive solution must have. [2]

```

```

**(c)** The following function calculates the sum of integers from 1 to `n` using recursion.

```
FUNCTION SumTo(n : INTEGER) RETURNS INTEGER
    IF n = 1 THEN
        RETURN 1
    ELSE
        RETURN n + SumTo(n - 1)
    ENDIF
ENDFUNCTION
```

Complete the **trace table** showing the recursive calls and return values for `SumTo(4)`. [3]

| Call | n | Returns | Calculation |
|------|---|---------|-------------|
| SumTo(4) | 4 | | |
| SumTo(3) | 3 | | |
| SumTo(2) | 2 | | |
| SumTo(1) | 1 | | |

---

### Question 8 [5 marks]

Write a **recursive** pseudocode function called `Power` that:
- Takes two INTEGER parameters: `Base` and `Exp` (where `Exp >= 0`)
- Returns `Base` raised to the power of `Exp`
- Uses the rule: `Base^Exp = Base * Base^(Exp-1)` and `Base^0 = 1`

```
FUNCTION Power(Base : INTEGER, Exp : INTEGER) RETURNS INTEGER

ENDFUNCTION
```

[5]

---

### Question 9 [6 marks]

A file called `inventory.txt` stores product data. Each line contains a product code, product name, and quantity, separated by commas. For example:
```
P001,Keyboard,50
P002,Mouse,120
P003,Monitor,30
```

Write pseudocode to:
- Read the file and find any product with a quantity **less than 40**
- Write these low-stock products to a **new** file called `lowstock.txt` in the same format

```
DECLARE Line : STRING
DECLARE Quantity : INTEGER

```

[6]

---

### Question 10 [5 marks]

Study the following pseudocode:

```
FUNCTION Mystery(s : STRING) RETURNS STRING
    DECLARE Result : STRING
    DECLARE i : INTEGER
    DECLARE c : CHAR
    Result ← ""
    FOR i ← LENGTH(s) DOWNTO 1
        c ← SUBSTRING(s, i, 1)
        IF c >= 'A' AND c <= 'Z' THEN
            Result ← Result & LCASE(c)
        ELSE
            IF c >= 'a' AND c <= 'z' THEN
                Result ← Result & UCASE(c)
            ELSE
                Result ← Result & c
            ENDIF
        ENDIF
    NEXT i
    RETURN Result
ENDFUNCTION
```

**(a)** Trace through `Mystery("Hello!")` and state the return value. [3]

| i | c | Condition | Added to Result | Result so far |
|---|---|-----------|-----------------|---------------|
|   |   |           |                 |               |
|   |   |           |                 |               |
|   |   |           |                 |               |
|   |   |           |                 |               |
|   |   |           |                 |               |
|   |   |           |                 |               |

Return value: __________

**(b)** Describe in words what the `Mystery` function does. [2]

```

```

---

**--- End of Homework ---**

**Total: 56 marks**

