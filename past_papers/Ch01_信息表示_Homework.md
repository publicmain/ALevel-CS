# Chapter 1: Information Representation - 课后作业 Homework

> 姓名：__________ 日期：__________ 总分：__/55

---

## Question 1 — Number Systems 进制转换 [6 marks]

> 中文提示：本题考查不同进制之间的转换，请写出详细的计算过程。

(a) Convert the denary number **219** into binary.
Show your working.
[2 marks]

(b) Convert the binary number **11010110** into hexadecimal.
Show your working.
[2 marks]

(c) Convert the hexadecimal number **3AF** into denary.
Show your working.
[2 marks]

---

## Question 2 — Binary Arithmetic 二进制运算 [8 marks]

> 中文提示：二进制加法和减法。注意进位（carry）和借位（borrow），以及是否发生溢出（overflow）。

(a) Add the following two 8-bit unsigned binary integers.
Show your working.

```
  0 1 1 0 1 1 0 1
+ 0 1 0 1 1 0 1 1
─────────────────
```

State whether an overflow has occurred. Give a reason for your answer.
[3 marks]

(b) Subtract the denary number **35** from the denary number **92** using binary subtraction.
Show your working.
[3 marks]

(c) A computer uses an 8-bit register to store unsigned integers.
State the range of denary values that can be represented.
[2 marks]

---

## Question 3 — Two's Complement 补码表示 [6 marks]

> 中文提示：补码（two's complement）用于表示有符号整数。最高位（MSB）是符号位，0表示正数，1表示负数。

(a) Represent the denary number **-53** in 8-bit two's complement binary.
Show your working.
[2 marks]

(b) Convert the following 8-bit two's complement binary number into denary.

```
1 0 1 1 0 1 0 0
```

Show your working.
[2 marks]

(c) A system uses 8-bit two's complement to represent integers.
State the range of denary values that can be represented.
[2 marks]

---

## Question 4 — BCD (Binary Coded Decimal) [4 marks]

> 中文提示：BCD用4位二进制表示一个十进制数字（0-9），每个十进制位单独编码。

(a) Represent the denary number **473** in BCD.
[2 marks]

(b) Explain one advantage of using BCD rather than pure binary to represent denary numbers.
[2 marks]

---

## Question 5 — Character Sets 字符集 [5 marks]

> 中文提示：ASCII和Unicode是两种常见的字符编码标准。思考它们的区别和各自的优缺点。

(a) State the number of bits used to represent one character in standard ASCII.
[1 mark]

(b) Explain why Unicode was developed when ASCII already existed.
[2 marks]

(c) A text file contains 2000 characters. The file is encoded using Unicode UTF-16 (16 bits per character).
Calculate the file size in kibibytes (KiB). Show your working.
[2 marks]

---

## Question 6 — Bitmap Images 位图图像 [8 marks]

> 中文提示：位图由像素（pixel）组成。分辨率（resolution）、色深（colour depth）和文件大小之间有数学关系。计算公式：文件大小 = 宽 x 高 x 色深。

(a) Define the following terms as they relate to bitmap images:

(i) Resolution
[1 mark]

(ii) Colour depth
[1 mark]

(b) A bitmap image has the following properties:
- Width: 1920 pixels
- Height: 1080 pixels
- Colour depth: 24 bits per pixel

Calculate the file size of the image in mebibytes (MiB). Show your working.
[3 marks]

(c) The colour depth of the image is reduced from 24 bits to 8 bits per pixel.
Describe the effect this would have on:

(i) the appearance of the image
[1 mark]

(ii) the file size of the image
[2 marks]

---

## Question 7 — Vector Graphics 矢量图 [4 marks]

> 中文提示：矢量图使用数学方程和属性（如坐标、颜色、线宽）来描述图形，而不是像素。思考矢量图与位图的区别。

(a) Describe how data is stored in a vector graphic file.
[2 marks]

(b) Give two advantages of using vector graphics instead of bitmap images.
[2 marks]

---

## Question 8 — Sound Representation 声音表示 [6 marks]

> 中文提示：声音采样涉及采样率（sampling rate）和采样精度/分辨率（sampling resolution）。这两个参数影响声音质量和文件大小。

(a) Explain how analogue sound is converted into a digital form for storage in a computer.
[3 marks]

(b) A music recording has the following properties:
- Sampling rate: 44,100 Hz
- Sampling resolution: 16 bits
- Duration: 3 minutes
- Stereo (2 channels)

Calculate the file size of this recording in mebibytes (MiB). Show your working.
[3 marks]

---

## Question 9 — Data Compression 数据压缩 [8 marks]

> 中文提示：压缩分为有损压缩（lossy）和无损压缩（lossless）。RLE（游程编码）是一种无损压缩方法。思考两种压缩方式的适用场景。

(a) Explain the difference between lossy and lossless compression.
[2 marks]

(b) State one file type where lossy compression would be suitable and one file type where it would NOT be suitable. Give a reason for each choice.
[4 marks]

(c) The following data represents pixel colour values in a simple image:

```
RRRRRGGGBBBBBBRRRRR
```

Apply Run-Length Encoding (RLE) to compress this data. Show the compressed output.
[2 marks]

---

### 答题完毕后请检查：
- 所有计算题是否写出了详细步骤（show your working）
- 解释题是否使用了正确的计算机科学术语
- 是否回答了每道题的所有小问

---

*Cambridge International AS Level Computer Science 9618 - Chapter 1 Homework*
