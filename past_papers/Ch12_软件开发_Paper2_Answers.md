# Chapter 12: Software Development - Paper 2 Answers

Mark scheme style answers with detailed marking points.

---

## 2024 May/June (9618/22)

### Question 5 (b)

Identify the type of error. **[1 mark]**

- ✓ Run-time error (also accept: logic error causing an infinite loop)

The program unexpectedly stops responding, which indicates an infinite loop — a type of run-time error where the program never reaches its termination condition.

> 用中文提示：程序无响应说明出现了运行时错误（Run-time error），通常是死循环（infinite loop）——程序永远无法到达终止条件。

### Question 7

**(a)** Three sub-modules for the text messaging module. **[3 marks]**

- Sub-module 1: ✓ CheckAvailability() — Use: Checks whether a space has become available in a class by comparing current membership against capacity
- Sub-module 2: ✓ GetWaitingList() — Use: Retrieves the list of members who are on the waiting list for the class that has availability
- Sub-module 3: ✓ SendTextMessage() — Use: Sends a text message to a specific member using their stored mobile phone number

> 用中文提示：分解（Decomposition）为三个子模块：①检查是否有空位 ②获取等候名单 ③发送短信。每个子模块执行一个独立的功能。

### Question 8 (a)

Reason for splitting into stages and benefit. **[2 marks]**

- ✓ Reason: The overall task is complex, so splitting it into stages makes each part simpler to develop, test and debug (decomposition / modular design)
- ✓ Benefit: Each stage produces a separate output file, so if an error occurs, the intermediate files can be examined to determine which stage caused the error / allows each stage to be tested independently

> 用中文提示：分阶段原因：复杂任务分解为更小的部分，便于开发和调试。好处：每个阶段产生中间文件，可以检查这些文件来定位错误发生在哪个阶段。

---

## 2024 Oct/Nov (9618/22)

### Question 1

**(a)** Stage of the program development life cycle for correcting the error. **[1 mark]**

- ✓ Maintenance (stage) — errors found after release are corrected during the maintenance phase of the program development life cycle

> 用中文提示：软件发布后发现的错误在"维护阶段"（Maintenance）修正。这是程序开发生命周期的最后一个阶段。

**(b)** Explain IDE features: watch window, single stepping, breakpoint. **[3 marks]**

- ✓ **Breakpoint**: First, set a breakpoint at the start of the Lookup() function. This causes the program to pause execution when it reaches this point, allowing the programmer to inspect the program state.
- ✓ **Single stepping**: After the breakpoint is reached, use single stepping to execute the function one line at a time. This allows the programmer to observe the flow of execution and see exactly where the incorrect value is produced.
- ✓ **Watch window**: While single stepping, use the watch window to monitor the values of key variables as each line executes. This helps identify which variable takes an unexpected value and at which line the error occurs.

Order: Set breakpoint first → program pauses at breakpoint → use single stepping through the function → observe variables in the watch window.

> 用中文提示：调试顺序：①先在 Lookup() 函数设置断点（Breakpoint）使程序暂停 ②用单步执行（Single Stepping）逐行运行代码 ③用监视窗口（Watch Window）观察变量值的变化，找出错误所在。

**(c)** Two IDE features that help during coding. **[2 marks]**

- ✓ 1: Auto-complete / code completion — suggests variable names, keywords, and function names as the programmer types, reducing typing errors
- ✓ 2: Syntax highlighting — displays different code elements (keywords, strings, comments) in different colours, making the code easier to read and helping to identify syntax errors

Other acceptable answers:
- Error highlighting / real-time syntax checking
- Auto-indentation
- Context-sensitive help / documentation lookup

> 用中文提示：IDE 编码辅助功能：①自动补全（Auto-complete）减少打字错误 ②语法高亮（Syntax Highlighting）用不同颜色显示不同代码元素，便于阅读和发现错误。

### Question 5

**(a)** Three statements that could generate run-time errors. **[3 marks]**

- Statement 1: ✓ `Count ← INT(100 / Number)`
  Explanation: If Number is 0, this will cause a division by zero error

- Statement 2: ✓ `Index ← Data[Number]`
  Explanation: If Number is less than 1 or greater than 100, this will cause an array index out of bounds error. Also, if Data[Number] returns a value outside the valid range, Index would be invalid for subsequent use.

- Statement 3: ✓ `ReturnValue ← TO_UPPER(RIGHT(Label, Count))`
  Explanation: If Count is greater than the length of Label, or if Count is 0 or negative, the RIGHT() function may generate an error / invalid string operation

Note: There is also a logic error — `RETURN RetVal` references an undeclared variable (should be `ReturnValue`), but this would be caught at compile time, not runtime.

> 用中文提示：三条可能产生运行时错误的语句：①100/Number 当 Number=0 时除零错误 ②Data[Number] 当 Number 超出数组范围时越界 ③RIGHT(Label, Count) 当 Count 无效时字符串操作错误。

**(b)** Programming construct that causes program freezing. **[2 marks]**

- Construct: ✓ Iteration / loop (specifically a WHILE loop or REPEAT...UNTIL loop)
- Explanation: ✓ If the loop's termination condition is never met (e.g., due to a logic error where the variable controlling the condition is never updated), the loop will execute indefinitely, causing the program to "freeze" / become unresponsive. This is known as an infinite loop.

> 用中文提示：导致程序"冻结"的结构是循环（Loop）。如果循环的终止条件永远无法满足（例如控制变量没有被更新），就会形成无限循环（Infinite Loop），程序无响应。

**(c)** Rewrite CASE structure as IF statement. **[2 marks]**

```
IF Index MOD 2 = 0 THEN                          // ✓
  ReturnValue ← TO_UPPER(RIGHT(Label, Count))
ELSE                                             // ✓
  ReturnValue ← "****"
ENDIF
```

> 用中文提示：CASE 结构只有两种情况（0 和 1），可以用 IF...THEN...ELSE...ENDIF 替代。Index MOD 2 = 0 对应 CASE 0，否则对应 CASE 1。

### Question 7

**(a)** Three items of customer information for the email module. **[3 marks]**

- ✓ Item 1: Email address — Justification: Required to send the email to the customer
- ✓ Item 2: Name — Justification: Required to personalise the email message
- ✓ Item 3: Date of last visit — Justification: Required to determine if the customer has not visited in the last three months (to decide whether to send the email)

> 用中文提示：三项信息：①邮箱地址（发送邮件）②姓名（个性化邮件内容）③最后访问日期（判断是否超过三个月未到访）。

**(b)** Computational thinking skill used. **[1 mark]**

- ✓ Abstraction — identifying the relevant/essential information and filtering out unnecessary details

> 用中文提示：所用的计算思维技能是"抽象"（Abstraction）——从大量信息中识别出与当前任务相关的关键信息，忽略不相关的细节。

**(c)** Three other items defined during the design stage. **[3 marks]**

- ✓ 1: User interface design / screen layouts / input/output formats
- ✓ 2: Data structures / data storage requirements / file formats
- ✓ 3: Test plan / test data and expected results

Other acceptable answers:
- Validation rules
- Security measures
- Module interfaces / parameters

> 用中文提示：设计阶段除了算法和模块设计外，还需要定义：①用户界面设计 ②数据结构/存储方式 ③测试计划。

**(d)** Structure chart for Init(), Reset(), and Check(). **[3 marks]**

```
           Check()
          /       \
         /         \
    Init()        Reset()
      |↑             |↑
      ||             ||
      |└─ BOOLEAN    |└─ INTEGER
      |   (return)   |   (return)
      |              └─ STRING
      |                 (parameter, down arrow)
```

Mark points:
- ✓ Check() at the top level, calling Init() and Reset()
- ✓ Init() shows a return value (BOOLEAN) going upward — no parameters going down
- ✓ Reset() shows a STRING parameter going down and an INTEGER return value going upward
- Selection symbol (diamond) or iteration symbol (curved arrow) may be shown on Check() to indicate repeated calls

> 用中文提示：结构图：Check() 在顶层，调用 Init() 和 Reset()。Init() 无参数，返回 BOOLEAN（向上箭头）。Reset() 接收 STRING 参数（向下箭头），返回 INTEGER（向上箭头）。

---

## 2023 May/June (9618/22)

### Question 5

**(a)** Why the program gives unexpected results. **[3 marks]**

- ✓ The parameter ThisNum in procedure DisplaySqrt() is passed by reference (BYREF)
- ✓ On line 52, ThisNum is assigned the square root value: `ThisNum ← SQRT(ThisNum)`. Because it is BYREF, this modifies the original variable Num in the calling code.
- ✓ Therefore, after calling DisplaySqrt(Num) with Num = 1.0, Num becomes 1.0 (sqrt of 1). Then Num + 1.0 = 2.0. But after calling DisplaySqrt with 2.0, Num becomes approximately 1.414... Then adding 1.0 gives 2.414..., not 3.0 as intended. The sequence of numbers processed is wrong.

> 用中文提示：参数 ThisNum 用 BYREF 传递，在过程内部被修改（赋值为平方根值）。因为是引用传递，原始变量 Num 也被改变了，导致后续计算的数字不是预期的 1,2,3,4...而是错误的序列。

**(b)** Why the compiler does not identify this error. **[1 mark]**

- ✓ The code is syntactically correct — BYREF is valid syntax and the assignment statement is valid. The compiler checks syntax, not the logic/intention of the program. This is a logic error which can only be detected at runtime.

> 用中文提示：编译器只检查语法错误，不检查逻辑错误。BYREF 语法正确，编译器无法判断程序员是否应该用 BYVAL。

**(c)** How an IDE could be used to identify this error. **[3 marks]**

- ✓ Set a breakpoint at the start of the REPEAT loop or at the CALL statement
- ✓ Use single stepping to execute the program line by line, stepping into the DisplaySqrt procedure
- ✓ Use a watch window to monitor the value of Num before and after the procedure call. The programmer would observe that Num's value changes unexpectedly after returning from DisplaySqrt, revealing the BYREF issue.

> 用中文提示：IDE 调试：①设断点 ②单步执行（包括步入过程内部）③用监视窗口观察 Num 的值。会发现 Num 在调用过程后意外改变，从而发现 BYREF 的问题。

**(d)** How to make a statement ignored by the compiler. **[1 mark]**

- ✓ Comment out the statement (turn it into a comment by adding `//` at the beginning of the line)

> 用中文提示：将语句注释掉（在行首加 `//`），编译器会忽略注释内容。

### Question 7

**(a)(i)** Three items of information for the new email module. **[3 marks]**

- ✓ Information: Email address — Justification: needed to send the email to the customer
- ✓ Information: Product categories they are interested in — Justification: needed to determine if the customer would be interested in the new products being promoted
- ✓ Information: How they would like to be contacted — Justification: needed to check that the customer has agreed to be contacted by email (consent/preference)

> 用中文提示：三项需要的信息：①邮箱地址（发送邮件）②感兴趣的产品类别（匹配新产品）③联系偏好（确认客户同意接收邮件）。

**(a)(ii)** Two items of information NOT required by the new module. **[2 marks]**

- ✓ Information: Payment details — Justification: sending a promotional email does not involve any financial transaction
- ✓ Information: Postal address — Justification: the module sends emails, not physical mail, so the postal address is not needed

> 用中文提示：不需要的信息：①支付详情（发邮件不涉及交易）②邮寄地址（发电子邮件不需要实际地址）。

**(b)** Complete the state-transition diagram for PIN validation. **[4 marks]**

The diagram should show:

- ✓ START → S1 (initial state)
- ✓ S1 → S2: Input PIN (transition when PIN is entered)
- ✓ S2 → S2: Re-input PIN / Display error (self-loop when PIN is wrong but tries remain)
- ✓ S2 → S1: Cancel / Re-prompt (return to start when cancelled)
- ✓ S2 → S4: Valid PIN / Enable payment (transition to final state on correct PIN)
- ✓ S2 → S3: Too many tries / Block Account (transition to blocked state)

States: S1 (waiting), S2 (checking), S3 (blocked — halting state), S4 (payment enabled — halting state)

> 用中文提示：PIN 验证的状态转换：S1（等待输入）→ S2（验证中）。从 S2 可以：重新输入（自环）、取消回到 S1、验证成功到 S4、尝试次数过多到 S3（账户锁定）。

### Question 8 (c)

Method to continue testing the main program. **[3 marks]**

- ✓ Method: Stub testing / use stub modules
- ✓ Description: Replace the modules SuppExists() and CheckSupplier() with simplified versions (stubs) that return predetermined/hard-coded values without performing the actual processing.
- ✓ For example, the stub for SuppExists() could always return TRUE (or a specific test value), and the stub for CheckSupplier() could return a fixed valid result. This allows the main program to be tested independently without relying on the faulty modules.

> 用中文提示：方法是"桩测试"（Stub Testing）。用简化版的"桩模块"替代有错误的模块，桩模块返回预定义的固定值（不执行实际功能），这样可以继续测试主程序的其他部分。

---

## 2022 Oct/Nov (9618/22)

### Question 1 (b)

Additional test stage before public release. **[4 marks]**

- ✓ Test stage: Beta testing / acceptance testing / user acceptance testing (UAT)
- ✓ Description: The program is given to a selected group of potential users / external testers who use the program in real-world conditions
- ✓ These testers report any bugs, usability issues, or unexpected behaviour they encounter
- ✓ This testing is important because external users may use the program in ways not anticipated by the developers / may test with different data, hardware, or operating conditions

Alternative: Alpha testing (if beta testing is the answer, alpha testing is also acceptable as the stage between in-house and full release)

> 用中文提示：公开发布前的额外测试阶段是 Beta 测试（或用户验收测试）。将程序交给外部用户在真实环境中使用，他们可能发现开发团队未预料到的问题。

### Question 6 (b)

Four invalid test strings for FindBaseNumber(). **[4 marks]**

| Input | Reason for choice |
|-------|------------------|
| "" (empty string) | ✓ Tests handling of empty/null input — no value to convert |
| "12.5" | ✓ Tests handling of a real/decimal number — not a valid integer |
| "-3" | ✓ Tests handling of a negative number — function requires positive, non-zero |
| "abc" | ✓ Tests handling of alphabetic characters — cannot be converted to integer |

Other acceptable answers:
- "0" — tests zero input (not positive, non-zero)
- "2 3" — tests input containing spaces
- "1e5" — tests scientific notation

> 用中文提示：四种无效测试输入：空字符串（无数据）、小数（非整数）、负数（非正数）、字母（非数字）。每种测试验证不同的输入验证方面。

---

## 2021 May/June (9618/22)

### Question 7

**(a)** Black-box test string for FormatName(). **[3 marks]**

- ✓ A test string such as: `∇∇∇Hello∇∇∇WORLD∇∇` (where ∇ represents a space)

This tests all four requirements:
- ✓ Requirement 1 (leading spaces): The spaces before "Hello" should be removed
- ✓ Requirement 2 (trailing spaces): The spaces after "WORLD" should be removed
- ✓ Requirement 3 (multiple spaces): The multiple spaces between "Hello" and "WORLD" should be reduced to a single space
- ✓ Requirement 4 (lowercase): "Hello" and "WORLD" should be converted to "hello" and "world"

Expected output: "hello∇world"

> 用中文提示：测试字符串需要同时包含：前导空格、尾随空格、单词间多个空格、大写字母。例如 "∇∇∇Hello∇∇∇WORLD∇∇"，预期输出 "hello∇world"。

**(b)** Two ways of exposing the fault. **[2 marks]**

- ✓ Way 1: Output/print the value of FString after the procedure call to check whether it has been assigned the expected value. If FString is unchanged or has an unexpected value, the fault is exposed.
- ✓ Way 2: Use an IDE debugger — set a watch on the global variable FString and step through the procedure to observe when/whether the assignment takes place. A breakpoint could be set after the expected assignment line.

> 用中文提示：两种暴露错误的方法：①在过程调用后输出 FString 的值检查是否被正确赋值 ②使用 IDE 调试器监视 FString 变量，单步执行观察赋值是否发生。
