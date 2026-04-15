# Chapter 4: Processor Fundamentals - 课后作业 Homework

> 姓名：__________ 日期：__________ 总分：__/58

---

## Question 1 — Von Neumann Architecture 冯·诺依曼架构 [6 marks]

> 中文提示：冯·诺依曼架构是现代计算机的基本设计模型。核心思想是程序和数据存储在同一个存储器中。

(a) State **three** features of the Von Neumann architecture.
[3 marks]

(b) Draw a labelled diagram showing the main components of a Von Neumann computer system, including:
- The processor (showing ALU, CU, and registers)
- Main memory (RAM)
- The three buses

[3 marks]

---

## Question 2 — CPU Components 处理器组件 [6 marks]

> 中文提示：CPU（中央处理器）由ALU（算术逻辑单元）、CU（控制单元）和寄存器（registers）组成。每个部分有不同的功能。

(a) Describe the function of each of the following components of the CPU:

(i) Arithmetic Logic Unit (ALU)
[2 marks]

(ii) Control Unit (CU)
[2 marks]

(b) State the purpose of each of the following special-purpose registers:

(i) Program Counter (PC)
[1 mark]

(ii) Memory Address Register (MAR)
[1 mark]

---

## Question 3 — Registers 寄存器 [5 marks]

> 中文提示：寄存器是CPU内部的高速存储单元。不同寄存器有不同的功能，如PC、MAR、MDR、CIR、ACC等。

State the name and describe the purpose of each of the following registers:

(a) MDR (Memory Data Register)
[1 mark]

(b) CIR (Current Instruction Register)
[1 mark]

(c) Accumulator (ACC)
[1 mark]

(d) Index Register (IX)
[1 mark]

(e) Status Register
[1 mark]

---

## Question 4 — Buses 总线 [6 marks]

> 中文提示：总线（bus）是连接CPU、内存和I/O设备的通信线路。三种总线是：地址总线（address bus）、数据总线（data bus）和控制总线（control bus）。

(a) Describe the purpose of each of the following buses:

(i) Address bus
[2 marks]

(ii) Data bus
[2 marks]

(iii) Control bus
[2 marks]

---

## Question 5 — Fetch-Execute Cycle 取指-执行周期 [8 marks]

> 中文提示：取指-执行周期（也叫取指-译码-执行周期）是CPU执行指令的基本过程。需要描述每一步中涉及的寄存器和总线操作。

(a) Describe the steps in the **fetch** stage of the fetch-execute cycle. You should refer to specific registers and buses in your answer.
[4 marks]

(b) Describe what happens during the **decode** stage of the fetch-execute cycle.
[2 marks]

(c) State **two** factors that affect the performance of the CPU.
[2 marks]

---

## Question 6 — Instruction Format and Addressing Modes 指令格式与寻址方式 [8 marks]

> 中文提示：机器指令由操作码（opcode）和操作数（operand）组成。不同的寻址方式（addressing mode）决定了操作数如何被解释。

(a) State what is meant by:

(i) opcode
[1 mark]

(ii) operand
[1 mark]

(b) Describe each of the following addressing modes and give an example of when each might be used:

(i) Immediate addressing (立即寻址)
[2 marks]

(ii) Direct addressing (直接寻址)
[2 marks]

(iii) Indirect addressing (间接寻址)
[2 marks]

---

## Question 7 — Addressing Modes in Practice 寻址方式实践 [5 marks]

> 中文提示：本题要求你根据给定的内存内容，计算不同寻址方式下加载到ACC中的值。

The following table shows the contents of some memory locations:

| Address | Contents |
|---------|----------|
| 100     | 50       |
| 101     | 200      |
| 200     | 75       |
| 201     | 300      |
| 300     | 42       |

The instruction `LDD 101` means "load the value using direct addressing from address 101".

State the value loaded into the Accumulator for each of the following instructions:

(a) `LDI #50` (Immediate addressing)
[1 mark]

(b) `LDD 100` (Direct addressing)
[1 mark]

(c) `LDI 101` (Indirect addressing — the operand gives the address of the address)
[1 mark]

(d) `LDX 100` (Indexed addressing — the Index Register contains the value 1)
[1 mark]

(e) Explain, with reference to part (c), why indirect addressing can be useful.
[1 mark]

---

## Question 8 — Assembly Language Programming 汇编语言编程 [8 marks]

> 中文提示：汇编语言使用助记符（mnemonics）来表示机器指令。常见指令包括LDD（加载）、STO（存储）、ADD（加法）、SUB（减法）、CMP（比较）、JMP（跳转）等。

(a) The following assembly language program adds two numbers from memory and stores the result.

```
LDD  50
ADD  51
STO  52
END
```

State what value is stored in address 52 if address 50 contains the value 20 and address 51 contains the value 35.
[1 mark]

(b) Write an assembly language program that:
- Loads the value from address 200
- Subtracts the value from address 201
- If the result is zero, jumps to the label EQUAL
- Otherwise stores the result in address 202
- The label EQUAL should store the value 0 in address 202

You may use the following instruction set:

| Mnemonic | Description |
|----------|-------------|
| LDD n    | Load contents of address n into ACC |
| STO n    | Store contents of ACC into address n |
| ADD n    | Add contents of address n to ACC |
| SUB n    | Subtract contents of address n from ACC |
| CMP n    | Compare ACC with contents of address n |
| JPE label| Jump to label if comparison is equal |
| JPN label| Jump to label if comparison is not equal |
| JMP label| Unconditional jump to label |
| END      | End of program |

[5 marks]

(c) State **two** advantages of writing programs in assembly language rather than machine code.
[2 marks]

---

## Question 9 — Bit Manipulation 位操作 [6 marks]

> 中文提示：位操作使用AND、OR、XOR掩码来操作二进制数据中的特定位。AND用于清零/提取位，OR用于置位，XOR用于翻转位。

An 8-bit register contains the value `10110101`.

(a) A programmer wants to set bits 0 and 1 to 1, without changing any other bits.
State which logical operation and mask should be used, and show the result.
[2 marks]

(b) A programmer wants to clear (set to 0) the upper four bits (bits 4-7), without changing the lower four bits.
State which logical operation and mask should be used, and show the result.
[2 marks]

(c) A programmer wants to toggle (flip) bits 2 and 3, without changing any other bits.
State which logical operation and mask should be used, and show the result.
[2 marks]

---

### 答题完毕后请检查：
- 取指-执行周期的描述是否按正确顺序，是否提到了关键的寄存器和总线
- 汇编语言程序是否逻辑正确
- 位操作题是否选择了正确的逻辑运算和掩码

---

*Cambridge International AS Level Computer Science 9618 - Chapter 4 Homework*
