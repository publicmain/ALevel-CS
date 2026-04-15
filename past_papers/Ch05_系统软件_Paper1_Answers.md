# Chapter 5: System Software - Paper 1 Mark Scheme Answers

> Topics: Operating systems (memory management, process management, utility software), language translators (compilers, interpreters, assemblers), IDEs

---

## 2024 May/June (9618/12)

### Question 6
A computer has an Operating System (OS). Explain how memory management and process management support multi-tasking. [4 marks]

**Memory management:**
✓ Memory management allocates a partition/section of memory to each process/application
✓ Memory management keeps track of which parts of memory are in use and which are free
✓ Memory management swaps data/pages between main memory and secondary storage (virtual memory / paging) when there is not enough RAM for all processes

> 提示：内存管理通过分区（partitioning）和虚拟内存（virtual memory/paging）让多个程序同时驻留内存

**Process management:**
✓ Process management allocates processor time to each process using scheduling algorithms
✓ Process management switches between processes rapidly (context switching) so they appear to run simultaneously
✓ Process management maintains the state of each process so it can be resumed after being interrupted

> 提示：进程管理通过调度算法（scheduling）和上下文切换（context switching）实现多任务并发

*Any 4 points from above for 4 marks*

---

### Question 8
(a) Describe the benefits of using the compiler when testing the final program. [2 marks]

✓ The compiled program runs/executes faster than an interpreted program (because it is translated into machine code as a complete unit / does not need to be translated each time it runs)
✓ The compiled program produces a standalone executable file that can be distributed to users without them needing the compiler / source code is not revealed to the end user
✓ The compiler produces a complete list of all errors at once, allowing the programmer to see all issues before distribution

> 提示：编译器优势 - 运行速度快（生成机器码），可生成独立可执行文件，源代码不会暴露

*Any 2 points for 2 marks*

---

(b) Complete the table by identifying one other common IDE feature for each purpose. [6 marks]

| Purpose | IDE feature | Description |
|---------|-------------|-------------|
| for coding | ✓ Auto-complete / context-sensitive prompts / code templates | ✓ The IDE predicts and suggests the rest of a keyword/variable/function name as the programmer types, reducing syntax errors and speeding up coding |
| for presentation | ✓ Pretty printing / syntax highlighting / colour coding | ✓ The IDE uses different colours/formatting for different parts of the code (keywords, strings, comments etc.) making it easier to read and identify elements of the program |
| for debugging | ✓ Breakpoints / single stepping / variable watch window | ✓ The programmer can set a point in the code where execution will pause, allowing them to inspect variable values and trace the program flow to locate logic errors |

> 提示：IDE功能 - 编码：自动补全；展示：语法高亮/美化打印；调试：断点/单步执行/变量监视窗口

*1 mark for each correct feature name + 1 mark for each correct description = 6 marks*

---

## 2024 Oct/Nov (9618/12)

### Question 3(c) (Process management)
Describe the process management tasks performed by an OS. [4 marks]

✓ Allocates processor time / CPU cycles to each process
✓ Uses scheduling algorithms (e.g. round robin, shortest job first) to determine the order in which processes are executed
✓ Manages interrupts -- when an interrupt occurs, the OS saves the current state of the process and handles the interrupt
✓ Manages the switching between processes (context switching) to allow multi-tasking
✓ Maintains process states (ready, running, waiting/blocked) and transitions between them
✓ Manages the priority of processes to determine which process gets CPU time first

> 提示：进程管理 - 分配CPU时间、调度算法、处理中断、上下文切换、管理进程状态（就绪/运行/等待）

*Any 4 points for 4 marks*

---

### Question 4
(a) Describe how the programmers can use the debugging features of a typical IDE during the development of the program. [4 marks]

✓ **Breakpoints** -- the programmer sets a point in the code where execution will pause so they can examine variable values at that point
✓ **Single stepping / stepping through** -- the programmer can execute the program one line/instruction at a time to trace the flow of execution
✓ **Variable watch window** -- the programmer can monitor the values of selected variables as the program executes to identify where incorrect values occur
✓ **Report window / error messages** -- the IDE displays runtime errors and their locations, helping the programmer identify and fix bugs
✓ **Call stack** -- shows the sequence of function/procedure calls that led to the current point, helping trace logic errors

> 提示：调试功能 - 断点（暂停执行）、单步执行（逐行运行）、变量监视（实时查看变量值）、错误报告

*Any 4 points for 4 marks*

---

(b) Describe the benefits to the programmers of creating a program library. [3 marks]

✓ Modules/subroutines in the library can be reused across multiple programs / by other programmers in the team, saving development time
✓ The library code has already been tested and debugged, so using it reduces the likelihood of errors in new programs
✓ The library provides a consistent approach / standardised code across the team, making the program easier to maintain
✓ Programmers do not need to rewrite code that has already been written, reducing duplication of effort

> 提示：程序库优势 - 代码复用节省时间、已测试减少错误、统一标准便于维护

*Any 3 points for 3 marks*

---

## 2023 May/June (9618/12)

### Question 3(a) (Assembler)
Draw lines to identify the pass in which each action takes place. [3 marks]

| Action | Pass |
|--------|------|
| generates object code | ✓ **Second** pass |
| reads the source code one line at a time | ✓ **First** pass (also in second pass, but primarily associated with first) |
| removes white space | ✓ **First** pass |
| adds labels to the symbol table | ✓ **First** pass |

> 提示：两遍汇编 - 第一遍：逐行读取源代码、去除空白、将标签加入符号表；第二遍：生成目标代码

*"reads source code" connects to first pass; "removes white space" connects to first pass; "adds labels to symbol table" connects to first pass; "generates object code" connects to second pass. 3 marks for all 4 correct, lose 1 mark per error.*

---

### Question 5(d)
(i) Describe how the Operating System (OS) manages processes in the computer. [5 marks]

✓ The OS allocates processor time to each process
✓ Uses scheduling algorithms to determine which process to run next
✓ Manages interrupts -- saves the state of the current process when an interrupt occurs
✓ Handles context switching between processes
✓ Maintains a queue of processes waiting to use the processor
✓ Manages the different states of processes: ready, running, blocked/waiting
✓ Allocates resources (memory, I/O devices) to processes
✓ Prevents deadlock where two or more processes are waiting for each other's resources

> 提示：OS进程管理 - 分配CPU时间、调度、中断处理、上下文切换、维护进程队列和状态、资源分配、防止死锁

*Any 5 points for 5 marks*

---

(ii) Describe the purpose of utility software in a computer. [2 marks]

✓ Utility software performs housekeeping/maintenance tasks on the computer system
✓ Examples include: virus checker (scans for malware), disk defragmenter (reorganises files to be contiguous), backup utility (creates copies of files), disk formatter (initialises a disk for use)
✓ Utility software helps to maintain the performance, security and efficiency of the computer

> 提示：实用程序（工具软件）用于系统维护，如杀毒、磁盘整理、备份、格式化等

*1 mark for general purpose + 1 mark for a described example = 2 marks*

---

### Question 7
(a)(i) Define the term program library. [2 marks]

✓ A program library is a collection of pre-written / pre-compiled code / subroutines / modules
✓ ...that can be called/used by other programs when needed / that can be incorporated into programs

> 提示：程序库 = 预编写的代码/子程序集合，可被其他程序调用

---

(a)(ii) Explain two benefits to the developer of choosing to create a Dynamic Link Library (DLL). [4 marks]

**Benefit 1:**
✓ DLL code is loaded into memory only when it is needed at runtime / not compiled into the main executable
✓ This means the executable file is smaller, saving disk space and memory when the DLL functions are not in use

**Benefit 2:**
✓ A DLL can be shared between multiple programs / applications simultaneously
✓ This means if the DLL is updated (e.g. bug fix), all programs that use it benefit from the update without needing to be recompiled

> 提示：DLL优势 - 1) 按需加载，节省内存和磁盘空间；2) 多程序共享，更新DLL即可同时更新所有调用程序

---

(b) Identify whether an interpreter or a compiler would be more appropriate at this stage. Justify your choice. [3 marks]

✓ An **interpreter** would be more appropriate at this stage (during development)
✓ An interpreter translates and executes the code one line at a time, so errors can be identified and fixed immediately without waiting for the whole program to compile
✓ The programmer can test parts of the program as they are written, making the development process faster and more interactive
✓ The programmer does not need to wait for the entire program to be compiled each time a change is made

> 提示：开发阶段用解释器 - 逐行执行、即时发现错误、修改后可立即测试，无需等待整个编译过程

*1 mark for correct identification + 2 marks for justification = 3 marks*

---

(c) Complete the table by describing the typical features found in an IDE. [4 marks]

| Feature | Description |
|---------|-------------|
| Breakpoints | ✓ Allows the programmer to set a marker/point in the code where program execution will pause, so the programmer can examine variable values and the state of the program at that point |
| Dynamic syntax checks | ✓ The IDE checks the syntax of the code as it is being typed/in real time and highlights/underlines errors before the program is run, allowing the programmer to fix errors immediately |
| Context-sensitive prompts | ✓ The IDE suggests/auto-completes keywords, variable names, function names or parameters as the programmer types, based on the current context of the code |
| Single stepping | ✓ Allows the programmer to execute the program one line/instruction at a time, so they can trace the logic and identify where errors occur by observing changes in variable values |

> 提示：断点=暂停执行点；动态语法检查=实时检测语法错误；上下文提示=自动补全；单步执行=逐行运行

---

(d) Explain how Artificial Intelligence (AI) can be used to convert user's speech into commands. [3 marks]

✓ The AI system uses machine learning / has been trained on large datasets of speech samples to recognise patterns in speech
✓ The system converts speech to text using speech recognition algorithms / Natural Language Processing (NLP)
✓ The AI interprets the meaning / context of the spoken words and maps them to appropriate program commands
✓ The system can learn and improve over time by processing more data / adapting to different accents, voices, speech patterns

> 提示：AI语音识别 - 机器学习训练语音数据集、语音转文字（NLP自然语言处理）、理解语义映射为命令、持续学习改进

*Any 3 points for 3 marks*

---

## 2023 Oct/Nov (9618/12)

### Question 8
(a) State one purpose of the Operating System. [1 mark]

✓ To provide an interface between the user and the hardware / to manage the hardware resources of the computer / to manage processes / to manage memory / to manage files / to manage I/O devices

> 提示：OS目的 - 在用户和硬件之间提供接口 / 管理硬件资源

---

(b) Identify one example of utility software that is not intended to improve security. Explain why this software is needed. [3 marks]

✓ **Disk defragmenter** (or: backup utility, disk formatter, file compression)
✓ Over time, files become fragmented (stored in non-contiguous locations on the disk) as files are created, modified and deleted
✓ The defragmenter reorganises the files so that they are stored in contiguous blocks, reducing the time the read/write head takes to access data and improving system performance

> 提示：磁盘碎片整理程序 - 文件碎片化导致访问变慢，整理后文件连续存储，提高读写速度

*1 mark for identification + 2 marks for explanation = 3 marks*

---

## 2022 Oct/Nov (9618/12)

### Question 1
(a) Draw one line from each utility software to its most appropriate purpose. [5 marks]

| Utility Software | Purpose |
|-----------------|---------|
| ✓ Virus checker | to scan for malicious program code |
| ✓ Disk formatter | to initialise a disk |
| ✓ Backup | to create copies of files in case the original is lost |
| ✓ Disk repair | to check for and fix inconsistencies on a disk |
| ✓ Defragmentation | to reorganise files so they are contiguous |

Note: "to decrease the file size" is the distractor (this would be file compression, which is not listed).

> 提示：病毒检查=扫描恶意代码；格式化=初始化磁盘；备份=创建文件副本；磁盘修复=检查修复不一致；碎片整理=重组文件使其连续

---

(b)(i) State two drawbacks of using a compiler compared to an interpreter during program development. [2 marks]

✓ The compiler must translate the entire program before any part of it can be executed, which is slower during development when frequent small changes are made
✓ If there are errors, the programmer must fix them and recompile the whole program before testing, rather than being able to test up to the point of the error

> 提示：编译器缺点（开发阶段）- 必须编译整个程序才能运行；有错误需重新编译整个程序

---

(b)(ii) Explain why high-level language programs might be partially compiled and partially interpreted. [2 marks]

✓ Some languages (e.g. Java) compile the source code into an intermediate code (bytecode) rather than directly into machine code
✓ The intermediate code / bytecode is then interpreted at runtime by a virtual machine, allowing the same compiled code to run on different platforms / operating systems (platform independence)

> 提示：部分编译+部分解释 - 如Java先编译成字节码（中间代码），再由虚拟机解释执行，实现跨平台运行

---

## 2021 May/June (9618/12)

### Question 7
(a) Describe how a program library can be used while writing a computer program. [2 marks]

✓ A program library contains pre-written / pre-tested subroutines/modules/code that can be imported/included into the programmer's program
✓ The programmer can call/invoke these subroutines in their program rather than having to write the code themselves, saving time and reducing errors

> 提示：程序库使用 - 导入预编写的模块/子程序，直接调用而无需自己编写，节省时间减少错误

---

(b)(i) Describe the ways in which Jennifer can use both a compiler and an interpreter while developing the program. [4 marks]

**Interpreter during development:**
✓ Jennifer uses the interpreter during the development/coding stage to test sections of code as she writes them
✓ The interpreter executes code line by line, immediately identifying errors so she can fix them quickly without waiting for full compilation

**Compiler for final version:**
✓ Jennifer uses the compiler once the program is complete and debugged, to produce a standalone executable file
✓ The compiled executable runs faster than interpreted code and can be distributed without revealing the source code

> 提示：开发阶段用解释器（逐行测试、快速定位错误）；完成后用编译器（生成快速运行的可执行文件，保护源代码）

---

(b)(ii) Identify two debugging tools that a typical IDE can provide. [2 marks]

✓ Breakpoints
✓ Single stepping / step through
✓ Variable watch window
✓ Call stack

> 提示：调试工具 - 断点、单步执行、变量监视窗口、调用栈（任选两个）

*Any 2 for 2 marks*
