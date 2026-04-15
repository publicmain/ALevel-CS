# Chapter 3: Hardware - Paper 1 Answers

> Topics: Logic gates, logic circuits, truth tables, Boolean expressions, input/output devices, sensors, embedded systems

---

## 2024 May/June (9618/12)

### Question 1

**(a)** Operation of each logic gate:

- **NAND**: Outputs 0 only when all inputs are 1; otherwise outputs 1 ✓
  > (NOT AND -- the opposite of AND)
- **NOR**: Outputs 1 only when all inputs are 0; otherwise outputs 0 ✓
  > (NOT OR -- the opposite of OR)
- **XOR**: Outputs 1 when the inputs are different; outputs 0 when the inputs are the same ✓
  > (Exclusive OR)
- **OR**: Outputs 1 when at least one input is 1; outputs 0 only when all inputs are 0 ✓

> 提示：NAND=与非（AND取反），NOR=或非（OR取反），XOR=异或（输入不同则为1），OR=或（至少一个1则为1）。

**(b)** Logic circuit for X = NOT ((A AND B) OR (C AND D)):

The circuit should contain:
- An AND gate with inputs A and B ✓
- An AND gate with inputs C and D
- An OR gate taking outputs of both AND gates
- A NOT gate on the output of the OR gate to produce X ✓

> 提示：先画两个AND门（A AND B）和（C AND D），然后接一个OR门，最后接一个NOT门输出X。

### Question 2 (partial - hardware/input-output devices)

**(a)** Complete the VR headset description:

- A headset can have one or two **screens / displays** ✓ that output the image to the user.
- This sensor is a **gyroscope / accelerometer** ✓
- The data is transmitted to a microprocessor that analyses the data to identify the **direction / speed / angle** ✓ of movement.
- Some headsets use **cameras / infrared sensors** ✓ that record the user's eye movements for analysis.

> 提示：VR头盔组成：屏幕/显示器 + 陀螺仪/加速度计传感器 + 摄像头/红外传感器追踪眼动。

**(b)** How a buffer is used when transmitting data between computer and VR headset:

- A buffer is a temporary storage area / region of memory ✓
- The computer writes data to the buffer at a faster rate than the VR headset can process / display it ✓
- The buffer holds the data until the VR headset is ready to receive / process it, allowing the two devices to operate at different speeds ✓

> 提示：缓冲区（buffer）是临时存储区域，用于协调两个速度不同的设备。电脑快速写入数据到缓冲区，VR头盔按自己的速度从缓冲区读取数据。

**(c)** Benefits of using EEPROM instead of other types of ROM:

- EEPROM can be reprogrammed / updated electronically without removing the chip from the device ✓
- This allows the firmware / software on the VR headset to be updated to fix bugs or add new features ✓
- Unlike EPROM, EEPROM does not require UV light to erase / can be erased and reprogrammed in-circuit / individual bytes can be erased and rewritten ✓

> 提示：EEPROM（电可擦可编程只读存储器）优点：(1) 可以电子方式擦除和重写，无需拆芯片 (2) 方便固件更新 (3) 不需要紫外线擦除（与EPROM相比）(4) 可以按字节擦写。

---

## 2024 Oct/Nov (9618/12)

### Question 1

**(a)** Truth table for X = (A XOR B) NAND (A AND (B XOR C)):

Working through each row:

Let P = A XOR B, Q = B XOR C, R = A AND Q, X = P NAND R

| A | B | C | A XOR B (P) | B XOR C (Q) | A AND Q (R) | X = P NAND R |
|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 0 | 1 ✓ |
| 0 | 0 | 1 | 0 | 1 | 0 | 1 |
| 0 | 1 | 0 | 1 | 1 | 0 | 1 |
| 0 | 1 | 1 | 1 | 0 | 0 | 1 |
| 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| 1 | 0 | 1 | 1 | 1 | 1 | 0 |
| 1 | 1 | 0 | 0 | 1 | 1 | 1 ✓ |
| 1 | 1 | 1 | 0 | 0 | 0 | 1 |

Final answers for X column: **1, 1, 1, 1, 1, 0, 1, 1**

> 提示：分步计算：先算内层的 XOR 和 AND，再算外层的 NAND。NAND = 当两个输入都为1时输出0，否则输出1。

**(b)** Logic circuit for W = P NAND ((Q OR NOT R) XOR (P XOR Q)):

The circuit should contain:
- A NOT gate on input R ✓
- An OR gate with inputs Q and NOT R
- An XOR gate with inputs P and Q
- An XOR gate taking the outputs of the OR gate and the previous XOR gate
- A NAND gate with inputs P and the output of the second XOR gate to produce W ✓

> 提示：从内向外构建：先画NOT R，然后Q OR (NOT R)；同时画P XOR Q；两个结果进XOR门；最后和P一起进NAND门。

### Question 2

**(a)** Drawbacks of embedded systems:

- Embedded systems are designed for a specific / single purpose and cannot be easily reprogrammed / adapted for other tasks ✓
- They have limited processing power / memory / storage compared to general-purpose computers ✓
- Updating / upgrading the software or hardware is difficult / may require specialist equipment or replacement of the entire system ✓

> 提示：嵌入式系统缺点：(1) 专用，不能轻易改变功能 (2) 处理能力/内存有限 (3) 升级困难，可能需要替换整个系统。

**(b)** Benefit of DRAM over SRAM in an embedded system:

✓ DRAM is cheaper to manufacture / costs less per unit of storage than SRAM

OR: DRAM has higher storage density / can store more data in the same physical space

> 提示：DRAM比SRAM便宜且存储密度更高（同样面积能存更多数据）。

**(c)** Two differences between EPROM and EEPROM:

- EPROM is erased using ultraviolet (UV) light, while EEPROM is erased electrically ✓
- EPROM must be removed from the circuit to be erased / reprogrammed, while EEPROM can be reprogrammed in-circuit / without removal ✓

Other valid differences:
- EPROM erases all data at once, while EEPROM can erase individual bytes / specific locations ✓
- EEPROM is generally more expensive than EPROM ✓

> 提示：EPROM用紫外线擦除（需拆下芯片），EEPROM用电信号擦除（可在电路中操作）。EPROM整体擦除，EEPROM可按字节擦除。

### Question 3(b) (partial - ports/monitors)

Benefits of HDMI over VGA:

- HDMI transmits digital signals, while VGA transmits analogue signals — digital signals provide a clearer / sharper / more accurate image ✓
- HDMI can transmit both video and audio through a single cable, so the built-in speakers can be used / VGA only transmits video ✓
- HDMI supports higher resolutions / the resolution of 2560 × 1600 may not be fully supported by VGA ✓
- HDMI provides better colour accuracy / wider colour range than VGA ✓

> 提示：HDMI优于VGA：(1) 数字信号更清晰 (2) 一根线传输音频+视频（VGA只能传视频）(3) 支持更高分辨率 (4) 颜色更准确。

### Question 9

**(a)** Two sensors for the bridge warning system:

| Sensor | How it is used |
|---|---|
| **Pressure sensor / weight sensor / strain gauge** ✓ | Placed on the road surface / bridge to measure the weight of vehicles — if the weight exceeds 10,000 kg, a warning is triggered ✓ |
| **Infrared / ultrasonic / laser (distance) sensor** ✓ | Positioned above the road to measure the height of vehicles — if the height exceeds 3 m, a warning is triggered ✓ |

> 提示：重量检测用压力传感器/称重传感器，高度检测用红外/超声波/激光距离传感器。

**(b)** Whether the system is monitoring or control:

- The system is an example of a **monitoring system** ✓
- The system detects / measures values (weight and height) and issues a warning / alerts the user, but it does not automatically take physical action to control the situation (e.g. it does not physically stop the vehicle) / a monitoring system reports data but does not change the environment ✓

> 提示：这是监控系统（monitoring system），因为它只检测数据并发出警告，不会自动采取物理行动（如拦截车辆）。控制系统（control system）会自动调整环境。

---

## 2023 May/June (9618/12)

### Question 5(c) (partial - ports)

**(i)** How data is transmitted through a USB port:

✓ Data is transmitted serially / one bit at a time through the USB port.

> 提示：USB是串行传输（serial），数据逐位传输。

**(ii)** Another type of port for connecting a monitor:

✓ HDMI / VGA / DisplayPort / DVI

> 提示：连接显示器的端口类型：HDMI、VGA、DisplayPort、DVI。

### Question 6

**(a)** Logic circuit for Z = (R XOR S) AND (NOT T NOR P):

The circuit should contain:
- An XOR gate with inputs R and S ✓
- A NOT gate on input T
- A NOR gate with inputs NOT T and P (or equivalently: NOT T NOR P)
- An AND gate combining the XOR output and the NOR output to produce Z ✓

Note: "NOT T NOR P" means (NOT T) NOR P, i.e., NOT(NOT T OR P).

> 提示：先画R XOR S，再画NOT T，然后(NOT T) NOR P，最后两个结果用AND门连接输出Z。

**(b)** Truth table for Z = (NOT P OR Q) XOR (R NOR Q):

Working: Let M = NOT P OR Q, N = R NOR Q (= NOT(R OR Q)), Z = M XOR N

| P | Q | R | NOT P | NOT P OR Q (M) | R OR Q | R NOR Q (N) | Z = M XOR N |
|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 1 | 1 | 0 | 1 | 0 |
| 0 | 0 | 1 | 1 | 1 | 1 | 0 | 1 |
| 0 | 1 | 0 | 1 | 1 | 1 | 0 | 1 |
| 0 | 1 | 1 | 1 | 1 | 1 | 0 | 1 |
| 1 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |
| 1 | 0 | 1 | 0 | 0 | 1 | 0 | 0 |
| 1 | 1 | 0 | 0 | 1 | 1 | 0 | 1 ✓ |
| 1 | 1 | 1 | 0 | 1 | 1 | 0 | 1 ✓ |

Final answers for Z column: **0, 1, 1, 1, 1, 0, 1, 1**

> 提示：NOR = NOT OR，先算OR再取反。XOR = 输入不同则为1。分步计算每个子表达式。

---

## 2023 Oct/Nov (9618/12)

### Question 1

**(a)** Appropriate sensor for counting chocolate bars:

✓ **Infrared sensor / light sensor / proximity sensor / photoelectric sensor**

> 提示：计数巧克力棒可用红外传感器/光传感器/接近传感器——每经过一根巧克力棒，传感器检测到信号变化，计数加1。

**(b)** Role of an actuator in the weight-checking system:

- An actuator is a device that converts an electrical signal into physical movement / action ✓
- In this system, the actuator (e.g. a motor / pneumatic arm / push mechanism) physically removes / pushes the chocolate bar off the conveyor belt when its weight is detected as incorrect ✓

> 提示：执行器（actuator）将电信号转换为物理动作。在此系统中，执行器（如电机/气动臂）把重量不合格的巧克力棒从传送带上推掉。

**(c)(i)** Two features of embedded systems:

- Dedicated to / designed for a single / specific task or function ✓
- Built into / part of a larger device or system ✓

Other valid features:
- Has limited / constrained processing power and memory ✓
- Often runs in real time ✓
- Does not have a traditional user interface (keyboard, monitor) ✓

> 提示：嵌入式系统特征：(1) 专用于单一任务 (2) 内置于更大设备中 (3) 处理能力有限 (4) 通常实时运行。

**(c)(ii)** One drawback of embedded systems:

✓ Difficult / impossible to upgrade or modify for a different purpose / task

OR: Limited processing power / memory means they cannot handle complex tasks ✓
OR: If it fails, the entire device may need to be replaced ✓

> 提示：嵌入式系统缺点：难以升级或修改功能；出故障可能需要更换整个设备。

### Question 4

**(a)** Boolean expression from logic circuit:

Since the actual circuit image is not provided in text form, the expected answer typically involves reading the gates from the diagram and writing the expression. The answer should be in the form:

✓✓✓ X = ... (3 marks for correctly identifying all gates and combining them into the correct expression)

> 提示：从逻辑电路图读取布尔表达式：从输入端开始，逐个门识别运算，写出完整表达式。

**(b)** Truth table for X = A XOR (B AND (A NAND B) AND NOT C):

Working: Let P = A NAND B, Q = NOT C, R = B AND P AND Q, X = A XOR R

| A | B | C | A NAND B (P) | NOT C (Q) | B AND P AND Q (R) | X = A XOR R |
|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 1 | 1 | 0 | 0 |
| 0 | 0 | 1 | 1 | 0 | 0 | 0 |
| 0 | 1 | 0 | 1 | 1 | 1 | 1 |
| 0 | 1 | 1 | 1 | 0 | 0 | 0 |
| 1 | 0 | 0 | 1 | 1 | 0 | 1 |
| 1 | 0 | 1 | 1 | 0 | 0 | 1 |
| 1 | 1 | 0 | 0 | 1 | 0 | 1 ✓ |
| 1 | 1 | 1 | 0 | 0 | 0 | 1 ✓ |

Final answers for X column: **0, 0, 1, 0, 1, 1, 1, 1**

> 提示：NAND = 当两个输入都为1时输出0，否则输出1。分步计算：先算 A NAND B，再算 NOT C，然后 B AND (NAND结果) AND (NOT C)，最后与A做XOR。

---

## 2022 Oct/Nov (9618/12)

### Question 3

**(a)** Logic circuit for the greenhouse window:

From the description:
- Window opens (X = 1) if: temperature too high AND wind speed acceptable AND (rain not detected OR manual override off)
- Boolean expression: X = T AND (NOT W) AND (NOT R OR NOT M)

The circuit should contain:
- A NOT gate on W ✓
- A NOT gate on R and a NOT gate on M
- An OR gate with inputs NOT R and NOT M
- An AND gate combining T, NOT W, and the OR gate output to produce X ✓✓

> 提示：X = T AND (NOT W) AND (NOT R OR NOT M)。先画NOT门（W, R, M取反），然后NOT R和NOT M接OR门，最后T、NOT W和OR输出接AND门。

**(b)** Truth table for X = NOT (A OR B OR C) AND (B NOR C):

Working: Let P = NOT(A OR B OR C), Q = B NOR C = NOT(B OR C), X = P AND Q

| A | B | C | A OR B OR C | NOT(A OR B OR C) (P) | B OR C | B NOR C (Q) | X = P AND Q |
|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 1 | 0 | 1 | 1 ✓ |
| 0 | 0 | 1 | 1 | 0 | 1 | 0 | 0 |
| 0 | 1 | 0 | 1 | 0 | 1 | 0 | 0 |
| 0 | 1 | 1 | 1 | 0 | 1 | 0 | 0 |
| 1 | 0 | 0 | 1 | 0 | 0 | 1 | 0 |
| 1 | 0 | 1 | 1 | 0 | 1 | 0 | 0 |
| 1 | 1 | 0 | 1 | 0 | 1 | 0 | 0 ✓ |
| 1 | 1 | 1 | 1 | 0 | 1 | 0 | 0 |

Final answers for X column: **1, 0, 0, 0, 0, 0, 0, 0**

> 提示：只有当A、B、C全为0时，NOT(A OR B OR C)才为1，同时B NOR C也为1，所以X=1。其他情况X都为0。

**(c)** Why ROM is used in an embedded system:

- ROM is non-volatile, meaning it retains its data when the power is turned off ✓
- This is important because the embedded system needs to store its program / instructions permanently so it can execute them immediately when powered on / the program does not need to be reloaded ✓

> 提示：ROM用于嵌入式系统因为：(1) 非易失性——断电不丢失数据 (2) 程序永久存储，上电即可运行，无需重新加载。

---

## 2021 May/June (9618/12)

### Question 3

**(a)** Logic circuit for S = (A AND B AND C) OR (B XOR C):

The circuit should contain:
- A three-input AND gate with inputs A, B, and C ✓✓
  (or two cascaded two-input AND gates)
- An XOR gate with inputs B and C ✓
- An OR gate combining the AND output and XOR output to produce S ✓

> 提示：画一个三输入AND门（A, B, C）和一个XOR门（B, C），然后两个输出接OR门得到S。

**(b)** Truth table for S = (A AND B AND C) OR (B XOR C):

| A | B | C | A AND B AND C | B XOR C | S = OR |
|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | **0** |
| 0 | 0 | 1 | 0 | 1 | **1** |
| 0 | 1 | 0 | 0 | 1 | **1** |
| 0 | 1 | 1 | 0 | 0 | **0** |
| 1 | 0 | 0 | 0 | 0 | **0** |
| 1 | 0 | 1 | 0 | 1 | **1** ✓ |
| 1 | 1 | 0 | 0 | 1 | **1** |
| 1 | 1 | 1 | 1 | 0 | **1** ✓ |

Final answers for S column: **0, 1, 1, 0, 0, 1, 1, 1**

> 提示：分别计算 A AND B AND C 和 B XOR C，然后取 OR。只要其中一个为1，结果就为1。
