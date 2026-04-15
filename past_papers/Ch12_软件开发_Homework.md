# Chapter 12: Software Development - 课后作业 Homework

> 姓名：__________ 日期：__________ 总分：__/50

---

### Question 1 [6 marks]

The **program development lifecycle** consists of several stages.

**(a)** List the five stages of the program development lifecycle in the correct order. [2]

| Order | Stage |
|-------|-------|
| 1     |       |
| 2     |       |
| 3     |       |
| 4     |       |
| 5     |       |

**(b)** For each of the following activities, state which stage of the lifecycle it belongs to: [2]

| Activity | Stage |
|----------|-------|
| Drawing structure charts and writing pseudocode | |
| Interviewing users to determine system requirements | |
| Using test data to check the program produces correct results | |
| Fixing a bug reported by users after the program has been deployed | |

**(c)** Explain why the program development lifecycle is described as **iterative**. [2]

```

```

---

### Question 2 [6 marks]

A programmer is testing a function that calculates a discount. The function takes a total purchase amount as input:
- If the amount is less than $50, no discount is applied
- If the amount is between $50 and $100 (inclusive), a 10% discount is applied
- If the amount is greater than $100, a 20% discount is applied

**(a)** The programmer uses **black-box testing**. Explain what black-box testing is. [2]

```

```

**(b)** Complete the test data table below. For each test, identify the **type of test data** (normal, abnormal, or boundary) and the **expected result**. [4]

| Test | Input Amount | Type of Test Data | Expected Result |
|------|-------------|-------------------|-----------------|
| 1    | $75         |                   |                 |
| 2    | $50         |                   |                 |
| 3    | $100        |                   |                 |
| 4    | $-10        |                   |                 |
| 5    | $150        |                   |                 |
| 6    | $49.99      |                   |                 |

---

### Question 3 [5 marks]

**(a)** Explain the difference between **white-box testing** and **black-box testing**. [2]

```

```

**(b)** A program contains the following pseudocode:

```
FUNCTION CheckGrade(Mark : INTEGER) RETURNS STRING
    IF Mark >= 90 THEN
        RETURN "A"
    ELSE
        IF Mark >= 70 THEN
            RETURN "B"
        ELSE
            IF Mark >= 50 THEN
                RETURN "C"
            ELSE
                RETURN "Fail"
            ENDIF
        ENDIF
    ENDIF
ENDFUNCTION
```

A **white-box test** must ensure every path through the code is tested. State the **minimum** set of test data values needed to test every path, and the expected output for each. [3]

| Test Data (Mark) | Path Taken | Expected Output |
|-------------------|------------|-----------------|
|                   |            |                 |
|                   |            |                 |
|                   |            |                 |
|                   |            |                 |

---

### Question 4 [5 marks]

Three types of errors can occur in programs.

**(a)** Define each type of error and give **one** example of each. [3]

| Error Type | Definition | Example |
|------------|------------|---------|
| Syntax error | | |
| Logic error | | |
| Runtime error | | |

**(b)** For each of the following code fragments, identify whether the error is a **syntax error**, **logic error**, or **runtime error**. [2]

| Code Fragment | Error Type |
|---------------|------------|
| `IF x > 5 THNE` (intended: `THEN`) | |
| A loop that should run 10 times but runs 11 times due to an incorrect condition | |
| Attempting to open a file that does not exist on disk | |
| Using `>` instead of `>=` in a boundary check, causing one value to be missed | |

---

### Question 5 [6 marks]

**(a)** Explain what is meant by **stub testing**. [2]

```

```

**(b)** Explain what is meant by **integration testing**. [2]

```

```

**(c)** A program has three modules: `InputData`, `ProcessData`, and `OutputResults`. The developer wants to test `ProcessData` before `InputData` is complete.

Write a pseudocode **stub** for `InputData` that returns a fixed set of test data (an array of 5 integers). Show how this stub would be used to test `ProcessData`. [2]

```
// Stub for InputData
FUNCTION InputData() RETURNS ARRAY OF INTEGER

ENDFUNCTION

// Using the stub to test ProcessData

```

---

### Question 6 [4 marks]

An **Integrated Development Environment (IDE)** provides several features to help programmers.

**(a)** Describe **four** features of an IDE and explain how each helps the programmer. [4]

| Feature | How it helps the programmer |
|---------|-----------------------------|
| 1. | |
| 2. | |
| 3. | |
| 4. | |

---

### Question 7 [5 marks]

A programmer is debugging a program that is supposed to calculate the total cost of items in a shopping cart, applying a 15% tax.

The pseudocode is:

```
DECLARE Items : ARRAY[1:10] OF REAL
DECLARE Total : INTEGER
DECLARE Tax : REAL
DECLARE FinalCost : REAL

Total ← 0
Items[1] ← 25.50
Items[2] ← 10.00
Items[3] ← 7.99

FOR i ← 1 TO 3
    Total ← Total + Items[i]
NEXT i

Tax ← Total * 15 / 100
FinalCost ← Total - Tax
OUTPUT "Total with tax: ", FinalCost
```

**(a)** Identify **three** errors in the pseudocode above. For each error, explain the problem and write the corrected line. [3]

| Error | Explanation | Corrected Line |
|-------|-------------|----------------|
| 1 | | |
| 2 | | |
| 3 | | |

**(b)** The programmer uses breakpoints and variable watches to debug this code. Explain how these debugging features are used. [2]

```

```

---

### Question 8 [5 marks]

A software company is developing a new application. After deployment, the company provides ongoing **maintenance**.

**(a)** Describe **three** types of maintenance that may be carried out after a program is deployed. [3]

| Type of Maintenance | Description |
|--------------------|-------------|
| 1. | |
| 2. | |
| 3. | |

**(b)** Explain why **documentation** is important for the maintenance stage. Give **two** reasons. [2]

```

```

---

### Question 9 [4 marks]

**(a)** Distinguish between **program documentation** (technical documentation) and **user documentation**. [2]

```

```

**(b)** Give **two** examples of information that would be found in technical documentation but NOT in user documentation. [2]

```

```

---

### Question 10 [4 marks]

A program calculates the Body Mass Index (BMI) using the formula: `BMI = weight / (height * height)` where weight is in kg and height is in metres.

The program should:
- Accept weight (must be between 20 and 300)
- Accept height (must be between 0.5 and 2.5)
- Calculate and display the BMI
- Display a category: Underweight (BMI < 18.5), Normal (18.5 to 24.9), Overweight (25.0 to 29.9), Obese (BMI >= 30.0)

**(a)** Complete the test plan below by providing appropriate test data for each type. [4]

| Test No. | Test Data Type | Weight (kg) | Height (m) | Expected BMI | Expected Category |
|----------|---------------|-------------|------------|-------------|-------------------|
| 1 | Normal | | | | |
| 2 | Normal | | | | |
| 3 | Boundary (weight) | | | | |
| 4 | Boundary (height) | | | | |
| 5 | Abnormal | | | | Error / rejected |
| 6 | Abnormal | | | | Error / rejected |

---

**--- End of Homework ---**

**Total: 50 marks**

