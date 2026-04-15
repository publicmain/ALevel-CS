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

> 中文提示：线性搜索——从头到尾逐个检查数组中的每个元素，用一个变量保存当前找到的最大值。

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

> 中文提示：跟踪表——逐步记录每次比较和交换后数组的状态。第一轮遍历FOR循环时，记录每一步i的值和数组的变化。

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

> 中文提示：二分查找——每次将搜索范围减半。描述如何计算中间位置、比较目标值、缩小搜索范围。

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

> 中文提示：用FUNCTION编写二分查找。需要用WHILE循环、计算Mid中间值、比较后调整Low/High边界。找到返回位置，找不到返回-1。

```
FUNCTION BinarySearch(Arr : ARRAY, n : INTEGER, Target : INTEGER) RETURNS INTEGER












ENDFUNCTION
```

[5]

---

### Question 5 [4 marks]

A program development team uses **stepwise refinement** and **decomposition** when designing a solution.

**(a)** Define the term **decomposition**. [1]

> 中文提示：分解——将一个复杂的大问题拆分成更小、更容易管理的子问题。

```


```

**(b)** Define the term **stepwise refinement**. [1]

> 中文提示：逐步细化——将每个步骤进一步细化为更详细的子步骤，直到每一步都足够简单可以直接编码。

```


```

**(c)** A school library system needs to manage book borrowing. The top-level tasks are identified as:
- Search for a book
- Borrow a book
- Return a book

Draw a **structure chart** showing the decomposition of the "Borrow a book" task into at least **three** sub-tasks, with one sub-task further decomposed into two lower-level sub-tasks. [2]

> 中文提示：结构图——用方框和连线表示任务分解的层次关系。顶层是"Borrow a book"，下面是子任务，其中一个子任务再分解。

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

> 中文提示：状态转换图——用圆圈表示状态，用箭头表示转换，箭头上标注触发事件/条件。记住包括初始状态标记。

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

> 中文提示：二维数组处理。外层循环遍历每个学生（行），内层循环计算每个学生5次测试的总分，再求平均。同时记录最高平均分和对应学生编号。

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

> 中文提示：流程图——用椭圆表示开始/结束，平行四边形表示输入/输出，矩形表示处理，菱形表示判断。

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

> 中文提示：找出伪代码中的语法错误。仔细检查关键字拼写、语法结构（IF...THEN）、循环变量、输出格式（用&连接字符串和变量）。

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

> 中文提示：线性搜索函数。逐个比较Products数组中的元素与SearchName，找到后返回对应位置的Prices值。遍历完都没找到则返回-1.0。

```
FUNCTION FindPrice(Products : ARRAY, Prices : ARRAY, SearchName : STRING) RETURNS REAL












ENDFUNCTION
```

[5]

---

**--- End of Homework ---**

**Total: 52 marks**

> 提交提醒：请确保所有伪代码使用Cambridge 9618规范的语法格式。注意缩进和关键字大写。
