# Chapter 3: Hardware - 课后作业 Homework

> 姓名：__________ 日期：__________ 总分：__/56

---

## Question 1 — Logic Gates 逻辑门 [6 marks]

(a) Complete the truth tables for the following logic gates:

**AND gate (与门)**

| Input A | Input B | Output |
|---------|---------|--------|
| 0       | 0       |        |
| 0       | 1       |        |
| 1       | 0       |        |
| 1       | 1       |        |

[1 mark]

**XOR gate (异或门)**

| Input A | Input B | Output |
|---------|---------|--------|
| 0       | 0       |        |
| 0       | 1       |        |
| 1       | 0       |        |
| 1       | 1       |        |

[1 mark]

(b) Draw the standard symbol for each of the following logic gates:

(i) NAND gate
[1 mark]

(ii) NOR gate
[1 mark]

(c) State the Boolean expression that represents:

(i) an AND gate with inputs A and B
[1 mark]

(ii) a NAND gate with inputs P and Q
[1 mark]

---

## Question 2 — Logic Circuits 逻辑电路 [8 marks]

(a) The following Boolean expression represents a logic circuit:

**X = (A AND B) OR (NOT C)**

(i) Draw a logic circuit for this expression using standard logic gate symbols.
[3 marks]

(ii) Complete the truth table for this circuit.

| A | B | C | X |
|---|---|---|---|
| 0 | 0 | 0 |   |
| 0 | 0 | 1 |   |
| 0 | 1 | 0 |   |
| 0 | 1 | 1 |   |
| 1 | 0 | 0 |   |
| 1 | 0 | 1 |   |
| 1 | 1 | 0 |   |
| 1 | 1 | 1 |   |

[3 marks]

(b) Write the Boolean expression for a circuit that outputs 1 only when:
- Input A is 1 AND Input B is 0, OR
- Input C is 1

[2 marks]

---

## Question 3 — Logic Problem 逻辑应用题 [6 marks]

A security system for a room has the following rules:
- The alarm (output Z) should sound (Z = 1) when:
  - The door sensor (D) detects the door is open AND the system is armed (A), OR
  - The motion sensor (M) detects movement AND the system is armed (A)

(a) Write the Boolean expression for output Z in terms of inputs D, A, and M.
[2 marks]

(b) Draw the logic circuit for this security system.
[2 marks]

(c) State the output Z when D = 1, A = 1, M = 0. Show your working.
[2 marks]

---

## Question 4 — Flip-Flops 触发器 [5 marks]

(a) State the purpose of a flip-flop circuit.
[1 mark]

(b) An SR flip-flop has two inputs: S (Set) and R (Reset), and two outputs: Q and NOT Q.

Complete the following table to show the behaviour of an SR flip-flop. Use Q(prev) to indicate "previous state of Q".

| S | R | Q          |
|---|---|------------|
| 0 | 0 |            |
| 0 | 1 |            |
| 1 | 0 |            |
| 1 | 1 |            |

[2 marks]

(c) Explain why the input combination S = 1, R = 1 is considered invalid for an SR flip-flop.
[2 marks]

---

## Question 5 — Input and Output Devices 输入与输出设备 [6 marks]

(a) For each of the following scenarios, state a suitable **input device** and explain why it is appropriate:

(i) A supermarket checkout system needs to read product information.
[2 marks]

(ii) A graphic designer needs to create detailed digital illustrations.
[2 marks]

(b) A museum wants to set up an interactive information kiosk for visitors.
State **one** suitable output device and explain your choice.
[2 marks]

---

## Question 6 — Sensors 传感器 [6 marks]

(a) Name a suitable sensor for each of the following applications and explain how it would be used:

(i) An automatic greenhouse watering system
[2 marks]

(ii) A street light that turns on when it gets dark
[2 marks]

(b) Explain why an Analogue-to-Digital Converter (ADC) is needed when connecting a sensor to a computer system.
[2 marks]

---

## Question 7 — Embedded Systems 嵌入式系统 [5 marks]

(a) Define the term **embedded system**.
[2 marks]

(b) Give **two** examples of devices that contain an embedded system.
For each example, describe the function of the embedded system within the device.
[2 marks]

(c) State **one** characteristic that distinguishes an embedded system from a general-purpose computer.
[1 mark]

---

## Question 8 — RFID and GPS 射频识别与全球定位系统 [8 marks]

(a) Describe how an **RFID** system works. Your answer should refer to the components involved and how they communicate.
[3 marks]

(b) Give **two** practical applications of RFID technology.
[2 marks]

(c) Describe how a **GPS** receiver determines its position.
[3 marks]

---

## Question 9 — Mixed Hardware Concepts 综合题 [6 marks]

A modern car contains many computer-based systems.

(a) Identify **two** sensors that would be used in a car's anti-lock braking system (ABS) and describe the role of each sensor.
[2 marks]

(b) Explain why the car's ABS uses an embedded system rather than a general-purpose computer.
[2 marks]

(c) The car has a keyless entry system that uses RFID technology.
Describe how the driver can unlock the car using this system.
[2 marks]

---

---

*Cambridge International AS Level Computer Science 9618 - Chapter 3 Homework*
