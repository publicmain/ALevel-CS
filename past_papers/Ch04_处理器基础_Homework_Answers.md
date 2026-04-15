# Chapter 4: Processor Fundamentals - Homework Answers

> 总分：58

---

## Question 1 — Von Neumann Architecture 冯·诺依曼架构 [6 marks]

**(a)** Three features of the Von Neumann architecture. [3 marks]

1. Both program instructions and data are stored together in the same main memory (stored program concept) ✓.
2. Instructions are fetched and executed sequentially (one at a time) unless a branch/jump instruction is encountered ✓.
3. There is a single set of buses (address bus, data bus, control bus) connecting the processor to memory, meaning instructions and data share the same pathway ✓.

---

**(b)** Labelled diagram. [3 marks]

```
┌────────────────────────────────────────────────────────┐
│                     PROCESSOR (CPU)                     │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │     CU       │  │     ALU      │  │  Registers   │  │
│  │(Control Unit)│  │(Arithmetic   │  │  - PC        │  │
│  │              │  │ Logic Unit)  │  │  - MAR       │  │
│  │              │  │              │  │  - MDR       │  │
│  │              │  │              │  │  - CIR       │  │
│  │              │  │              │  │  - ACC       │  │
│  └──────────────┘  └──────────────┘  └──────────────┘  │
└──────────┬──────────────┬──────────────┬───────────────┘
           │              │              │
     Address Bus     Data Bus      Control Bus
     (unidirectional) (bidirectional) (bidirectional)
           │              │              │
     ┌─────┴──────────────┴──────────────┴──────┐
     │              MAIN MEMORY (RAM)            │
     │  ┌───────┬──────────┐                     │
     │  │Address│ Contents │                     │
     │  ├───────┼──────────┤                     │
     │  │  000  │ xxxxxxxx │                     │
     │  │  001  │ xxxxxxxx │                     │
     │  │  ...  │   ...    │                     │
     │  └───────┴──────────┘                     │
     └──────────────────────────────────────────┘
```

✓ Processor shown with ALU and CU.
✓ Registers shown within the processor.
✓ Three separate buses connecting processor to main memory (RAM).

---

## Question 2 — CPU Components 处理器组件 [6 marks]

**(a)(i)** Arithmetic Logic Unit (ALU). [2 marks]

The ALU performs all arithmetic operations (such as addition, subtraction, multiplication, division) ✓ and all logical/comparison operations (such as AND, OR, NOT, XOR, comparisons like equal to, greater than, less than) on data ✓.

---

**(a)(ii)** Control Unit (CU). [2 marks]

The CU coordinates and controls the operations of all other components of the CPU. It sends control signals along the control bus to manage the flow of data between the processor, memory, and I/O devices ✓. It decodes instructions fetched from memory and directs the ALU, registers, and other components to execute them in the correct sequence ✓.

---

**(b)(i)** Program Counter (PC). [1 mark]

The PC holds/stores the memory address of the next instruction to be fetched and executed ✓.

---

**(b)(ii)** Memory Address Register (MAR). [1 mark]

The MAR holds the memory address of the location in memory that is about to be read from or written to ✓.

---

## Question 3 — Registers 寄存器 [5 marks]

**(a)** MDR (Memory Data Register). [1 mark]

The MDR holds the data that has been read from memory or the data that is to be written to memory. It acts as a buffer between the processor and main memory ✓.

---

**(b)** CIR (Current Instruction Register). [1 mark]

The CIR holds the current instruction being decoded and executed. The instruction is copied here from the MDR during the fetch stage ✓.

---

**(c)** Accumulator (ACC). [1 mark]

The ACC is a general-purpose register that stores the result of calculations performed by the ALU. It acts as the primary working register for arithmetic and logic operations ✓.

---

**(d)** Index Register (IX). [1 mark]

The IX holds a value that is added to the operand of an instruction to produce the effective/actual memory address when using indexed addressing ✓.

---

**(e)** Status Register. [1 mark]

The Status Register contains individual bits (flags) that are set or cleared to indicate the current status/state of the processor, such as whether the last operation resulted in zero, a carry, an overflow, or a negative result ✓.

---

## Question 4 — Buses 总线 [6 marks]

**(a)(i)** Address bus. [2 marks]

The address bus carries the memory address from the processor to memory (or I/O devices), specifying which memory location is to be read from or written to ✓. It is unidirectional (signals travel only from the processor to memory). The width of the address bus determines the maximum number of memory locations that can be addressed (e.g., a 32-bit address bus can address 2^32 locations) ✓.

---

**(a)(ii)** Data bus. [2 marks]

The data bus carries data between the processor, memory, and I/O devices ✓. It is bidirectional -- data can travel from memory to the processor (reading) or from the processor to memory (writing). The width of the data bus determines how many bits of data can be transferred in a single operation ✓.

---

**(a)(iii)** Control bus. [2 marks]

The control bus carries control signals from the Control Unit to other components (and status signals back) to coordinate and synchronise the operations of the computer system ✓. Examples of control signals include: memory read, memory write, clock signal, interrupt request, and bus request ✓.

---

## Question 5 — Fetch-Execute Cycle 取指-执行周期 [8 marks]

**(a)** Fetch stage. [4 marks]

1. The contents of the Program Counter (PC) are copied to the Memory Address Register (MAR). The address is then sent along the address bus to memory ✓.
2. A memory read signal is sent along the control bus ✓.
3. The data (instruction) stored at the addressed memory location is transferred along the data bus to the Memory Data Register (MDR) ✓.
4. The contents of the MDR are copied to the Current Instruction Register (CIR). The Program Counter (PC) is incremented by 1 to point to the next instruction ✓.

---

**(b)** Decode stage. [2 marks]

The Control Unit decodes/interprets the instruction held in the CIR ✓. The instruction is split into its opcode (which identifies the operation to be performed) and its operand (which identifies the data or address to be used). The CU then determines what signals need to be sent to execute the instruction ✓.

---

**(c)** Two factors affecting CPU performance. [2 marks]

1. **Clock speed:** A higher clock speed means more fetch-execute cycles can be completed per second, leading to faster processing ✓.
2. **Number of cores:** A processor with multiple cores can execute multiple instructions simultaneously (in parallel), improving overall performance ✓.

---

## Question 6 — Instruction Format and Addressing Modes 指令格式与寻址方式 [8 marks]

**(a)(i)** Opcode. [1 mark]

The opcode is the part of a machine code instruction that specifies the operation to be performed (e.g., ADD, LOAD, STORE, JUMP) ✓.

---

**(a)(ii)** Operand. [1 mark]

The operand is the part of a machine code instruction that specifies the data to be used, or the address of the data, or the address to jump to ✓.

---

**(b)(i)** Immediate addressing. [2 marks]

In immediate addressing, the operand in the instruction IS the actual data value to be used, not a memory address ✓. Example use: Loading a constant value into the accumulator (e.g., `LDM #5` loads the value 5 directly into the ACC), useful when a fixed/known value is needed in a calculation ✓.

---

**(b)(ii)** Direct addressing. [2 marks]

In direct addressing, the operand in the instruction gives the memory address where the required data is stored ✓. Example use: Loading a variable's value from a known fixed memory location (e.g., `LDD 100` loads the value stored at address 100 into the ACC), useful for accessing data stored in specific memory locations ✓.

---

**(b)(iii)** Indirect addressing. [2 marks]

In indirect addressing, the operand gives the memory address of a location that itself contains the address of the required data (a pointer) ✓. Example use: Accessing data through a pointer, which is useful when the actual memory address of the data is not known at compile time, or for implementing data structures such as linked lists where addresses are stored within the data structure itself ✓.

---

## Question 7 — Addressing Modes in Practice 寻址方式实践 [5 marks]

Memory contents for reference:

| Address | Contents |
|---------|----------|
| 100     | 50       |
| 101     | 200      |
| 200     | 75       |
| 201     | 300      |
| 300     | 42       |

**(a)** `LDI #50` (Immediate addressing). [1 mark]

The operand IS the value. ACC = **50** ✓

---

**(b)** `LDD 100` (Direct addressing). [1 mark]

Go to address 100, load its contents. ACC = **50** ✓

---

**(c)** `LDI 101` (Indirect addressing). [1 mark]

Working:
```
Go to address 101 --> contents = 200
Go to address 200 --> contents = 75
```

ACC = **75** ✓

---

**(d)** `LDX 100` (Indexed addressing, IX = 1). [1 mark]

Working:
```
Effective address = operand + IX = 100 + 1 = 101
Go to address 101 --> contents = 200
```

ACC = **200** ✓

---

**(e)** Why indirect addressing is useful. [1 mark]

In part (c), indirect addressing allows the program to access data at address 200 (containing 75) by first looking up the address stored at location 101. This is useful because the actual address of the data can be changed at runtime by simply updating the value stored in address 101, without needing to change the instruction itself. This enables the use of pointers and dynamic data structures ✓.

---

## Question 8 — Assembly Language Programming 汇编语言编程 [8 marks]

**(a)** Value stored in address 52. [1 mark]

Working:
```
LDD 50    // ACC = 20
ADD 51    // ACC = 20 + 35 = 55
STO 52    // address 52 = 55
```

Value stored: **55** ✓

---

**(b)** Assembly language program. [5 marks]

```
        LDD  200        // Load value from address 200 into ACC        ✓
        SUB  201        // Subtract value at address 201 from ACC      ✓
        CMP  #0         // Compare ACC with 0                          ✓
        JPE  EQUAL      // Jump to EQUAL if result is zero             ✓
        STO  202        // Store result in address 202
        JMP  DONE       // Jump to end to avoid falling into EQUAL
EQUAL:  LDM  #0         // Load 0 into ACC
        STO  202        // Store 0 in address 202                      ✓
DONE:   END             // End of program
```

Note: `CMP #0` compares ACC with value 0 using immediate addressing. If `CMP` does not support immediate operands in the given instruction set, an alternative approach:

```
        LDD  200
        SUB  201
        JPE  EQUAL       // If ACC = 0 after SUB, jump to EQUAL
        STO  202
        JMP  DONE
EQUAL:  STO  202         // ACC is already 0, so store it
DONE:   END
```

---

**(c)** Two advantages of assembly language over machine code. [2 marks]

1. Assembly language uses mnemonics (e.g., LDD, ADD, STO) which are easier for humans to read, understand, and remember than raw binary/hexadecimal machine code ✓.
2. Assembly language allows the use of labels (e.g., EQUAL, DONE) for memory addresses and jump targets, making programs easier to write and maintain, rather than having to calculate and remember numerical memory addresses ✓.

---

## Question 9 — Bit Manipulation 位操作 [6 marks]

Register value: `10110101`

**(a)** Set bits 0 and 1 to 1. [2 marks]

**Logical operation: OR** ✓
**Mask: 00000011**

Working:
```
  10110101    (original)
  00000011    (mask)
  ────────
  10110111    (result)     ✓
```

OR with 1 sets the bit to 1; OR with 0 leaves the bit unchanged.

---

**(b)** Clear the upper four bits (bits 4-7). [2 marks]

**Logical operation: AND** ✓
**Mask: 00001111**

Working:
```
  10110101    (original)
  00001111    (mask)
  ────────
  00000101    (result)     ✓
```

AND with 0 clears the bit to 0; AND with 1 leaves the bit unchanged.

---

**(c)** Toggle bits 2 and 3. [2 marks]

**Logical operation: XOR** ✓
**Mask: 00001100**

Working:
```
  10110101    (original)
  00001100    (mask)
  ────────
  10111001    (result)     ✓
```

XOR with 1 toggles/flips the bit; XOR with 0 leaves the bit unchanged.

Verification: bit 2 was 1, toggled to 0. Bit 3 was 0, toggled to 1.

---

*Cambridge International AS Level Computer Science 9618 - Chapter 4 Homework Answers*
