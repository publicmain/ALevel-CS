# Chapter 4: Processor Fundamentals - 课后作业 Homework

> 姓名：__________ 日期：__________ 总分：__/58

---

## Question 1 — Von Neumann Architecture 冯·诺依曼架构 [6 marks]

(a) State **three** features of the Von Neumann architecture.
[3 marks]

(b) Draw a labelled diagram showing the main components of a Von Neumann computer system, including:
- The processor (showing ALU, CU, and registers)
- Main memory (RAM)
- The three buses

[3 marks]

---

## Question 2 — CPU Components 处理器组件 [6 marks]

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

(a) Describe the purpose of each of the following buses:

(i) Address bus
[2 marks]

(ii) Data bus
[2 marks]

(iii) Control bus
[2 marks]

---

## Question 5 — Fetch-Execute Cycle 取指-执行周期 [8 marks]

(a) Describe the steps in the **fetch** stage of the fetch-execute cycle. You should refer to specific registers and buses in your answer.
[4 marks]

(b) Describe what happens during the **decode** stage of the fetch-execute cycle.
[2 marks]

(c) State **two** factors that affect the performance of the CPU.
[2 marks]

---

## Question 6 — Instruction Format and Addressing Modes 指令格式与寻址方式 [8 marks]

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

---

*Cambridge International AS Level Computer Science 9618 - Chapter 4 Homework*
