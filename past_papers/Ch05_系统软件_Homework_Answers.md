# Chapter 5: System Software - Homework Answers

> Total: 55 marks

---

## Question 1 [4 marks]

Describe **two** functions of memory management that the operating system performs to support multi-tasking.

**Answer:**

1. ✓ The OS allocates a separate area/partition of memory to each process/application that is running
   ✓ This prevents one process from accessing or overwriting the memory space of another process (memory protection)

2. ✓ The OS manages the swapping of processes between main memory (RAM) and secondary storage (virtual memory / paging)
   ✓ When RAM is full, the OS moves inactive pages/segments to disk to free up memory for the active process

---

## Question 2 [6 marks]

**(a)** Explain what is meant by **process scheduling**. [2 marks]

**Answer:**

✓ Process scheduling is the method by which the operating system determines which process/task gets to use the processor (CPU) and for how long
✓ It is needed because there are usually more processes waiting to be executed than there are processors available, so the OS must manage access to the CPU

**(b)** Describe **two** different scheduling algorithms. For each, give one advantage and one disadvantage. [4 marks]

**Answer:**

1. **Round Robin:**
   ✓ Each process is given an equal fixed time slice (quantum) of CPU time in turn; when the time slice expires, the process is moved to the back of the queue and the next process is given a time slice
   - Advantage: Every process gets a fair share of CPU time; no process is starved
   - Disadvantage: If the time slice is too short, excessive context switching overhead occurs; if too long, response time suffers

2. **Shortest Job First (SJF):**
   ✓ The process with the shortest estimated execution time is selected to run next
   - Advantage: Minimises the average waiting time for all processes
   - Disadvantage: Longer processes may be starved (never get to run) if shorter processes keep arriving; requires advance knowledge of execution times

---

## Question 3 [5 marks]

**(a)** State **three** tasks that an operating system performs as part of file management. [3 marks]

**Answer:**

✓ Creating, deleting, renaming, copying and moving files and directories/folders
✓ Controlling access to files by managing file permissions / access rights (read, write, execute)
✓ Managing the allocation of disk space to files and keeping track of where files are stored on the disk

**(b)** Explain the role of a **file allocation table (FAT)** in file management. [2 marks]

**Answer:**

✓ The FAT is a data structure maintained by the OS that records which disk blocks/clusters are allocated to each file
✓ It maps filenames to the physical locations on disk where the file's data is stored, allowing the OS to locate and retrieve file data; it also tracks which blocks are free/available for new data

---

## Question 4 [6 marks]

| Utility software | Purpose | Why it is needed |
|-----------------|---------|------------------|
| Disk defragmenter | ✓ Reorganises the data on a hard disk so that files are stored in contiguous (adjacent) blocks/sectors rather than being scattered across the disk | ✓ Over time, as files are created, deleted, and modified, they become fragmented; defragmentation improves read/write speed and overall disk performance |
| Virus checker | ✓ Scans files and programs on the computer for known malware (viruses, worms, trojans) by comparing them against a database of virus signatures/definitions | ✓ Malware can damage or delete data, steal personal information, or slow down the system; regular scanning helps detect and remove threats |
| Backup utility | ✓ Creates copies of files and data, which can be stored on a separate medium (e.g. external drive, cloud) | ✓ If data is lost due to hardware failure, accidental deletion, or malware, the backup can be used to restore the data to its previous state |

---

## Question 5 [6 marks]

**(a)** Explain the difference between a **compiler** and an **interpreter**. [4 marks]

**Answer:**

**Compiler:**
✓ Translates the entire source code of a high-level language program into machine code (object code) in one go, before the program is run
✓ Produces a standalone executable file that can be run without the compiler being present; errors are reported after the whole program has been analysed

**Interpreter:**
✓ Translates and executes the source code one line/statement at a time; each line is translated and immediately executed before moving to the next
✓ Does not produce a separate executable file; the interpreter must be present every time the program is run; stops at the first error encountered and reports it

**(b)** State the role of an **assembler** in translating programs. [2 marks]

**Answer:**

✓ An assembler translates a program written in assembly language into machine code (object code)
✓ It converts assembly language mnemonics (e.g. LDA, ADD, STO) into their corresponding binary/machine code instructions on a one-to-one (one mnemonic to one machine code instruction) basis

---

## Question 6 [8 marks]

**(a)** Describe what happens during **lexical analysis**. [3 marks]

**Answer:**

✓ The source code is read and unnecessary whitespace and comments are removed
✓ The remaining code is broken down into individual tokens (tokenisation) — e.g. keywords, identifiers, operators, literals
✓ A symbol table is created/populated, storing details of identifiers (variable names, procedure names) along with their attributes (e.g. data type, scope, memory address)

**(b)** Describe what happens during **syntax analysis**. [3 marks]

**Answer:**

✓ The stream of tokens produced by lexical analysis is checked against the grammar rules of the programming language
✓ A parse tree / abstract syntax tree (AST) is built to represent the structure of the program
✓ Any syntax errors (e.g. missing semicolons, mismatched brackets, incorrect use of keywords) are identified and reported to the programmer

**(c)** State **two** ways in which a compiler might perform **code optimisation**. [2 marks]

**Answer:**

✓ Removing redundant instructions — e.g. eliminating code that is never executed (dead code elimination) or simplifying expressions that can be computed at compile time (constant folding)
✓ Optimising loops — e.g. moving calculations that produce the same result out of a loop so they are only performed once (loop-invariant code motion), or replacing repeated variable lookups with register usage

---

## Question 7 [6 marks]

**(a)** Describe **three** features of an IDE that help during the coding stage. [3 marks]

**Answer:**

✓ **Auto-complete / code suggestion** — the IDE predicts and suggests the rest of a keyword, variable name, or function name as the programmer types, reducing typing errors and speeding up coding
✓ **Syntax highlighting** — different elements of the code (keywords, strings, comments, variables) are displayed in different colours/styles, making the code easier to read and helping the programmer spot errors
✓ **Auto-indentation / code formatting** — the IDE automatically indents code blocks (e.g. inside loops, conditionals), making the structure of the program clearer

**(b)** Describe **three** debugging features provided by a typical IDE. [3 marks]

**Answer:**

✓ **Breakpoints** — the programmer can set markers at specific lines of code; the program pauses execution at each breakpoint, allowing the programmer to inspect the state of variables and the flow of execution at that point
✓ **Stepping (step over / step into)** — allows the programmer to execute the program one line at a time, observing the effect of each statement; this helps locate the exact line where an error occurs
✓ **Variable watch / inspect** — the programmer can monitor the values of selected variables in real time as the program runs; this helps identify where a variable takes an unexpected or incorrect value

---

## Question 8 [4 marks]

Explain the role of the operating system in **I/O management**.

**Answer:**

✓ The OS manages communication between the CPU and all input/output peripheral devices (keyboard, mouse, printer, disk, etc.)
✓ It uses device drivers — software that translates general OS commands into specific instructions that each hardware device can understand
✓ It manages the use of buffers — temporary memory areas where data is held while being transferred between devices operating at different speeds (e.g. a fast CPU and a slow printer)
✓ It handles interrupts generated by I/O devices — when a device needs attention (e.g. data is ready, transfer is complete), it sends an interrupt signal to the CPU, and the OS ensures the interrupt is handled appropriately

---

## Question 9 [4 marks]

**Arguments FOR using an interpreter during development:**

✓ An interpreter reports errors one at a time and stops at the first error, making it easier for the programmer to locate and fix bugs during development
✓ The program can be tested and run immediately without waiting for the entire program to be compiled, speeding up the development/debugging cycle

**Arguments AGAINST using an interpreter during development:**

✓ An interpreted program runs more slowly than a compiled program because each line must be translated every time it is executed; this can make testing slow for large programs
✓ The interpreter must be present in memory every time the program is run, which uses additional resources; a compiled program produces a standalone executable that runs independently

---

## Question 10 [6 marks]

**(a)** Identify stages A, B, and C. [3 marks]

**Answer:**

✓ Stage A: Lexical analysis
✓ Stage B: Syntax analysis (parsing)
✓ Stage C: Code generation (and/or code optimisation)

**(b)** Explain what a symbol table contains and how it is used in later stages. [3 marks]

**Answer:**

✓ The symbol table contains entries for each identifier (variable name, constant name, procedure/function name) found in the source code, along with attributes such as data type, scope, and memory address
✓ During syntax analysis, the symbol table is used to check that variables have been declared before use and that operations are type-compatible (e.g. not adding a string to an integer)
✓ During code generation, the symbol table is used to allocate memory addresses to variables and to generate the correct machine code instructions for accessing those variables

---

**--- END OF ANSWERS ---**
