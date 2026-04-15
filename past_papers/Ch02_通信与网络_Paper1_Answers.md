# Chapter 2: Communication & Networks - Paper 1 Answers

> Topics: Networks (LAN/WAN), internet structure, protocols, IP addressing, network topologies, data transmission

---

## 2024 May/June (9618/12)

### Question 3(b)(c) (Network components)

**(b)** Two characteristics of a thin-client and how used:

| Characteristic | How used in this software |
|---|---|
| Processing is carried out on the server / minimal local processing ✓ | The marking / annotation of exam papers is processed on the server, not on the marker's local device ✓ |
| Data is stored on the server / minimal local storage ✓ | The digitised exam papers and marks are stored centrally on the server, not on the marker's device ✓ |

Other valid characteristics:
- The client device requires less powerful hardware ✓
- Software / applications are run from the server ✓
- Requires a network connection to function ✓

> 提示：瘦客户端（thin-client）特点：(1) 处理在服务器端完成 (2) 数据存储在服务器端 (3) 客户端硬件要求低 (4) 需要网络连接。

**(c)(i)** Role of routers in internet data transmission:

- Routers direct / forward data packets between networks / from source to destination ✓
- Routers examine the destination IP address in each packet and use routing tables to determine the best / most efficient path / next hop for the packet ✓

> 提示：路由器（router）根据目标IP地址和路由表，将数据包沿最佳路径转发到下一个网络节点。

**(c)(ii)** Role of PSTN in internet data transmission:

- The PSTN provides the physical infrastructure / cabling / telephone lines through which internet data can be transmitted ✓
- Data from a computer is converted (by a modem) into a form suitable for transmission over the telephone network / allows connection to an ISP ✓

> 提示：PSTN（公共交换电话网络）提供物理线路基础设施，数据通过调制解调器（modem）转换后可在电话线上传输。

---

## 2023 May/June (9618/12)

### Question 1

**(a)** Two benefits of connecting computers to a LAN:

- Users can share resources such as printers, scanners, and storage devices ✓
- Users can share files / data easily between computers on the network ✓

Other valid points:
- Users can share an internet connection ✓
- Software can be installed / managed centrally ✓
- Users can communicate with each other (e.g. email, messaging) ✓

> 提示：LAN的好处：共享资源（打印机等）、共享文件、共享网络连接、集中管理软件。

**(b)** Two characteristics of a LAN:

- Covers a small geographical area / contained within a single building or site ✓
- The hardware / cabling / infrastructure is owned by the organisation ✓

Other valid points:
- Typically uses Ethernet or Wi-Fi for connectivity ✓
- Higher data transfer rates compared to WAN ✓

> 提示：LAN的特征：(1) 覆盖小范围地理区域（一栋建筑/一个场所）(2) 硬件由组织自己拥有/管理。

**(c)** Star topology diagram:

The diagram should show:
- A central switch / hub in the middle ✓
- The server and four computers each connected directly to the central switch with individual cables ✓

(Note: All devices connect to the central device; no device connects directly to another device.)

> 提示：星型拓扑：所有设备（服务器和电脑）都通过独立的线缆连接到中心交换机/集线器，设备之间不直接相连。

**(d)** Description of Ethernet:

- Ethernet is a set of protocols / standards for connecting devices in a network ✓
- It defines how data is formatted into frames for transmission ✓
- It uses CSMA/CD (Carrier Sense Multiple Access with Collision Detection) to manage access to the transmission medium / to handle collisions ✓

> 提示：以太网（Ethernet）是一组网络协议/标准，定义了数据帧格式和传输规则，使用CSMA/CD来管理网络访问和处理冲突。

**(e)** Description of thick-client model:

- In a thick-client model, most of the processing / data processing is carried out on the client computer / local machine ✓
- The client stores data and applications locally / does not depend heavily on the server for processing ✓

> 提示：厚客户端（thick-client）：大部分处理在本地客户端完成，数据和应用程序存储在本地，对服务器依赖较少。

---

## 2023 Oct/Nov (9618/12)

### Question 7

**(a)** Why 192.168.3.2 is not an IPv6 address:

- IPv6 addresses use 128 bits / are much longer than this address ✓
- IPv6 addresses are written in hexadecimal and consist of 8 groups of 4 hex digits separated by colons (e.g. 2001:0db8:...) / this address uses decimal notation with dots which is the format for IPv4 ✓

> 提示：IPv6用128位，格式为8组4位十六进制数用冒号分隔。而192.168.3.2是IPv4格式（十进制+点分隔，32位）。

**(b)(i)** Star topology diagram of the LAN:

The diagram should show:
- The router as the central device ✓
- The server and two laptops each connected directly to the router with individual connections ✓

> 提示：画星型拓扑图：路由器在中心，服务器和两台笔记本分别用独立线缆连到路由器。

**(b)(ii)** How data is transmitted between two laptops in the LAN:

- Data is sent from the source laptop to the central device (router/switch) ✓
- The central device reads the destination address (MAC address) and forwards the data to the destination laptop only ✓

> 提示：数据从源笔记本发送到中心设备（路由器/交换机），中心设备根据目标MAC地址将数据转发给目标笔记本。

**(b)(iii)** Two other reasons why subnetting is used:

Reason 1:
- Description: Subnetting improves network security ✓
- Explanation: Different subnets can have different access permissions / traffic between subnets can be controlled / filtered, preventing unauthorised access to sensitive areas of the network ✓

Reason 2:
- Description: Subnetting reduces network traffic / congestion ✓
- Explanation: Broadcast traffic is contained within each subnet rather than being sent to the entire network, improving performance ✓

Other valid reasons:
- Makes the network easier to manage / troubleshoot ✓
- Allows more efficient use of IP addresses ✓

> 提示：子网划分（subnetting）的好处：(1) 提高安全性（隔离不同区域）(2) 减少网络拥堵（广播流量限制在子网内）(3) 便于管理 (4) 更高效地使用IP地址。

**(c)** Three tasks performed by CSMA/CD:

- Before transmitting, the device listens / checks if the channel / medium is idle / free ✓
- If a collision is detected, both devices stop transmitting and send a jam signal ✓
- Each device waits a random amount of time before attempting to retransmit ✓

> 提示：CSMA/CD三步：(1) 发送前先监听信道是否空闲 (2) 检测到冲突则停止发送并发出干扰信号（jam signal）(3) 等待随机时间后重新尝试发送。

**(d)** IP address types and descriptions:

| Type | Description |
|---|---|
| **Public IP** | An IP address that is visible to / can be accessed by any device on the internet ✓ |
| **Static IP** | An IP address that does not change / remains the same each time the device connects to the network ✓ |
| **Private IP** | An IP address that is only visible / accessible to devices within the local area network (LAN) ✓ |
| **Dynamic IP** | An IP address that is allocated by a DHCP server / changes each time the device connects to the network ✓ |

> 提示：公有IP = 互联网上可见。私有IP = 仅局域网内可见。静态IP = 不变。动态IP = 每次连接时由DHCP分配，可能改变。

---

## 2022 Oct/Nov (9618/12)

### Question 10

**(a)** Star topology diagram:

✓ All four computers and the server should be connected to the central switch (each with its own connection). No device connects directly to another device.

> 提示：所有电脑和服务器都连接到中心交换机（switch）。

**(b)(i)** Device to connect the router to:

- ✓ The **switch**
- Reason: The switch is the central device that connects all other devices on the LAN, so connecting the router to the switch gives all devices on the LAN access to the internet ✓

> 提示：路由器连接到交换机，因为交换机是所有设备的中心连接点，这样所有设备都能通过路由器访问互联网。

**(b)(ii)** Role and function of the router:

- The router connects the LAN to the internet / connects two or more different networks ✓
- The router directs / forwards data packets between networks using IP addresses / examines the destination IP address in each packet ✓
- The router uses a routing table to determine the best path / next hop for each packet ✓

> 提示：路由器的功能：(1) 连接LAN和互联网（连接不同网络）(2) 根据目标IP地址转发数据包 (3) 使用路由表确定最佳路径。

---

## 2021 May/June (9618/12)

### Question 5(c)(d) (Cloud computing and IP addresses)

**(c)(i)** Two benefits of storing data using cloud computing:

- Data can be accessed from any location / any device with an internet connection ✓
- The cloud provider manages backups / disaster recovery / data is less likely to be lost ✓

Other valid points:
- Storage capacity can be easily scaled up or down as needed ✓
- No need to purchase / maintain local storage hardware ✓
- Multiple users can collaborate on / access the same data simultaneously ✓

> 提示：云计算存储数据的好处：(1) 随时随地可访问 (2) 提供商负责备份和灾难恢复 (3) 存储容量可弹性扩展 (4) 无需自己维护硬件。

**(c)(ii)** Two drawbacks of using cloud computing:

- Requires a reliable internet connection / no access to data if the internet is unavailable ✓
- Data security / privacy concerns — data is stored on third-party servers and could potentially be accessed by unauthorised users / the provider ✓

Other valid points:
- Ongoing subscription costs may be more expensive over time than local storage ✓
- Less control over data / dependent on the cloud provider's service availability ✓
- Potential latency issues when accessing large files ✓

> 提示：云计算的缺点：(1) 依赖网络连接 (2) 数据安全/隐私担忧 (3) 长期成本可能更高 (4) 对数据控制力较低。

**(d)** Matching IP address types to descriptions:

- **Public IP address** → It is visible to any device on the internet ✓
- **Private IP address** → It is only visible to devices within the Local Area Network (LAN) ✓
- **Dynamic IP address** → A new one is reallocated each time a device connects to the internet ✓
- **Static IP address** → It does not change each time a device connects to the internet ✓

> 提示：公有IP→互联网可见；私有IP→仅LAN内可见；动态IP→每次连接重新分配；静态IP→不变。
