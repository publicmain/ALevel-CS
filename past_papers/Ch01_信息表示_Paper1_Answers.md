# Chapter 1: Information Representation - Paper 1 Answers

> Topics: Number systems, binary arithmetic, data representation, character sets, multimedia (images, sound, video), compression

---

## 2024 May/June (9618/12)

### Question 7

**(a)** ✓ **3300 kibibytes**

Working:
- 3300 kibibytes = 3300 × 1024 = 3,379,200 bytes
- 0.3 megabytes = 0.3 × 1,000,000 = 300,000 bytes
- 3 mebibytes = 3 × 1,048,576 = 3,145,728 bytes
- 3300 kilobytes = 3300 × 1000 = 3,300,000 bytes

3,379,200 > 3,300,000 > 3,145,728 > 300,000 -- 3300 kibibytes is the largest.

> 提示：1 kibibyte (KiB) = 1024 bytes, 1 mebibyte (MiB) = 1024 × 1024 = 1,048,576 bytes, 1 kilobyte (KB) = 1000 bytes, 1 megabyte (MB) = 1,000,000 bytes。逐个换算成 bytes 再比较大小。

**(b)** Working:

Convert 100 to binary:
- 100 = 64 + 32 + 4 = 01100100 ✓

Convert 10 to binary:
- 10 = 8 + 2 = 00001010 ✓

Binary subtraction: 01100100 - 00001010

```
  01100100
- 00001010
----------
  01011010  ✓
```

Answer: **01011010** (= 90 in denary)

> 提示：二进制减法可以用借位法（borrow），也可以用补码加法（把减数取反加1，再相加）。

**(c)** Convert C0F₁₆ to denary:

- C = 12, 0 = 0, F = 15
- C0F = 12 × 16² + 0 × 16¹ + 15 × 16⁰ ✓
- = 12 × 256 + 0 × 16 + 15 × 1
- = 3072 + 0 + 15
- = **3087** ✓

> 提示：十六进制转十进制，每位乘以16的幂次（从右往左：16⁰, 16¹, 16²...），然后求和。

### Question 2(d) (partial - multimedia component)

**(i)** How data for a bitmapped image is encoded:

- The image is made up of pixels ✓
- Each pixel is assigned a binary value / colour code that represents its colour ✓
- The number of bits used per pixel determines the colour depth / number of colours available ✓

> 提示：位图图像由像素（pixels）组成，每个像素存储一个颜色值，颜色深度（colour depth）决定了可用颜色数量。

**(ii)** Contents of a vector graphic drawing list:

- A drawing list contains a set of commands / instructions that define each object (e.g. line, circle, rectangle) ✓
- Each object is defined by its properties such as coordinates, dimensions, line colour, line thickness, fill colour ✓

> 提示：矢量图的绘图列表（drawing list）包含描述每个图形对象的命令和属性（坐标、大小、颜色等）。

**(iii)** Two reasons why the video does not need to be compressed:

- The video needs to be transmitted in real time, so there is no time to compress/decompress ✓
- Compression/decompression would introduce latency / delay which would affect the VR experience ✓

Alternative valid points:
- The bandwidth / data transfer rate between the computer and headset is sufficient to transmit uncompressed data ✓
- Lossy compression would reduce the image quality which would affect the VR experience ✓

> 提示：VR实时传输不压缩是因为：(1) 压缩/解压会引入延迟 (2) 带宽足够 (3) 有损压缩会降低画质影响体验。

---

## 2024 Oct/Nov (9618/12)

### Question 7

**(a)(i)** Define bitmap terms:

- **Colour depth**: The number of bits used to represent / encode the colour of each pixel ✓
- **File header**: Metadata stored at the beginning of the file that contains information about the image, e.g. image dimensions / resolution / colour depth / file type ✓

> 提示：颜色深度 = 每个像素用多少位来表示颜色。文件头 = 文件开头存储的元数据（图像宽高、分辨率等信息）。

**(a)(ii)** Effect of changing resolution on:

- **Image quality**: Increasing resolution means more pixels per unit area / more pixels to represent the image, so more detail is captured and the image quality improves ✓ (and vice versa)
- **File size**: More pixels means more data needs to be stored, so the file size increases ✓ (and vice versa)

> 提示：分辨率越高 → 像素越多 → 图像越清晰 + 文件越大。

**(a)(iii)** One lossless method of compressing an image:

✓ Run-length encoding (RLE)

> 提示：无损压缩方法：游程编码（RLE）。

**(b)** Define vector graphic terms:

- **Property**: An attribute / characteristic of a drawing object, e.g. line colour, line thickness / style, fill colour, coordinates, dimensions, radius ✓
- **Drawing list**: A list / set of commands / instructions used to define / recreate each drawing object in the vector graphic image ✓

> 提示：属性（property）= 图形对象的特征（颜色、粗细等）。绘图列表（drawing list）= 重新绘制图形所需的指令集合。

---

## 2023 May/June (9618/12)

### Question 4

**(a)** Number of unique binary values in 16 bits:

✓ **65536** (2¹⁶ = 65536)

> 提示：n位二进制可以表示 2ⁿ 个不同的值。

**(b)** 8-bit one's complement of -120:

First, convert 120 to binary:
- 120 = 64 + 32 + 16 + 8 = 01111000 ✓

One's complement: invert all bits:
- **10000111** ✓

> 提示：反码（one's complement）：先写出正数的二进制，然后把每一位取反（0变1，1变0）。

**(c)** Convert A04₁₆ to denary:

- A = 10, 0 = 0, 4 = 4
- A04 = 10 × 16² + 0 × 16¹ + 4 × 16⁰ ✓
- = 10 × 256 + 0 × 16 + 4 × 1
- = 2560 + 0 + 4
- = **2564** ✓

> 提示：A=10，十六进制转十进制用位权展开法。

**(d)** 2-place left logical shift on 01001111:

- Shift left 2 places: remove the 2 leftmost bits (01), shift remaining bits left, fill right with 0s
- ✓ **00111100**

> 提示：逻辑左移2位：左边丢弃2位，右边补2个0。注意左移可能导致溢出。

---

## 2023 Oct/Nov (9618/12)

### Question 3

**(a)** Difference between kibibyte and megabyte:

✓ A kibibyte is 1024 bytes (2¹⁰) while a megabyte is 1,000,000 bytes (10⁶)

OR: A kibibyte uses a binary-based measurement (powers of 2) while a megabyte uses a decimal-based measurement (powers of 10)

OR: They represent different quantities of data — a megabyte is much larger than a kibibyte

> 提示：kibibyte = 1024 bytes（基于2的幂），megabyte = 1,000,000 bytes（基于10的幂）。单位大小和计算基数都不同。

**(b)(i)** Convert -196 to 12-bit two's complement:

Convert 196 to binary:
- 196 = 128 + 64 + 4 = 11000100
- In 12 bits: 000011000100

Two's complement: invert all bits and add 1:
- Invert: 111100111011
- Add 1: 111100111100

✓ **111100111100**

> 提示：补码（two's complement）= 反码 + 1。先写正数的二进制，取反，再加1。

**(b)(ii)** Convert BCD 100001100101 to denary:

Split into groups of 4 bits:
- 1000 | 0110 | 0101
- 8 | 6 | 5

✓ **865**

> 提示：BCD（二进制编码十进制）：每4位二进制表示一个十进制数字。

**(b)(iii)** Convert unsigned binary 000111010110 to denary:

- 000111010110
- = 256 + 128 + 64 + 16 + 4 + 2
- = **470**

✓ **470**

> 提示：从右往左，每位乘以2的幂次再求和。

**(c)** Practical application of BCD and justification:

- Application: Digital clocks / watches / timers / calculators / any device that displays decimal digits ✓
- Justification: BCD allows each decimal digit to be stored and displayed separately / individual digits can be easily sent to a display / avoids binary-to-decimal conversion errors / more accurate for representing decimal values ✓

> 提示：BCD常用于数字时钟、计算器等需要逐位显示十进制数字的设备，因为每个十进制数字可以单独存储和显示，无需复杂的二进制转换。

### Question 6

**(a)** Compression type for real-time video streaming:

✓ **Lossy**

Justification:
- Lossy compression provides a much greater reduction in file size than lossless ✓
- This is important for streaming because the data needs to be transmitted in real time / reduces bandwidth requirements ✓
- Some loss of quality is acceptable / not noticeable to the viewer in a video stream ✓

> 提示：实时视频流选择有损压缩（lossy），因为：(1) 压缩率更高 (2) 减少带宽需求以保证实时性 (3) 少量画质损失人眼不易察觉。

**(b)** Impact of changing sampling resolution on accuracy:

- Sampling resolution is the number of bits used to represent each sample ✓
- Increasing the sampling resolution means each sample can be recorded with greater precision / more possible values for each sample ✓
- This means the recorded value is closer to the original analogue value / less quantisation error / more accurate representation of the sound wave ✓

> 提示：采样精度（sampling resolution/bit depth）= 每个采样点用多少位表示。位数越多 → 每个采样值越精确 → 量化误差越小 → 录音越准确。

**(c)** Estimate file size of bitmap image:

Working:
- Number of pixels = 2048 × 1024 = 2,097,152 pixels ✓
- File size in bits = 2,097,152 × 10 = 20,971,520 bits
- File size in bytes = 20,971,520 / 8 = 2,621,440 bytes
- File size in MiB = 2,621,440 / (1024 × 1024) = 2,621,440 / 1,048,576 = **2.5 MiB** ✓

> 提示：文件大小 = 像素数 × 颜色深度（位）。记得除以8转换为字节，再除以1024²转换为MiB。

---

## 2022 Oct/Nov (9618/12)

### Question 2

**(a)(i)** Convert two's complement 10010110 to denary:

- MSB = 1, so the number is negative
- 10010110: -128 + 16 + 4 + 2 = -128 + 22 = **-106**

✓ **-106**

> 提示：补码转十进制：最高位权重为 -128（对于8位），其余位正常计算，然后求和。

**(a)(ii)** Convert unsigned binary 10010110 to hexadecimal:

- Split into nibbles: 1001 | 0110
- 1001 = 9, 0110 = 6

✓ **96**

> 提示：二进制转十六进制：每4位一组，分别转换。

**(a)(iii)** Convert unsigned binary 10010101 to BCD:

Working:
- First convert binary to denary: 10010101 = 128 + 16 + 4 + 1 = **149** ✓
- Convert each digit to 4-bit BCD:
  - 1 = 0001
  - 4 = 0100
  - 9 = 1001
- BCD: **0001 0100 1001** ✓

> 提示：先把二进制转成十进制（149），再把每个十进制数字转成4位BCD。

**(b)** Binary addition: 10001100 + 01000110

```
  10001100
+ 01000110
----------
  11010010  ✓
```

> 提示：二进制加法规则：0+0=0, 0+1=1, 1+1=10（进位），1+1+1=11（进位）。

### Question 8

**(a)** Effect on image file size:

| Action | Effect |
|--------|--------|
| Change colour depth from 24 to 16 bits per pixel | **Decreases** ✓ |
| Change screen resolution to 1366 × 768 pixels | **No change** ✓ |
| Change rectangle colour from black to red | **No change** |

> 提示：改变颜色深度会改变文件大小。改变屏幕分辨率只影响显示，不影响图像文件本身。改变颜色不影响文件大小（每个像素仍占同样的位数）。

**(b)** Two benefits of vector graphics over bitmap:

- Vector graphics can be resized / scaled without loss of quality / resolution ✓
- Vector graphic files are generally smaller in file size (for simple images / drawings) ✓

Other valid points:
- Individual objects / elements can be edited separately ✓
- Vector graphics do not become pixelated when enlarged ✓

> 提示：矢量图优点：(1) 可无损缩放 (2) 文件通常更小 (3) 可以单独编辑各个图形对象。

**(c)(i)** RLE compression:

Row 1 (decompress): 2AB 2FF 11D 167
- ✓ **AB AB FF FF 1D 67**

Row 2 (compress): 32 32 80 81 81
- ✓ **232 180 281**

> 提示：RLE格式：频率+数据。2AB = AB重复2次。压缩时统计连续相同值的个数。

**(c)(ii)** Why lossless compression is more appropriate than lossy for a text file:

- Lossless compression allows the original data to be perfectly reconstructed / no data is lost ✓
- Text files require every character to be preserved exactly / losing or changing any characters would alter the meaning of the text / make it unreadable / corrupt the data ✓

> 提示：文本文件必须用无损压缩，因为每个字符都必须完整保留——丢失任何数据都会改变文本含义或使其不可读。

### Question 6(b) (partial - sound recording)

**(i)** Effect of increasing sampling rate on accuracy:

- A higher sampling rate means more samples are taken per second ✓
- This means the sound wave is sampled more frequently / at shorter intervals, so the digital recording is a closer approximation to the original analogue sound wave / more accurate ✓

> 提示：采样率（sampling rate）越高 → 每秒取样次数越多 → 数字录音越接近原始模拟声波 → 越准确。

**(ii)** Effect of decreasing sampling resolution on file size:

- Decreasing sampling resolution means fewer bits are used to store each sample ✓
- Therefore each sample takes up less storage space, resulting in a smaller file size ✓

> 提示：采样精度降低 → 每个采样点用更少的位 → 文件更小。

---

## 2021 May/June (9618/12)

### Question 6

**(a)** Number of characters:

- ASCII: ✓ **128** characters (uses 7 bits)
- Extended ASCII: ✓ **256** characters (uses 8 bits)

> 提示：ASCII用7位表示128个字符，扩展ASCII用8位表示256个字符。

**(b)** How 'HOUSE' is represented in ASCII:

- Each character in the word is represented by a unique binary code / numeric value ✓
- For example, H has one code, O has another code, etc. Each character is stored as a binary number (typically 7 or 8 bits) and the codes are stored in sequence ✓

> 提示：每个字符对应一个唯一的ASCII码值（二进制数），字符按顺序存储。例如 H=72, O=79, U=85, S=83, E=69。

**(c)(i)** Hexadecimal value for Unicode character '1' (denary 49):

- 49 ÷ 16 = 3 remainder 1
- ✓ **31**

> 提示：49 = 3×16 + 1，所以十六进制是31。

**(c)(ii)** Denary value for Unicode character '5':

- '1' = 49, so '2' = 50, '3' = 51, '4' = 52, '5' = 53
- ✓ **53**

> 提示：字符'0'-'9'的ASCII/Unicode值是连续的。'1'=49，所以'5'=49+4=53。
