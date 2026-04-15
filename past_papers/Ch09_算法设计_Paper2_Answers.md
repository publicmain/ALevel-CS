# Chapter 9: Algorithm Design & Problem-solving - Paper 2 Answers

Mark scheme style answers with detailed marking points.

---

## 2024 May/June (9618/22)

### Question 2

**(a)** Flowchart to find the largest of three different values and output the largest and the average. **[5 marks]**

The flowchart should contain:

- INPUT Num1, Num2, Num3 ✓
- First decision: Is Num1 > Num2?
  - Yes branch: Second decision: Is Num1 > Num3?
    - Yes: Ans <- Num1 ✓
    - No: Ans <- Num3
  - No branch: Third decision: Is Num2 > Num3?
    - Yes: Ans <- Num2 ✓
    - No: Ans <- Num3
- OUTPUT "Largest is " & Ans ✓
- OUTPUT "Average is " & (Num1 + Num2 + Num3) / 3 ✓

> 用中文提示：此题考查用流程图实现"三数取最大值"的逻辑。需要两层嵌套判断（decision box），先比较两个数，再用胜出者与第三个比较。最后输出最大值和平均值。

**(b)** Pseudocode for the flowchart algorithm. **[5 marks]**

```
DECLARE Flag : BOOLEAN
DECLARE Port : INTEGER

Flag ← GetStat()                          // ✓ call function and assign result
IF Flag = FALSE THEN                      // ✓ check flag condition
  Port ← 1                               // ✓ initialise Port
  WHILE Port <> 4 DO                      // ✓ correct loop structure (or REPEAT...UNTIL Port = 4)
    CALL Reset(Port)                      // ✓ call procedure with Port
    Port ← Port + 1
  ENDWHILE
ENDIF
```

Mark points:
- ✓ Assign return value of GetStat() to Flag
- ✓ Conditional check on Flag (IF Flag = FALSE / IF NOT Flag)
- ✓ Initialise Port to 1
- ✓ Loop construct repeating while Port <> 4 (or equivalent)
- ✓ CALL Reset(Port) and increment Port inside loop

> 用中文提示：从流程图转写伪代码。GetStat() 是函数调用（有返回值），Reset() 是过程调用（用 CALL）。循环从 Port=1 到 Port=3（当 Port=4 时退出）。

### Question 7 (b)

**(i)** Complete the state-transition table. **[5 marks]**

Starting from S1, the table should be:

| Input | Output | Next state |
|-------|--------|------------|
| (Current state: S1) | | |
| Input-A | none | S3 |
| Input-B | Output-W | S2 ✓ |
| Input-A | none | S4 ✓ |
| Input-B | Output-Y | S5 ✓ |
| Input-A | Output-X | S4 ✓ |

> Note: The exact answers depend on the diagram transitions. Key marking points:
- ✓ Correct output for Input-B from S1 (Output-W)
- ✓ Correct next state for Input-B from S1 (S2)
- ✓ Correct output and next state for row 4
- ✓ Correct output and next state for row 5
- ✓ All entries consistent with the state-transition diagram

> 用中文提示：状态转换表要根据状态转换图逐步填写。每一行的"当前状态"由上一行的"下一状态"决定。注意区分有输出和无输出的转换。

**(ii)** Minimum number of state changes from S1 to S4. **[1 mark]**

- Input-A, Input-A ✓ (S1 → S3 → S4, two state changes)

> 用中文提示：从 S1 到 S4 的最短路径。通过状态图找最少步骤的输入序列。

---

## 2024 Oct/Nov (9618/22)

### Question 4

Pseudocode for procedure Timer(). **[6 marks]**

```
PROCEDURE Timer(Minutes : INTEGER, Seconds : INTEGER)
  DECLARE Start : INTEGER                                    // ✓
  DECLARE TotalMS : INTEGER
  DECLARE WarningMS : INTEGER

  TotalMS ← (Minutes * 60 + Seconds) * 1000                 // ✓ convert to milliseconds
  WarningMS ← TotalMS - 30000                                // ✓ calculate 30-second warning point

  Start ← Tick                                               // ✓ record start time

  REPEAT
    // do nothing - wait for warning time
  UNTIL Tick >= Start + WarningMS                            // ✓ wait until 30 seconds before end

  OUTPUT "30 seconds to go"

  REPEAT
    // do nothing - wait for total time
  UNTIL Tick >= Start + TotalMS                              // ✓ wait until total time elapsed

  OUTPUT "The time is up!"
ENDPROCEDURE
```

Mark points:
- ✓ Procedure header with two integer parameters
- ✓ Calculate total elapsed time in milliseconds
- ✓ Calculate warning time (total minus 30000)
- ✓ Record start time from Tick
- ✓ First loop waiting until warning time reached, then output warning message
- ✓ Second loop waiting until total time reached, then output final message

> 用中文提示：Timer 过程利用全局变量 Tick（每毫秒自增）来计时。关键是把分钟和秒转换成毫秒，然后用两个 REPEAT 循环：第一个等到"提前30秒"的时刻输出警告，第二个等到总时间到了输出结束消息。

---

## 2023 May/June (9618/22)

### Question 2

**(a)** Assign date 17/11/2007 to MyDOB. **[1 mark]**

```
MyDOB ← SETDATE(17, 11, 2007)           // ✓
```

> 用中文提示：使用 SETDATE 函数设置日期值，参数顺序为 日, 月, 年。

**(b)** Calculate number of months from birth month to end of year. **[2 marks]**

```
NumMonths ← 12 - MONTH(MyDOB)           // ✓✓
```

Mark points:
- ✓ Use of MONTH() function to extract month
- ✓ Correct calculation: 12 minus the month value

> 用中文提示：用 MONTH() 提取月份，再用 12 减去该月份。例如 7 月出生，12-7=5 个月到年底。

**(c)** Algorithm to output the day of the week. **[6 marks]**

Array definition:
- ✓ A 1D array of 7 elements of type STRING, storing "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday" (indexed 1 to 7 or 0 to 6)

Step 1: ✓ Use the DAYINDEX() function (or equivalent from the insert) to extract a numeric value representing the day of the week from MyDOB

Step 2: ✓ Store the returned value as an index variable

Step 3: ✓ Use the index to look up the corresponding day name from the array

Step 4: ✓ Output the day name string

> 用中文提示：先定义一个存放星期名称的数组，再用日期函数获取星期几的数字索引，用该索引从数组中查找对应的星期名称并输出。

---

## 2023 Oct/Nov (9618/22)

### Question 2

**(a)** Flowchart for the algorithm. **[5 marks]**

The flowchart should contain:

```
START
  ↓
INPUT Value          ✓ (first input)
  ↓
Is Value = 27?  ──No──→ (loop back to INPUT)    ✓ (loop until 27 found)
  ↓ Yes
Sum ← 0             ✓ (initialise sum)
  ↓
INPUT Value          ✓ (input next value)
  ↓
Is Value = 0?  ──No──→ Sum ← Sum + Value → (loop back to INPUT)
  ↓ Yes
OUTPUT Sum           ✓ (output result)
  ↓
END
```

Mark points:
- ✓ Input values in a loop
- ✓ Decision to check for value 27 (ignore values before 27)
- ✓ Initialise Sum to 0 after finding 27
- ✓ Second loop: input values, add to Sum, check for 0
- ✓ Output Sum when value = 0

> 用中文提示：流程图分两部分：第一个循环不断输入直到遇到 27；第二个循环不断输入并累加，直到遇到 0 则输出总和。

**(b)** Name of suitable loop structure. **[2 marks]**

- ✓ Post-condition loop / REPEAT...UNTIL (repeat-until loop)
- ✓ Justification: The value must be input at least once before it can be checked / the condition is tested after the input is made, so a post-condition loop is appropriate

> 用中文提示：REPEAT...UNTIL 是后测循环（先执行后判断），适合此场景因为必须先输入一个值才能检查它是否为 27 或 0。

### Question 5

Trace table for CALL Process(3). **[6 marks]**

Initial array values: Mix[1]=1, Mix[2]=3, Mix[3]=4, Mix[4]=2

```
PROCEDURE Process(Start : INTEGER)   // Start = 3
  Index ← 3, Count ← 0
  
  Iteration 1: Value ← Mix[3]=4, Mix[3] ← 4-1=3, Index ← 4, Count ← 1
  Iteration 2: Value ← Mix[4]=2, Mix[4] ← 2-1=1, Index ← 2, Count ← 2
  Iteration 3: Value ← Mix[2]=3, Mix[2] ← 3-1=2, Index ← 3, Count ← 3
  Iteration 4: Value ← Mix[3]=3, Mix[3] ← 3-1=2, Index ← 3, Count ← 4
  Iteration 5: Value ← Mix[3]=2, Mix[3] ← 2-1=1, Index ← 2, Count ← 5
  
  After loop: Mix[4] ← 5 * 2 = 10
```

| Index | Value | Count | Mix[1] | Mix[2] | Mix[3] | Mix[4] |
|-------|-------|-------|--------|--------|--------|--------|
| 3 | | 0 | 1 | 3 | 4 | 2 |
| 4 | 4 | 1 | 1 | 3 | 3 | 2 | ✓
| 2 | 2 | 2 | 1 | 3 | 3 | 1 | ✓
| 3 | 3 | 3 | 1 | 2 | 3 | 1 | ✓
| 3 | 3 | 4 | 1 | 2 | 2 | 1 | ✓
| 2 | 2 | 5 | 1 | 2 | 1 | 1 | ✓
| | | | 1 | 2 | 1 | 10 | ✓

> 用中文提示：干运行（trace table）是逐步执行代码并记录每个变量的值。注意 Mix[Index] 先被读取赋给 Value，然后 Mix[Index] 自减 1，然后 Index 变成 Value 的值。最后 Mix[4] = Count * Index = 5 * 2 = 10。

### Question 7

**(a)** Structure chart. **[4 marks]**

```
              Module-A()
           /    |     |    \
          /     |     |     \
   Module-X()  Module-Y()  Module-Z()
   (T1:INT,    (RA:INT,    (SA:INT)
    S2:REAL)    RB:BOOL)    RETURNS INT
       |        RETURNS
       |        BOOL
       |          |
    Reset()    Restore()
   (BYREF      (OldCode:INT)
    Code:INT)   RETURNS BOOL
```

Mark points:
- ✓ Module-A() at the top level calling all other top-level modules
- ✓ Module-X() shown with parameters T1 (INTEGER) and S2 (REAL), calling Reset()
- ✓ Module-Y() shown with parameters RA (INTEGER) and RB (BOOLEAN), calling Restore()
- ✓ Module-Z() shown with parameter SA (INTEGER) and return type INTEGER
- ✓ Correct parameter passing arrows (down for input, up for return values, filled/open circles for BYREF/BYVAL)

> 用中文提示：结构图（Structure Chart）展示模块间的调用关系和参数传递。箭头向下表示输入参数，向上表示返回值。BYREF 参数用特殊标记表示。

**(b)** Meaning of the diamond symbol in a structure chart. **[2 marks]**

- ✓ The diamond symbol indicates that the module call is conditional / the call is only made if a certain condition is met
- ✓ It represents selection — the module below the diamond is only called under certain circumstances (not every time the parent module executes)

> 用中文提示：结构图中的菱形符号表示"有条件调用"，即该模块只在满足特定条件时才被调用（选择/条件执行）。

---

## 2022 Oct/Nov (9618/22)

### Question 2 (a)

**(i)** Describe the algorithm steps. **[5 marks]**

- ✓ Step 1: Open the existing file Support_List.txt in APPEND mode
- ✓ Step 2: Set up a loop to repeat 35 times (once for each student)
- ✓ Step 3: Prompt and input the student's name and test mark
- ✓ Step 4: Check if the test mark is less than 20
- ✓ Step 5: If the mark is less than 20, write the student's name to the file
- Close the file after all 35 students have been processed

> 用中文提示：算法步骤：以 APPEND 模式打开文件 → 循环 35 次 → 每次输入姓名和分数 → 判断分数是否 < 20 → 是则写入文件 → 关闭文件。

**(ii)** Why store in a file rather than an array. **[1 mark]**

- ✓ The data needs to be persistent / stored permanently so that it is available after the program ends. An array only exists while the program is running; a file retains data between program executions.

> 用中文提示：文件是持久化存储，程序关闭后数据仍然存在；数组只在程序运行时存在于内存中。

**(iii)** Why WRITE mode cannot be used. **[1 mark]**

- ✓ WRITE mode would overwrite/delete the existing data in the file. The file already contains data from other group tests, so APPEND mode must be used to add new data without losing the existing data.

> 用中文提示：WRITE 模式会覆盖文件原有内容。因为文件已有其他组测试的数据，必须用 APPEND 模式追加数据。

### Question 2 (b)

Complete the state-transition table. **[4 marks]**

| Input | Output | Next state |
|-------|--------|------------|
| (Current state: S1) | | |
| Input-A | Output-X | S2 ✓ |
| Input-B | none | S2 ✓ |
| Input-A | none | S3 ✓ |
| Input-B | Output-W | S4 ✓ |

> 用中文提示：根据状态转换图，从 S1 开始，逐行追踪输入、输出和下一个状态。

### Question 4

**(a)** Pseudocode for the flowchart algorithm. **[6 marks]**

```
DECLARE UserID : STRING
DECLARE Average : REAL
DECLARE Total : REAL
DECLARE Index : INTEGER
DECLARE Last : REAL

INPUT UserID                                    // ✓
Average ← GetAverage(UserID)                    // ✓
Total ← 0                                      // ✓
Index ← 4
REPEAT                                          // ✓
  Index ← Index + 1
  Last ← SameMonth[Index]
  IF Average > Last THEN                        // ✓
    Total ← Total + Average
  ELSE
    Total ← Total + Last
  ENDIF
UNTIL Index >= 7                                // ✓ (or UNTIL NOT(Index < 7))
CALL Update(UserID, Total)
```

Mark points:
- ✓ INPUT UserID
- ✓ Function call: Average ← GetAverage(UserID)
- ✓ Initialise Total to 0
- ✓ Loop structure (REPEAT...UNTIL or equivalent)
- ✓ IF...THEN...ELSE for comparing Average with Last
- ✓ CALL Update(UserID, Total) after loop

> 用中文提示：从流程图转伪代码。注意循环是先加 1 再判断（Index 从 4 开始，加 1 后为 5，循环到 Index 不再 < 7 即 Index=7 时退出）。IF 判断选择 Average 和 Last 中较大的加到 Total。

**(b)** Name of the iterative construct. **[1 mark]**

- ✓ Post-condition loop / REPEAT...UNTIL (the condition is checked after the loop body executes)

> 用中文提示：后条件循环（REPEAT...UNTIL），因为流程图中先执行循环体，然后才检查条件。

---

## 2021 May/June (9618/22)

### Question 2 (a)

**(i)** Complete the table for the state-transition diagram. **[4 marks]**

| | Answer |
|---|--------|
| The number of transitions that result in a different state | 2 ✓ |
| The number of transitions with associated outputs | 2 ✓ |
| The label that should replace 'X' | S1 (start state) ✓ |
| The final or halting state | S3 ✓ |

> 用中文提示：根据状态转换图：转换到不同状态的数量（不包括自环）、有输出的转换数量、起始状态标签、终止状态。

**(ii)** Four consecutive "Low level detected" inputs from state S1. **[2 marks]**

- Number of outputs: 2 ✓
  - Input 1 (S1): Low level detected → Activate pump (output) → S2
  - Input 2 (S2): Low level detected → no output → stays at S2 (self-loop)
  - Input 3 (S2): Low level detected → no output → stays at S2
  - Input 4 (S2): Low level detected → no output → stays at S2

- Current state: S2 ✓

> 用中文提示：从 S1 开始，第一个"Low level detected"有输出（Activate pump）并转到 S2。之后在 S2 的"Low level detected"是自环，无输出。所以共 2 次输出（包括第一次从S1到S2的），最终状态 S2。

### Question 2 (b)

**(i)** Three items of data for each loan. **[2 marks]**

Any three from:
- ✓ Book identifier / ISBN / book title
- ✓ Borrower identifier / member ID / borrower name
- ✓ Date of loan / date borrowed
- ✓ Date due for return / loan period
- ✓ Date returned

> 用中文提示：每笔借阅需要记录：哪本书、谁借的、什么时候借的（或到期日）。

**(ii)** One item of data in the library system but not stored per loan. **[1 mark]**

Any one from:
- ✓ The borrower's address / contact details / phone number
- ✓ The book's author / publisher / genre
- ✓ The maximum loan period

> 用中文提示：属于图书馆系统但不需要每笔借阅都存储的数据，例如借阅者的地址或书籍的作者信息。

**(iii)** Two other operations on loan data. **[2 marks]**

Any two from:
- ✓ Add a new loan record (when a book is borrowed)
- ✓ Delete/update a loan record (when a book is returned)
- ✓ Search for a specific loan / check if a book is currently on loan
- ✓ Count the number of books currently borrowed by a specific user
- ✓ Extend/renew a loan

> 用中文提示：除了列出逾期图书外，还可以：新增借阅记录、删除/更新记录（还书时）、查找特定借阅等。

### Question 4

Detailed description of the algorithm to assign grades and output average mark. **[6 marks]**

- ✓ Step 1: Input the number of students (or use a known class size)
- ✓ Step 2: Set up a running total variable initialised to 0
- ✓ Step 3: Loop for each student:
  - Input the student's mark
  - Add the mark to the running total
- ✓ Step 4: Determine the grade based on the mark using selection (e.g., IF or CASE structure with defined grade boundaries such as: A >= 70, B >= 60, C >= 50, etc.)
- ✓ Step 5: Output the student's grade
- ✓ Step 6: After all students have been processed, calculate the average (total divided by number of students) and output it

> 用中文提示：算法描述（不写伪代码）：输入学生数量 → 循环输入每个学生分数 → 累加总分 → 根据分数范围判定等级并输出 → 最后计算平均分并输出。
