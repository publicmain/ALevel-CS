# Chapter 11: Programming - Paper 2 Answers

Mark scheme style answers with detailed marking points.

---

## 2024 May/June (9618/22)

### Question 1

**(a)** Complete the table with ticks. **[4 marks]**

| Pseudocode example | Selection | Iteration | Input/Output |
|-------------------|-----------|-----------|--------------|
| `FOR Index ← 1 TO 10` / `Data[Index] ← 0` / `NEXT Index` | | ✓ | |
| `WRITEFILE ThisFile, "****"` | | | ✓ |
| `UNTIL Level > 25` | | ✓ | |
| `IF Mark > 74 THEN` / `READFILE OldFile, Data` / `ENDIF` | ✓ | | ✓ |

Mark points:
- ✓ FOR...NEXT is iteration only
- ✓ WRITEFILE is input/output only
- ✓ UNTIL is iteration only (part of REPEAT...UNTIL)
- ✓ IF...ENDIF is selection AND READFILE is input/output (two ticks for this row)

> 用中文提示：FOR 循环 = 迭代；WRITEFILE/READFILE = 输入输出；UNTIL = 迭代（REPEAT...UNTIL 的一部分）；IF = 选择。最后一行同时有选择（IF）和输入输出（READFILE）。

**(b)** Complete function expressions. **[4 marks]**

| Expression |
|------------|
| MyInt ← **INT**(3.1415926) ✓ |
| MyChar ← **MID**("Elwood", 3, 1) ✓ |
| MyString ← **NUM_TO_STR**(**INT**(27.509)) ✓ |
| MyInt ← **STR_TO_NUM**(**RIGHT**("ABC123", 3)) ✓ |

Explanations:
- ✓ INT() truncates the real number to integer → MyInt = 3
- ✓ MID() extracts 1 character from position 3 → MyChar = 'w'
- ✓ INT(27.509) = 27, then NUM_TO_STR(27) = "27" → MyString = "27"
- ✓ RIGHT("ABC123", 3) = "123", then STR_TO_NUM("123") = 123 → MyInt = 123

> 用中文提示：INT() 取整、MID() 取子串、NUM_TO_STR() 数字转字符串、STR_TO_NUM() 字符串转数字、RIGHT() 取右边字符。

**(c)** Documenting variables. **[2 marks]**

- ✓ A suitable way: an identifier table / data dictionary / variable table
- ✓ Additional information: the purpose/use of the variable (what it represents) / valid range of values / scope of the variable

> 用中文提示：用标识符表（Identifier Table）记录变量信息。除了数据类型外，还应记录变量的用途/含义。

### Question 4

Pseudocode for procedure IsRA(). **[5 marks]**

```
PROCEDURE IsRA()
  DECLARE A, B, C, Temp : INTEGER

  OUTPUT "Enter three side lengths"
  INPUT A                                        // ✓ input three values
  INPUT B
  INPUT C

  // Find the longest side and assign to A       // ✓ find longest side
  IF B > A AND B > C THEN
    Temp ← A
    A ← B
    B ← Temp
  ELSE
    IF C > A AND C > B THEN
      Temp ← A
      A ← C
      C ← Temp
    ENDIF
  ENDIF

  IF A * A = (B * B) + (C * C) THEN             // ✓ test equation
    OUTPUT "This is a right-angled triangle"     // ✓ output message for right-angled
  ELSE
    OUTPUT "This is NOT a right-angled triangle" // ✓ output message for not right-angled
  ENDIF
ENDPROCEDURE
```

Mark points:
- ✓ Input three integer values
- ✓ Find the largest value (rearrange so A is the longest side)
- ✓ Test using A * A = (B * B) + (C * C)
- ✓ Output suitable message if right-angled
- ✓ Output suitable message if not right-angled

Python equivalent:
```python
def IsRA():
    A = int(input("Enter side 1: "))
    B = int(input("Enter side 2: "))
    C = int(input("Enter side 3: "))

    # Ensure A is the largest
    if B > A:
        A, B = B, A
    if C > A:
        A, C = C, A

    if A * A == (B * B) + (C * C):
        print("This is a right-angled triangle")
    else:
        print("This is NOT a right-angled triangle")
```

> 用中文提示：先输入三条边，然后找出最长边赋给 A（可能需要交换），再用勾股定理 A²=B²+C² 判断是否为直角三角形。

### Question 5

**(a)(i)** Three errors in the pseudocode. **[3 marks]**

- ✓ Syntax error 1: `INPUT Data[Index]` — Index is 0, but the array index starts from 1 / OR the INPUT statement should not be there at all as it is before the loop
- ✓ Syntax error 2: `NEXT Index` — this is FOR loop syntax but the loop uses WHILE...ENDWHILE. Should be `ENDWHILE` instead of `NEXT Index`
- ✓ Other error: The `WHILE` loop and `NEXT Index` are mixed — the loop structure is inconsistent. The WHILE loop has no ENDWHILE, and NEXT Index belongs to a FOR loop. (OR: `Index ← 0` then `Data[Index]` causes an out-of-range error since the first element index is 1)

> 用中文提示：语法错误1：WHILE 和 NEXT 混用（WHILE 应配 ENDWHILE，NEXT 配 FOR）。语法错误2：Index 初始为 0，但数组从索引 1 开始。其他错误：INPUT Data[Index] 在循环外且 Index=0 时数组越界。

**(a)(ii)** Statement that is not needed. **[2 marks]**

- Statement: ✓ `OTHERWISE : OUTPUT "Alarm 1201"`
- Explanation: ✓ The expression `Index MOD 2` can only produce values 0 or 1 (since any integer modulo 2 is either 0 or 1). Therefore, the OTHERWISE case can never be reached and is unnecessary.

> 用中文提示：`Index MOD 2` 只能得到 0 或 1，所以 OTHERWISE 分支永远不会执行，是多余的。

### Question 6

**(a)** Pseudocode for function Trim(). **[7 marks]**

```
FUNCTION Trim(Title : STRING) RETURNS STRING
  DECLARE Result : STRING
  DECLARE SpacePos : INTEGER

  IF LENGTH(Title) <= 16 THEN                    // ✓ check if trimming needed
    RETURN Title
  ENDIF

  Result ← Title                                 // ✓ initialise working string

  WHILE LENGTH(Result) >= 14 DO                  // ✓ loop removing words
    SpacePos ← LENGTH(Result)                    // ✓ find last space
    WHILE MID(Result, SpacePos, 1) <> ' ' DO
      SpacePos ← SpacePos - 1
    ENDWHILE
    Result ← LEFT(Result, SpacePos - 1)          // ✓ remove last word and preceding space
  ENDWHILE

  Result ← Result & "..."                        // ✓ add three dots
  RETURN Result                                  // ✓ return result
ENDFUNCTION
```

Mark points:
- ✓ Function header with string parameter, returns STRING
- ✓ Check if title is already 16 characters or fewer (no trimming needed)
- ✓ Loop to remove words while length >= 14
- ✓ Find the position of the last space character
- ✓ Remove the last word (and its preceding space) from the string
- ✓ Append "..." to the result after loop ends
- ✓ Return the result string

Python equivalent:
```python
def Trim(title):
    if len(title) <= 16:
        return title
    result = title
    while len(result) >= 14:
        space_pos = result.rfind(' ')
        result = result[:space_pos]
    return result + "..."
```

> 用中文提示：Trim 函数：如果标题 ≤16 字符则直接返回；否则循环从末尾删除单词（找到最后一个空格，截取空格前的部分），直到长度 <14，然后加上 "..."。

**(b)(i)** Drawback of adding leading '0' characters. **[1 mark]**

- ✓ Wastes storage space / increases file size because each sample uses 8 characters regardless of its actual value (e.g., the value 48 only needs 2 characters but uses 8)

> 用中文提示：前导零浪费存储空间，每个样本都占用固定 8 个字符。

**(b)(ii)** Alternative method without leading zeros. **[1 mark]**

- ✓ Use a delimiter/separator character between each sample value (e.g., a comma: "456,48,37652,...,673")

> 用中文提示：用分隔符（如逗号）分隔每个样本值，不需要前导零。

**(b)(iii)** Drawback of the alternative method. **[1 mark]**

- ✓ The file size becomes variable / individual samples cannot be accessed directly by position (need to parse the string to find each sample) / may use more storage for large values if delimiter is counted

> 用中文提示：使用分隔符后不能直接通过位置计算定位每个样本，需要解析字符串才能提取。

### Question 8

**(a)** Reason for splitting into stages and benefit. **[2 marks]**

- ✓ Reason: The problem is complex, so it is split into smaller, more manageable sub-problems (decomposition) / each stage performs a distinct task making it easier to develop and test
- ✓ Benefit: If an error occurs, the file from the previous stage can be examined to help locate which stage caused the error / provides an audit trail for debugging

> 用中文提示：分阶段的原因：分解复杂问题使其更易管理和测试。好处：每个阶段产生的文件可用于调试，方便定位错误。

**(b)** Pseudocode for DeleteSpaces(). **[6 marks]**

```
FUNCTION DeleteSpaces(Line : STRING) RETURNS STRING
  DECLARE Index : INTEGER                        // ✓

  IF LENGTH(Line) = 0 THEN                       // ✓ handle empty string
    RETURN ""
  ENDIF

  Index ← 1                                     // ✓ start from first character

  WHILE Index <= LENGTH(Line) AND MID(Line, Index, 1) = ' ' DO   // ✓ find first non-space
    Index ← Index + 1
  ENDWHILE

  IF Index > LENGTH(Line) THEN                   // ✓ all spaces
    RETURN ""
  ENDIF

  RETURN RIGHT(Line, LENGTH(Line) - Index + 1)   // ✓ return from first non-space to end
ENDFUNCTION
```

Mark points:
- ✓ Function header correct
- ✓ Handle edge case of empty string
- ✓ Initialise index to 1
- ✓ Loop while character at Index is a space
- ✓ Increment Index in loop
- ✓ Return substring from first non-space character to end of line

Python equivalent:
```python
def DeleteSpaces(line):
    index = 0
    while index < len(line) and line[index] == ' ':
        index += 1
    return line[index:]
```

> 用中文提示：DeleteSpaces 函数：从字符串开头逐个检查字符，跳过所有空格，返回从第一个非空格字符开始的子串。

**(c)** Pseudocode for Stage_2(). **[8 marks]**

```
PROCEDURE Stage_2(InputFile : STRING, OutputFile : STRING)
  DECLARE Line : STRING                          // ✓
  DECLARE BlankCount : INTEGER

  BlankCount ← 0                                 // ✓

  OPENFILE InputFile FOR READ                    // ✓ open input file
  OPENFILE OutputFile FOR APPEND                 // ✓ open output file (APPEND as it already exists)

  WHILE NOT EOF(InputFile) DO                    // ✓ loop through input file
    READFILE InputFile, Line
    Line ← DeleteSpaces(Line)                    // ✓ remove leading spaces
    Line ← DeleteComment(Line)                   // ✓ remove comments

    IF LENGTH(Line) = 0 THEN                     // ✓ check for blank line
      BlankCount ← BlankCount + 1
    ELSE
      WRITEFILE OutputFile, Line
    ENDIF
  ENDWHILE

  CLOSEFILE InputFile
  CLOSEFILE OutputFile

  OUTPUT "Blank lines removed: " & NUM_TO_STR(BlankCount)   // ✓ output count
ENDPROCEDURE
```

Mark points:
- ✓ Procedure header with two string parameters
- ✓ Initialise blank line counter to 0
- ✓ Open input file for READ
- ✓ Open output file for APPEND (existing file)
- ✓ Loop through input file until EOF
- ✓ Call DeleteSpaces() to remove leading spaces
- ✓ Call DeleteComment() to remove comments
- ✓ Check if resulting line is blank; if so, increment counter; if not, write to output file
- ✓ Output message with count of blank lines removed

> 用中文提示：Stage_2 过程：打开输入和输出文件 → 循环读取每行 → 调用 DeleteSpaces() 和 DeleteComment() 处理 → 空行计数不写入 → 非空行写入输出文件 → 最后输出删除的空行数。

---

## 2024 Oct/Nov (9618/22)

### Question 1 (d)

Data types for variables. **[3 marks]**

| Variable name | Used to store | Data type |
|--------------|--------------|-----------|
| Name | A customer name | STRING ✓ |
| Index | An array index | INTEGER ✓ |
| Result | The result of division of any two non-zero numbers | REAL ✓ |

> 用中文提示：客户姓名用 STRING，数组索引用 INTEGER，除法结果可能有小数所以用 REAL。

### Question 2

Pseudocode for function Conceal(). **[6 marks]**

```
FUNCTION Conceal(CardNum : STRING) RETURNS STRING
  DECLARE Result : STRING                        // ✓
  DECLARE Index : INTEGER
  DECLARE CardLength : INTEGER

  CardLength ← LENGTH(CardNum)                   // ✓ get length
  Result ← ""                                    // ✓ initialise result

  FOR Index ← 1 TO CardLength - 4               // ✓ loop for characters to replace
    Result ← Result & "*"                        // ✓ replace with asterisk
  NEXT Index

  Result ← Result & RIGHT(CardNum, 4)            // ✓ append last 4 characters
  RETURN Result
ENDFUNCTION
```

Mark points:
- ✓ Function header with string parameter, returns STRING
- ✓ Determine the length of the card number
- ✓ Initialise result string
- ✓ Loop to add asterisks for all characters except the last 4
- ✓ Concatenate asterisks with the last 4 characters (using RIGHT function)
- ✓ Return the modified string

Python equivalent:
```python
def Conceal(card_num):
    hidden_length = len(card_num) - 4
    return '*' * hidden_length + card_num[-4:]
```

> 用中文提示：Conceal 函数：计算需要隐藏的字符数（总长度减 4），用 '*' 替换前面的字符，保留最后 4 个字符。

### Question 6

**(a)** Pseudocode for procedure Special(). **[7 marks]**

```
PROCEDURE Special()
  DECLARE Fill1, Fill2 : STRING                  // ✓
  DECLARE BreadChoice : STRING
  DECLARE Index1, Index2, Index3 : INTEGER

  REPEAT                                         // ✓ find first valid filling
    Index1 ← INT(RAND(35)) + 1
  UNTIL Filling[Index1] <> ""

  REPEAT                                         // ✓ find second different valid filling
    Index2 ← INT(RAND(35)) + 1
  UNTIL Filling[Index2] <> "" AND Index2 <> Index1    // ✓ must be different and non-empty

  REPEAT                                         // ✓ find valid bread
    Index3 ← INT(RAND(10)) + 1
  UNTIL Bread[Index3] <> ""

  Fill1 ← Filling[Index1]                        // ✓
  Fill2 ← Filling[Index2]
  BreadChoice ← Bread[Index3]

  OUTPUT "The daily special is " & Fill1 & " and " & Fill2 & " on " & BreadChoice & " bread."  // ✓
ENDPROCEDURE
```

Mark points:
- ✓ Generate random index for first filling in valid range
- ✓ Check first filling is not an empty string (repeat if empty)
- ✓ Generate random index for second filling
- ✓ Ensure second filling is different from first AND not empty
- ✓ Generate random index for bread, ensure not empty
- ✓ Retrieve values from arrays
- ✓ Output formatted message with two fillings and bread

Python equivalent:
```python
import random
def Special():
    while True:
        i1 = random.randint(0, 34)
        if Filling[i1] != "":
            break
    while True:
        i2 = random.randint(0, 34)
        if Filling[i2] != "" and i2 != i1:
            break
    while True:
        i3 = random.randint(0, 9)
        if Bread[i3] != "":
            break
    print(f"The daily special is {Filling[i1]} and {Filling[i2]} on {Bread[i3]} bread.")
```

> 用中文提示：Special 过程：随机选择两个不同的、非空的馅料和一种非空的面包。用 REPEAT...UNTIL 循环确保随机选择的元素不是空字符串且两个馅料不同。

**(b)** Preventing certain filling combinations. **[2 marks]**

- ✓ Create a 2D array (or a list of pairs) that stores the combinations of fillings that should not go together
- ✓ After randomly selecting two fillings, check whether they appear together in the incompatible combinations list. If they do, repeat the random selection until a valid combination is found.

> 用中文提示：建立一个"不兼容组合"列表（二维数组），随机选择后检查两个馅料是否在列表中，如果是则重新选择。

---

## 2023 May/June (9618/22)

### Question 1

**(a)(i)** More appropriate way of representing postal costs. **[1 mark]**

- ✓ Use a named constant (e.g., CONSTANT PostalCost = 3.75)

> 用中文提示：使用命名常量（Named Constant）代替硬编码的数值，例如 CONSTANT PostalCost = 3.75。

**(a)(ii)** Advantages of using a named constant. **[3 marks]**

- ✓ The value only needs to be changed in one place if the postal cost changes (easier maintenance)
- ✓ The name makes the code more readable / self-documenting (PostalCost is more meaningful than 3.75)
- ✓ Reduces the risk of errors — if the value needs to change, there is no risk of missing an occurrence / prevents accidental modification of the value during program execution

> 用中文提示：命名常量的好处：①只需在一处修改值 ②代码更易读 ③减少出错风险（不会被意外修改）。

**(b)** Three features that make the code easier to understand. **[3 marks]**

- ✓ Meaningful/descriptive variable names (e.g., Weight, ValidAddress, ItemPostalCost, ItemStatus)
- ✓ Comments (e.g., // set postal cost for item to $3.75)
- ✓ Indentation (the statements inside the IF block are indented)

> 用中文提示：提高代码可读性的特征：有意义的变量名、注释、缩进。

**(c)** Data types. **[3 marks]**

- ValidAddress: ✓ BOOLEAN
- ItemPostalCost: ✓ REAL
- ItemStatus: ✓ STRING

> 用中文提示：TRUE/FALSE 用 BOOLEAN，金额（带小数）用 REAL，文本（如 "Valid"）用 STRING。

### Question 4

Pseudocode for function GetNum(). **[6 marks]**

```
FUNCTION GetNum(Text : STRING, SearchChar : CHAR) RETURNS INTEGER
  DECLARE Count : INTEGER                        // ✓
  DECLARE Index : INTEGER

  Count ← 0                                     // ✓ initialise counter

  FOR Index ← 1 TO LENGTH(Text)                 // ✓ loop through string
    IF MID(Text, Index, 1) = SearchChar THEN     // ✓ compare characters (case sensitive)
      Count ← Count + 1                         // ✓ increment counter
    ENDIF
  NEXT Index

  RETURN Count                                   // ✓ return the count
ENDFUNCTION
```

Mark points:
- ✓ Function header with STRING and CHAR parameters, RETURNS INTEGER
- ✓ Initialise Count to 0
- ✓ Loop through each character of the string
- ✓ Compare each character with SearchChar (case sensitive — no conversion needed)
- ✓ Increment Count when match found
- ✓ Return Count

Python equivalent:
```python
def GetNum(text, search_char):
    count = 0
    for char in text:
        if char == search_char:  # case sensitive
            count += 1
    return count
```

> 用中文提示：GetNum 函数：遍历字符串的每个字符，与目标字符比较（区分大小写），匹配则计数加 1，最后返回计数。

### Question 6

Pseudocode for procedure Square(). **[6 marks]**

```
PROCEDURE Square(Num : INTEGER)
  DECLARE Row, Col : INTEGER                     // ✓
  DECLARE NumChar : STRING
  DECLARE Line : STRING

  NumChar ← NUM_TO_STR(Num)                      // ✓ convert to character

  FOR Row ← 1 TO Num                            // ✓ loop for each row
    Line ← ""
    FOR Col ← 1 TO Num                          // ✓ loop for each column
      IF Row = 1 OR Row = Num OR Col = 1 OR Col = Num THEN   // ✓ boundary check
        Line ← Line & NumChar
      ELSE
        Line ← Line & "*"                       // ✓ inside character
      ENDIF
    NEXT Col
    OUTPUT Line
  NEXT Row
ENDPROCEDURE
```

Mark points:
- ✓ Procedure header with INTEGER parameter
- ✓ Convert parameter to a character/string for output
- ✓ Outer loop for rows (1 to Num)
- ✓ Inner loop for columns (1 to Num)
- ✓ Condition to check if on boundary (first/last row or first/last column)
- ✓ Use parameter digit for boundary, '*' for interior

Python equivalent:
```python
def Square(num):
    for row in range(num):
        line = ""
        for col in range(num):
            if row == 0 or row == num-1 or col == 0 or col == num-1:
                line += str(num)
            else:
                line += "*"
        print(line)
```

> 用中文提示：Square 过程：双重循环（行和列），如果在边界（第一/最后行或第一/最后列）则输出数字字符，否则输出 '*'。

### Question 8

**(a)** Pseudocode for CheckInfo(). **[7 marks]**

```
FUNCTION CheckInfo(Info : STRING) RETURNS BOOLEAN
  DECLARE ItemNum : STRING                       // ✓
  DECLARE SuppCode : STRING
  DECLARE Description : STRING
  DECLARE NumVal : INTEGER

  IF LENGTH(Info) < 19 THEN                      // ✓ minimum length check (4+3+12=19)
    RETURN FALSE
  ENDIF

  ItemNum ← LEFT(Info, 4)                        // ✓ extract ItemNum
  SuppCode ← MID(Info, 5, 3)                     // ✓ extract SupplierCode
  Description ← RIGHT(Info, LENGTH(Info) - 7)    // ✓ extract Description

  // Check ItemNum is numeric and in range
  NumVal ← STR_TO_NUM(ItemNum)
  IF NumVal < 1 OR NumVal > 5999 THEN            // ✓ validate range
    RETURN FALSE
  ENDIF

  // Check SupplierCode is all alphabetic
  IF OnlyAlpha(SuppCode) = FALSE THEN            // ✓ use OnlyAlpha module
    RETURN FALSE
  ENDIF

  // Check Description is at least 12 characters
  IF LENGTH(Description) < 12 THEN
    RETURN FALSE
  ENDIF

  RETURN TRUE
ENDFUNCTION
```

Mark points:
- ✓ Function header with string parameter, returns BOOLEAN
- ✓ Extract ItemNum (first 4 characters)
- ✓ Validate ItemNum is in range "0001" to "5999"
- ✓ Extract SupplierCode (next 3 characters)
- ✓ Use OnlyAlpha() to check SupplierCode contains only alphabetic characters
- ✓ Extract Description (remaining characters)
- ✓ Check Description is at least 12 characters long

> 用中文提示：CheckInfo 函数：从字符串中提取三个部分（ItemNum 前 4 字符、SupplierCode 接下来 3 字符、Description 剩余部分），分别验证：ItemNum 在 0001-5999 范围内、SupplierCode 全是字母（用 OnlyAlpha）、Description 至少 12 字符。

**(b)** Pseudocode for AddItem(). **[7 marks]**

```
PROCEDURE AddItem(NewInfo : STRING)
  DECLARE Line : STRING                          // ✓
  DECLARE Added : BOOLEAN
  DECLARE NewItemNum : STRING

  NewItemNum ← LEFT(NewInfo, 4)                  // ✓ extract item number
  Added ← FALSE

  OPENFILE "Stock.txt" FOR READ                  // ✓ open source file
  OPENFILE "NewStock.txt" FOR WRITE              // ✓ open destination file

  WHILE NOT EOF("Stock.txt") DO                  // ✓ loop through file
    READFILE "Stock.txt", Line

    IF Added = FALSE AND NewItemNum < LEFT(Line, 4) THEN   // ✓ find correct position
      WRITEFILE "NewStock.txt", NewInfo           // ✓ write new item
      Added ← TRUE
    ENDIF

    WRITEFILE "NewStock.txt", Line                // write existing line
  ENDWHILE

  IF Added = FALSE THEN                          // handle case where new item goes at end
    WRITEFILE "NewStock.txt", NewInfo
  ENDIF

  CLOSEFILE "Stock.txt"
  CLOSEFILE "NewStock.txt"
ENDPROCEDURE
```

Mark points:
- ✓ Open Stock.txt for READ and NewStock.txt for WRITE
- ✓ Extract item number from new info for comparison
- ✓ Loop through each line of Stock.txt
- ✓ Compare new item number with current line's item number
- ✓ Write new item at the correct position (before the first item with a larger number)
- ✓ Copy all existing lines to NewStock.txt
- ✓ Handle case where new item should be added at the end / close both files

> 用中文提示：AddItem 过程：打开原文件读取，打开新文件写入。逐行读取原文件，在正确位置（按 ItemNum 升序）插入新记录，其余行照抄到新文件。

---

## 2023 Oct/Nov (9618/22)

### Question 1

**(a)** Identifier table. **[4 marks]**

| Example value | Explanation | Variable name | Data type |
|--------------|-------------|---------------|-----------|
| "Mr Khan" | The name of the customer | CustomerName ✓ | STRING ✓ |
| 3 | The number of items in the order | NumItems ✓ | INTEGER ✓ |
| TRUE | Whether this is a new customer | IsNewCustomer ✓ | BOOLEAN ✓ |
| 15.75 | The deposit paid by the customer | Deposit ✓ | REAL ✓ |

> 用中文提示：变量命名要有意义。数据类型根据示例值判断：带引号的文本 = STRING，整数 = INTEGER，TRUE/FALSE = BOOLEAN，带小数 = REAL。

**(b)** Evaluate expressions. **[4 marks]**

| Expression | Evaluates to |
|-----------|-------------|
| (Total * DepRate) + 1.5 | (124.00 * 2.00) + 1.5 = **249.5** ✓ |
| RIGHT(Description, 7) | **"(small)"** ✓ |
| (LENGTH(Description) - 8) > 16 | (31 - 8) > 16 = 23 > 16 = **TRUE** ✓ |
| NUM_TO_STR(INT(DepRate * 10)) & '%' | NUM_TO_STR(INT(20.0)) & '%' = "20" & '%' = **"20%"** ✓ |

> 用中文提示：逐步计算表达式：注意 RIGHT 取右边字符、LENGTH 返回字符串长度、INT 取整、NUM_TO_STR 转字符串、& 连接字符串。

### Question 4

**(a)** Pseudocode for procedure Count(). **[6 marks]**

```
PROCEDURE Count()
  DECLARE Value : INTEGER                        // ✓
  DECLARE OddCount, EvenCount : INTEGER

  OddCount ← 0                                  // ✓ initialise counters
  EvenCount ← 0

  REPEAT                                         // ✓ loop structure
    OUTPUT "Enter a value (99 to stop): "
    INPUT Value                                  // ✓ input value

    IF Value <> 99 THEN                          // ✓ exclude 99 from counting
      IF Value MOD 2 = 0 THEN
        EvenCount ← EvenCount + 1
      ELSE
        OddCount ← OddCount + 1
      ENDIF
    ENDIF
  UNTIL Value = 99                               // ✓ stop condition

  OUTPUT "Odd values: " & NUM_TO_STR(OddCount)
  OUTPUT "Even values: " & NUM_TO_STR(EvenCount)
ENDPROCEDURE
```

Mark points:
- ✓ Declare and initialise two counters (odd and even) to 0
- ✓ REPEAT...UNTIL loop
- ✓ Input value
- ✓ Check if value is odd or even using MOD 2
- ✓ Do not count the value 99
- ✓ Output both counts with suitable messages after loop ends

> 用中文提示：Count 过程：初始化奇数和偶数计数器为 0 → REPEAT 循环输入值 → 判断奇偶（MOD 2）→ 值为 99 时不计数且退出循环 → 输出两个计数。

**(b)** Three test data sequences. **[3 marks]**

| Sequence | Test data | Purpose |
|----------|-----------|---------|
| 1 | 99 | ✓ Test with only the terminating value — both counts should be 0 (boundary test) |
| 2 | 3, 5, 7, 99 | ✓ Test with only odd values — even count should be 0 |
| 3 | 2, 4, 6, 99 | ✓ Test with only even values — odd count should be 0 |

> 用中文提示：三种测试序列：①只输入 99（边界测试，计数应为 0）②只有奇数 ③只有偶数。

### Question 6

**(a)** Pseudocode for CreateFiles(). **[6 marks]**

```
PROCEDURE CreateFiles(FileName : STRING, NumFiles : INTEGER)
  DECLARE Count : INTEGER                        // ✓
  DECLARE Suffix : STRING
  DECLARE FullName : STRING

  FOR Count ← 1 TO NumFiles                     // ✓ loop for number of files
    // Create three-character suffix
    IF Count < 10 THEN                           // ✓ format suffix as 3 characters
      Suffix ← ".00" & NUM_TO_STR(Count)
    ELSE
      IF Count < 100 THEN
        Suffix ← ".0" & NUM_TO_STR(Count)
      ELSE
        Suffix ← "." & NUM_TO_STR(Count)
      ENDIF
    ENDIF

    FullName ← FileName & Suffix                  // ✓ create full filename

    OPENFILE FullName FOR WRITE                   // ✓ create file
    WRITEFILE FullName, "This is File " & FullName   // ✓ write content
    CLOSEFILE FullName
  NEXT Count
ENDPROCEDURE
```

Mark points:
- ✓ Procedure header with string and integer parameters
- ✓ Loop from 1 to NumFiles
- ✓ Create 3-character suffix with leading zeros (e.g., .001, .010, .100)
- ✓ Concatenate filename with suffix
- ✓ Open/create each file for writing
- ✓ Write the required content string and close the file

> 用中文提示：CreateFiles 过程：循环创建指定数量的文件。关键是生成三位数的后缀（前补零），例如 .001, .002, ..., .010, ..., .100。

**(b)(i)** Type of module for CheckFiles(). **[1 mark]**

- ✓ FUNCTION (because it needs to return a count value)

> 用中文提示：CheckFiles 应该是 FUNCTION，因为它需要返回文件数量。

**(b)(ii)** Module header for CheckFiles(). **[1 mark]**

```
FUNCTION CheckFiles(FileName : STRING) RETURNS INTEGER   // ✓
```

> 用中文提示：函数头：接受文件名字符串参数，返回整数（文件数量）。

**(b)(iii)** File mode for CheckFiles(). **[1 mark]**

- ✓ READ mode (the procedure only needs to check if files exist / read them, not modify them)

> 用中文提示：用 READ 模式打开文件，因为只需要检查文件是否存在，不需要修改。

### Question 8

**(a)** Pseudocode for GetPort(). **[7 marks]**

```
FUNCTION GetPort(DestID : STRING) RETURNS INTEGER
  DECLARE IDNum : INTEGER                        // ✓
  DECLARE Row : INTEGER

  IDNum ← STR_TO_NUM(DestID)                     // ✓ convert string to integer

  Row ← 1                                       // ✓ start search
  WHILE Row <= 6 DO                              // ✓ loop through RouteTable
    IF RouteTable[Row, 1] = -1 THEN              // ✓ check for -1 (no range)
      RETURN -1
    ENDIF
    IF IDNum >= RouteTable[Row, 1] AND IDNum <= RouteTable[Row, 2] THEN   // ✓ check range
      RETURN RouteTable[Row, 3]                  // ✓ return port number
    ENDIF
    Row ← Row + 1
  ENDWHILE

  RETURN -1                                      // no match found
ENDFUNCTION
```

Mark points:
- ✓ Function header with string parameter, returns INTEGER
- ✓ Convert DestinationID string to integer for comparison
- ✓ Loop through rows of RouteTable
- ✓ Check for -1 sentinel value (end of valid entries)
- ✓ Compare IDNum with range (column 1 and column 2)
- ✓ Return port number (column 3) when match found
- ✓ Return -1 if no matching range found

> 用中文提示：GetPort 函数：将目标 ID 转为整数，遍历 RouteTable 每行，检查 ID 是否在该行的范围内（列1~列2），是则返回端口号（列3），遇到 -1 或遍历完则返回 -1。

**(b)** Pseudocode for ProcessMsg(). **[7 marks]**

```
PROCEDURE ProcessMsg(Message : STRING)
  DECLARE DestID : STRING                        // ✓
  DECLARE Port : INTEGER
  DECLARE Success : BOOLEAN

  IF LENGTH(Message) <= 3 THEN                   // ✓ ignore zero-length data field
    RETURN
  ENDIF

  DestID ← LEFT(Message, 3)                     // ✓ extract DestinationID
  Port ← GetPort(DestID)                        // ✓ get port number

  IF Port = -1 THEN                              // ✓ check if this computer
    // DestinationID is this computer — add to local stack (stack 0 or similar)
    Success ← StackMsg(Message, 0)
  ELSE
    // Forward message to appropriate port stack
    Success ← StackMsg(Message, Port)            // ✓ use StackMsg to add to stack
  ENDIF

  IF Success = FALSE THEN                        // ✓ check if message added successfully
    OUTPUT "Error: message could not be added to stack"
  ENDIF
ENDPROCEDURE
```

Mark points:
- ✓ Procedure header with string parameter
- ✓ Check for zero-length data (message length <= 3, since DestID is 3 chars)
- ✓ Extract DestinationID (first 3 characters)
- ✓ Call GetPort() with DestinationID
- ✓ Determine if message is for this computer or to be forwarded
- ✓ Call StackMsg() with message and appropriate stack number
- ✓ Output error if StackMsg() returns FALSE

> 用中文提示：ProcessMsg 过程：检查数据字段是否为空 → 提取前 3 位目标 ID → 调用 GetPort() 获取端口 → 根据结果决定是本机消息还是转发 → 调用 StackMsg() 入栈 → 失败则输出错误消息。

**(c)(i)** Problem with using a stack. **[3 marks]**

- ✓ Circumstance: Lines from the file are sent sequentially (line 1, then line 2, etc.) and pushed onto the stack
- ✓ Problem: A stack is LIFO (Last In, First Out), so when messages are popped from the stack, they come out in reverse order
- ✓ This means the file will be written with lines in the wrong (reversed) order

> 用中文提示：栈是后进先出（LIFO），文件行按顺序入栈后，出栈时顺序是反的，导致文件内容顺序颠倒。

**(c)(ii)** More appropriate ADT. **[1 mark]**

- ✓ Queue — because a queue is FIFO (First In, First Out), so the lines would be retrieved in the same order they were received

> 用中文提示：队列（Queue）是先进先出（FIFO），可以保持文件行的原始顺序。

---

## 2022 Oct/Nov (9618/22)

### Question 1

**(a)(i)** Two reasons for using a subroutine. **[2 marks]**

- ✓ Code reuse — the subroutine can be called from multiple places in the program, avoiding code duplication
- ✓ Makes the program easier to understand/maintain/debug — the program is broken into smaller, manageable modules (decomposition)

> 用中文提示：使用子程序的原因：①代码重用（避免重复）②程序更易理解、维护和调试。

**(a)(ii)** Term for Count and Message, and their use. **[2 marks]**

- Term: ✓ Parameters (formal parameters)
- Use: ✓ They receive values passed from the calling statement (arguments/actual parameters) when the procedure is called. They allow data to be passed into the procedure for it to use.

> 用中文提示：Count 和 Message 是形式参数（formal parameters），用于接收调用时传入的值（实际参数），使过程能够使用外部数据。

**(c)** Evaluate expressions. **[3 marks]**

| Expression | Evaluation |
|-----------|------------|
| MID(CharList, MONTH(FlagDay), 1) | MONTH(23/04/2004) = 4, MID("ABCDEF", 4, 1) = **"D"** ✓ |
| INT(Count / LENGTH(CharList)) | INT(29 / 6) = INT(4.833...) = **4** ✓ |
| (Count >= 29) AND (DAY(FlagDay) > 23) | (TRUE) AND (FALSE) = **FALSE** ✓ |

> 用中文提示：MONTH() 提取月份=4，MID 第 4 个字符是 "D"；INT(29/6) 取整=4；29>=29 为 TRUE 但 23>23 为 FALSE，TRUE AND FALSE = FALSE。

### Question 5

Rewrite as four separate IF statements. **[4 marks]**

```
IF A = TRUE AND B = TRUE AND C = TRUE THEN          // ✓
  CALL Sub1()
ENDIF

IF A = TRUE AND B = TRUE AND C = FALSE THEN          // ✓
  CALL Sub2()
ENDIF

IF (A = FALSE AND B = TRUE AND C = FALSE) OR (A = FALSE AND B = FALSE AND C = FALSE) THEN   // ✓
  CALL Sub3()
ENDIF

IF (A = FALSE AND B = TRUE AND C = TRUE) OR (A = FALSE AND B = FALSE AND C = TRUE) THEN     // ✓
  CALL Sub4()
ENDIF
```

Simplified:
```
IF A AND B AND C THEN CALL Sub1() ENDIF                           // ✓
IF A AND B AND NOT C THEN CALL Sub2() ENDIF                       // ✓
IF NOT A AND NOT C THEN CALL Sub3() ENDIF                         // ✓
IF NOT A AND C THEN CALL Sub4() ENDIF                             // ✓
```

Mark points:
- ✓ Sub1: A AND B AND C
- ✓ Sub2: A AND B AND NOT C
- ✓ Sub3: NOT A AND NOT C (simplified from the two cases where C is FALSE and A is FALSE)
- ✓ Sub4: NOT A AND C (simplified from the two cases where C is TRUE and A is FALSE)

> 用中文提示：分析嵌套 IF 的每个路径，找出调用每个子程序的条件：Sub1 需要 A、B、C 全为 TRUE；Sub2 需要 A 和 B 为 TRUE、C 为 FALSE；Sub3 需要 A 和 C 都为 FALSE；Sub4 需要 A 为 FALSE、C 为 TRUE。

### Question 6

**(a)** Pseudocode for FindBaseNumber(). **[7 marks]**

```
FUNCTION FindBaseNumber(Value : INTEGER) RETURNS INTEGER
  DECLARE Factorial : INTEGER                    // ✓
  DECLARE Base : INTEGER

  Factorial ← 1                                  // ✓ initialise
  Base ← 1                                       // ✓

  WHILE Factorial < Value DO                      // ✓ build up factorial
    Base ← Base + 1
    Factorial ← Factorial * Base                  // ✓ multiply by next number
  ENDWHILE

  IF Factorial = Value THEN                       // ✓ check if exact match
    RETURN Base
  ELSE
    RETURN -1                                    // ✓ not a factorial
  ENDIF
ENDFUNCTION
```

Mark points:
- ✓ Function header with integer parameter, returns INTEGER
- ✓ Initialise Factorial to 1
- ✓ Initialise Base to 1
- ✓ Loop while Factorial is less than Value
- ✓ Increment Base and multiply Factorial by Base
- ✓ After loop, check if Factorial equals Value exactly
- ✓ Return Base if match, -1 if not

Python equivalent:
```python
def FindBaseNumber(value):
    factorial = 1
    base = 1
    while factorial < value:
        base += 1
        factorial *= base
    if factorial == value:
        return base
    else:
        return -1
```

> 用中文提示：FindBaseNumber 函数：从 1 开始逐步计算阶乘（1, 1*2=2, 2*3=6, 6*4=24, 24*5=120...），直到阶乘 >= 参数值。如果恰好相等则返回底数，否则返回 -1。

**(b)** Four invalid test strings. **[4 marks]**

| Input | Reason for choice |
|-------|------------------|
| "" (empty string) | ✓ Test with no input / empty string — should be rejected |
| "abc" | ✓ Test with non-numeric characters — cannot be converted to integer |
| "-5" | ✓ Test with a negative number — not a positive, non-zero integer |
| "0" | ✓ Test with zero — the function requires a positive, non-zero value |

> 用中文提示：四种无效测试数据：空字符串、非数字字符串、负数、零。分别测试不同的验证方面。

### Question 7 (a)

Pseudocode for OutputError() using efficient search. **[6 marks]**

```
PROCEDURE OutputError(LineNum : INTEGER, ErrNum : INTEGER)
  DECLARE Low, High, Mid : INTEGER               // ✓
  DECLARE Found : BOOLEAN

  Low ← 1                                        // ✓ binary search setup
  High ← 500
  Found ← FALSE

  WHILE Low <= High AND Found = FALSE DO          // ✓ binary search loop
    Mid ← INT((Low + High) / 2)

    IF ErrCode[Mid] = ErrNum THEN                 // ✓ found
      OUTPUT ErrText[Mid] & " on line " & NUM_TO_STR(LineNum)
      Found ← TRUE
    ELSE
      IF ErrCode[Mid] < ErrNum THEN               // ✓ adjust search range
        Low ← Mid + 1
      ELSE
        High ← Mid - 1
      ENDIF
    ENDIF
  ENDWHILE

  IF Found = FALSE THEN                           // ✓ not found
    OUTPUT "Unknown error on line " & NUM_TO_STR(LineNum)
  ENDIF
ENDPROCEDURE
```

Mark points:
- ✓ Procedure header with two integer parameters
- ✓ Binary search (efficient — data is in ascending order)
- ✓ Initialise Low, High, Mid correctly
- ✓ Loop with correct termination condition
- ✓ Compare and adjust search range (Low or High)
- ✓ Output correct message (found or unknown error) with line number

> 用中文提示：因为 ErrCode 按升序排列，所以用二分查找（Binary Search）更高效。每次比较中间元素，缩小搜索范围。找到则输出错误描述，找不到则输出"未知错误"。

### Question 7 (b)

Efficient bubble sort for SortArrays(). **[8 marks]**

```
PROCEDURE SortArrays()
  DECLARE Top : INTEGER                          // ✓
  DECLARE Index : INTEGER
  DECLARE TempCode : INTEGER
  DECLARE TempText : STRING
  DECLARE Swapped : BOOLEAN

  Top ← 500                                     // ✓
  REPEAT                                         // ✓ outer loop
    Swapped ← FALSE                              // ✓ flag for optimisation
    FOR Index ← 1 TO Top - 1                     // ✓ inner loop
      IF ErrCode[Index] > ErrCode[Index + 1] THEN   // ✓ compare adjacent
        // Swap ErrCode elements
        TempCode ← ErrCode[Index]               // ✓ swap both arrays together
        ErrCode[Index] ← ErrCode[Index + 1]
        ErrCode[Index + 1] ← TempCode
        // Swap corresponding ErrText elements
        TempText ← ErrText[Index]
        ErrText[Index] ← ErrText[Index + 1]
        ErrText[Index + 1] ← TempText
        Swapped ← TRUE
      ENDIF
    NEXT Index
    Top ← Top - 1                                // ✓ reduce comparison range
  UNTIL Swapped = FALSE OR Top = 1
ENDPROCEDURE
```

Mark points:
- ✓ Procedure header
- ✓ Outer loop (REPEAT...UNTIL or WHILE)
- ✓ Boolean flag (Swapped) to detect when no swaps occur (optimisation)
- ✓ Inner loop through array elements
- ✓ Compare adjacent elements in ErrCode
- ✓ Swap ErrCode elements when out of order
- ✓ Also swap corresponding ErrText elements to keep arrays synchronised
- ✓ Reduce upper bound after each pass (Top ← Top - 1)

> 用中文提示：高效冒泡排序：用 Swapped 标志检测是否发生交换（无交换则已排好序可提前退出）。关键：交换 ErrCode 的同时必须同步交换 ErrText，保持两个数组的对应关系。每趟后减少比较范围。

---

## 2021 May/June (9618/22)

### Question 1

**(a)(i)** Data types. **[4 marks]**

| Variable | Example data value | Data type |
|----------|-------------------|-----------|
| Name | "Catherine" | STRING ✓ |
| Index | 100 | INTEGER ✓ |
| Modified | FALSE | BOOLEAN ✓ |
| Holiday | 25/12/2020 | DATE ✓ |

> 用中文提示：带引号的文本=STRING，整数=INTEGER，TRUE/FALSE=BOOLEAN，日期=DATE。

**(a)(ii)** Evaluate expressions. **[4 marks]**

| Expression | Evaluates to |
|-----------|-------------|
| Modified OR Index > 100 | FALSE OR FALSE = **FALSE** ✓ |
| LENGTH("Student: " & Name) | LENGTH("Student: Catherine") = **19** ✓ |
| INT(Index + 2.9) | INT(102.9) = **102** ✓ |
| MID(Name, 1, 3) | **"Cat"** ✓ |

> 用中文提示：Modified=FALSE, 100>100=FALSE, FALSE OR FALSE=FALSE；"Student: " 有 10 个字符 + "Catherine" 有 9 个字符 = 19；INT(102.9)=102；MID 从位置 1 取 3 个字符="Cat"。

**(b)** Selection, assignment, or iteration. **[3 marks]**

| Statement | Selection | Assignment | Iteration |
|-----------|-----------|------------|-----------|
| Index ← Index + 1 | | ✓ | |
| IF Modified = TRUE THEN | ✓ | | |
| ENDWHILE | | | ✓ |

> 用中文提示：← 是赋值，IF 是选择，ENDWHILE 是迭代（循环的一部分）。

### Question 5

**(a)(i)** Pseudocode for random array with counting. **[6 marks]**

```
DECLARE RNum : ARRAY[1:100] OF INTEGER           // ✓
DECLARE Index : INTEGER
DECLARE Count : INTEGER

Count ← 0                                        // ✓ initialise counter

FOR Index ← 1 TO 100                             // ✓ loop 100 times
  RNum[Index] ← INT(RAND(200)) + 1               // ✓ random 1 to 200
  IF RNum[Index] >= 66 AND RNum[Index] <= 173 THEN   // ✓ check range
    Count ← Count + 1
  ENDIF
NEXT Index

OUTPUT "Count: " & NUM_TO_STR(Count)              // ✓ output count
```

Mark points:
- ✓ Declare array of 100 integers
- ✓ Initialise count to 0
- ✓ Loop 100 times
- ✓ Generate random number 1 to 200 and assign to array element
- ✓ Check if value is between 66 and 173 inclusive
- ✓ Output the count

> 用中文提示：声明 100 元素的整数数组 → 循环生成 1-200 的随机数 → 检查是否在 66-173 范围内 → 计数并输出。RAND(200) 生成 0-199，加 1 得到 1-200。

**(a)(ii)** Changes for unique values. **[3 marks]**

- ✓ After generating a random number, check whether it already exists in the array (search through all previously assigned elements)
- ✓ If the value already exists, generate a new random number and check again (repeat until a unique value is found)
- ✓ Use a loop (e.g., REPEAT...UNTIL) to keep generating new values until a unique one is found, or use a flag variable to track whether a duplicate was found

> 用中文提示：为保证唯一值：生成随机数后，检查数组中已有元素是否重复。如果重复则重新生成，直到找到唯一值。需要内层循环来检查重复。

**(b)(i)** Examine the StringClean function. **[4 marks]**

| | Answer |
|---|--------|
| Give a line number containing an example of an initialisation statement | **07** (OutString ← "") ✓ |
| Give a line number containing the start of a repeating block of code | **09** (FOR Counter ← 1 TO LENGTH(InString)) ✓ |
| Give a line number containing a logic operation | **12** (NOT, OR) ✓ |
| Give the number of parameters to the function MID() | **3** ✓ |

> 用中文提示：初始化=赋初始值（第7行）；重复块起始=FOR循环开始（第9行）；逻辑运算=NOT、OR（第12行）；MID 有 3 个参数。

**(b)(ii)** Simplified version of line 12. **[2 marks]**

```
IF NextChar >= 'a' AND NextChar <= 'z' THEN     // ✓✓
```

Explanation:
- Original: `IF NOT((NextChar < 'a') OR (NextChar > 'z'))`
- By De Morgan's law: NOT(A OR B) = NOT A AND NOT B
- NOT(NextChar < 'a') = NextChar >= 'a'
- NOT(NextChar > 'z') = NextChar <= 'z'
- Result: NextChar >= 'a' AND NextChar <= 'z'

> 用中文提示：用德摩根定律化简：NOT(A OR B) = NOT A AND NOT B。原式等价于 NextChar >= 'a' AND NextChar <= 'z'。

### Question 6

Pseudocode for procedure CountVowels(). **[8 marks]**

```
PROCEDURE CountVowels(Text : STRING)
  DECLARE Index : INTEGER                        // ✓
  DECLARE ThisChar : CHAR
  DECLARE LowerText : STRING
  DECLARE VowelStr : STRING
  DECLARE Pos : INTEGER

  VowelStr ← "aeiou"                             // ✓ define vowels

  // Initialise CharCount array (global, 6 elements)
  FOR Index ← 1 TO 6                             // ✓ initialise counts
    CharCount[Index] ← 0
  NEXT Index

  LowerText ← TO_LOWER(Text)                     // ✓ convert to lowercase

  FOR Index ← 1 TO LENGTH(LowerText)             // ✓ loop through string
    ThisChar ← MID(LowerText, Index, 1)

    // Check if it's a letter
    IF ThisChar >= 'a' AND ThisChar <= 'z' THEN
      Pos ← 0
      // Check each vowel
      IF ThisChar = 'a' THEN
        Pos ← 1
      ELSE IF ThisChar = 'e' THEN
        Pos ← 2
      ELSE IF ThisChar = 'i' THEN
        Pos ← 3
      ELSE IF ThisChar = 'o' THEN
        Pos ← 4
      ELSE IF ThisChar = 'u' THEN
        Pos ← 5
      ENDIF

      IF Pos > 0 THEN                            // ✓ is a vowel
        CharCount[Pos] ← CharCount[Pos] + 1
      ELSE
        CharCount[6] ← CharCount[6] + 1          // ✓ other alphabetic
      ENDIF
    ENDIF
  NEXT Index

  OUTPUT "a: " & NUM_TO_STR(CharCount[1])         // ✓ output counts
  OUTPUT "e: " & NUM_TO_STR(CharCount[2])
  OUTPUT "i: " & NUM_TO_STR(CharCount[3])
  OUTPUT "o: " & NUM_TO_STR(CharCount[4])
  OUTPUT "u: " & NUM_TO_STR(CharCount[5])
  OUTPUT "Other: " & NUM_TO_STR(CharCount[6])
ENDPROCEDURE
```

Mark points:
- ✓ Procedure header with string parameter
- ✓ Initialise all 6 elements of CharCount to 0
- ✓ Convert string to lowercase (to handle both cases)
- ✓ Loop through each character of the string
- ✓ Identify whether each character is a vowel
- ✓ Increment the appropriate vowel counter (elements 1-5)
- ✓ Increment the other alphabetic counter (element 6) for non-vowel letters
- ✓ Output all six count values

> 用中文提示：CountVowels 过程：初始化 6 个计数器 → 将字符串转小写 → 遍历每个字符 → 判断是哪个元音（a=1, e=2, i=3, o=4, u=5）或其他字母（6）→ 相应计数器加 1 → 输出所有计数。

### Question 8

**(a)** Pseudocode for IgnoreWord(). **[5 marks]**

```
FUNCTION IgnoreWord(Word : STRING) RETURNS BOOLEAN
  DECLARE Index : INTEGER                        // ✓
  DECLARE LowerWord : STRING

  LowerWord ← TO_LOWER(Word)                     // ✓ convert to lowercase for comparison

  FOR Index ← 1 TO 10                            // ✓ search through IgnoreList
    IF TO_LOWER(IgnoreList[Index]) = LowerWord THEN   // ✓ case-insensitive comparison
      RETURN TRUE
    ENDIF
  NEXT Index

  RETURN FALSE                                   // ✓ word not found in ignore list
ENDFUNCTION
```

Mark points:
- ✓ Function header with string parameter, returns BOOLEAN
- ✓ Convert word to lowercase for case-insensitive comparison
- ✓ Loop through all 10 elements of IgnoreList
- ✓ Compare word with each element (case-insensitive)
- ✓ Return TRUE if found, FALSE if not found after checking all elements

> 用中文提示：IgnoreWord 函数：将输入单词转为小写，遍历 IgnoreList 数组（10 个元素），逐个比较（不区分大小写）。找到返回 TRUE，遍历完未找到返回 FALSE。

**(b)** Pseudocode for GetInitials(). **[8 marks]**

```
PROCEDURE GetInitials()
  DECLARE WordNum : INTEGER                      // ✓
  DECLARE StartPos : INTEGER
  DECLARE CurrentWord : STRING
  DECLARE Initials : STRING
  DECLARE FirstChar : CHAR

  Initials ← ""                                  // ✓ initialise result string
  WordNum ← 1                                    // ✓ start with first word
  StartPos ← GetStart(WordNum)                   // ✓ get position of first word

  WHILE StartPos <> -1 DO                        // ✓ loop while words exist
    CurrentWord ← GetWord(StartPos)              // ✓ get the word

    IF IgnoreWord(CurrentWord) = FALSE THEN       // ✓ check if word should be included
      FirstChar ← MID(CurrentWord, 1, 1)
      Initials ← Initials & TO_UPPER(FirstChar)  // ✓ add uppercase initial
    ENDIF

    WordNum ← WordNum + 1
    StartPos ← GetStart(WordNum)                 // get next word position
  ENDWHILE

  OUTPUT Initials                                 // ✓ output the initials
ENDPROCEDURE
```

Mark points:
- ✓ Initialise result string to empty
- ✓ Start with word number 1
- ✓ Call GetStart() to get position of current word
- ✓ Loop while GetStart() does not return -1
- ✓ Call GetWord() with the start position
- ✓ Call IgnoreWord() to check if word should be skipped
- ✓ If not ignored, extract first character and convert to upper case, append to result
- ✓ Output the final initials string

> 用中文提示：GetInitials 过程：从第 1 个单词开始循环 → 调用 GetStart() 获取位置（-1 表示无更多单词）→ 调用 GetWord() 获取单词 → 调用 IgnoreWord() 检查是否忽略 → 不忽略则取首字母转大写加入结果 → 最后输出缩写。
