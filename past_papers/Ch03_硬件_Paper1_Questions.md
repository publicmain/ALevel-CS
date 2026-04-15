# Chapter 3: Hardware - Paper 1 Past Questions

> Topics: Logic gates, logic circuits, truth tables, Boolean expressions, input/output devices, sensors, embedded systems

---

## 2024 May/June (9618/12)

### Question 1
(a) Describe the operation of each of the following logic gates:
- NAND
- NOR
- XOR
- OR
[4 marks]

(b) Draw a logic circuit for this logic expression:
X = NOT ((A AND B) OR (C AND D))
[2 marks]

### Question 2 (partial - hardware/input-output devices)
A computer game is being designed that users will be able to play using a virtual reality (VR) headset.

(a) Complete the description of the principal operation of a VR headset.
A headset can have one or two .................... that output the image to the user. The headset has speakers that output surround sound to give a realistic experience. The user's head movements are detected using a sensor. This sensor is a .................... . The data is transmitted to a microprocessor that analyses the data to identify the .................... of movement. Some headsets use .................... that record the user's eye movements for analysis.
[4 marks]

(b) The computer uses a buffer when transmitting data to the VR headset.
Explain how a buffer is used when data is transmitted between the computer and the VR headset.
[3 marks]

(c) The VR headset has Electrically Erasable Programmable Read Only Memory (EEPROM).
Explain the benefits of using EEPROM instead of other types of Read Only Memory (ROM) in the VR headset.
[3 marks]

---

## 2024 Oct/Nov (9618/12)

### Question 1
(a) Complete the truth table for the logic expression:
X = (A XOR B) NAND (A AND (B XOR C))

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

[2 marks]

(b) Draw the logic circuit for the logic expression:
W = P NAND ((Q OR NOT R) XOR (P XOR Q))
[2 marks]

### Question 2
Embedded systems are used in many electronic devices.

(a) Describe the drawbacks of embedded systems.
[3 marks]

(b) An embedded system has Dynamic RAM (DRAM).
Identify one benefit of using DRAM instead of Static RAM (SRAM) in an embedded system.
[1 mark]

(c) Give two differences between Erasable Programmable ROM (EPROM) and Electrically Erasable Programmable ROM (EEPROM).
[2 marks]

### Question 3(b) (partial - ports/monitors)
The student needs to connect the computer to a monitor that has a screen resolution of 2560 x 1600 pixels. The monitor also has built-in speakers. The computer has a Video Graphics Array (VGA) port and a High Definition Multimedia Interface (HDMI) port.

Explain the benefits of connecting the monitor to the computer using the HDMI port instead of the VGA port.
[4 marks]

### Question 9
A road bridge has a weight limit and a height limit for vehicles. For example, a vehicle must weigh less than 10,000 kg and must have a height of less than 3 m. The bridge has a warning system.

(a) The bridge warning system uses sensors to detect if a vehicle exceeds the limits.
Complete the table by identifying two different sensors that could be used by the system and describe how each sensor is used by the system.
[4 marks]

(b) Explain whether the bridge warning system is an example of a monitoring system or of a control system.
[2 marks]

---

## 2023 May/June (9618/12)

### Question 5(c) (partial - ports)
Peripherals are connected to the laptop using ports.

(i) A printer is connected to a Universal Serial Bus (USB) port.
Describe how data is transmitted through a USB port.
[1 mark]

(ii) A monitor is connected to the laptop using a different type of port.
Identify one other type of port that can be used to connect the monitor.
[1 mark]

### Question 6
(a) Draw the logic circuit for this logic expression:
Z = (R XOR S) AND (NOT T NOR P)
[2 marks]

(b) Complete the truth table for this logic expression:
Z = (NOT P OR Q) XOR (R NOR Q)

| P | Q | R | Z |
|---|---|---|---|
| 0 | 0 | 0 |   |
| 0 | 0 | 1 |   |
| 0 | 1 | 0 |   |
| 0 | 1 | 1 |   |
| 1 | 0 | 0 |   |
| 1 | 0 | 1 |   |
| 1 | 1 | 0 |   |
| 1 | 1 | 1 |   |

[2 marks]

---

## 2023 Oct/Nov (9618/12)

### Question 1
A factory makes chocolate bars. The factory uses a conveyor belt that moves the products from one stage of production to the next stage.

(a) An automated system counts the number of chocolate bars made at the end of production. The system includes a sensor positioned above the conveyor belt.
Identify one appropriate type of sensor that can be used.
[1 mark]

(b) A second automated system removes chocolate bars with an incorrect weight from the production line.
Describe the role of an actuator in this second system.
[2 marks]

(c) The factory has many different machines with embedded systems.

(i) Identify two features of embedded systems.
[2 marks]

(ii) Identify one drawback of embedded systems.
[1 mark]

### Question 4
(a) Write the Boolean expression that corresponds to the following logic circuit.
[Logic circuit with inputs A, B, C and output X shown]
[3 marks]

(b) Complete the truth table for the logic expression:
X = A XOR (B AND (A NAND B) AND NOT C)

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

[2 marks]

---

## 2022 Oct/Nov (9618/12)

### Question 3
(a) A greenhouse has an automatic window.
The window (X) operates according to the following criteria:

| Parameter | Description | Binary value | Condition |
|---|---|---|---|
| T | Temperature | 1 / 0 | Too high / Acceptable |
| W | Wind speed | 1 / 0 | Too high / Acceptable |
| R | Rain | 1 / 0 | Detected / Not detected |
| M | Manual override | 1 / 0 | On / Off |

The window opens (X = 1) if:
- the temperature is too high and the wind speed is acceptable
- and
- rain is not detected, or the manual override is off.

Draw a logic circuit to represent the operation of the window.
[3 marks]

(b) Complete the truth table for the logic expression:
X = NOT (A OR B OR C) AND (B NOR C)

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

[2 marks]

(c) Embedded systems contain Read Only Memory (ROM) and Random Access Memory (RAM).
Explain the reasons why ROM is used in an embedded system.
[2 marks]

---

## 2021 May/June (9618/12)

### Question 3
A logic expression is given:
S = (A AND B AND C) OR (B XOR C)

(a) Draw the logic circuit for the given expression.
[4 marks]

(b) Complete the truth table for the logic expression:
S = (A AND B AND C) OR (B XOR C)

| A | B | C | S |
|---|---|---|---|
| 0 | 0 | 0 |   |
| 0 | 0 | 1 |   |
| 0 | 1 | 0 |   |
| 0 | 1 | 1 |   |
| 1 | 0 | 0 |   |
| 1 | 0 | 1 |   |
| 1 | 1 | 0 |   |
| 1 | 1 | 1 |   |

[2 marks]
