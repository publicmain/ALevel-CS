# Chapter 10: Data Types & Structures - Paper 2 Past Questions

This file covers: arrays, records, stacks, queues, linked lists, abstract data types (ADTs).

---

## 2024 May/June (9618/22)

### Question 3
A factory needs a program to help manage its production of items. Data will be stored about each item.

The data for each item will be held in a record structure of type Component.

The programmer has started to define the fields that will be needed as shown in the table:

| Field | Example value | Comment |
|-------|--------------|---------|
| Item_Num | 123478 | a numeric value used as an array index |
| Reject | FALSE | TRUE if this item has been rejected |
| Stage | 'B' | a letter to indicate the stage of production |
| Limit_1 | 13.5 | any value in the range 0 to 100 inclusive |
| Limit_2 | 26.4 | any value in the range 0 to 100 inclusive |

**(a) (i)** Write pseudocode to declare the record structure for type Component.

**[4 marks]**

**(a) (ii)** A 1D array Item of 2000 elements will store the data for all items. Write pseudocode to declare the array Item.

**[2 marks]**

**(b)** State three benefits of using an array of records to store the data for all items.

**[3 marks]**

---

## 2024 Oct/Nov (9618/22)

### Question 2 (b)
The requirements have been changed. Conceal() will now be written as a procedure which will process 100 card numbers each time it is called.

The card numbers will be stored in a 2D array CardNumber. The original string will be stored in column one and the modified string in column two.

**(i)** Write pseudocode to declare the array.

**[2 marks]**

**(ii)** The new procedure Conceal() will write the modified string to the corresponding element in column two. The array CardNumber is passed as a parameter to the new procedure Conceal().

Identify how this parameter should be specified in the new procedure header.

**[1 mark]**

### Question 3
A program uses a stack to hold up to 60 numeric values.

The stack is implemented using two integer variables and a 1D array.

The array is declared in pseudocode as shown:
```
DECLARE ThisStack : ARRAY[1:60] OF REAL
```

The stack operates as follows:
- Global variable SP acts as a stack pointer that points to the next available stack location. The value of SP represents an array index.
- Global variable OnStack represents the number of values currently on the stack.
- The stack grows upwards from array element index 1.

**(a) (i)** Give the initial values that should be assigned to the two variables.

SP: ...
OnStack: ...

**[1 mark]**

**(a) (ii)** Explain why it is not necessary to initialise the array elements before the stack is used.

**[2 marks]**

**(b)** A function to add a value to ThisStack is expressed in pseudocode as shown.
The function will return a value to indicate whether the operation was successful or not.

Complete the pseudocode by filling in the gaps.

```
FUNCTION Push(ThisValue : REAL) RETURNS BOOLEAN
  DECLARE ReturnValue : BOOLEAN
  IF ................................................ THEN
    RETURN ................................................ // stack is already full
  ENDIF
  ................................................ <- ThisValue
  SP <- ................................................
  OnStack <- OnStack + 1
  RETURN TRUE
ENDFUNCTION
```

**[4 marks]**

### Question 8
A program is being developed to implement a game for up to six players. During the game, each player assembles a team of characters. At the start of the game there are 45 characters available.

Each character has four attributes:

| Attribute | Examples | Comment |
|-----------|----------|---------|
| Player | 0, 1, 3 | The player the character is assigned to. |
| Role | Builder, Teacher, Doctor | The job that the character will perform in the game. |
| Name | Bill, Lee, Farah, Mo | The name of the character. Several characters may perform the same role, but they will each have a unique name. |
| Level | 14, 23, 76 | The skill level of the character. An integer in the range 0 to 100 inclusive. |

The programmer has defined a record type to define each character:

```
TYPE CharacterType
  DECLARE Player : INTEGER
  DECLARE Role : STRING
  DECLARE Name : STRING
  DECLARE Level : INTEGER
ENDTYPE
```

The Player field indicates the player to which the character is assigned (1 to 6). The field value is 0 if the character is not assigned to any player.

Global array: `DECLARE Character : ARRAY[1:45] OF CharacterType`

**(a)** Module Assign():
- called with two parameters: an integer representing a player, a string representing a character role
- search the Character array for an unassigned character with the required role
- If found, assign the character to the given player and output a confirmation message, e.g.: "Bill the Builder has been assigned to player 3"
- If no unassigned character with the required role is found, output a suitable message.

Write pseudocode for module Assign().

**[7 marks]**

**(b)** Module Save():
- form a string from each record with fields separated by the character '^'
- write each string to a separate line of the new file named SaveFile.txt

Complete the pseudocode for module Save().

```
PROCEDURE Save()
  ...
ENDPROCEDURE
```

**[7 marks]**

**(c)** The program is changed and the record type definition is modified as follows:
```
TYPE CharacterType
  DECLARE Player : INTEGER
  DECLARE Role : STRING
  DECLARE Name : STRING
  DECLARE Level : INTEGER
  DECLARE Status : BOOLEAN
ENDTYPE
```

Describe how the additional Boolean field may be stored with the rest of the fields on one line of a text file.

**[2 marks]**

**(d)** The save operation is to be extended so that multiple files may be saved as the game progresses. This will allow the user to restore the game from any saved position. The filename must reflect the sequence in which the files are saved.

Describe a method that would allow multiple files to be saved and give an example of two consecutive filenames.

**[2 marks]**

---

## 2023 May/June (9618/22)

### Question 3
A program stores data in a text file. When data is read from the file, it is placed in a queue.

**(a)** The diagram below represents an Abstract Data Type (ADT) implementation of the queue. Each data item is stored in a separate location in the data structure. During initial design, the queue is limited to holding a maximum of 10 data items.

The operation of this queue may be summarised as follows:
- The Front of Queue Pointer points to the next data item to be removed.
- The End of Queue Pointer points to the last data item added.
- The queue is circular so that locations can be reused.

```
0:
1:
2:
3:
4:
5: Red          <- Front of Queue Pointer
6: Green
7: Blue
8: Pink         <- End of Queue Pointer
9:
```

**(i)** Describe how the data items Orange and Yellow are added to the queue shown in the diagram.

**[4 marks]**

**(ii)** The following diagram shows the state of the queue after several operations have been performed. All queue locations have been used at least once.

```
0: D4
1: D3           <- End of Queue Pointer
2: D27
3: D8
4: D33
5: D17          <- Front of Queue Pointer
6: D2
7: D1
8: D45
9: D60
```

State the number of data items in the queue.

**[1 mark]**

**(b)** The design of the queue is completed and the number of locations is increased.

A function AddToQueue() has been written. It takes a string as a parameter and adds this to the queue. The function will return TRUE if the string was added successfully.

A procedure FileToQueue() will add each line from the file to the queue. This procedure will end when all lines have been added or when the queue is full.

Describe the algorithm for procedure FileToQueue(). Do not use pseudocode in your answer.

**[5 marks]**

---

## 2023 Oct/Nov (9618/22)

### Question 1 (c)
The data that needs to be stored for each customer order in part (a) is not all of the same type.

Describe an effective way of storing this data for many customer orders while the program is running.

**[3 marks]**

### Question 3
The diagram represents a linked list Abstract Data Type (ADT).

- Ptr1 is the start pointer. Ptr2 is the free list pointer.
- Labels D40, D32, D11 and D100 represent the data items of nodes in the list.
- Labels F1, F2, F3 and F4 represent the data items of nodes in the free list.
- The symbol null represents a null pointer.

```
Ptr1 -> D40 -> D32 -> D11 -> D100 -> null
Ptr2 -> F1 -> F2 -> F3 -> F4 -> null
```

**(a)** The linked list is implemented using two variables and two 1D arrays as shown.

The pointer variables and the elements of the Pointer array store the indices (index numbers) of elements in the Data array.

Complete the diagram to show how the linked list as shown above may be represented using the variables and arrays.

| Variable | Value |
|----------|-------|
| Start_Pointer | |
| Free_List_Pointer | 5 |

| Index | Data array | Pointer array |
|-------|-----------|---------------|
| 1 | D32 | 2 |
| 2 | | 3 |
| 3 | | |
| 4 | D40 | |
| 5 | | |
| 6 | F2 | 7 |
| 7 | | |
| 8 | | |

**[5 marks]**

**(b)** The original linked list is to be modified. A new node D6 is inserted between nodes D32 and D11.

The algorithm required is expressed in four steps as shown. Complete the steps.

1. Assign the data item .................. to .................. .
2. Set the .................. of this node to point to .................. .
3. Set Ptr2 to point to .................. .
4. Set pointer of .................. to point to .................. .

**[4 marks]**

---

## 2022 Oct/Nov (9618/22)

### Question 3
A stack is used in a program to store string data which needs to be accessed in several modules.

**(a)** A stack is an example of an Abstract Data Type (ADT). Identify one other example of an ADT and describe its main features.

**[3 marks]**

**(b)** Explain how the stack can be implemented using an array.

**[5 marks]**

**(c)** A second stack is used in the program. The diagram below shows the initial state of this stack. Value X is at the top of the stack and was the last item added.

Upper-case letters are used to represent different data values.

Stack operations are performed in three groups as follows:

Group 1: PUSH D, PUSH E
Group 2: POP, POP, POP
Group 3: PUSH A, PUSH B, POP, PUSH C

Complete the diagram to show the state of the stack after each group of operations has been performed. Include the current stack pointer (SP) after each group.

| Memory location | Initial state | After Group 1 | After Group 2 | After Group 3 |
|----------------|--------------|---------------|---------------|---------------|
| 957 | | | | |
| 956 | | | | |
| 955 | | | | |
| 954 | | | | |
| 953 | X <- SP | | | |
| 952 | Y | | | |
| 951 | Z | | | |
| 950 | P | | | |

**[5 marks]**

### Question 7 (c)
Two 1D arrays were described at the beginning of the question. Both arrays contain 500 elements.
- Array ErrCode contains integer values that represent an error number in the range 1 to 800.
- Array ErrText contains string values that represent an error description.

The two arrays will be replaced by a single array. A user-defined data type (record structure) has been declared as follows:

```
TYPE ErrorRec
  DECLARE ErrCode : STRING
  DECLARE ErrText : STRING
ENDTYPE
```

**(i)** State the error in the record declaration.

**[1 mark]**

**(ii)** State two benefits of using the single array of the user-defined data type.

**[2 marks]**

**(iii)** Write the declaration for the single array in pseudocode.

**[1 mark]**

---

## 2021 May/June (9618/22)

### Question 3
The following diagram represents an Abstract Data Type (ADT).

```
        A          B
Dolphin -> Cat -> Fish -> Elk
```

**(a)** Identify this type of ADT.

**[1 mark]**

**(b)** Give the technical term for the item labelled A in the diagram.

**[1 mark]**

**(c)** Give the technical term for the item labelled B in the diagram.
Explain the meaning of the value given to this item.

Term: ...
Meaning: ...

**[2 marks]**

**(d)** Complete the diagram to show the ADT after the data has been sorted in alphabetical order.

```
Dolphin  Cat  Fish  Elk
```

**[2 marks]**
