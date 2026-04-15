# Chapter 11: Programming - Paper 2 Past Questions

This file covers: programming concepts, string handling, file handling, pseudocode writing, functions/procedures, parameter passing.

---

## 2024 May/June (9618/22)

### Question 1
**(a)** The following table contains pseudocode examples. Each example may contain statements that relate to one or more of the following: selection, iteration (repetition), input/output.

Complete the table by placing one or more ticks in each row.

| Pseudocode example | Selection | Iteration | Input/Output |
|-------------------|-----------|-----------|--------------|
| `FOR Index <- 1 TO 10` / `Data[Index] <- 0` / `NEXT Index` | | | |
| `WRITEFILE ThisFile, "****"` | | | |
| `UNTIL Level > 25` | | | |
| `IF Mark > 74 THEN` / `READFILE OldFile, Data` / `ENDIF` | | | |

**[4 marks]**

**(b)** Program variables have data types as follows:

| Variable | Data type |
|----------|-----------|
| MyChar | CHAR |
| MyString | STRING |
| MyInt | INTEGER |

Complete the table by filling in each gap with a function (from the insert) so that each expression is valid.

| Expression |
|------------|
| MyInt <- ..................(3.1415926) |
| MyChar <- ..................("Elwood", 3, 1) |
| MyString <- ..................(..................(27.509)) |
| MyInt <- ..................(..................("ABC123", 3)) |

**[4 marks]**

**(c)** The variables given in part (b) are chosen during the design stage of the program development life cycle.

The choices are to be documented to simplify program maintenance.

State a suitable way of documenting the variables and give one piece of information that should be recorded, in addition to the data type.

**[2 marks]**

### Question 4
A triangle has sides of length A, B and C. In this example, A is the length of the longest side.

This triangle is said to be right-angled if the following equation is true:
A x A = (B x B) + (C x C)

A procedure IsRA() will be written to check whether three lengths represent a right-angled triangle. The lengths will be input in any sequence.

The procedure will:
- prompt and input three integer values representing the three lengths
- test whether the three lengths correspond to the sides of a right-angled triangle
- output a suitable message.

The length of the longest side may not be the first value input.

Write pseudocode for the procedure IsRA().

**[5 marks]**

### Question 5
A program is being designed in pseudocode. The program contains a global 1D array Data of type string containing 200 elements. The first element has the index value 1.

A procedure is written to initialise the values in the array:

```
PROCEDURE Process(Label : STRING)
  DECLARE Index : INTEGER
  Index <- 0
  INPUT Data[Index]
  WHILE Index < 200
    Index <- Index + 1
    CASE OF (Index MOD 2)
      0 : Data[Index] <- TO_UPPER(Label)
      1 : Data[Index] <- TO_LOWER(Label)
      OTHERWISE : OUTPUT "Alarm 1201"
    ENDCASE
  NEXT Index
  OUTPUT "Completed " & Index & " times"
ENDPROCEDURE
```

**(a) (i)** The pseudocode contains two syntax errors and one other error. Identify the errors.

Syntax error 1: ...
Syntax error 2: ...
Other error: ...

**[3 marks]**

**(a) (ii)** The procedure contains a statement that is not needed. Identify the pseudocode statement and explain why it is not needed.

Statement: ...
Explanation: ...

**[2 marks]**

### Question 6
A music player stores music in a digital form and has a display which shows the track being played.

**(a)** Up to 16 characters can be displayed. Track titles longer than 16 characters will need to be trimmed as follows:
- Words must be removed from the end of the track title until the resulting title is less than 14 characters.
- When a word is removed, the space in front of that word is also removed.
- Three dots are added to the end of the last word displayed when one or more words have been removed.

| Original title | Display string |
|---------------|----------------|
| Bat out of Hull | `Bat out of Hull` |
| Bohemian Symphony | `Bohemian...` |
| Paperbook Writer | `Paperbook Writer` |
| Chris Sings the Blues | `Chris Sings...` |
| Green Home Alabama | `Green Home...` |

A function Trim() will:
- take a string representing the original title
- return the string to be displayed.

Assume:
- Words in the original title are separated by a single space character.
- There are no spaces before the first word or after the last word of the original title.
- The first word of the original title is less than 14 characters.

Write pseudocode for the function Trim().

**[7 marks]**

**(b)** Music is stored as a sequence of digital samples. Each digital sample is a denary value in the range 0 to 99999999 (8 digits).

The samples are to be stored in a text file. Each sample is converted to a numeric string and 32 samples are concatenated (joined) to form a single line of the text file. Each numeric string is 8 characters in length; leading '0' characters are added as required.

Example:
| Sample | Denary value | String |
|--------|-------------|--------|
| 1 | 456 | "00000456" |
| 2 | 48 | "00000048" |
| 3 | 37652 | "00037652" |
| 32 | 673 | "00000673" |

Stored as: "000004560000004800037652...00000673"

**(i)** Identify one drawback of adding leading '0' characters to each numeric string.

**[1 mark]**

**(ii)** Suggest an alternative method of storing the samples which does not involve adding leading '0' characters but which would still allow each individual sample to be extracted.

**[1 mark]**

**(iii)** State one drawback of the alternative method given in part (b)(ii).

**[1 mark]**

### Question 8
A teacher is designing a program to process pseudocode projects written by her students. Each student project is stored in a text file. The process is split into a number of stages.

| File name | Comment |
|-----------|---------|
| MichaelAday_src.txt | Student project file produced by student Michael Aday |
| MichaelAday_S1.txt | File produced by stage 1 |
| MichaelAday_S2.txt | File produced by stage 2 |

**(a)** Suggest a reason why the teacher's program has been split into a number of stages and give the benefit of producing a different file from each stage.

**[2 marks]**

**(b)** Module DeleteSpaces():
- called with a parameter of type string representing a line of pseudocode from a student's project file
- returns the line after removing any leading space characters

Before: "    IF X2 > 13 THEN"
After: "IF X2 > 13 THEN"

Complete the pseudocode for module DeleteSpaces().

```
FUNCTION DeleteSpaces(Line : STRING) RETURNS STRING
  ...
ENDFUNCTION
```

**[6 marks]**

**(c)** Two modules are defined:

Module DeleteComment():
- called with a parameter of type string representing a line of pseudocode
- returns the line after removing any comment

Module Stage_2():
- called with two parameters: a string representing an input file name, a string representing an output file name
- copies each line from the input file to the existing output file having first removed all leading spaces and comments from that line
- does not write blank lines to the output file
- outputs a final message giving the number of blank lines removed

Write pseudocode for module Stage_2(). Modules DeleteComment() and DeleteSpaces() must be used in your solution.

**[8 marks]**

---

## 2024 Oct/Nov (9618/22)

### Question 1 (d)
The new module referred to in part (c) introduces three new variables. Complete the following table by giving the appropriate data type for each.

| Variable name | Used to store | Data type |
|--------------|--------------|-----------|
| Name | A customer name. | |
| Index | An array index. | |
| Result | The result of the division of any two non-zero numbers. | |

**[3 marks]**

### Question 2
A program is being developed to process bank card information. When a card number is displayed, all the characters except the last four are replaced with the asterisk character '*'.

Card numbers are stored as strings. The strings are between 10 and 20 characters in length.

The function Conceal() will take a string representing a card number and return a modified string.

| Original string | Modified string |
|----------------|----------------|
| "1234567890" | "******7890" |
| "1234567897652" | "*********7652" |
| "1234567890123456" | "************3456" |

**(a)** The function Conceal() will:
- take a numeric string as a parameter representing the card number
- return a string in which the asterisk character replaces all except the last four characters of the card number parameter.

Write pseudocode for the function Conceal().

**[6 marks]**

### Question 4
*(See Ch09 for the full Timer() question -- this question is primarily about algorithm design using the Tick variable)*

### Question 6
A shop sells sandwiches and snacks. The owner chooses a 'daily special' sandwich which is displayed on a board outside the shop.

The program designer decides to store the possible sandwich fillings in a 1D array of type string:
`DECLARE Filling : ARRAY [1:35] OF STRING`

A second 1D array stores the possible bread used:
`DECLARE Bread : ARRAY [1:10] OF STRING`

Both arrays may contain unused elements (empty strings).

A procedure Special() will output a message giving the 'daily special' sandwich made from two randomly selected different fillings and one randomly selected bread. Unused array elements must not be used.

Example output: "The daily special is Cheese and Onion on Brown bread."

**(a)** Complete the pseudocode for the procedure Special(). Assume both arrays are global.

```
PROCEDURE Special()
  ...
ENDPROCEDURE
```

**[7 marks]**

**(b)** The owner decides that some combinations of fillings do not go well together. For example, anchovies and peanut butter.

Describe how the design could be changed to prevent certain combinations being selected.

**[2 marks]**

---

## 2023 May/June (9618/22)

### Question 1
A program calculates the postal cost based on the weight of the item and its destination.

For example, the postal cost of $3.75 is used in the following lines of pseudocode:

```
IF Weight < 250 AND ValidAddress = TRUE THEN
  ItemPostalCost <- 3.75  // set postal cost for item to $3.75
  ItemStatus <- "Valid"   // item can be sent
ENDIF
```

**(a) (i)** Identify a more appropriate way of representing the postal costs.

**[1 mark]**

**(a) (ii)** Describe the advantages of your answer to part (a)(i) with reference to this program.

**[3 marks]**

**(b)** The lines of pseudocode contain features that make them easier to understand. State three of these features.

**[3 marks]**

**(c)** Give the appropriate data types for the following variables:
- ValidAddress: ...
- ItemPostalCost: ...
- ItemStatus: ...

**[3 marks]**

### Question 4
A function GetNum() will:
1. take two parameters: a string and a character
2. count the number of times that the character occurs in the string
3. return the count.

Any comparison between characters needs to be case sensitive. For example, character 'a' and character 'A' are not identical.

Write pseudocode for function GetNum().

**[6 marks]**

### Question 6
A procedure Square() will take an integer value in the range 1 to 9 as a parameter and output a number square.

The boundary of a number square is made up of the character representing the parameter value. The inside of the number square is made up of the asterisk character (*).

| Parameter value | 1 | 2 | 3 | 4 | 9 |
|----------------|---|---|---|---|---|
| Output | 1 | 22 / 22 | 333 / 3*3 / 333 | 4444 / 4**4 / 4**4 / 4444 | 999999999 / 9*******9 / ... / 999999999 |

The pseudocode command OUTPUT starts each output on a new line.

Write pseudocode for procedure Square(). Parameter validation is not required.

**[6 marks]**

### Question 8
A computer shop assembles computers using items bought from several suppliers. A text file Stock.txt contains information about each item.

Information for each item is stored as a single line: `<ItemNum><SupplierCode><Description>`

| Format | Comment |
|--------|---------|
| ItemNum - 4 numeric characters | unique number for each item in the range "0001" to "5999" inclusive |
| SupplierCode - 3 alphabetic characters | to identify the supplier of the item |
| Description - a string | a minimum of 12 characters |

The file is organised in ascending order of ItemNum.

Module OnlyAlpha() (already written): called with a parameter of type string, returns TRUE if the string contains only alphabetic characters.

Module CheckInfo(): called with a parameter of type string representing a line of item information, checks validity, returns TRUE if valid.

**(a)** Write pseudocode for module CheckInfo(). Module OnlyAlpha() should be used as part of your solution.

**[7 marks]**

**(b)** Module AddItem():
- called with a parameter of type string representing valid information for a new item not currently in Stock.txt
- creates a new file NewStock.txt from the contents of Stock.txt and adds the new item information at the appropriate place in NewStock.txt

Write pseudocode for module AddItem().

**[7 marks]**

---

## 2023 Oct/Nov (9618/22)

### Question 1
A shop sells car accessories. A customer order is created if an item cannot be supplied from current stock.

**(a)** The following identifier table shows some of the data that will be stored for each order. Complete the identifier table by adding meaningful variable names and appropriate data types.

| Example value | Explanation | Variable name | Data type |
|--------------|-------------|---------------|-----------|
| "Mr Khan" | The name of the customer | | |
| 3 | The number of items in the order | | |
| TRUE | To indicate whether this is a new customer | | |
| 15.75 | The deposit paid by the customer | | |

**[4 marks]**

**(b)** Other variables in the program have example values as shown:

| Variable | Example value |
|----------|--------------|
| Total | 124.00 |
| DepRate | 2.00 |
| Description | "AB12345:Cleaning Brush (small)" |

Complete the table by evaluating each expression using the example values.

| Expression | Evaluates to |
|-----------|-------------|
| (Total * DepRate) + 1.5 | |
| RIGHT(Description, 7) | |
| (LENGTH(Description) - 8) > 16 | |
| NUM_TO_STR(INT(DepRate * 10)) & '%' | |

**[4 marks]**

### Question 4
A procedure Count() will:
1. input a value (all values will be positive integers)
2. count the number of odd values and count the number of even values
3. repeat from step 1 until the value input is 99
4. output the two count values, with a suitable message.

The value 99 must not be counted.

**(a)** Write pseudocode for the procedure Count().

**[6 marks]**

**(b)** The procedure Count() is to be tested.

Typical test data would consist of odd and even values, for example:
23, 5, 64, 100, 2002, 1, 8, 900, 99

Give three test data sequences that may be used to test different aspects of the procedure. Do not include invalid data.

Sequence 1: Test data / Purpose of test
Sequence 2: Test data / Purpose of test
Sequence 3: Test data / Purpose of test

**[3 marks]**

### Question 6
**(a)** A procedure CreateFiles() will take two parameters:
- a string representing a file name
- an integer representing the number of files to be created.

The procedure will create the number of text files specified. Each file is given a different name by concatenating the file name with a suffix based on the file number (always three characters).

For example, `CreateFiles("TestData", 3)` would create TestData.001, TestData.002, TestData.003.

Each file will contain a single line. For example, file TestData.002 would contain: "This is File TestData.002"

Write pseudocode for CreateFiles(). Assume both parameters are valid and that the integer value is between 1 and 999, inclusive.

**[6 marks]**

**(b)** A module CheckFiles() will count the number of files produced by CreateFiles().

**(i)** Identify the type of module that should be used for CheckFiles().

**[1 mark]**

**(ii)** Write the module header for CheckFiles().

**[1 mark]**

**(iii)** State the file mode that should be used in CheckFiles().

**[1 mark]**

### Question 8
A class of students are developing a program to send data between computers. Many computers are connected together to form a wired network. Serial ports are used to connect one computer to another.

Each computer:
- is assigned a unique three-digit ID
- has three ports, each identified by an integer value
- is connected to between one and three other computers.

Data is sent as individual message strings: `<DestinationID><Data>`

RouteTable is a global 2D array of integers:
`DECLARE RouteTable : ARRAY[1:6,1:3] OF INTEGER`

Example contents:
| | Column 1 | Column 2 | Column 3 |
|---|----------|----------|----------|
| Row 1 | 100 | 199 | 1 |
| Row 2 | 200 | 259 | 2 |
| Row 3 | -1 | undefined | undefined |
| Row 4 | 260 | 399 | 2 |
| Row 5 | 400 | 599 | 3 |
| Row 6 | 600 | 999 | 1 |

**(a)** Module GetPort():
- takes a DestinationID as a parameter of type string
- searches for the range corresponding to the DestinationID in the array
- returns the port number, or returns -1 if no corresponding range is found

Write pseudocode for module GetPort(). Assume DestinationID contains a valid three-digit string.

**[7 marks]**

**(b)** Additional modules:

Module StackMsg() (already written):
- takes two parameters: a string (message) and an integer (stack number)
- adds the message to the required stack
- returns TRUE if added, FALSE otherwise

Module ProcessMsg():
- takes a message as a parameter
- ignores any message with a zero-length data field
- extracts the DestinationID from the message
- checks whether the DestinationID is this computer or whether the message is to be forwarded
- uses StackMsg() to add the message to the appropriate stack
- outputs an error if the message could not be added to the stack

Write pseudocode for module ProcessMsg(). Module StackMsg() must be used.

**[7 marks]**

**(c)** The program contains a module GetFile() which receives text files sent from another computer.

**(i)** Lines from the file are sent one at a time and added to stack 1. Module GetFile() removes messages from stack 1 and writes the data to a text file.

Describe the circumstances and explain the problem.

**[3 marks]**

**(ii)** Suggest a more appropriate Abstract Data Type that could be used to store the messages that would not have the same problem.

**[1 mark]**

---

## 2022 Oct/Nov (9618/22)

### Question 1
**(a)** A programmer is developing an algorithm to solve a problem. Part of the algorithm would be appropriate to implement as a subroutine (a procedure or a function).

**(i)** State two reasons why the programmer may decide to use a subroutine.

**[2 marks]**

**(ii)** A procedure header is shown in pseudocode:
`PROCEDURE MyProc(Count : INTEGER, Message : STRING)`

Give the correct term for the identifiers Count and Message and explain their use.

Term: ...
Use: ...

**[2 marks]**

**(c)** Part of an identifier table is shown:

| Variable | Type | Example value |
|----------|------|--------------|
| FlagDay | DATE | 23/04/2004 |
| CharList | STRING | "ABCDEF" |
| Count | INTEGER | 29 |

Complete the table by evaluating each expression using the example values.

| Expression | Evaluation |
|-----------|------------|
| MID(CharList, MONTH(FlagDay), 1) | |
| INT(Count / LENGTH(CharList)) | |
| (Count >= 29) AND (DAY(FlagDay) > 23) | |

**[3 marks]**

### Question 5
Examine the following pseudocode.

```
IF A = TRUE THEN
  IF B = TRUE THEN
    IF C = TRUE THEN
      CALL Sub1()
    ELSE
      CALL Sub2()
    ENDIF
  ENDIF
ELSE
  IF B = TRUE THEN
    IF C = TRUE THEN
      CALL Sub4()
    ELSE
      CALL Sub3()
    ENDIF
  ELSE
    IF C = FALSE THEN
      CALL Sub3()
    ELSE
      CALL Sub4()
    ENDIF
  ENDIF
ENDIF
```

A programmer wants to re-write the pseudocode as four separate IF...THEN...ENDIF statements, each containing a single CALL statement. This involves writing a single, simplified logic expression as the condition in each statement.

Write the amended pseudocode.

1: ...
2: ...
3: ...
4: ...

**[4 marks]**

### Question 6
**(a)** The factorial of an integer number is the product of all the integers from that number down to 1.

In general, the factorial of n is n x (n-1) x ... x 2 x 1

For example, the factorial of 5 is 5 x 4 x 3 x 2 x 1 = 120 (BaseNumber)

A function FindBaseNumber() will:
- be called with a positive, non-zero integer value as a parameter
- return the BaseNumber if the parameter value is the factorial of the BaseNumber
- return -1 if the parameter value is not a factorial.

| Parameter value | Value returned |
|----------------|---------------|
| 120 | 5 |
| 12 | -1 |
| 6 | 3 |
| 1 | 1 |

Write pseudocode for the function FindBaseNumber().

**[7 marks]**

**(b)** A program is written to allow a user to input a sequence of values to be checked using FindBaseNumber().

The user will input one value at a time. The variable used to store the user input has to be of type string because the user will input 'End' to end the program.

Complete the table by giving four invalid strings that may be used to test distinct aspects of the required validation. Give the reason for your choice in each case.

| Input | Reason for choice |
|-------|------------------|
| | |
| | |
| | |
| | |

**[4 marks]**

### Question 7 (a)
A teacher is designing a program to perform simple syntax checks on programs written by students.

Two global 1D arrays are used to store the syntax error data (500 elements each):
- Array ErrCode contains integer values (error numbers 1 to 800)
- Array ErrText contains string values (error descriptions)

Values in ErrCode are stored in ascending order. Unused elements have value 999.

Module OutputError():
- takes two integer parameters: a line number and an error number
- searches for the error number in ErrCode
- if found, outputs the corresponding error description and line number, e.g.: "Bracket mismatch on line 34"
- if not found, outputs the line number and a warning, e.g.: "Unknown error on line 34"

Write efficient pseudocode for module OutputError().

**[6 marks]**

### Question 7 (b)
Module SortArrays(): sorts the arrays into ascending order of ErrCode.

Write an efficient bubble sort algorithm in pseudocode for module SortArrays().

**[8 marks]**

---

## 2021 May/June (9618/22)

### Question 1
**(a) (i)** Complete the following table by giving the appropriate data type in each case.

| Variable | Example data value | Data type |
|----------|-------------------|-----------|
| Name | "Catherine" | |
| Index | 100 | |
| Modified | FALSE | |
| Holiday | 25/12/2020 | |

**[4 marks]**

**(a) (ii)** Evaluate each expression in the following table by using the initial data values shown in part (a)(i).

| Expression | Evaluates to |
|-----------|-------------|
| Modified OR Index > 100 | |
| LENGTH("Student: " & Name) | |
| INT(Index + 2.9) | |
| MID(Name, 1, 3) | |

**[4 marks]**

**(b)** Each pseudocode statement in the following table contains an example of selection, assignment or iteration.

Put one tick in the appropriate column for each statement.

| Statement | Selection | Assignment | Iteration |
|-----------|-----------|------------|-----------|
| Index <- Index + 1 | | | |
| IF Modified = TRUE THEN | | | |
| ENDWHILE | | | |

**[3 marks]**

### Question 5
**(a)** A student wants to write a program to:
- declare a 1D array RNum of 100 elements of type INTEGER
- assign each element a random value in the range 1 to 200 inclusive
- count and output how many numbers generated were between 66 and 173 inclusive.

**(i)** Write pseudocode to represent the algorithm.

**[6 marks]**

**(ii)** The student decides to modify the algorithm so that each element of the array will contain a unique value. Describe the changes that the student needs to make to the algorithm.

**[3 marks]**

**(b)** The following is a pseudocode function.

```
01 FUNCTION StringClean(InString : STRING) RETURNS STRING
02
03   DECLARE NextChar : CHAR
04   DECLARE OutString : STRING
05   DECLARE Counter : INTEGER
06
07   OutString <- ""
08
09   FOR Counter <- 1 TO LENGTH(InString)
10     NextChar <- MID(InString, Counter, 1)
11     NextChar <- LCASE(NextChar)
12     IF NOT((NextChar < 'a') OR (NextChar > 'z')) THEN
13       OutString <- OutString & NextChar
14     ENDIF
15   NEXT Counter
16
17   RETURN OutString
18
19 ENDFUNCTION
```

**(i)** Examine the pseudocode and complete the following table.

| | Answer |
|---|--------|
| Give a line number containing an example of an initialisation statement. | |
| Give a line number containing the start of a repeating block of code. | |
| Give a line number containing a logic operation. | |
| Give the number of parameters to the function MID(). | |

**[4 marks]**

**(ii)** Write a simplified version of the statement in line 12.

**[2 marks]**

### Question 6
A procedure CountVowels() will:
- be called with a string containing alphanumeric characters as its parameter
- count and output the number of occurrences of each vowel (a, e, i, o, u) in the string
- count and output the number of occurrences of the other alphabetic characters (as a single total).

The string may contain both upper and lower case characters.

Each count value will be stored in a unique element of a global 1D array CharCount of type INTEGER. The array will contain six elements.

Write pseudocode for the procedure CountVowels().

**[8 marks]**

### Question 8
A program is needed to take a string containing a full name and to produce a new string of initials.

Some words in the full name will be ignored. For example, "the", "and", "of", "for" and "to" may all be ignored. Each letter of the new string must be upper case.

| Full name | Initials |
|-----------|----------|
| Integrated Development Environment | IDE |
| The American Standard Code for Information Interchange | ASCII |

The programmer has decided to use:
- a ten element 1D array IgnoreList of type STRING to store the ignored words
- a string FNString to store the full name string.

Modules defined:

| Module | Description |
|--------|------------|
| GetStart() | Called with an INTEGER parameter representing the number of a word in FNString. Returns the character start position of that word in FNString or returns -1 if that word does not exist. Example: GetStart(3) applied to "hot and cold" returns 9 |
| GetWord() | Called with the position of the first character of a word in FNString as its parameter. Returns the word from FNString. Example: if FNString contains "hot and cold", GetWord(9) returns "cold" |
| IgnoreWord() | Called with a STRING parameter representing a word. Searches for the word in the array IgnoreList. Returns TRUE if found, otherwise returns FALSE |
| GetInitials() | Processes the sequence of words in the full name one word at a time. Calls GetStart(), GetWord() and IgnoreWord() to process each word to form the new string. Outputs the new string. |

**(a)** Write pseudocode for the module IgnoreWord().

**[5 marks]**

**(b)** Write pseudocode for the module GetInitials().

**[8 marks]**
