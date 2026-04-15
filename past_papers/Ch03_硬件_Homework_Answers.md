# Chapter 3: Hardware - Homework Answers

> 总分：56

---

## Question 1 — Logic Gates 逻辑门 [6 marks]

**(a)** Truth tables. [2 marks]

**AND gate (与门)** ✓

| Input A | Input B | Output |
|---------|---------|--------|
| 0       | 0       | 0      |
| 0       | 1       | 0      |
| 1       | 0       | 0      |
| 1       | 1       | 1      |

**XOR gate (异或门)** ✓

| Input A | Input B | Output |
|---------|---------|--------|
| 0       | 0       | 0      |
| 0       | 1       | 1      |
| 1       | 0       | 1      |
| 1       | 1       | 0      |

---

**(b)** Logic gate symbols. [2 marks]

**(i) NAND gate** ✓

```
  A ───\
        |D○───── Output
  B ───/
```

(Standard AND gate shape with a small circle/bubble at the output to indicate negation.)

**(ii) NOR gate** ✓

```
  A ───\
        )○───── Output
  B ───/
```

(Standard OR gate shape with a small circle/bubble at the output to indicate negation.)

---

**(c)** Boolean expressions. [2 marks]

**(i)** AND gate with inputs A and B: **X = A AND B** ✓

**(ii)** NAND gate with inputs P and Q: **X = NOT (P AND Q)** ✓

---

## Question 2 — Logic Circuits 逻辑电路 [8 marks]

**(a)(i)** Logic circuit for X = (A AND B) OR (NOT C). [3 marks]

```
  A ───┐
       ├─[AND]───┐
  B ───┘          ├─[OR]───── X   ✓
                  │
  C ───[NOT]─────┘
```

✓ Two inputs A and B connected to an AND gate.
✓ Input C connected to a NOT gate.
✓ Outputs of the AND gate and NOT gate connected to an OR gate producing output X.

---

**(a)(ii)** Truth table for X = (A AND B) OR (NOT C). [3 marks]

| A | B | C | A AND B | NOT C | X |
|---|---|---|---------|-------|---|
| 0 | 0 | 0 | 0       | 1     | 1 |
| 0 | 0 | 1 | 0       | 0     | 0 |
| 0 | 1 | 0 | 0       | 1     | 1 |
| 0 | 1 | 1 | 0       | 0     | 0 |
| 1 | 0 | 0 | 0       | 1     | 1 |
| 1 | 0 | 1 | 0       | 0     | 0 |
| 1 | 1 | 0 | 1       | 1     | 1 |
| 1 | 1 | 1 | 1       | 0     | 1 |

✓✓✓ (All 8 rows correct)

---

**(b)** Boolean expression. [2 marks]

**X = (A AND NOT B) OR C** ✓✓

---

## Question 3 — Logic Problem 逻辑应用题 [6 marks]

**(a)** Boolean expression for the security system. [2 marks]

**Z = (D AND A) OR (M AND A)** ✓

This can be simplified to: **Z = A AND (D OR M)** ✓

---

**(b)** Logic circuit. [2 marks]

```
  D ───┐
       ├─[AND]───┐
  A ───┤          ├─[OR]───── Z   ✓
       ├─[AND]───┘
  M ───┘
```

More precisely:
```
  D ───┐
       ├─[AND]──────┐
  A ───┤             ├─[OR]───── Z
       │             │
  M ───┤             │
       ├─[AND]──────┘
  A ───┘
```

✓ D and A feed into one AND gate; M and A feed into another AND gate; both AND gate outputs feed into an OR gate producing Z.

---

**(c)** Output when D = 1, A = 1, M = 0. [2 marks]

Working:
```
Z = (D AND A) OR (M AND A)
Z = (1 AND 1) OR (0 AND 1)  ✓
Z = 1 OR 0
Z = 1  ✓
```

The alarm **would sound** (Z = 1) because the door sensor detects the door is open and the system is armed.

---

## Question 4 — Flip-Flops 触发器 [5 marks]

**(a)** Purpose of a flip-flop circuit. [1 mark]

A flip-flop is a circuit that can store one bit of data. It is a bistable device that has two stable states (0 or 1) and can be used as a single-bit memory element ✓.

---

**(b)** SR flip-flop behaviour table. [2 marks]

| S | R | Q              |
|---|---|----------------|
| 0 | 0 | Q(prev)        |
| 0 | 1 | 0              |
| 1 | 0 | 1              |
| 1 | 1 | INVALID        |

✓ S=0, R=0 retains previous state; S=0, R=1 resets Q to 0; S=1, R=0 sets Q to 1.
✓ S=1, R=1 is the invalid/not allowed state.

---

**(c)** Why S=1, R=1 is invalid. [2 marks]

When S=1 and R=1, the flip-flop is being told to simultaneously set Q to 1 (by S) and reset Q to 0 (by R), which is a contradiction ✓. When both inputs return to 0, the output becomes unpredictable/indeterminate because it depends on which gate responds fractionally faster, leading to an unstable/undefined state ✓.

---

## Question 5 — Input and Output Devices 输入与输出设备 [6 marks]

**(a)(i)** Supermarket checkout system. [2 marks]

**Barcode scanner/reader** ✓.

A barcode scanner can quickly and accurately read the barcode printed on each product, which encodes the product identifier. This is much faster and more accurate than manually typing in product codes, reducing errors and speeding up the checkout process ✓.

---

**(a)(ii)** Graphic designer creating illustrations. [2 marks]

**Graphics tablet (digitiser tablet)** ✓.

A graphics tablet allows the designer to draw directly using a stylus, providing pressure-sensitive input that closely mimics the natural feel of drawing with a pen or brush. This gives much finer control and precision for creating detailed illustrations compared to using a mouse ✓.

---

**(b)** Museum interactive kiosk output device. [2 marks]

**Touchscreen monitor** ✓.

A touchscreen serves as both an output device (displaying text, images, videos about exhibits) and allows intuitive interaction. It is suitable for a public kiosk because visitors do not need training to use it -- they simply touch the screen to navigate, making it accessible for all ages and abilities ✓.

---

## Question 6 — Sensors 传感器 [6 marks]

**(a)(i)** Automatic greenhouse watering system. [2 marks]

**Moisture/humidity sensor** ✓.

The moisture sensor is placed in the soil to continuously measure the moisture level. When the soil moisture drops below a predetermined threshold, the computer system activates the water pump/sprinklers to irrigate the plants. When the moisture level reaches the desired level, the watering stops ✓.

---

**(a)(ii)** Street light that turns on when dark. [2 marks]

**Light sensor (LDR / Light Dependent Resistor)** ✓.

The light sensor measures the ambient light level. When the light level falls below a certain threshold (indicating that it is getting dark), the system automatically turns on the street light. When the light level rises above the threshold (daylight), the light is turned off ✓.

---

**(b)** Why an ADC is needed. [2 marks]

Sensors produce analogue signals (continuously varying voltages) that represent the physical quantity being measured ✓. A computer can only process digital data (discrete binary values), so an Analogue-to-Digital Converter (ADC) is needed to convert the continuous analogue signal from the sensor into a digital/binary value that the computer can store and process ✓.

---

## Question 7 — Embedded Systems 嵌入式系统 [5 marks]

**(a)** Definition of embedded system. [2 marks]

An embedded system is a computer system built into (embedded within) a larger device, designed to perform a specific/dedicated function or set of functions ✓. It typically consists of a microprocessor/microcontroller, memory, and input/output interfaces, and runs pre-programmed software that is usually stored in ROM ✓.

---

**(b)** Two examples of embedded systems. [2 marks]

1. **Washing machine:** The embedded system controls the wash cycle by monitoring sensor inputs (water temperature, water level, drum speed) and controlling outputs (motor, water valves, heater) according to the selected program/settings ✓.

2. **Microwave oven:** The embedded system controls the cooking time and power level, monitors the temperature, manages the display and keypad inputs, and ensures safety interlocks are functioning correctly ✓.

---

**(c)** One distinguishing characteristic. [1 mark]

An embedded system is designed to perform a single specific/dedicated task, whereas a general-purpose computer can run many different applications and be used for a wide variety of tasks ✓.

---

## Question 8 — RFID and GPS 射频识别与全球定位系统 [8 marks]

**(a)** How RFID works. [3 marks]

An RFID system consists of an RFID tag (transponder) and an RFID reader (interrogator) ✓. The RFID tag contains a small microchip that stores a unique identification code, attached to an antenna. The reader emits radio frequency signals through its antenna ✓. When a passive RFID tag enters the reader's electromagnetic field, the tag's antenna absorbs energy from the radio waves, powering the microchip. The tag then transmits its stored data back to the reader. The reader receives this data and passes it to a computer system for processing ✓.

---

**(b)** Two practical applications of RFID. [2 marks]

1. **Inventory/stock management in warehouses or retail:** RFID tags on products allow rapid, automated tracking of stock levels and locations without needing line-of-sight scanning ✓.
2. **Contactless payment cards / access control cards:** RFID-enabled cards or key fobs are used to make payments or gain entry to buildings by tapping near a reader ✓.

---

**(c)** How GPS determines position. [3 marks]

A GPS receiver picks up signals from multiple GPS satellites orbiting the Earth ✓. Each satellite continuously broadcasts its current position and the exact time the signal was sent. The GPS receiver calculates the distance to each satellite by measuring the time delay between when the signal was sent and when it was received (using the speed of light) ✓. By receiving signals from at least three satellites (trilateration), the receiver can calculate its position in two dimensions (latitude and longitude). A fourth satellite is needed to also determine altitude and to correct timing errors ✓.

---

## Question 9 — Mixed Hardware Concepts 综合题 [6 marks]

**(a)** Two sensors in a car's ABS. [2 marks]

1. **Wheel speed sensor:** Attached to each wheel, this sensor measures the rotational speed of the wheel. If a wheel is about to lock up (its speed drops suddenly compared to the others), the ABS system detects this and takes corrective action ✓.

2. **Pressure sensor:** Monitors the hydraulic brake pressure being applied. The ABS system uses this information to rapidly modulate (release and re-apply) the brake pressure to prevent the wheels from locking ✓.

---

**(b)** Why ABS uses an embedded system. [2 marks]

An ABS system needs to respond extremely quickly (in milliseconds) to changes in wheel speed to prevent wheel lock-up. An embedded system is dedicated to this single task, providing the fast, reliable, real-time response required ✓. A general-purpose computer would be too large, too expensive, consume too much power, and might not provide the guaranteed real-time response needed for safety-critical braking operations ✓.

---

**(c)** How keyless entry works using RFID. [2 marks]

The driver carries a key fob that contains an RFID tag/transponder. When the driver approaches the car and presses the door handle (or is within a certain proximity), the car's RFID reader sends out a radio signal ✓. The key fob's RFID tag receives this signal and responds by transmitting its unique encrypted identification code. The car's system receives this code, verifies it matches the authorised code stored in its memory, and if valid, unlocks the doors ✓.

---

*Cambridge International AS Level Computer Science 9618 - Chapter 3 Homework Answers*
