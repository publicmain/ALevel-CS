# Chapter 4: Processor Fundamentals - Paper 1 Past Questions

> Topics: CPU architecture (Von Neumann), registers, buses, assembly language, instruction sets, addressing modes, fetch-execute cycle, bit manipulation

---

## 2024 May/June (9618/12)

### Question 5
The following table shows part of the instruction set for a processor. The processor has two registers: the Accumulator (ACC) and an Index Register (IX).

Instruction set:
- LDM #n — Immediate addressing. Load the number n to ACC
- LDD <address> — Direct addressing. Load the contents of the location at the given address to ACC
- LDI <address> — Indirect addressing. The address to be used is at the given address. Load the contents of this second address to ACC
- LDX <address> — Indexed addressing. Form the address from <address> + the contents of the index register. Copy the contents of this calculated address to ACC
- LDR #n — Immediate addressing. Load the number n to IX
- ADD #n/Bn/&n — Add the number n to the ACC
- ADD <address> — Add the contents of the given address to the ACC
- SUB #n/Bn/&n — Subtract the number n from the ACC
- SUB <address> — Subtract the contents of the given address from the ACC
- INC <register> — Add 1 to the contents of the register (ACC or IX)

(a) The current contents of memory are shown:

| Address | Data |
|---------|------|
| 10 | 1 |
| 11 | 3 |
| 12 | 5 |
| 13 | 11 |
| 14 | 10 |
| 15 | 16 |
| 16 | 12 |

ACC = 10, IX = 0

Complete the table by writing the content of the ACC after each program has run.

| Program | Code | ACC content |
|---------|------|-------------|
| 1 | LDI 15 / SUB #1 | |
| 2 | LDD 14 / ADD 11 | |
| 3 | LDM #11 / ADD #3 / SUB 16 | |
| 4 | LDR #2 / LDX 14 / ADD #2 | |

[4 marks]

(b) The processor includes these bit manipulation instructions:
- AND #n/Bn/&n — Bitwise AND operation of the contents of ACC with the operand
- AND <address> — Bitwise AND of ACC with contents of <address>
- XOR #n/Bn/&n — Bitwise XOR operation of ACC with the operand
- XOR <address> — Bitwise XOR of ACC with contents of <address>
- OR #n/Bn/&n — Bitwise OR operation of ACC with the operand
- OR <address> — Bitwise OR of ACC with contents of <address>

Memory contents:

| Address | Data |
|---------|------|
| 25 | 11000110 |
| 26 | 11100001 |
| 27 | 10000001 |
| 28 | 11001101 |
| 29 | 00001111 |

ACC = 01000110

Complete the table (ACC reloaded to 01000110 before each program):

| Program | Code | ACC content |
|---------|------|-------------|
| 1 | XOR 29 | |
| 2 | AND #29 | |
| 3 | OR B11111111 | |

[3 marks]

---

## 2024 Oct/Nov (9618/12)

### Question 3(a) (Registers)
The computer is designed using the Von Neumann model for a computer system.
Complete the table by describing the purpose of each of the given registers.

| Register | Purpose |
|----------|---------|
| Program Counter (PC) | |
| Memory Address Register (MAR) | |
| Memory Data Register (MDR) | |
| Index Register (IX) | |

[4 marks]

### Question 8
The following table shows part of the instruction set for a processor. The processor has two registers, the Accumulator (ACC) and the Index Register (IX).

Instruction set: LDM, LDD, LDI, LDX, LDR, ADD, SUB, INC, DEC

(a) The current contents of memory are shown:

| Address | Data |
|---------|------|
| 19 | 25 |
| 20 | 23 |
| 21 | 2 |
| 22 | 4 |
| 23 | 15 |
| 24 | 50 |
| 25 | 22 |

ACC = 50, IX = 20

Complete the table by writing the content of the ACC and the IX after each set of instructions has run.

| Instructions | ACC content | IX content |
|---|---|---|
| 1: LDM #19 / DEC ACC | | |
| 2: LDD 23 / ADD 19 | | |
| 3: LDI 25 / INC ACC | | |
| 4: LDR #21 / LDX 2 | | |

[5 marks]

(b) The instruction set also includes bit manipulation instructions: AND, XOR, OR, LSL, LSR.

ACC = 10011010

(i) Complete the table (ACC reloaded to 10011010 before each set):

| Instructions | ACC content |
|---|---|
| 1: LSL #2 / ADD #5 | |
| 2: AND #30 / OR B11110010 | |
| 3: INC ACC | |

[3 marks]

(ii) Explain how bit manipulation can be used to test whether the binary number stored in the ACC represents an odd denary number.
Write the bit manipulation instruction that will be used.
[3 marks]

---

## 2023 May/June (9618/12)

### Question 3
A program is written in assembly language.

(a) The program is converted into machine code by a two-pass assembler.
Draw one or more lines to identify the pass or passes in which each action takes place.

Actions:
- generates object code
- reads the source code one line at a time
- removes white space
- adds labels to the symbol table

Passes: first, second
[3 marks]

(b) Assembly language statements can use different modes of addressing.
Complete the following description of addressing modes.

.................... addressing is when the operand holds the memory address of the data.
.................... addressing is when the operand holds a memory address that stores the memory address of the data.
.................... addressing is when the operand is the data.
[3 marks]

### Question 5(a)(b) (CPU architecture)
A student has purchased a new laptop. The laptop is designed using the Von Neumann model for a computer system.

(a) Identify two types of signal that a control bus can transfer.
[2 marks]

(b) Describe two ways the hardware of a laptop can be upgraded to improve the performance and explain how each upgrade improves the performance.
[4 marks]

---

## 2023 Oct/Nov (9618/12)

### Question 8(c) (Buses)
An optical disc reader/writer is connected to the computer.

(i) Give the name of one port that can provide a connection for the optical disc reader/writer.
[1 mark]

(ii) Describe the roles of the address bus, the data bus and buffers in the process of writing data to the optical disc reader/writer.
[3 marks]

### Question 9
The following table shows part of the instruction set for a processor. The processor has two registers, the Accumulator (ACC) and the Index Register (IX).

Instruction set includes: LDD, LDX, LDR, STO, ADD, JMP, INC, CMP, CMI, JPE, IN, OUT, END.

(a) The instructions in the processor's instruction set can be grouped according to their function.
Identify the instruction group for each of the following opcodes:
- IN
- ADD
- JPE
- CMI
[4 marks]

(b) The current contents of main memory and selected values from the ASCII character set are given.
Trace the program currently in memory using the trace table when the input is '1'.

Program:
```
10  LDR #0
11  IN
12  STO 101
13  LDX 110
14  CMP 100
15  JPE 21
16  LDD 101
17  ADD #16
18  INC IX
19  STO 100
20  JMP 13
21  OUT
22  END
```

Memory: 100=0, 101=0, 110=51, 111=65
ASCII: 49=1, 50=2, 51=3, 52=4, 65=A, 66=B, 67=C, 68=D
[4 marks]

---

## 2022 Oct/Nov (9618/12)

### Question 7
The following table shows part of the instruction set for a processor. The processor has one general purpose register, the Accumulator (ACC), and an Index Register (IX).

Instruction set includes: LDM, LDD, LDX, LDR, STO, ADD, INC, JMP, CMP, CMI, JPE, JPN, END.

(a) Trace the program currently in memory using the trace table, stopping when line 90 is executed for a second time.

Program:
```
75  LDR #0
76  LDX 110
77  CMI 102
78  JPE 91
79  CMP 103
80  JPN 84
81  ADD 101
82  STO 101
83  JMP 86
84  INC ACC
85  STO 101
86  LDD 100
87  INC ACC
88  STO 100
89  INC IX
90  JMP 76
91  END
```

Memory: 100=0, 101=0, 102=112, 103=4, 110=1, 111=4, 112=0
[5 marks]

(b) Bit manipulation instructions: AND, XOR, OR, LSL, LSR.

Memory: 50=01001101, 51=10001111

(i) ACC = 01010011. Show ACC after: XOR B00011111
[1 mark]

(ii) ACC = 01010011. Show ACC after: AND 50
[1 mark]

(iii) ACC = 01010011. Show ACC after: LSL #3
[1 mark]

(iv) ACC = 01010011. Show ACC after: OR 51
[1 mark]

(c) Write the register transfer notation for each of the stages in the fetch-execute cycle:
- Copy the address of the next instruction into the Memory Address Register.
- Increment the Program Counter.
- Copy the contents of the Memory Data Register into the Current Instruction Register.
[3 marks]

---

## 2021 May/June (9618/12)

### Question 4
The table shows part of the instruction set for a processor. The processor has one general purpose register, the Accumulator (ACC), and an Index Register (IX).

Instruction set includes: LDM, LDD, STO, ADD, INC, DEC, CMP, JPE, JPN, JMP, IN, OUT, END.

Program and memory:
```
70  IN
71  CMP 100
72  JPE 80
73  CMP 101
74  JPE 76
75  JMP 80
76  LDD 102
77  INC ACC
78  STO 102
79  JMP 70
80  LDD 102
81  DEC ACC
82  STO 102
83  JMP 70
```

Memory: 100=68, 101=65, 102=100
ASCII: 65=A, 66=B, 67=C, 68=D

(a) Complete the trace table for the program when the following characters are input: A D
Do not trace the program any further when the third input is required.
[4 marks]

(b) Some bit manipulation instructions: AND, XOR, OR.

Memory address 300 contains: 01100110

(i) Write the denary value of the unsigned binary integer in memory address 300.
[1 mark]

(ii) An assembly language program needs to test if bit number 2 in memory address 300 is a 1.
Complete the assembly language instruction to perform this test: .................... #4
[1 mark]

(iii) An assembly language program needs to set bit numbers 4, 5, 6 and 7 to 0, but keep bits 0 to 3 with their existing values.
Write the assembly language instruction to perform this action.
[2 marks]

### Question 5(a)(b) (CPU components)
Seth uses a computer for work.

(a) Complete the following descriptions of internal components of a computer by writing the missing terms.
- The .................... transmits the signals to coordinate events based on the electronic pulses of the .................... .
- The .................... carries data to the components, while the .................... carries the address where data needs to be written to or read from.
- The .................... performs mathematical operations and logical comparisons.
[5 marks]

(b) Describe the ways in which the following factors can affect the performance of his laptop computer.
- Number of cores
- Clock speed
[4 marks]
