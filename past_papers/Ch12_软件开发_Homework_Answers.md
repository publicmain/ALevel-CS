# Chapter 12: Software Development - Homework Answers

> Total: 50 marks

---

### Question 1 [6 marks]

**(a)** Five stages of the program development lifecycle: [2]

| Order | Stage |
|-------|-------|
| 1     | Analysis ✓ |
| 2     | Design |
| 3     | Coding (Implementation) |
| 4     | Testing ✓ |
| 5     | Maintenance |

**Mark scheme:**
- ✓ All five stages listed
- ✓ In the correct order

**(b)** Activities matched to stages: [2]

| Activity | Stage |
|----------|-------|
| Drawing structure charts and writing pseudocode | Design ✓ |
| Interviewing users to determine system requirements | Analysis |
| Using test data to check the program produces correct results | Testing ✓ |
| Fixing a bug reported by users after the program has been deployed | Maintenance |

**Mark scheme:**
- ✓ First two activities correctly matched
- ✓ Last two activities correctly matched

**(c)** Why the lifecycle is iterative: [2]

```
The lifecycle is iterative because each stage may need to be revisited
and repeated. ✓ For example, if testing reveals errors, the developer
must return to the coding or design stage to fix them, and if
requirements change during maintenance, the team may need to revisit
analysis and design. ✓
```

**Mark scheme:**
- ✓ Stages may need to be revisited / repeated
- ✓ Example: e.g., testing may reveal issues requiring return to design/coding, or user feedback may require changes

---

### Question 2 [6 marks]

**(a)** Black-box testing: [2]

```
Black-box testing is a testing method where the tester does not have
access to or knowledge of the internal structure/code of the
program. ✓ The tester only considers the inputs and expected outputs,
testing whether the program meets its specification. ✓
```

**Mark scheme:**
- ✓ Testing without knowledge of the internal code/structure
- ✓ Tests based on inputs and expected outputs / against the specification

**(b)** Test data table: [4]

| Test | Input Amount | Type of Test Data | Expected Result |
|------|-------------|-------------------|-----------------|
| 1    | $75         | Normal            | 10% discount applied; pay $67.50 ✓ |
| 2    | $50         | Boundary          | 10% discount applied; pay $45.00 ✓ |
| 3    | $100        | Boundary          | 10% discount applied; pay $90.00 ✓ |
| 4    | $-10        | Abnormal          | Rejected / error message |
| 5    | $150        | Normal            | 20% discount applied; pay $120.00 ✓ |
| 6    | $49.99      | Boundary          | No discount; pay $49.99 |

**Mark scheme:**
- ✓ Normal data correctly identified with correct expected results
- ✓ Boundary values correctly identified ($50 and $100 are boundaries)
- ✓ Abnormal data correctly identified (negative value)
- ✓ All expected results calculated correctly

---

### Question 3 [5 marks]

**(a)** White-box vs black-box testing: [2]

```
White-box testing examines the internal logic and structure of the code.
The tester has access to the source code and designs tests to ensure
every path through the code is executed. ✓

Black-box testing only considers inputs and expected outputs based on
the specification, without knowledge of the internal code. ✓
```

**Mark scheme:**
- ✓ White-box: tester has access to code, tests internal paths/logic
- ✓ Black-box: tester only considers inputs and outputs, no knowledge of code

**(b)** Minimum test data for every path: [3]

| Test Data (Mark) | Path Taken | Expected Output |
|-------------------|------------|-----------------|
| 95 | Mark >= 90 → TRUE | "A" ✓ |
| 75 | Mark >= 90 → FALSE, Mark >= 70 → TRUE | "B" ✓ |
| 60 | Mark >= 90 → FALSE, Mark >= 70 → FALSE, Mark >= 50 → TRUE | "C" |
| 30 | Mark >= 90 → FALSE, Mark >= 70 → FALSE, Mark >= 50 → FALSE | "Fail" ✓ |

**Mark scheme:**
- ✓ Four test values covering all four paths
- ✓ Correct path described for each
- ✓ Correct expected output for each (accept any values that trigger the correct paths)

---

### Question 4 [5 marks]

**(a)** Three types of errors: [3]

| Error Type | Definition | Example |
|------------|------------|---------|
| Syntax error | An error where the code violates the grammatical rules of the programming language, preventing it from being compiled/interpreted. ✓ | Writing `PRNT` instead of `PRINT`, or missing a closing bracket |
| Logic error | An error where the program runs without crashing but produces incorrect results due to a mistake in the algorithm or logic. ✓ | Using `+` instead of `-` in a calculation, or using `>` instead of `>=` |
| Runtime error | An error that occurs during program execution, causing the program to crash or terminate abnormally. ✓ | Division by zero, or attempting to access a file that does not exist |

**Mark scheme:** ✓ 1 mark each for correct definition with appropriate example

**(b)** Identifying error types: [2]

| Code Fragment | Error Type |
|---------------|------------|
| `IF x > 5 THNE` (intended: `THEN`) | Syntax error ✓ |
| A loop that should run 10 times but runs 11 times due to an incorrect condition | Logic error |
| Attempting to open a file that does not exist on disk | Runtime error ✓ |
| Using `>` instead of `>=` in a boundary check, causing one value to be missed | Logic error |

**Mark scheme:**
- ✓ First two correctly identified
- ✓ Last two correctly identified

---

### Question 5 [6 marks]

**(a)** Stub testing: [2]

```
Stub testing is a technique used during top-down development where
incomplete modules are replaced with simplified "stub" versions that
return fixed or dummy data. ✓ This allows higher-level modules to be
tested before the lower-level modules they depend on are complete. ✓
```

**Mark scheme:**
- ✓ A stub is a simplified/dummy version of a module that returns test data
- ✓ Allows testing of calling modules before called modules are implemented

**(b)** Integration testing: [2]

```
Integration testing is the testing of individual modules combined
together to check that they interact and work correctly as a
group. ✓ It ensures that data is passed correctly between modules
and that the combined system functions as expected. ✓
```

**Mark scheme:**
- ✓ Testing modules when they are combined together
- ✓ Checks that modules interact / interface correctly

**(c)** Stub for InputData: [2]

```
// Stub for InputData
FUNCTION InputData() RETURNS ARRAY OF INTEGER
    DECLARE TestData : ARRAY[1:5] OF INTEGER           // ✓
    TestData[1] ← 10
    TestData[2] ← 25
    TestData[3] ← 8
    TestData[4] ← 42
    TestData[5] ← 17
    RETURN TestData
ENDFUNCTION

// Using the stub to test ProcessData
DECLARE Data : ARRAY[1:5] OF INTEGER                    // ✓
Data ← InputData()
CALL ProcessData(Data)
```

**Mark scheme:**
- ✓ Stub function returns a fixed array of 5 integers (hardcoded test data)
- ✓ Calling code uses the stub to obtain data and passes it to ProcessData

---

### Question 6 [4 marks]

**(a)** Four IDE features: [4]

| Feature | How it helps the programmer |
|---------|-----------------------------|
| 1. Code editor with syntax highlighting | Displays keywords, strings, and variables in different colours, making code easier to read and helping to spot syntax errors quickly. ✓ |
| 2. Auto-completion / code suggestions | Suggests variable names, function names, and keywords as the programmer types, reducing typing errors and speeding up coding. ✓ |
| 3. Debugger (breakpoints, stepping, variable watch) | Allows the programmer to pause execution at specific lines, step through code line by line, and inspect variable values to find and fix logic and runtime errors. ✓ |
| 4. Error diagnostics / compiler messages | Reports syntax errors and warnings with line numbers and descriptions, allowing the programmer to quickly locate and fix mistakes before running the program. ✓ |

**Mark scheme:** ✓ 1 mark for each feature with a clear explanation of how it helps

---

### Question 7 [5 marks]

**(a)** Three errors in the pseudocode: [3]

| Error | Explanation | Corrected Line |
|-------|-------------|----------------|
| 1 | `Total` is declared as INTEGER but it stores the sum of REAL values. This will cause loss of precision / incorrect rounding. ✓ | `DECLARE Total : REAL` |
| 2 | `FinalCost ← Total - Tax` subtracts the tax instead of adding it. The program should add tax to the total. ✓ | `FinalCost ← Total + Tax` |
| 3 | The loop variable `i` is not declared. ✓ | `DECLARE i : INTEGER` (add before the loop) |

**Mark scheme:**
- ✓ Total should be REAL not INTEGER (precision error)
- ✓ Should be `Total + Tax` not `Total - Tax` (logic error — tax should be added)
- ✓ Third error identified (accept: undeclared loop variable, or any other valid error such as only processing 3 of 10 items)

**(b)** Breakpoints and variable watches: [2]

```
A breakpoint is a marker placed on a line of code that causes the
program to pause execution when it reaches that line. This allows
the programmer to examine the program state at that point. ✓

A variable watch allows the programmer to monitor the value of
specific variables as the program executes. The watch window
displays the current value of watched variables, updating in
real-time as the programmer steps through the code, making it
easy to spot where values become incorrect. ✓
```

**Mark scheme:**
- ✓ Breakpoint: pauses execution at a specific line so the programmer can inspect the state
- ✓ Variable watch: monitors the value of specified variables during execution to track changes

---

### Question 8 [5 marks]

**(a)** Three types of maintenance: [3]

| Type of Maintenance | Description |
|--------------------|-------------|
| 1. Corrective maintenance | Fixing bugs and errors that are discovered after the software has been deployed and is in use. ✓ |
| 2. Adaptive maintenance | Modifying the software to work in a changed environment, such as a new operating system, new hardware, or changes in regulations. ✓ |
| 3. Perfective maintenance | Improving the software by adding new features, enhancing performance, or improving usability in response to user feedback. ✓ |

**Mark scheme:** ✓ 1 mark each for correct type name and description

**(b)** Importance of documentation for maintenance: [2]

```
1. Documentation helps new or different programmers understand the
   purpose, structure, and logic of the code, so they can make
   changes without introducing errors. ✓

2. Documentation records design decisions, data structures, and
   algorithms used, allowing maintainers to quickly identify which
   parts of the code need modification and understand the impact of
   changes on other modules. ✓
```

**Mark scheme:**
- ✓ Helps programmers (who may not be the original authors) understand the code
- ✓ Makes it easier to locate sections that need changing and understand the impact of changes

---

### Question 9 [4 marks]

**(a)** Program documentation vs user documentation: [2]

```
Program (technical) documentation is written for programmers and
developers. It describes the internal workings of the program,
including code structure, algorithms, data structures, and design
decisions. ✓

User documentation is written for end users. It explains how to
install, operate, and use the software, without requiring
technical knowledge of the code. ✓
```

**Mark scheme:**
- ✓ Technical documentation: for developers, describes internal code and design
- ✓ User documentation: for end users, describes how to use the software

**(b)** Two examples found in technical documentation but NOT in user documentation: [2]

```
1. Variable names, data structures, and algorithm descriptions
   used in the program code. ✓

2. Program flowcharts, structure charts, or pseudocode showing
   the design of the solution. ✓
```

**Mark scheme:**
- ✓ Any valid example of technical content (e.g., variable/data structure descriptions, pseudocode, program logic, test plans)
- ✓ A second valid example different from the first

---

### Question 10 [4 marks]

**(a)** Test plan: [4]

| Test No. | Test Data Type | Weight (kg) | Height (m) | Expected BMI | Expected Category |
|----------|---------------|-------------|------------|-------------|-------------------|
| 1 | Normal | 70 | 1.75 | 22.86 | Normal ✓ |
| 2 | Normal | 100 | 1.80 | 30.86 | Obese ✓ |
| 3 | Boundary (weight) | 20 | 1.70 | 6.92 | Underweight ✓ |
| 4 | Boundary (height) | 70 | 0.5 | 280.00 | Obese |
| 5 | Abnormal | -5 | 1.70 | - | Error / rejected ✓ |
| 6 | Abnormal | 70 | 3.0 | - | Error / rejected |

**Mark scheme:**
- ✓ Normal test data with correct BMI calculation and category
- ✓ Second normal test data covering a different category
- ✓ Boundary values at the edges of valid ranges (weight: 20 or 300; height: 0.5 or 2.5)
- ✓ Abnormal data outside valid ranges with expected rejection

---

**--- End of Answers ---**

**Total: 50 marks**
