# Chapter 4: Processor Fundamentals - Paper 1 Answers

> Topics: CPU architecture (Von Neumann), registers, buses, assembly language, instruction sets, addressing modes, fetch-execute cycle, bit manipulation

---

## 2024 May/June (9618/12)

### Question 5

**(a)** ACC and IX contents after each program:

Memory: 10=1, 11=3, 12=5, 13=11, 14=10, 15=16, 16=12. ACC=10, IX=0.

**Program 1**: LDI 15 / SUB #1
- LDI 15: Address 15 contains 16, so go to address 16 which contains 12. ACC = 12
- SUB #1: ACC = 12 - 1 = 11
- ✓ ACC = **11**

> 提示：LDI（间接寻址）：地址15的内容是16，再去地址16取值12加载到ACC。

**Program 2**: LDD 14 / ADD 11
- LDD 14: Load contents of address 14. ACC = 10
- ADD 11: Add contents of address 11 to ACC. ACC = 10 + 3 = 13
- ✓ ACC = **13**

> 提示：LDD（直接寻址）：直接取地址14的内容。ADD 11：加上地址11的内容。

**Program 3**: LDM #11 / ADD #3 / SUB 16
- LDM #11: Load the number 11 into ACC. ACC = 11
- ADD #3: ACC = 11 + 3 = 14
- SUB 16: Subtract contents of address 16 from ACC. ACC = 14 - 12 = 2
- ✓ ACC = **2**

> 提示：LDM（立即寻址）：直接加载数值11。#号表示立即数，无#号表示地址。

**Program 4**: LDR #2 / LDX 14 / ADD #2
- LDR #2: Load 2 into IX. IX = 2
- LDX 14: Indexed addressing. Address = 14 + IX = 14 + 2 = 16. Load contents of address 16. ACC = 12
- ADD #2: ACC = 12 + 2 = 14
- ✓ ACC = **14**

> 提示：LDX（变址寻址）：实际地址 = 给定地址 + IX寄存器的值。LDR加载IX寄存器。

**(b)** Bit manipulation results:

Memory: 25=11000110, 26=11100001, 27=10000001, 28=11001101, 29=00001111. ACC=01000110.

**Program 1**: XOR 29
- ACC XOR contents of address 29
- 01000110 XOR 00001111

```
  01000110
XOR 00001111
----------
  01001001
```
✓ ACC = **01001001**

> 提示：XOR：相同为0，不同为1。

**Program 2**: AND #29
- #29 is immediate value 29 in denary = 00011101 in binary
- 01000110 AND 00011101

```
  01000110
AND 00011101
-----------
  00000100
```
✓ ACC = **00000100**

> 提示：AND #29 中的29是十进制立即数（不是地址），需先转为二进制 00011101，再做按位与。

**Program 3**: OR B11111111
- B prefix means binary value
- 01000110 OR 11111111

```
  01000110
OR  11111111
-----------
  11111111
```
✓ ACC = **11111111**

> 提示：任何数 OR 11111111 都等于 11111111。B前缀表示二进制数。

---

## 2024 Oct/Nov (9618/12)

### Question 3(a) (Registers)

| Register | Purpose |
|----------|---------|
| **Program Counter (PC)** | Stores the address of the next instruction to be fetched and executed ✓ |
| **Memory Address Register (MAR)** | Stores the address of the memory location that is to be read from or written to ✓ |
| **Memory Data Register (MDR)** | Stores the data that has been read from or is to be written to memory ✓ |
| **Index Register (IX)** | Stores a value that is added to the operand address in indexed addressing to form the effective address ✓ |

> 提示：PC=下一条指令地址；MAR=要访问的内存地址；MDR=从内存读出或要写入的数据；IX=变址寄存器，用于变址寻址时加到操作数地址上。

### Question 8

**(a)** Trace table:

Memory: 19=25, 20=23, 21=2, 22=4, 23=15, 24=50, 25=22. ACC=50, IX=20.

**Program 1**: LDM #19 / DEC ACC
- LDM #19: ACC = 19 (immediate value)
- DEC ACC: ACC = 19 - 1 = 18
- ✓ ACC = **18**, IX = **20** (unchanged)

> 提示：LDM加载立即数19，DEC减1。IX没有被修改所以保持20。

**Program 2**: LDD 23 / ADD 19
- LDD 23: Load contents of address 23. ACC = 15
- ADD 19: Add contents of address 19. ACC = 15 + 25 = 40
- ✓ ACC = **40**, IX = **20** (unchanged)

> 提示：LDD直接寻址取地址23的内容(15)，ADD加上地址19的内容(25)。

**Program 3**: LDI 25 / INC ACC
- LDI 25: Indirect addressing. Address 25 contains 22, so go to address 22 which contains 4. ACC = 4
- INC ACC: ACC = 4 + 1 = 5
- ✓ ACC = **5**, IX = **20** (unchanged)

> 提示：LDI间接寻址：地址25内容是22，再去地址22取值4。然后INC加1得5。

**Program 4**: LDR #21 / LDX 2
- LDR #21: Load 21 into IX. IX = 21
- LDX 2: Indexed addressing. Address = 2 + IX = 2 + 21 = 23. Load contents of address 23. ACC = 15
- ✓ ACC = **15**, IX = **21**

> 提示：LDR加载21到IX。LDX变址寻址：实际地址 = 2 + 21 = 23，取地址23的内容(15)。

**(b)(i)** Bit manipulation results (ACC = 10011010 = 154 in denary):

**Program 1**: LSL #2 / ADD #5
- LSL #2: Logical shift left 2 places. 10011010 -> 01101000 (= 104 in denary)
- ADD #5: 104 + 5 = 109. In binary: 01101101
- ✓ ACC = **01101101**

> 提示：LSL左移2位（右边补0，左边丢弃）：10011010 → 01101000。然后加5。

**Program 2**: AND #30 / OR B11110010
- AND #30: 30 in denary = 00011110 in binary
- 10011010 AND 00011110 = 00011010
- OR B11110010: 00011010 OR 11110010 = 11111010
- ✓ ACC = **11111010**

> 提示：AND #30（十进制30=00011110）做按位与，再OR B11110010做按位或。

**Program 3**: INC ACC
- ACC = 10011010 (154 in denary)
- INC ACC: ACC = 154 + 1 = 155 = 10011011
- ✓ ACC = **10011011**

> 提示：INC就是加1。10011010 + 1 = 10011011。

**(b)(ii)** Testing if ACC contains an odd number:

- Perform a bitwise AND with the value 1 (binary 00000001) ✓
- This masks / isolates the least significant bit (bit 0) ✓
- If the result is 1, the number is odd; if the result is 0, the number is even ✓

Instruction: **AND #1** (or AND B00000001)

> 提示：用 AND #1（即 AND 00000001）来检测最低位。如果结果为1则是奇数，为0则是偶数。这叫做"位掩码"（bit masking）。

---

## 2023 May/June (9618/12)

### Question 3

**(a)** Two-pass assembler actions:

| Action | Pass |
|---|---|
| Generates object code | **Second pass** ✓ |
| Reads the source code one line at a time | **Both first and second pass** ✓ |
| Removes white space | **First pass** ✓ |
| Adds labels to the symbol table | **First pass** |

> 提示：第一遍（first pass）：读源码、去空白、建立符号表（记录标签地址）。第二遍（second pass）：再次读源码、生成目标代码（机器码）。

**(b)** Addressing modes:

- **Direct** addressing is when the operand holds the memory address of the data. ✓
- **Indirect** addressing is when the operand holds a memory address that stores the memory address of the data. ✓
- **Immediate** addressing is when the operand is the data. ✓

> 提示：直接寻址（Direct）= 操作数是数据的地址。间接寻址（Indirect）= 操作数是"地址的地址"。立即寻址（Immediate）= 操作数就是数据本身。

### Question 5(a)(b) (CPU architecture)

**(a)** Two types of signal transferred by the control bus:

- Read / write signal (to indicate whether data is to be read from or written to memory) ✓
- Clock signal / timing signal ✓

Other valid answers:
- Interrupt signal ✓
- Bus request / bus grant signal ✓
- Reset signal ✓

> 提示：控制总线传输的信号类型：读/写信号、时钟信号、中断信号、总线请求信号等。

**(b)** Two hardware upgrades to improve laptop performance:

**Upgrade 1**: Increase the amount of RAM ✓
- Explanation: More RAM allows more programs / data to be held in main memory simultaneously, reducing the need to swap data to/from the hard disk, which improves processing speed ✓

**Upgrade 2**: Replace the hard disk with an SSD (solid-state drive) ✓
- Explanation: An SSD has faster read/write speeds than a traditional hard disk, so data can be loaded and saved more quickly, improving overall system responsiveness ✓

Other valid upgrades:
- Upgrade to a processor with more cores — allows more processes to be executed simultaneously / true parallel processing ✓
- Upgrade to a processor with a higher clock speed — more instructions can be executed per second ✓
- Add more cache memory — frequently used data/instructions can be accessed faster ✓

> 提示：提升笔记本性能的硬件升级：(1) 加内存RAM (2) 换SSD固态硬盘 (3) 升级多核处理器 (4) 提高时钟频率 (5) 增加缓存。

---

## 2023 Oct/Nov (9618/12)

### Question 8(c) (Buses)

**(i)** Port for optical disc reader/writer:

✓ **USB** (Universal Serial Bus)

> 提示：光驱通常通过USB端口连接。

**(ii)** Roles of address bus, data bus and buffers:

- The **address bus** carries the address of the memory location where data is to be written to / read from on the optical disc ✓
- The **data bus** carries the actual data being transferred between the processor and the optical disc reader/writer ✓
- **Buffers** are used as temporary storage to hold data being transferred, compensating for the difference in speed between the processor and the optical disc reader/writer ✓

> 提示：地址总线传送地址，数据总线传送数据，缓冲区（buffer）临时存储数据以协调处理器和光驱之间的速度差异。

### Question 9

**(a)** Instruction groups:

| Opcode | Instruction Group |
|---|---|
| IN | **Input/Output** ✓ |
| ADD | **Arithmetic** ✓ |
| JPE | **Branch / Jump / Transfer of control** ✓ |
| CMI | **Comparison** ✓ |

> 提示：IN=输入输出类，ADD=算术运算类，JPE=跳转/分支类，CMI=比较类。

**(b)** Trace table for the program when input is '1':

Memory: 100=0, 101=0, 110=51, 111=65. ASCII: 49='1', 51='3', 65='A'.

Step-by-step execution:

| Line | Instruction | ACC | IX | Memory 100 | Memory 101 | Notes |
|---|---|---|---|---|---|---|
| 10 | LDR #0 | - | 0 | 0 | 0 | IX = 0 |
| 11 | IN | 49 | 0 | 0 | 0 | Input '1' = ASCII 49 |
| 12 | STO 101 | 49 | 0 | 0 | 49 | Store 49 at address 101 |
| 13 | LDX 110 | 51 | 0 | 0 | 49 | Indexed: addr=110+0=110, contents=51 ✓ |
| 14 | CMP 100 | 51 | 0 | 0 | 49 | Compare ACC(51) with contents of 100(0) |
| 15 | JPE 21 | 51 | 0 | 0 | 49 | Not equal, so no jump |
| 16 | LDD 101 | 49 | 0 | 0 | 49 | ACC = contents of 101 = 49 |
| 17 | ADD #16 | 65 | 0 | 0 | 49 | ACC = 49 + 16 = 65 |
| 18 | INC IX | 65 | 1 | 0 | 49 | IX = 0 + 1 = 1 |
| 19 | STO 100 | 65 | 1 | 65 | 49 | Store 65 at address 100 ✓ |
| 20 | JMP 13 | 65 | 1 | 65 | 49 | Jump back to line 13 |
| 13 | LDX 110 | 65 | 1 | 65 | 49 | Indexed: addr=110+1=111, contents=65 |
| 14 | CMP 100 | 65 | 1 | 65 | 49 | Compare ACC(65) with contents of 100(65) |
| 15 | JPE 21 | 65 | 1 | 65 | 49 | Equal! Jump to line 21 ✓ |
| 21 | OUT | 65 | 1 | 65 | 49 | Output ASCII 65 = **'A'** ✓ |
| 22 | END | - | - | - | - | Program ends |

Output: **A**

> 提示：这个程序将输入字符'1'（ASCII 49）加16得到65（ASCII 'A'），然后输出'A'。变址寻址用IX作为偏移量来遍历内存中的数据。

---

## 2022 Oct/Nov (9618/12)

### Question 7

**(a)** Trace table:

Memory: 100=0, 101=0, 102=112, 103=4, 110=1, 111=4, 112=0.

Program starts at line 75. Stop when line 90 is executed for a second time.

| Line | Instruction | ACC | IX | Mem 100 | Mem 101 | Notes |
|---|---|---|---|---|---|---|
| 75 | LDR #0 | - | 0 | 0 | 0 | IX = 0 |
| 76 | LDX 110 | 1 | 0 | 0 | 0 | Indexed: addr=110+0=110, contents=1 ✓ |
| 77 | CMI 102 | 1 | 0 | 0 | 0 | Indirect: addr 102 contains 112, contents of 112=0. Compare ACC(1) with 0 |
| 78 | JPE 91 | 1 | 0 | 0 | 0 | Not equal, no jump |
| 79 | CMP 103 | 1 | 0 | 0 | 0 | Compare ACC(1) with contents of 103(4) |
| 80 | JPN 84 | 1 | 0 | 0 | 0 | 1 is not equal to 4, so jump to 84 ✓ |
| 84 | INC ACC | 2 | 0 | 0 | 0 | ACC = 1 + 1 = 2 |
| 85 | STO 101 | 2 | 0 | 0 | 2 | Store 2 at address 101 |
| 86 | LDD 100 | 0 | 0 | 0 | 2 | ACC = contents of 100 = 0 |
| 87 | INC ACC | 1 | 0 | 0 | 2 | ACC = 0 + 1 = 1 |
| 88 | STO 100 | 1 | 0 | 1 | 2 | Store 1 at address 100 |
| 89 | INC IX | 1 | 1 | 1 | 2 | IX = 0 + 1 = 1 |
| 90 | JMP 76 | 1 | 1 | 1 | 2 | Jump to 76 (1st execution of line 90) ✓ |
| 76 | LDX 110 | 4 | 1 | 1 | 2 | Indexed: addr=110+1=111, contents=4 |
| 77 | CMI 102 | 4 | 1 | 1 | 2 | Indirect: addr 102=112, contents of 112=0. Compare ACC(4) with 0 |
| 78 | JPE 91 | 4 | 1 | 1 | 2 | Not equal, no jump |
| 79 | CMP 103 | 4 | 1 | 1 | 2 | Compare ACC(4) with contents of 103(4) |
| 80 | JPN 84 | 4 | 1 | 1 | 2 | Equal, so do NOT jump (JPN = Jump if Not equal) |
| 81 | ADD 101 | 6 | 1 | 1 | 2 | ACC = 4 + contents of 101(2) = 6 |
| 82 | STO 101 | 6 | 1 | 1 | 6 | Store 6 at address 101 ✓ |
| 83 | JMP 86 | 6 | 1 | 1 | 6 | Jump to 86 |
| 86 | LDD 100 | 1 | 1 | 1 | 6 | ACC = contents of 100 = 1 |
| 87 | INC ACC | 2 | 1 | 1 | 6 | ACC = 1 + 1 = 2 |
| 88 | STO 100 | 2 | 1 | 2 | 6 | Store 2 at address 100 |
| 89 | INC IX | 2 | 2 | 2 | 6 | IX = 1 + 1 = 2 |
| 90 | JMP 76 | 2 | 2 | 2 | 6 | Jump to 76 (2nd execution — STOP) ✓ |

> 提示：CMI是间接比较（先取地址102的内容112作为新地址，再取地址112的内容0来比较）。JPN = Jump if Not equal（不相等则跳转）。逐行追踪，注意每条指令对ACC、IX和内存的影响。

**(b)** Bit manipulation:

Memory: 50=01001101, 51=10001111. ACC starts at 01010011 for each.

**(i)** XOR B00011111:
```
  01010011
XOR 00011111
-----------
  01001100
```
✓ ACC = **01001100**

> 提示：XOR：相同为0，不同为1。

**(ii)** AND 50 (contents of address 50 = 01001101):
```
  01010011
AND 01001101
-----------
  01000001
```
✓ ACC = **01000001**

> 提示：AND：两个都为1才为1。

**(iii)** LSL #3 (logical shift left 3 places):
- 01010011 shifted left 3: 10011000
✓ ACC = **10011000**

> 提示：左移3位：左边丢弃3位，右边补3个0。01010011 → 10011000。

**(iv)** OR 51 (contents of address 51 = 10001111):
```
  01010011
OR  10001111
-----------
  11011111
```
✓ ACC = **11011111**

> 提示：OR：至少一个为1则为1。

**(c)** Register transfer notation for fetch-execute cycle:

- Copy address of next instruction into MAR: **MAR <- [PC]** ✓
- Increment the Program Counter: **PC <- [PC] + 1** ✓
- Copy contents of MDR into CIR: **CIR <- [MDR]** ✓

> 提示：取指-执行周期的寄存器传输表示法：MAR←[PC]（PC的内容复制到MAR），PC←[PC]+1（PC加1），CIR←[MDR]（MDR的内容复制到CIR）。方括号表示"寄存器的内容"。

---

## 2021 May/June (9618/12)

### Question 4

Program and memory: 100=68('D'), 101=65('A'), 102=100. ASCII: 65=A, 66=B, 67=C, 68=D.

**(a)** Trace table for inputs A then D:

| Line | Instruction | ACC | Mem 102 | Notes |
|---|---|---|---|---|
| 70 | IN | 65 | 100 | Input 'A' (ASCII 65) |
| 71 | CMP 100 | 65 | 100 | Compare 65 with contents of 100 (68='D') |
| 72 | JPE 80 | 65 | 100 | 65 != 68, no jump |
| 73 | CMP 101 | 65 | 100 | Compare 65 with contents of 101 (65='A') |
| 74 | JPE 76 | 65 | 100 | 65 == 65, jump to 76 ✓ |
| 76 | LDD 102 | 100 | 100 | ACC = contents of 102 = 100 |
| 77 | INC ACC | 101 | 100 | ACC = 100 + 1 = 101 |
| 78 | STO 102 | 101 | 101 | Store 101 at address 102 ✓ |
| 79 | JMP 70 | 101 | 101 | Jump back to 70 |
| 70 | IN | 68 | 101 | Input 'D' (ASCII 68) |
| 71 | CMP 100 | 68 | 101 | Compare 68 with contents of 100 (68='D') |
| 72 | JPE 80 | 68 | 101 | 68 == 68, jump to 80 ✓ |
| 80 | LDD 102 | 101 | 101 | ACC = contents of 102 = 101 |
| 81 | DEC ACC | 100 | 101 | ACC = 101 - 1 = 100 |
| 82 | STO 102 | 100 | 100 | Store 100 at address 102 ✓ |
| 83 | JMP 70 | 100 | 100 | Jump back to 70 — STOP (3rd input required) |

> 提示：这个程序：输入'A'时地址102的值加1，输入'D'时地址102的值减1。初始值100，输入A后变101，输入D后变回100。

**(b)** Bit manipulation:

Memory address 300 contains: 01100110

**(i)** Denary value of unsigned binary 01100110:
- 64 + 32 + 4 + 2 = **102**
- ✓ **102**

> 提示：01100110 = 64+32+4+2 = 102。

**(ii)** Instruction to test if bit 2 is a 1:

✓ **AND** #4

(4 in binary = 00000100, which has only bit 2 set. AND with this value isolates bit 2.)

> 提示：AND #4（4的二进制是00000100），用来检测第2位。如果AND结果非零，则第2位为1。位编号从右往左从0开始。

**(iii)** Instruction to set bits 4-7 to 0 while keeping bits 0-3:

✓ **AND #15** (or AND B00001111)

Working: 15 in binary = 00001111. ANDing with 00001111 will keep bits 0-3 unchanged and set bits 4-7 to 0.

✓✓ (2 marks: 1 for AND, 1 for correct operand)

> 提示：AND #15（即AND 00001111）：高4位与0做AND变为0，低4位与1做AND保持不变。这是"位掩码"（bit masking）技术。

### Question 5(a)(b) (CPU components)

**(a)** Missing terms:

- The **control unit** ✓ transmits the signals to coordinate events based on the electronic pulses of the **clock** ✓.
- The **data bus** ✓ carries data to the components, while the **address bus** ✓ carries the address where data needs to be written to or read from.
- The **Arithmetic Logic Unit (ALU)** ✓ performs mathematical operations and logical comparisons.

> 提示：控制单元（Control Unit）+ 时钟（Clock）协调事件；数据总线（Data Bus）传数据；地址总线（Address Bus）传地址；算术逻辑单元（ALU）执行运算和比较。

**(b)** Effect of factors on laptop performance:

**Number of cores**:
- More cores allow the processor to execute multiple instructions / processes simultaneously / in parallel ✓
- This improves the overall throughput / speed of the computer when running multiple programs or tasks that can be parallelised ✓

**Clock speed**:
- Clock speed determines the number of instruction cycles (fetch-decode-execute) that can be performed per second ✓
- A higher clock speed means more instructions can be processed per second, so programs run faster ✓

> 提示：核心数（cores）：越多核 → 越多任务可以并行处理。时钟频率（clock speed）：越高 → 每秒执行的指令周期越多 → 程序运行越快。
