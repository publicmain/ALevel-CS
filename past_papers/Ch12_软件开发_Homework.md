# Chapter 12: Software Development - 课后作业 Homework

> 姓名：__________ 日期：__________ 总分：__/50

---

### Question 1 [6 marks]

The **program development lifecycle** consists of several stages.

**(a)** List the five stages of the program development lifecycle in the correct order. [2]

> 中文提示：程序开发生命周期的五个阶段：分析(Analysis)、设计(Design)、编码(Coding)、测试(Testing)、维护(Maintenance)。

| Order | Stage |
|-------|-------|
| 1     |       |
| 2     |       |
| 3     |       |
| 4     |       |
| 5     |       |

**(b)** For each of the following activities, state which stage of the lifecycle it belongs to: [2]

> 中文提示：判断每项活动属于哪个开发阶段。

| Activity | Stage |
|----------|-------|
| Drawing structure charts and writing pseudocode | |
| Interviewing users to determine system requirements | |
| Using test data to check the program produces correct results | |
| Fixing a bug reported by users after the program has been deployed | |

**(c)** Explain why the program development lifecycle is described as **iterative**. [2]

> 中文提示：迭代——开发过程可能需要反复回到前面的阶段。例如测试发现问题可能需要回到编码甚至设计阶段。

```



```

---

### Question 2 [6 marks]

A programmer is testing a function that calculates a discount. The function takes a total purchase amount as input:
- If the amount is less than $50, no discount is applied
- If the amount is between $50 and $100 (inclusive), a 10% discount is applied
- If the amount is greater than $100, a 20% discount is applied

**(a)** The programmer uses **black-box testing**. Explain what black-box testing is. [2]

> 中文提示：黑盒测试——不查看程序内部代码，只关注输入和预期输出是否匹配。测试者只知道程序应该做什么（规格说明），不知道程序怎么实现。

```



```

**(b)** Complete the test data table below. For each test, identify the **type of test data** (normal, abnormal, or boundary) and the **expected result**. [4]

> 中文提示：Normal=正常数据（在有效范围内的典型值），Boundary=边界数据（在范围边界上的值），Abnormal=异常数据（无效的、不合理的输入）。

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

> 中文提示：白盒测试——查看程序内部代码结构，确保所有路径/分支都被测试到。黑盒测试——不看代码，只测试输入/输出是否符合规格说明。

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

> 中文提示：白盒测试要覆盖所有分支路径。这段代码有4条路径（>=90, 70-89, 50-69, <50），所以至少需要4个测试值。

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

> 中文提示：Syntax error=语法错误（代码不符合语言规则，编译时发现），Logic error=逻辑错误（程序能运行但结果不正确），Runtime error=运行时错误（程序运行中发生的错误，如除以零）。

| Error Type | Definition | Example |
|------------|------------|---------|
| Syntax error | | |
| Logic error | | |
| Runtime error | | |

**(b)** For each of the following code fragments, identify whether the error is a **syntax error**, **logic error**, or **runtime error**. [2]

> 中文提示：判断每段代码中的错误类型。

| Code Fragment | Error Type |
|---------------|------------|
| `IF x > 5 THNE` (intended: `THEN`) | |
| A loop that should run 10 times but runs 11 times due to an incorrect condition | |
| Attempting to open a file that does not exist on disk | |
| Using `>` instead of `>=` in a boundary check, causing one value to be missed | |

---

### Question 5 [6 marks]

**(a)** Explain what is meant by **stub testing**. [2]

> 中文提示：存根测试——在测试主程序时，用简化的"存根"（stub）代替尚未完成的子程序。存根通常只返回固定值或输出简单消息，以验证主程序的逻辑。

```



```

**(b)** Explain what is meant by **integration testing**. [2]

> 中文提示：集成测试——将各个已单独测试过的模块/组件组合在一起进行测试，检查它们之间的接口和交互是否正确。

```



```

**(c)** A program has three modules: `InputData`, `ProcessData`, and `OutputResults`. The developer wants to test `ProcessData` before `InputData` is complete.

Write a pseudocode **stub** for `InputData` that returns a fixed set of test data (an array of 5 integers). Show how this stub would be used to test `ProcessData`. [2]

> 中文提示：写一个简单的InputData存根，不真正读取输入，而是直接返回预设的测试数据，用于测试ProcessData模块。

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

> 中文提示：IDE常见功能包括：代码编辑器（语法高亮、自动补全）、编译器/解释器、调试器（断点、单步执行、变量监视）、错误提示/报告、代码格式化、自动缩进、项目管理等。

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

> 中文提示：仔细检查数据类型声明、计算逻辑（Total应该是REAL而非INTEGER，因为要存储小数）、最终计算（应该是加税不是减税）等。

| Error | Explanation | Corrected Line |
|-------|-------------|----------------|
| 1 | | |
| 2 | | |
| 3 | | |

**(b)** The programmer uses breakpoints and variable watches to debug this code. Explain how these debugging features are used. [2]

> 中文提示：断点(breakpoint)——在某行设置标记，程序运行到该行时暂停。变量监视(watch)——在暂停时查看变量的当前值，追踪变量变化过程。

```



```

---

### Question 8 [5 marks]

A software company is developing a new application. After deployment, the company provides ongoing **maintenance**.

**(a)** Describe **three** types of maintenance that may be carried out after a program is deployed. [3]

> 中文提示：三种维护类型——Corrective（纠正性维护：修复发现的bug），Adaptive（适应性维护：适应环境变化，如新操作系统），Perfective（完善性维护：改进功能或性能以满足新需求）。

| Type of Maintenance | Description |
|--------------------|-------------|
| 1. | |
| 2. | |
| 3. | |

**(b)** Explain why **documentation** is important for the maintenance stage. Give **two** reasons. [2]

> 中文提示：文档对维护的重要性——帮助维护人员理解原始代码的设计意图，减少理解和修改代码所需的时间。

```



```

---

### Question 9 [4 marks]

**(a)** Distinguish between **program documentation** (technical documentation) and **user documentation**. [2]

> 中文提示：技术文档——面向程序员/开发者，描述代码结构、算法、数据结构等。用户文档——面向最终用户，解释如何安装和使用软件。

```



```

**(b)** Give **two** examples of information that would be found in technical documentation but NOT in user documentation. [2]

> 中文提示：技术文档中有但用户文档中没有的内容，例如：源代码注释、变量/数据结构说明、算法描述、模块间的接口定义等。

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

> 中文提示：为每种测试数据类型选择合适的值。Normal=正常范围内的典型值，Boundary=边界值（恰好在有效范围的边界上），Abnormal=超出有效范围的值或无效输入。

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

> 提交提醒：本章重点在于理解软件开发过程和测试方法。回答理论题时请用完整的英文句子，必要时举例说明。测试相关题目要注明测试数据类型（normal/abnormal/boundary）。
