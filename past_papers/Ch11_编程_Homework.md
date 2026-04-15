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

> 中文提示：字符串函数——LENGTH返回长度，SUBSTRING(s, start, length)提取子串（位置从1开始），UCASE转大写，LCASE转小写，&连接字符串。

| Expression | Output |
|------------|--------|
| `LENGTH("Computer")` | |
| `SUBSTRING("Cambridge", 4, 3)` | |
| `UCASE("hello")` | |
| `LCASE("WORLD") & " " & UCASE("cup")` | |

**(b)** Write a single pseudocode expression that extracts the **last 3 characters** of a string variable `Word`. Your expression should work for any string length. [2]

> 中文提示：用LENGTH获取字符串长度，再用SUBSTRING从合适的位置提取最后3个字符。

```


```

---

### Question 2 [6 marks]

Write a pseudocode **function** called `CountChar` that:
- Takes a `Text` parameter of type STRING and a `Target` parameter of type CHAR
- Returns the number of times `Target` appears in `Text`

> 中文提示：遍历字符串中的每个字符，用SUBSTRING(Text, i, 1)取出第i个字符，与Target比较，相同则计数器+1。

```
FUNCTION CountChar(Text : STRING, Target : CHAR) RETURNS INTEGER










ENDFUNCTION
```

[6]

---

### Question 3 [5 marks]

Explain the differences between a **function** and a **procedure** in pseudocode.

**(a)** State **two** differences between a function and a procedure. [2]

> 中文提示：函数(FUNCTION)有返回值，用RETURNS声明返回类型；过程(PROCEDURE)不返回值。函数可以在表达式中使用，过程用CALL调用。

| | Function | Procedure |
|---|----------|-----------|
| Difference 1 | | |
| Difference 2 | | |

**(b)** The following pseudocode uses a function. Rewrite it as a **procedure** that achieves the same result, using a parameter passed **by reference** to return the result. [3]

> 中文提示：BYREF参数传递——过程通过修改引用参数来"返回"结果，调用者的变量会被直接修改。

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

> 中文提示：BYVAL=传值，子程序收到的是副本，修改不影响原变量；BYREF=传引用，子程序直接操作原变量，修改会影响原变量。

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

> 中文提示：逐行追踪代码。注意a是按值传递（BYVAL），b是按引用传递（BYREF）。过程内x的修改不影响a，但y的修改会影响b。

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

> 中文提示：第一步——打开文件读取所有成绩到数组并计数，计算平均值。第二步——遍历数组，统计高于平均值的个数。记住先CLOSEFILE再重新处理。

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

> 中文提示：用OPENFILE("report.txt", WRITE)创建/覆盖文件，用循环将每个学生的信息用WRITEFILE写入，最后写总数行，再CLOSEFILE。

```
PROCEDURE SaveReport(Names : ARRAY, Scores : ARRAY, n : INTEGER)










ENDPROCEDURE
```

[5]

---

### Question 7 [6 marks]

**(a)** Define the term **recursion**. [1]

> 中文提示：递归——一个子程序（函数或过程）在其定义中调用自身。

```

```

**(b)** State **two** essential components that every recursive solution must have. [2]

> 中文提示：递归必须有基本情况（base case，终止条件）和递归情况（recursive case，调用自身且问题规模缩小）。

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

> 中文提示：从SumTo(4)开始，每次调用SumTo(n-1)直到n=1，然后从最深层开始返回，逐层计算结果。

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

> 中文提示：基本情况——Exp等于0时返回1。递归情况——返回Base乘以Power(Base, Exp-1)。

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

> 中文提示：读取每一行，用字符串处理找到最后一个逗号后的数字（数量），转换为整数比较。可以逐字符找逗号位置，或者假设有合适的字符串分割方式。Cambridge伪代码中没有内置的Split函数，需要用SUBSTRING和循环来解析。

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

> 中文提示：逐个字符处理（从后往前）。大写字母转小写，小写字母转大写，其他字符不变。结果是反转后并交换大小写。

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

> 提交提醒：请确保所有伪代码使用Cambridge 9618规范的语法格式。字符串连接用&符号，文件操作记得CLOSEFILE，递归函数必须有base case。
