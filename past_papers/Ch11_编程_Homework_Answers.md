# Chapter 11: Programming - Homework Answers

> Total: 56 marks

---

### Question 1 [6 marks]

**(a)** String expression outputs: [4]

| Expression | Output |
|------------|--------|
| `LENGTH("Computer")` | `8` ✓ |
| `SUBSTRING("Cambridge", 4, 3)` | `"bri"` ✓ |
| `UCASE("hello")` | `"HELLO"` ✓ |
| `LCASE("WORLD") & " " & UCASE("cup")` | `"world CUP"` ✓ |

**Mark scheme:** ✓ 1 mark for each correct output

**(b)** Expression to extract the last 3 characters of `Word`: [2]

```
SUBSTRING(Word, LENGTH(Word) - 2, 3)                  // ✓ ✓
```

**Mark scheme:**
- ✓ Use of `LENGTH(Word)` to determine start position dynamically
- ✓ Correct expression: `SUBSTRING(Word, LENGTH(Word) - 2, 3)`

---

### Question 2 [6 marks]

```
FUNCTION CountChar(Text : STRING, Target : CHAR) RETURNS INTEGER
    DECLARE Count : INTEGER                            // ✓
    DECLARE i : INTEGER
    DECLARE c : CHAR
    Count ← 0                                          // ✓
    FOR i ← 1 TO LENGTH(Text)                         // ✓
        c ← SUBSTRING(Text, i, 1)                     // ✓
        IF c = Target THEN                             // ✓
            Count ← Count + 1
        ENDIF
    NEXT i
    RETURN Count                                       // ✓
ENDFUNCTION
```

**Mark scheme:**
- ✓ Declare Count and initialise to 0
- ✓ Initialise counter variable correctly
- ✓ Loop through each character using `FOR i ← 1 TO LENGTH(Text)`
- ✓ Extract each character using `SUBSTRING(Text, i, 1)`
- ✓ Compare character with Target and increment Count if match
- ✓ Return Count

---

### Question 3 [5 marks]

**(a)** Two differences between a function and a procedure: [2]

| | Function | Procedure |
|---|----------|-----------|
| Difference 1 | Returns a value to the calling code using RETURN ✓ | Does not return a value (or uses BYREF parameters) |
| Difference 2 | Is called as part of an expression / assignment (e.g. `x ← Func()`) ✓ | Is called using the CALL keyword (e.g. `CALL Proc()`) |

**Mark scheme:**
- ✓ Function returns a value; procedure does not
- ✓ Function is used in expressions/assignments; procedure is invoked with CALL

**(b)** Rewrite as procedure using BYREF: [3]

```
PROCEDURE Double(BYREF x : INTEGER)                   // ✓
    x ← x * 2                                          // ✓
ENDPROCEDURE

// Rewrite the calling code:
DECLARE Result : INTEGER
Result ← 5                                              // ✓
CALL Double(Result)
OUTPUT Result
```

**Mark scheme:**
- ✓ Procedure header with BYREF parameter
- ✓ Modifies the parameter directly (`x ← x * 2`) instead of using RETURN
- ✓ Calling code assigns value before calling, uses CALL, and outputs the variable after

---

### Question 4 [6 marks]

**(a)** Difference between BYVAL and BYREF: [2]

```
BYVAL (by value): A copy of the argument's value is passed to the
subroutine. Changes made to the parameter inside the subroutine do
NOT affect the original variable. ✓

BYREF (by reference): A reference (address) of the original variable
is passed. Changes made to the parameter inside the subroutine DO
affect the original variable. ✓
```

**Mark scheme:**
- ✓ BYVAL: a copy is passed; changes do not affect the original
- ✓ BYREF: a reference is passed; changes do affect the original

**(b)** Trace table: [4]

| Step | x | y | a | b | Output |
|------|---|---|---|---|--------|
| Before CALL | - | - | 5 | 5 | | ✓
| After x ← x + 10 | 15 | 5 | 5 | 5 | | ✓
| After y ← y + 10 | 15 | 15 | 5 | 15 | | ✓
| OUTPUT in procedure | 15 | 15 | 5 | 15 | `15 15` |
| OUTPUT after CALL | - | - | 5 | 15 | `5 15` | ✓

**Full output:**
```
15 15
5 15
```

**Mark scheme:**
- ✓ a and b correctly initialised to 5
- ✓ x changes to 15 (copy of a, so a stays 5)
- ✓ y changes to 15, and because y is BYREF, b also changes to 15
- ✓ Final output: `15 15` then `5 15` (a unchanged because passed BYVAL, b changed because passed BYREF)

---

### Question 5 [6 marks]

**(a)** Read marks, calculate average, count above average: [6]

```
DECLARE Marks : ARRAY[1:1000] OF INTEGER
DECLARE Count : INTEGER
DECLARE Total : INTEGER
DECLARE Average : REAL
DECLARE AboveCount : INTEGER

Count ← 0
Total ← 0

OPENFILE "marks.txt" FOR READ                          // ✓
WHILE NOT EOF("marks.txt") DO                          // ✓
    Count ← Count + 1
    READFILE "marks.txt", Marks[Count]
    Total ← Total + Marks[Count]                       // ✓
ENDWHILE
CLOSEFILE "marks.txt"

Average ← Total / Count                                // ✓

AboveCount ← 0                                         // ✓
FOR i ← 1 TO Count
    IF Marks[i] > Average THEN
        AboveCount ← AboveCount + 1
    ENDIF
NEXT i                                                  // ✓

OUTPUT "Average: ", Average
OUTPUT "Above average: ", AboveCount
```

**Mark scheme:**
- ✓ Open file and read marks in a loop until EOF
- ✓ Correct loop structure with Count and reading into array
- ✓ Accumulate Total while reading
- ✓ Calculate Average = Total / Count after reading all marks
- ✓ Initialise AboveCount and loop through array to count marks above average
- ✓ Correct comparison and counting logic, output results

---

### Question 6 [5 marks]

```
PROCEDURE SaveReport(Names : ARRAY, Scores : ARRAY, n : INTEGER)
    OPENFILE "report.txt" FOR WRITE                    // ✓
    FOR i ← 1 TO n                                     // ✓
        WRITEFILE "report.txt", "Name: " & Names[i] & ", Score: " & Scores[i]  // ✓ ✓
    NEXT i
    WRITEFILE "report.txt", "Total students: " & n      // ✓
    CLOSEFILE "report.txt"
ENDPROCEDURE
```

**Mark scheme:**
- ✓ Open file for WRITE mode
- ✓ Loop from 1 to n
- ✓ Correct string concatenation for each line
- ✓ Format matches specification: `"Name: [name], Score: [score]"`
- ✓ Write final line with total count and close file

---

### Question 7 [6 marks]

**(a)** Definition of recursion: [1]

```
Recursion is a programming technique where a subroutine (function or
procedure) calls itself as part of its own definition. ✓
```

**(b)** Two essential components of recursive solutions: [2]

```
1. A base case — a condition that stops the recursion and returns
   a value without making a further recursive call. ✓
2. A recursive case — the subroutine calls itself with a modified
   argument that moves closer to the base case. ✓
```

**Mark scheme:**
- ✓ Base case (terminating condition)
- ✓ Recursive case (call to itself with a value that progresses toward the base case)

**(c)** Trace table for `SumTo(4)`: [3]

| Call | n | Returns | Calculation |
|------|---|---------|-------------|
| SumTo(4) | 4 | 10 | 4 + SumTo(3) = 4 + 6 = 10 ✓ |
| SumTo(3) | 3 | 6 | 3 + SumTo(2) = 3 + 3 = 6 ✓ |
| SumTo(2) | 2 | 3 | 2 + SumTo(1) = 2 + 1 = 3 |
| SumTo(1) | 1 | 1 | Base case: RETURN 1 ✓ |

**Mark scheme:**
- ✓ Correct base case identified (n=1 returns 1)
- ✓ Correct unwinding of recursive calls with proper calculations
- ✓ Final return value of 10 for SumTo(4)

---

### Question 8 [5 marks]

```
FUNCTION Power(Base : INTEGER, Exp : INTEGER) RETURNS INTEGER
    IF Exp = 0 THEN                                    // ✓
        RETURN 1                                        // ✓
    ELSE
        RETURN Base * Power(Base, Exp - 1)              // ✓ ✓ ✓
    ENDIF
ENDFUNCTION
```

**Mark scheme:**
- ✓ Function header with correct parameters and return type
- ✓ Base case: `IF Exp = 0 THEN RETURN 1`
- ✓ Recursive case: returns `Base * Power(Base, Exp - 1)`
- ✓ Correct recursive call with `Exp - 1` (progresses toward base case)
- ✓ Correct overall structure with IF/ELSE and ENDIF

---

### Question 9 [6 marks]

```
DECLARE Line : STRING
DECLARE Quantity : INTEGER
DECLARE Code : STRING                                   // ✓
DECLARE Name : STRING
DECLARE CommaPos1 : INTEGER
DECLARE CommaPos2 : INTEGER
DECLARE QuantityStr : STRING

OPENFILE "inventory.txt" FOR READ                       // ✓
OPENFILE "lowstock.txt" FOR WRITE                       // ✓

WHILE NOT EOF("inventory.txt") DO                       // ✓
    READFILE "inventory.txt", Line
    // Parse the line to extract quantity
    // Find positions of commas and extract the quantity field
    CommaPos1 ← 1
    WHILE SUBSTRING(Line, CommaPos1, 1) <> "," DO
        CommaPos1 ← CommaPos1 + 1
    ENDWHILE
    CommaPos2 ← CommaPos1 + 1
    WHILE SUBSTRING(Line, CommaPos2, 1) <> "," DO
        CommaPos2 ← CommaPos2 + 1
    ENDWHILE
    QuantityStr ← SUBSTRING(Line, CommaPos2 + 1, LENGTH(Line) - CommaPos2)
    Quantity ← STRING_TO_INT(QuantityStr)

    IF Quantity < 40 THEN                               // ✓
        WRITEFILE "lowstock.txt", Line                  // ✓
    ENDIF
ENDWHILE

CLOSEFILE "inventory.txt"
CLOSEFILE "lowstock.txt"
```

**Mark scheme:**
- ✓ Open inventory.txt for READ
- ✓ Open lowstock.txt for WRITE
- ✓ Loop until EOF reading each line
- ✓ Extract/parse the quantity from the line (accept any reasonable parsing approach)
- ✓ Compare quantity with 40
- ✓ Write matching lines to lowstock.txt and close both files

---

### Question 10 [5 marks]

**(a)** Trace through `Mystery("Hello!")`: [3]

| i | c | Condition | Added to Result | Result so far |
|---|---|-----------|-----------------|---------------|
| 6 | `!` | Not A-Z, not a-z | `!` | `!` |
| 5 | `o` | Lowercase (a-z) | `O` | `!O` |
| 4 | `l` | Lowercase (a-z) | `L` | `!OL` |
| 3 | `l` | Lowercase (a-z) | `L` | `!OLL` |
| 2 | `e` | Lowercase (a-z) | `E` | `!OLLE` |
| 1 | `H` | Uppercase (A-Z) | `h` | `!OLLEh` |

✓ ✓

Return value: **`!OLLEh`** ✓

**Mark scheme:**
- ✓ Correct iteration order (from LENGTH down to 1) and correct character extraction
- ✓ Correct case swapping for each character
- ✓ Correct final return value: `!OLLEh`

**(b)** Description of what `Mystery` does: [2]

```
The function reverses the input string ✓ and swaps the case of all
alphabetic characters (uppercase becomes lowercase and vice versa),
while leaving non-alphabetic characters unchanged. ✓
```

**Mark scheme:**
- ✓ Reverses the string
- ✓ Swaps the case of letters (uppercase to lowercase and vice versa)

---

**--- End of Answers ---**

**Total: 56 marks**
