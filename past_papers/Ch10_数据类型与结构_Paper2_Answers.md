# Chapter 10: Data Types & Structures - Paper 2 Answers

Mark scheme style answers with detailed marking points.

---

## 2024 May/June (9618/22)

### Question 3

**(a)(i)** Pseudocode to declare the record structure for type Component. **[4 marks]**

```
TYPE Component
  DECLARE Item_Num : INTEGER               // ✓
  DECLARE Reject : BOOLEAN                 // ✓
  DECLARE Stage : CHAR                     // ✓
  DECLARE Limit_1 : REAL                   // ✓
  DECLARE Limit_2 : REAL
ENDTYPE
```

Mark points:
- ✓ Correct TYPE...ENDTYPE syntax
- ✓ Item_Num as INTEGER
- ✓ Reject as BOOLEAN, Stage as CHAR
- ✓ Limit_1 and Limit_2 as REAL

> 用中文提示：记录类型声明用 TYPE...ENDTYPE。根据示例值判断数据类型：数字索引用 INTEGER，TRUE/FALSE 用 BOOLEAN，单个字母用 CHAR，带小数的用 REAL。

**(a)(ii)** Declare the array Item. **[2 marks]**

```
DECLARE Item : ARRAY[1:2000] OF Component   // ✓✓
```

Mark points:
- ✓ Correct ARRAY declaration syntax with bounds [1:2000]
- ✓ Data type is Component (the user-defined record type)

> 用中文提示：数组声明格式：DECLARE 数组名 : ARRAY[下界:上界] OF 数据类型。

**(b)** Three benefits of using an array of records. **[3 marks]**

- ✓ All related data for one item is grouped together in a single record, making the data easier to manage and understand
- ✓ A single array can store all items, allowing easy access using an index (e.g., Item[i].Stage)
- ✓ New fields can be added to the record structure without changing the array declaration / the structure is easily extensible

Other acceptable answers:
- Data can be passed efficiently as a single parameter to procedures/functions
- The code is more readable and maintainable

> 用中文提示：记录数组的好处：①相关数据组织在一起 ②用索引方便访问 ③结构易于扩展。

---

## 2024 Oct/Nov (9618/22)

### Question 2 (b)

**(i)** Declare the 2D array for card numbers. **[2 marks]**

```
DECLARE CardNumber : ARRAY[1:100, 1:2] OF STRING   // ✓✓
```

Mark points:
- ✓ 2D array with 100 rows and 2 columns
- ✓ Correct syntax and STRING data type

> 用中文提示：二维数组声明：100 行（每张卡一行）、2 列（原始字符串和修改后的字符串）。

**(ii)** How the parameter should be specified. **[1 mark]**

- ✓ BYREF (by reference) — because the procedure needs to modify the array contents (writing to column 2) and the changes must be reflected in the original array

> 用中文提示：用 BYREF（引用传递），因为过程需要修改数组内容，修改必须反映到原数组。

### Question 3

**(a)(i)** Initial values for SP and OnStack. **[1 mark]**

- SP: 1 ✓
- OnStack: 0 ✓

> 用中文提示：栈从索引 1 开始向上增长，初始时 SP 指向第一个可用位置（1），栈中元素数为 0。

**(a)(ii)** Why it is not necessary to initialise the array elements. **[2 marks]**

- ✓ The stack pointer (SP) and OnStack variable control which elements are considered to be part of the stack
- ✓ Only elements below SP (from index 1 to SP-1) are treated as valid stack data. Any values in uninitialised elements will never be accessed because the Pop operation checks OnStack before reading / the stack operations prevent reading beyond the valid range

> 用中文提示：不需要初始化数组元素，因为 SP 和 OnStack 变量控制着哪些元素属于栈。未使用的元素不会被访问到。

**(b)** Complete the Push function pseudocode. **[4 marks]**

```
FUNCTION Push(ThisValue : REAL) RETURNS BOOLEAN
  DECLARE ReturnValue : BOOLEAN
  IF OnStack = 60 THEN                          // ✓ check if stack is full
    RETURN FALSE                                 // ✓ return FALSE when full
  ENDIF
  ThisStack[SP] ← ThisValue                      // ✓ store value at SP position
  SP ← SP + 1                                    // ✓ increment stack pointer
  OnStack ← OnStack + 1
  RETURN TRUE
ENDFUNCTION
```

Mark points:
- ✓ `OnStack = 60` (or `SP > 60` or `SP = 61`) — condition to check stack full
- ✓ `FALSE` — return value when stack is full
- ✓ `ThisStack[SP]` — store value at current stack pointer position
- ✓ `SP + 1` — increment stack pointer

> 用中文提示：Push 操作：先检查栈是否已满（OnStack=60）→ 将值存入 ThisStack[SP] → SP 加 1 → OnStack 加 1 → 返回 TRUE。

### Question 8

**(a)** Pseudocode for module Assign(). **[7 marks]**

```
PROCEDURE Assign(PlayerNum : INTEGER, RequiredRole : STRING)
  DECLARE Index : INTEGER                                    // ✓
  DECLARE Found : BOOLEAN
  Found ← FALSE                                             // ✓

  Index ← 1
  WHILE Index <= 45 AND Found = FALSE DO                     // ✓ search loop
    IF Character[Index].Player = 0 THEN                      // ✓ check unassigned
      IF Character[Index].Role = RequiredRole THEN           // ✓ check matching role
        Character[Index].Player ← PlayerNum                  // ✓ assign to player
        OUTPUT Character[Index].Name & " the " & RequiredRole & " has been assigned to player " & NUM_TO_STR(PlayerNum)
        Found ← TRUE
      ENDIF
    ENDIF
    Index ← Index + 1
  ENDWHILE

  IF Found = FALSE THEN                                      // ✓ no match found
    OUTPUT "No unassigned " & RequiredRole & " is available"
  ENDIF
ENDPROCEDURE
```

Mark points:
- ✓ Procedure header with integer and string parameters
- ✓ Loop through Character array (1 to 45)
- ✓ Check Player = 0 (unassigned)
- ✓ Check Role matches RequiredRole
- ✓ Assign PlayerNum to Character[Index].Player
- ✓ Output confirmation message with character name, role, and player number
- ✓ Output suitable message if no unassigned character with required role found

> 用中文提示：遍历 Character 数组，找到 Player=0（未分配）且 Role 匹配的角色，将其分配给指定玩家并输出确认消息。找不到则输出提示消息。

**(b)** Pseudocode for module Save(). **[7 marks]**

```
PROCEDURE Save()
  DECLARE Index : INTEGER                                    // ✓
  DECLARE LineString : STRING

  OPENFILE "SaveFile.txt" FOR WRITE                          // ✓ open file for writing

  FOR Index ← 1 TO 45                                       // ✓ loop through all characters
    LineString ← NUM_TO_STR(Character[Index].Player)         // ✓ convert integer to string
                 & "^"
                 & Character[Index].Role                     // ✓ concatenate with separator
                 & "^"
                 & Character[Index].Name
                 & "^"
                 & NUM_TO_STR(Character[Index].Level)        // ✓ convert integer to string
    WRITEFILE "SaveFile.txt", LineString                      // ✓ write to file
  NEXT Index

  CLOSEFILE "SaveFile.txt"
ENDPROCEDURE
```

Mark points:
- ✓ Open file for WRITE
- ✓ Loop through all 45 elements
- ✓ Form string with fields separated by '^'
- ✓ Convert integer fields (Player, Level) to strings using NUM_TO_STR()
- ✓ Concatenate all fields with '^' separator
- ✓ Write each string to the file
- ✓ Close the file

> 用中文提示：Save 过程：打开文件（WRITE 模式）→ 循环 45 个角色 → 将每个记录的字段用 '^' 连接成字符串（注意整数字段需要 NUM_TO_STR 转换）→ 写入文件 → 关闭文件。

**(c)** How to store the additional Boolean field in a text file. **[2 marks]**

- ✓ Convert the Boolean value to a string representation, e.g., "TRUE" or "FALSE" (or "1" / "0")
- ✓ Concatenate this string with the other fields using the same '^' separator before writing to the file line

> 用中文提示：布尔值不能直接写入文本文件，需要转换为字符串（如 "TRUE"/"FALSE"），然后用同样的 '^' 分隔符与其他字段连接。

**(d)** Method for saving multiple files with sequential filenames. **[2 marks]**

- ✓ Use a counter/sequence number that increments each time a file is saved. Concatenate this number with a base filename to create a unique filename.
- ✓ Example consecutive filenames: SaveFile001.txt and SaveFile002.txt (or SaveFile_1.txt and SaveFile_2.txt)

> 用中文提示：使用递增的序号作为文件名的一部分，例如 SaveFile001.txt, SaveFile002.txt。每次保存时序号加 1。

---

## 2023 May/June (9618/22)

### Question 3

**(a)(i)** Describe how Orange and Yellow are added to the queue. **[4 marks]**

- ✓ Orange is added after Pink — the End of Queue Pointer moves from index 8 to index 9, and "Orange" is stored at index 9
- ✓ The End of Queue Pointer now points to index 9
- ✓ Yellow is added next — because the queue is circular, after index 9 the next location is index 0. "Yellow" is stored at index 0
- ✓ The End of Queue Pointer now points to index 0

> 用中文提示：循环队列添加元素：End 指针从 8 移到 9（存 Orange），再从 9 循环到 0（存 Yellow）。这就是"循环"的含义——到达末尾后回到开头。

**(a)(ii)** Number of data items in the queue. **[1 mark]**

- ✓ 7 (from index 5 through to index 1, wrapping around: indices 5, 6, 7, 8, 9, 0, 1)

> Note: Front pointer at 5, End pointer at 1. Count = (1 - 5 + 10) MOD 10 + 1 = 7

> 用中文提示：从 Front(5) 到 End(1) 循环计数：5,6,7,8,9,0,1 共 7 个元素。

**(b)** Describe algorithm for FileToQueue(). **[5 marks]**

- ✓ Step 1: Open the text file for reading
- ✓ Step 2: Start a loop that continues while the file is not at end-of-file AND the queue is not full
- ✓ Step 3: Read a line from the file
- ✓ Step 4: Call AddToQueue() with the line as a parameter; check the return value to determine if the queue is full
- ✓ Step 5: When the loop ends (either all lines read or queue full), close the file

> 用中文提示：FileToQueue 算法：打开文件 → 循环读取每一行 → 调用 AddToQueue() 添加到队列 → 检查返回值判断队列是否已满 → 文件读完或队列满时停止 → 关闭文件。

---

## 2023 Oct/Nov (9618/22)

### Question 1 (c)

Describe an effective way of storing data for many customer orders. **[3 marks]**

- ✓ Define a record type (user-defined data type) with fields for each item of data in the customer order (e.g., customer name, number of items, new customer flag, deposit)
- ✓ Declare a 1D array of this record type to store multiple customer orders
- ✓ This groups related data of different types together in a structured way, and the array allows multiple orders to be stored and accessed by index

> 用中文提示：使用记录类型（Record Type）定义每个订单的数据结构，然后声明一个该类型的一维数组来存储多个订单。记录允许不同数据类型的字段组合在一起。

### Question 3

**(a)** Complete the linked list diagram. **[5 marks]**

| Variable | Value |
|----------|-------|
| Start_Pointer | 4 ✓ |
| Free_List_Pointer | 5 |

| Index | Data array | Pointer array |
|-------|-----------|---------------|
| 1 | D32 | 2 |
| 2 | D11 | 3 ✓ |
| 3 | D100 | -1 ✓ (null) |
| 4 | D40 | 1 ✓ |
| 5 | F1 | 6 ✓ |
| 6 | F2 | 7 |
| 7 | F3 | 8 ✓ |
| 8 | F4 | -1 (null) |

Explanation of mark points:
- ✓ Start_Pointer = 4 (D40 is the first data item, stored at index 4)
- ✓ Index 4 pointer = 1 (D40 points to D32 at index 1)
- ✓ Index 2 (D11) pointer = 3 (D11 points to D100 at index 3)
- ✓ Index 3 (D100) pointer = -1 (null, end of data list)
- ✓ Index 5 (F1) pointer = 6, Index 7 (F3) pointer = 8 (free list chain)

> 用中文提示：链表用两个数组实现：Data 数组存数据，Pointer 数组存下一个节点的索引。Start_Pointer 指向第一个数据节点。链表顺序：D40(4) → D32(1) → D11(2) → D100(3) → null。空闲链表：F1(5) → F2(6) → F3(7) → F4(8) → null。

**(b)** Four steps to insert D6 between D32 and D11. **[4 marks]**

1. Assign the data item **D6** to **the node at the position indicated by Ptr2 (i.e., F1 at index 5)** ✓
2. Set the **pointer** of this node to point to **D11 (the node that D32 currently points to, i.e., index 2)** ✓
3. Set Ptr2 to point to **the next node in the free list (F2, i.e., index 6)** ✓
4. Set pointer of **D32 (node at index 1)** to point to **the new node (index 5)** ✓

> 用中文提示：插入节点的四步：①将数据 D6 存入空闲链表的第一个节点 ②新节点的指针指向 D11 ③更新空闲链表指针指向下一个空闲节点 ④D32 的指针改为指向新节点。

---

## 2022 Oct/Nov (9618/22)

### Question 3

**(a)** Another example of an ADT and its main features. **[3 marks]**

Queue:
- ✓ A queue is an Abstract Data Type that follows the FIFO (First In, First Out) principle
- ✓ Items are added at the rear/end of the queue (enqueue operation)
- ✓ Items are removed from the front of the queue (dequeue operation)

Alternative answer — Linked List:
- ✓ A linked list is an ADT where each node contains data and a pointer to the next node
- ✓ Nodes can be inserted or removed at any position
- ✓ The list is traversed by following pointers from one node to the next

> 用中文提示：抽象数据类型（ADT）的另一个例子是队列（Queue）：先进先出（FIFO），从尾部添加，从头部移除。或链表（Linked List）：每个节点有数据和指针，可在任意位置插入/删除。

**(b)** Explain how a stack can be implemented using an array. **[5 marks]**

- ✓ Declare a 1D array large enough to hold the maximum number of stack elements
- ✓ Use a variable as a stack pointer (SP) to track the position of the top of the stack / the next available position
- ✓ Initialise the stack pointer to indicate an empty stack (e.g., SP = 0 or SP = base index)
- ✓ PUSH operation: check the stack is not full, then store the value at the position indicated by SP and increment SP
- ✓ POP operation: check the stack is not empty, then decrement SP and return the value at that position

> 用中文提示：用数组实现栈：声明数组 → 用栈指针变量跟踪栈顶位置 → PUSH 时存入数据并移动指针 → POP 时移动指针并取出数据。需要检查栈满和栈空条件。

**(c)** Stack operations diagram. **[5 marks]**

Initial state: Z(950), P(950 is wrong - let me recalculate)

Initial: P at 950, Z at 951, Y at 952, X at 953, SP → 953

Wait, looking at the diagram again: stack grows upward, so SP points to the top item.

| Memory location | Initial state | After Group 1 | After Group 2 | After Group 3 |
|----------------|--------------|---------------|---------------|---------------|
| 957 | | | | |
| 956 | | | | C ✓ |
| 955 | | E ← SP | | |
| 954 | | D | | A ← SP |
| 953 | X ← SP | X | | X |
| 952 | Y | Y | Y ← SP | Y |
| 951 | Z | Z | Z | Z |
| 950 | P | P | P | P |

Note: SP convention matters. Assuming SP points to the top occupied element:

**After Group 1** (PUSH D, PUSH E): ✓
- D pushed to 954, E pushed to 955
- SP → 955

**After Group 2** (POP, POP, POP): ✓
- POP removes E (955), POP removes D (954), POP removes X (953)
- SP → 952

**After Group 3** (PUSH A, PUSH B, POP, PUSH C): ✓
- PUSH A to 953, PUSH B to 954, POP removes B (954), PUSH C to 954
- SP → 954

| Memory location | Initial state | After Group 1 | After Group 2 | After Group 3 |
|----------------|--------------|---------------|---------------|---------------|
| 957 | | | | |
| 956 | | | | |
| 955 | | E ← SP | | |
| 954 | | D | | C ← SP |
| 953 | X ← SP | X | | A |
| 952 | Y | Y | Y ← SP | Y |
| 951 | Z | Z | Z | Z |
| 950 | P | P | P | P |

> 用中文提示：栈操作：PUSH 将数据压入栈顶（SP 上移），POP 从栈顶弹出数据（SP 下移）。注意 POP 后数据在内存中可能还在，但逻辑上已不属于栈。

### Question 7 (c)

**(i)** Error in the record declaration. **[1 mark]**

- ✓ ErrCode should be declared as INTEGER, not STRING (the question states error numbers are integer values in the range 1 to 800)

> 用中文提示：ErrCode 应该是 INTEGER 类型，不是 STRING。因为错误编号是 1 到 800 的整数值。

**(ii)** Two benefits of using the single array of user-defined data type. **[2 marks]**

- ✓ The error code and error text are stored together in a single record, ensuring related data stays linked / reduces the risk of data becoming mismatched
- ✓ Only one array needs to be managed/sorted/searched instead of two separate parallel arrays

> 用中文提示：好处：①相关数据（错误代码和描述）组合在一起不会错位 ②只需管理一个数组而不是两个并行数组。

**(iii)** Declaration for the single array. **[1 mark]**

```
DECLARE ErrData : ARRAY[1:500] OF ErrorRec    // ✓
```

> 用中文提示：声明一个包含 500 个 ErrorRec 类型元素的一维数组。

---

## 2021 May/June (9618/22)

### Question 3

**(a)** Identify this type of ADT. **[1 mark]**

- ✓ Linked list

> 用中文提示：这是链表（Linked List），每个节点包含数据和指向下一个节点的指针。

**(b)** Technical term for item labelled A. **[1 mark]**

- ✓ Pointer (or link / reference)

> 用中文提示：A 是指针（Pointer），指向链表中的下一个节点。

**(c)** Technical term for item labelled B and its meaning. **[2 marks]**

- Term: ✓ Null pointer (null)
- Meaning: ✓ It indicates the end of the linked list / there is no next node to point to. It shows that Elk is the last node in the list.

> 用中文提示：B 是空指针（Null Pointer），表示链表的末尾，没有下一个节点了。

**(d)** Diagram after sorting in alphabetical order. **[2 marks]**

```
Cat → Dolphin → Elk → Fish → null     ✓✓
```

Mark points:
- ✓ Correct alphabetical order: Cat, Dolphin, Elk, Fish
- ✓ Pointers correctly updated to reflect the new order, with null at the end (after Fish)

> 用中文提示：按字母顺序排列：Cat → Dolphin → Elk → Fish → null。重新设置每个节点的指针使其按顺序连接。
