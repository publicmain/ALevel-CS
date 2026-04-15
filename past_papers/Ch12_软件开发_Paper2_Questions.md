# Chapter 12: Software Development - Paper 2 Past Questions

This file covers: program development lifecycle, testing, debugging, IDE features, error types, stub testing, black-box/white-box testing.

---

## 2024 May/June (9618/22)

### Question 5 (b)
After correcting all syntax errors, the pseudocode is translated into program code which compiles without generating any errors.

When the program is executed it unexpectedly stops responding.

Identify the type of error that has occurred.

**[1 mark]**

### Question 7
A fitness club has a computerised membership system. The system stores information for each club member: name, home address, email address, mobile phone number, date of birth and exercise preferences.

Many classes are full, and the club creates a waiting list for each class. When the system identifies that a space is available in one of the classes, a new module will send a text message to each member who is on the waiting list.

**(a)** Decomposition will be used to break the new module into sub-modules (sub-problems). Identify three sub-modules that could be used in the design and describe their use.

Sub-module 1: ... Use: ...
Sub-module 2: ... Use: ...
Sub-module 3: ... Use: ...

**[3 marks]**

### Question 8 (a)
A teacher is designing a program to process pseudocode projects written by her students. Each student project is stored in a text file. The process is split into a number of stages. Each stage performs a different task and creates a new file.

Suggest a reason why the teacher's program has been split into a number of stages and give the benefit of producing a different file from each stage.

Reason: ...
Benefit: ...

**[2 marks]**

---

## 2024 Oct/Nov (9618/22)

### Question 1
A program has been developed and released for general use. After a few months of use an error is detected where under certain circumstances it outputs an unexpected value.

**(a)** The error in the program needs to be corrected. Identify the stage of the program development life cycle that this correction is made in.

**[1 mark]**

**(b)** The program contains a function Lookup(). After investigation, it is found that this is the function that sometimes returns an incorrect value.

An Integrated Development Environment (IDE) is used to help locate the error. The IDE features of watch window, single stepping and breakpoint will be used.

Explain these features including the order that they will be used in to locate the error in Lookup().

**[3 marks]**

**(c)** To solve the error a programmer decides to create a new module. The design of the new module has been completed and the module is being coded.

Identify two features of an IDE that will help during the coding of this new module.

1: ...
2: ...

**[2 marks]**

### Question 5
A program contains a global 1D array Data with 100 elements of type INTEGER. The program contains a function Process() expressed in pseudocode as follows:

```
FUNCTION Process(Number : INTEGER, Label : STRING) RETURNS STRING
  DECLARE Index, Count : INTEGER
  DECLARE ReturnValue : STRING
  Count <- INT(100 / Number)
  Index <- Data[Number]
  CASE OF (Index MOD 2)
    0 : ReturnValue <- TO_UPPER(RIGHT(Label, Count))
    1 : ReturnValue <- "****"
  ENDCASE
  RETURN RetVal
ENDFUNCTION
```

**(a)** Run-time errors can be generated in different ways. For example, a run-time error will be generated if a function is called with invalid parameters.

The pseudocode contains three statements that could generate a run-time error. Write the three statements and explain how each could generate a run-time error.

Statement 1: ...
Explanation: ...

Statement 2: ...
Explanation: ...

Statement 3: ...
Explanation: ...

**[3 marks]**

**(b)** One type of run-time error can cause a program to stop responding ('freezing'). Identify a particular type of programming construct that can generate this type of error and explain why it occurs.

Construct: ...
Explanation: ...

**[2 marks]**

**(c)** The function Process() contains a selection construct using a CASE structure. Write pseudocode using a single selection construct with the same functionality without using a CASE structure.

**[2 marks]**

### Question 7
A coffee shop runs a computerised loyalty card system. Customers are issued with a loyalty card with their name together with a unique customer ID. Loyalty points are added to their card each time they spend money at the shop.

The following information is stored for each customer: ID, name, home address, email address, mobile phone number, date of birth, number of points, date of last visit and amount of money spent at last visit.

A new module will generate a personalised email message to each loyalty card customer who has not visited the coffee shop in the last three months.

**(a)** Identify three items of customer information that will be used by the new module and justify your choices.

Item 1: ... Justification: ...
Item 2: ... Justification: ...
Item 3: ... Justification: ...

**[3 marks]**

**(b)** Identify the computational thinking skill that you needed to use to answer part (a).

**[1 mark]**

**(c)** It is decided to adopt a formal program development life cycle model for the development of the new module. The analysis of the new module is complete and the project moves on to the design stage. During this stage all the necessary algorithms and module designs will be defined.

State three other items that will be defined for the new module during the design stage.

1: ...
2: ...
3: ...

**[3 marks]**

**(d)** Part of the coffee shop program contains three program modules as follows:
- Module Init() has no parameters and returns a Boolean.
- Module Reset() takes a string as a parameter and returns an Integer.
- Module Check() repeatedly calls Init() followed by Reset().

Draw a structure chart to represent the relationship between the three modules, including all parameters and return values.

**[3 marks]**

---

## 2023 May/June (9618/22)

### Question 5
A programmer has produced the following pseudocode to output the square root of the numbers from 1 to 10.

```
10  DECLARE Num : REAL
11  Num <- 1.0
...
40  REPEAT
41    CALL DisplaySqrt(Num)
42    Num <- Num + 1.0
43  UNTIL Num > 10
...
50  PROCEDURE DisplaySqrt(BYREF ThisNum : REAL)
51    OUTPUT ThisNum
52    ThisNum <- SQRT(ThisNum)  // SQRT returns the square root
53    OUTPUT " has a square root of ", ThisNum
54  ENDPROCEDURE
```

The pseudocode is correctly converted into program code. Function SQRT() is a library function and contains no errors. The program code compiles without errors, but the program gives unexpected results. These are caused by a design error.

**(a)** Explain why the program gives unexpected results.

**[3 marks]**

**(b)** Explain why the compiler does not identify this error.

**[1 mark]**

**(c)** Describe how a typical Integrated Development Environment (IDE) could be used to identify this error.

**[3 marks]**

**(d)** The pseudocode is converted into program code as part of a larger program. During compilation, a complex statement generates an error. The programmer does not want to delete the complex statement but wants to change the statement so that it is ignored by the compiler.

State how this may be achieved.

**[1 mark]**

### Question 7
A computer system for a shop stores information about each customer. The items of information include name and address (both postal and email) together with payment details and order history. The system also stores the product categories they are interested in and how they would like to be contacted.

**(a)** The shop wants to add a program module that will generate emails to be sent to customers who may be interested in receiving details of new products.

**(i)** State three items of information that the new module would need. Justify your choice in each case.

Information: ... Justification: ...
Information: ... Justification: ...
Information: ... Justification: ...

**[3 marks]**

**(ii)** Identify two items of customer information that would not be required by the new module. Justify your choice in each case.

Information: ... Justification: ...
Information: ... Justification: ...

**[2 marks]**

**(b)** The program includes a module to validate a Personal Identification Number (PIN). This is used when customers pay for goods using a bank card.

A state-transition diagram has been produced for this module.

| Current state | Input | Output | Next state |
|--------------|-------|--------|------------|
| S1 | Input PIN | | S2 |
| S2 | Re-input PIN | Display error | S2 |
| S2 | Cancel | Re-prompt | S1 |
| S2 | Valid PIN | Enable payment | S4 |
| S2 | Too many tries | Block Account | S3 |

Complete the state-transition diagram to represent the information given in the table.

(Diagram shows: START -> S1, with Cancel | Re-prompt going S2 -> S1)

**[4 marks]**

### Question 8 (c)
The program contains modules SuppExists() and CheckSupplier(). These have been written but contain errors. These modules are called from several places in the main program and testing of the main program (integration testing) has had to stop.

Identify a method that can be used to continue testing the main program before the errors in these modules have been corrected and describe how this would work.

Method: ...
Description: ...

**[3 marks]**

---

## 2022 Oct/Nov (9618/22)

### Question 1 (b)
The algorithm in part (a) is part of a program that will be sold to the public. All the software errors that were identified during in-house testing have been corrected.

Identify and describe the additional test stage that may be carried out before the program is sold to the public.

Test stage: ...
Description: ...

**[4 marks]**

### Question 6 (b)
A program is written to allow a user to input a sequence of values to be checked using the function FindBaseNumber().

The user will input one value at a time. The variable used to store the user input has to be of type string because the user will input 'End' to end the program.

Valid input will be converted to an integer and passed to FindBaseNumber() and the return value will be output.

Complete the table by giving four invalid strings that may be used to test distinct aspects of the required validation. Give the reason for your choice in each case.

| Input | Reason for choice |
|-------|------------------|
| | |
| | |
| | |
| | |

**[4 marks]**

---

## 2021 May/June (9618/22)

### Question 7
A procedure FormatName():
- is called with a string containing words and spaces as its parameter. In this context, a word is any sequence of characters that does not contain a space character.
- creates a new formatted string from this string with the following requirements:
  1. Any leading spaces removed (spaces before the first word).
  2. Any trailing spaces removed (spaces after the last word).
  3. Any multiple spaces between words converted to a single space.
  4. All characters converted to lower case.

The procedure FormatName() has been written in a programming language and is to be tested using the black-box method.

**(a)** Give a test string that could be used to show that all four formatting requirements have been applied correctly.
Use the symbol ∇ to represent a space character.

**[3 marks]**

**(b)** The procedure FormatName() should assign a value to the global variable FString. There is a fault in the program, which means that the assignment does not always take place.

Explain two ways of exposing the fault.

**[2 marks]**
