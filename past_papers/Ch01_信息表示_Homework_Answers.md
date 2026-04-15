# Chapter 1: Information Representation - Homework Answers

> 总分：55

---

## Question 1 — Number Systems 进制转换 [6 marks]

**(a)** Convert the denary number **219** into binary. [2 marks]

Working:
```
219 / 2 = 109 remainder 1
109 / 2 = 54  remainder 1
 54 / 2 = 27  remainder 0
 27 / 2 = 13  remainder 1
 13 / 2 = 6   remainder 1
  6 / 2 = 3   remainder 0
  3 / 2 = 1   remainder 1
  1 / 2 = 0   remainder 1
```

Read remainders from bottom to top: **11011011** ✓ (1 mark for correct working, 1 mark for correct answer)

---

**(b)** Convert the binary number **11010110** into hexadecimal. [2 marks]

Working:
```
Split into 4-bit groups:
1101  0110
```
- `1101` = 8 + 4 + 0 + 1 = 13 = D ✓
- `0110` = 0 + 4 + 2 + 0 = 6 = 6 ✓

Answer: **D6**

---

**(c)** Convert the hexadecimal number **3AF** into denary. [2 marks]

Working:
```
3   A   F
3 x 16^2  +  10 x 16^1  +  15 x 16^0   ✓
= 3 x 256  +  10 x 16   +  15 x 1
= 768       +  160        +  15
```

Answer: **943** ✓

---

## Question 2 — Binary Arithmetic 二进制运算 [8 marks]

**(a)** Add the two 8-bit unsigned binary integers. [3 marks]

Working:
```
    1 1 1 1 1 1       (carries)
    0 1 1 0 1 1 0 1   (109)
  + 0 1 0 1 1 0 1 1   (91)
  ─────────────────
    1 1 0 0 1 0 0 0   (200)
```

Answer: **11001000** ✓

Overflow: **Yes, an overflow has occurred.** ✓
Reason: The carry from bit 6 into bit 7 (the most significant bit) means the result (200) is still within the range of an unsigned 8-bit integer (0-255), however there is no carry out of bit 7, so **no overflow has occurred** for unsigned addition. ✓

**Correction:** There is **no** carry out of bit 7. The result 200 fits within an unsigned 8-bit register (0-255). Therefore **no overflow has occurred**. ✓

---

**(b)** Subtract 35 from 92 using binary subtraction. [3 marks]

Working:
```
Convert to binary:
92 = 01011100  ✓
35 = 00100011  ✓

  01011100   (92)
- 00100011   (35)
──────────
  00111001   (57)  ✓
```

Verification: 32 + 16 + 8 + 0 + 0 + 1 = 57 = 92 - 35 ✓

---

**(c)** Range of denary values for an 8-bit unsigned integer. [2 marks]

- Minimum value: **0** ✓ (when all bits are 0: 00000000)
- Maximum value: **255** ✓ (when all bits are 1: 11111111 = 2^8 - 1)

---

## Question 3 — Two's Complement 补码表示 [6 marks]

**(a)** Represent **-53** in 8-bit two's complement. [2 marks]

Working:
```
Step 1: Write +53 in binary:
53 = 00110101  ✓

Step 2: Flip all bits (one's complement):
11001010

Step 3: Add 1:
  11001010
+ 00000001
──────────
  11001011  ✓
```

Answer: **11001011**

---

**(b)** Convert `10110100` (8-bit two's complement) into denary. [2 marks]

Working:
```
MSB is 1, so the number is negative.  ✓

Step 1: Flip all bits:
01001011

Step 2: Add 1:
  01001011
+ 00000001
──────────
  01001100

Step 3: Convert to denary:
64 + 8 + 4 = 76
```

Answer: **-76** ✓

---

**(c)** Range of denary values for 8-bit two's complement. [2 marks]

- Minimum value: **-128** ✓ (which is -2^7)
- Maximum value: **+127** ✓ (which is 2^7 - 1)

---

## Question 4 — BCD (Binary Coded Decimal) [4 marks]

**(a)** Represent **473** in BCD. [2 marks]

Working:
```
Each denary digit is represented as a 4-bit binary nibble:  ✓
4 = 0100
7 = 0111
3 = 0011
```

Answer: **0100 0111 0011** ✓

---

**(b)** One advantage of BCD over pure binary. [2 marks]

BCD allows each denary digit to be individually converted to/from binary without complex calculations ✓, which makes it particularly useful for electronic displays (e.g., digital clocks, calculators) where each digit needs to be displayed separately, and avoids rounding errors that can occur with pure binary representation of decimal fractions (e.g., in financial/currency calculations) ✓.

---

## Question 5 — Character Sets 字符集 [5 marks]

**(a)** Number of bits for one ASCII character. [1 mark]

**7 bits** ✓ (standard ASCII uses 7 bits, giving 128 possible characters)

---

**(b)** Why Unicode was developed. [2 marks]

ASCII only uses 7 bits and can represent a maximum of 128 characters ✓. This is not enough to represent characters from all of the world's languages and writing systems (e.g., Chinese, Arabic, Japanese, emoji). Unicode was developed to provide a universal character set that can represent characters from every language and many symbols, using up to 32 bits per character ✓.

---

**(c)** File size calculation for 2000 characters in UTF-16. [2 marks]

Working:
```
File size = number of characters x bits per character
         = 2000 x 16
         = 32,000 bits  ✓

Convert to kibibytes:
32,000 bits / 8 = 4,000 bytes
4,000 / 1024 = 3.90625 KiB  ✓
```

Answer: **3.91 KiB** (or 3.90625 KiB)

---

## Question 6 — Bitmap Images 位图图像 [8 marks]

**(a)(i)** Resolution [1 mark]

Resolution is the number of pixels per unit of measurement (e.g., dots per inch / dpi), or the total number of pixels that make up the image (width x height in pixels). ✓

---

**(a)(ii)** Colour depth [1 mark]

Colour depth is the number of bits used to represent the colour of each pixel in the image. ✓

---

**(b)** File size calculation. [3 marks]

Working:
```
Total number of pixels = 1920 x 1080 = 2,073,600 pixels  ✓

File size in bits = 2,073,600 x 24 = 49,766,400 bits  ✓

Convert to mebibytes:
49,766,400 / 8 = 6,220,800 bytes
6,220,800 / 1024 = 6,075 KiB
6,075 / 1024 = 5.93 MiB  ✓
```

Answer: **approximately 5.93 MiB**

---

**(c)(i)** Effect on appearance. [1 mark]

The image quality would decrease / appear less realistic ✓. With only 8 bits per pixel the image can only display 256 different colours (instead of approximately 16.7 million with 24 bits), so colour gradients would appear blocky/banded and subtle colour differences would be lost.

---

**(c)(ii)** Effect on file size. [2 marks]

The file size would be reduced to one third of the original ✓.

Working:
```
Original: 24 bits per pixel
New: 8 bits per pixel
Ratio: 8/24 = 1/3

New file size = 5.93 x (8/24) = approximately 1.98 MiB  ✓
```

---

## Question 7 — Vector Graphics 矢量图 [4 marks]

**(a)** How data is stored in a vector graphic file. [2 marks]

A vector graphic file stores an image as a list of geometric objects/shapes (such as lines, curves, rectangles, circles, polygons) ✓. Each object is defined by its mathematical properties/attributes such as coordinates, length, radius, line colour, fill colour, line thickness/weight, and layering order ✓.

---

**(b)** Two advantages of vector graphics over bitmap images. [2 marks]

1. Vector graphics can be scaled (enlarged or reduced) to any size without any loss of quality/resolution, because the image is recalculated from its mathematical definitions ✓.
2. Vector graphic files are generally smaller in file size than equivalent bitmap images, because only the mathematical properties of each object need to be stored rather than data for every individual pixel ✓.

---

## Question 8 — Sound Representation 声音表示 [6 marks]

**(a)** How analogue sound is converted to digital. [3 marks]

1. A microphone converts the analogue sound wave into an analogue electrical signal ✓.
2. An Analogue-to-Digital Converter (ADC) samples the amplitude of the analogue signal at regular time intervals (determined by the sampling rate) ✓.
3. Each sampled amplitude value is rounded to the nearest available level and stored as a binary number. The precision of each sample is determined by the sampling resolution (bit depth) ✓.

---

**(b)** File size calculation. [3 marks]

Working:
```
Duration in seconds = 3 x 60 = 180 seconds  ✓

File size = sampling rate x sampling resolution x duration x number of channels
         = 44,100 x 16 x 180 x 2
         = 254,016,000 bits  ✓

Convert to mebibytes:
254,016,000 / 8 = 31,752,000 bytes
31,752,000 / 1024 = 31,007.8125 KiB
31,007.8125 / 1024 = 30.28 MiB  ✓
```

Answer: **approximately 30.28 MiB**

---

## Question 9 — Data Compression 数据压缩 [8 marks]

**(a)** Difference between lossy and lossless compression. [2 marks]

**Lossy compression** permanently removes some data from the file to reduce file size. The original file cannot be perfectly reconstructed from the compressed version ✓.

**Lossless compression** reduces the file size without losing any data. The original file can be perfectly reconstructed from the compressed version ✓.

---

**(b)** Suitable file types. [4 marks]

**Lossy suitable:** Photographic image files (e.g., JPEG) ✓. Reason: Small losses in colour accuracy are generally not noticeable to the human eye, and the significant reduction in file size is beneficial for storage and transmission ✓.

**Lossy NOT suitable:** Program/executable files or text documents ✓. Reason: Losing even a single bit of data could corrupt the program code or alter the meaning of the text, making the file unusable ✓.

---

**(c)** Run-Length Encoding of `RRRRRGGGBBBBBBRRRRR`. [2 marks]

Compressed output: **R5 G3 B6 R5** ✓✓

(Each group is encoded as the character value followed by the count of consecutive repetitions.)

---

*Cambridge International AS Level Computer Science 9618 - Chapter 1 Homework Answers*
