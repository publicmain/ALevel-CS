# Chapter 2: Communication & Networking Technologies - Homework Answers

> 总分：52

---

## Question 1 — Network Types 网络类型 [4 marks]

**(a)** Define the term LAN (Local Area Network). [2 marks]

A LAN is a network that covers a small geographical area ✓, such as a single building or campus, where the hardware and cabling are typically owned and managed by the organisation that uses it ✓.

---

**(b)** Two differences between a LAN and a WAN. [2 marks]

1. A LAN covers a small geographical area (e.g., one building), whereas a WAN covers a large geographical area (e.g., across cities, countries or continents) ✓.
2. A LAN uses infrastructure (cables/hardware) that is owned by the organisation, whereas a WAN uses third-party communication links (e.g., telephone lines, satellite links) that are leased or rented ✓.

---

## Question 2 — Network Topologies 网络拓扑 [6 marks]

**(a)** Star topology diagram. [2 marks]

```
  [Workstation 1]         [Workstation 2]
         \                    /
          \                  /
           [Central Switch]--------[Server]  ✓
          /                  \
         /                    \
  [Workstation 3]         [Workstation 4]
```

✓ All workstations and server connected to a central switch via individual cables. Each device has its own dedicated connection to the central switch.

---

**(b)** Two advantages of star topology over bus topology. [2 marks]

1. If one cable or workstation fails in a star topology, only that device is affected; the rest of the network continues to function. In a bus topology, a break in the main cable brings down the entire network ✓.
2. In a star topology, data collisions are reduced or eliminated because each device has a dedicated connection to the switch, resulting in better performance than a bus topology where all devices share the same cable ✓.

---

**(c)** One disadvantage of star topology over bus topology. [2 marks]

A star topology requires more cabling than a bus topology because each device needs its own individual cable to the central switch ✓. This makes the initial installation more expensive. Additionally, the network is dependent on the central switch -- if the switch fails, the entire network fails ✓.

---

## Question 3 — Client-Server and Peer-to-Peer 客户端-服务器与对等网络 [6 marks]

**(a)** Client-server network model. [2 marks]

In a client-server network, one or more dedicated servers provide services and resources (such as file storage, authentication, email, printing) to the other computers on the network, which act as clients ✓. Clients send requests to the server, and the server processes these requests and sends back responses. The server centrally manages security, user accounts, and shared resources ✓.

---

**(b)** Peer-to-peer network model. [2 marks]

In a peer-to-peer network, all computers (peers) have equal status and there is no dedicated server ✓. Each computer can act as both a client and a server, sharing its own resources (files, printers) directly with other peers on the network. Each computer is responsible for its own security ✓.

---

**(c)** Suitable model for a school with 200 computers. [2 marks]

**Client-server** would be more suitable ✓.

Reason: With 200 users, centralised management of user accounts, access permissions, security policies, file storage, and backups is essential. A client-server model allows administrators to manage all users centrally from the server, which would be impractical in a peer-to-peer network of this size ✓.

---

## Question 4 — Thin Client and Thick Client 瘦客户端与胖客户端 [4 marks]

**(a)** What is meant by a thin client. [2 marks]

A thin client is a computer that has minimal hardware (limited processing power and storage) and depends on a central server to perform most of the data processing ✓. The thin client acts mainly as a terminal for displaying output and sending user input to the server, where applications and data are stored and executed ✓.

---

**(b)** One advantage and one disadvantage of thin clients. [2 marks]

**Advantage:** Thin clients are cheaper to purchase and maintain than thick clients, and software only needs to be installed/updated on the server, reducing IT administration costs across 500 employees ✓.

**Disadvantage:** Thin clients are entirely dependent on the server and network connection. If the server or network fails, employees will be unable to work, as they cannot run applications locally ✓.

---

## Question 5 — Transmission Media and Wireless 传输介质与无线网络 [6 marks]

**(a)(i)** Two advantages of WiFi over Ethernet. [2 marks]

1. WiFi allows devices to connect to the network without the need for physical cables, providing mobility and flexibility for users to move around freely ✓.
2. WiFi is easier and cheaper to set up in an existing building because there is no need to install cabling throughout the building ✓.

---

**(a)(ii)** Two advantages of Ethernet over WiFi. [2 marks]

1. Ethernet generally provides faster and more consistent data transfer speeds than WiFi, with lower latency ✓.
2. Ethernet is more secure because a physical connection is required to access the network, making it harder for unauthorised users to intercept data ✓.

---

**(b)** Why a hospital would use wired Ethernet for critical systems. [2 marks]

Wired Ethernet provides a more reliable and stable connection than WiFi, which is essential for critical medical systems where any interruption could endanger patients ✓. WiFi signals can suffer from interference (from other electronic devices, walls, etc.) and are more vulnerable to security breaches, which is unacceptable for sensitive medical data and life-critical equipment ✓.

---

## Question 6 — The Internet and Infrastructure 互联网基础设施 [6 marks]

**(a)(i)** Role of a Router. [2 marks]

A router is a device that forwards/routes data packets between different networks ✓. It examines the destination IP address in each packet's header and uses routing tables to determine the best path to forward the packet toward its destination ✓.

---

**(a)(ii)** Role of a Gateway. [2 marks]

A gateway is a device (or software) that connects two networks that use different protocols or data formats ✓. It translates data from one protocol to another so that devices on different types of networks can communicate with each other ✓.

---

**(b)** Role of an ISP. [2 marks]

An ISP provides the home user with a connection to the internet, typically through a broadband/fibre/DSL connection ✓. The ISP assigns the user an IP address, routes their data traffic to and from the internet, and may also provide additional services such as email, DNS resolution, and web hosting ✓.

---

## Question 7 — IP Addressing IP地址 [6 marks]

**(a)** What is meant by an IP address. [1 mark]

An IP address is a unique numerical identifier assigned to every device connected to a network, used to identify the device and enable routing of data to/from that device ✓.

---

**(b)** Why IPv6 was introduced. [2 marks]

IPv4 uses 32-bit addresses, providing approximately 4.3 billion (2^32) unique addresses ✓. Due to the rapid growth of internet-connected devices (computers, smartphones, IoT devices), the pool of available IPv4 addresses has been exhausted. IPv6 uses 128-bit addresses, providing a vastly larger address space (2^128 addresses) to accommodate current and future devices ✓.

---

**(c)** Public vs private IP addresses. [3 marks]

A **public IP address** is an address that is globally unique and routable on the internet. It is assigned by the ISP and is used to identify a device or network on the public internet ✓.

A **private IP address** is an address used within a local/internal network (LAN) and is not routable on the public internet ✓.

Public IP addresses are used for devices/routers that need to communicate directly over the internet (e.g., a web server, the external interface of a home router). Private IP addresses are used for devices within an internal network (e.g., computers, printers within a home or office LAN). A NAT (Network Address Translation) device/router translates between private and public addresses to allow internal devices to access the internet ✓.

---

## Question 8 — Protocols 网络协议 [6 marks]

**(a)** Definition of protocol. [1 mark]

A protocol is a set of rules that governs how data is formatted, transmitted, and received during communication between devices on a network ✓.

---

**(b)(i)** HTTP / HTTPS [1 mark]

HTTP (HyperText Transfer Protocol) / HTTPS (HTTP Secure) is used for transferring web pages and web content between a web server and a web browser. HTTPS encrypts the data for secure communication ✓.

---

**(b)(ii)** FTP [1 mark]

FTP (File Transfer Protocol) is used for transferring files between a client and a server across a network ✓.

---

**(b)(iii)** SMTP [1 mark]

SMTP (Simple Mail Transfer Protocol) is used for sending/transmitting email messages from a client to an email server, or between email servers ✓.

---

**(c)** Importance of standardised protocols. [2 marks]

Standardised protocols ensure that hardware and software from different manufacturers can communicate with each other (interoperability) ✓. Without standardised protocols, devices from different vendors would not be able to understand each other's data formats, making it impossible to build a global network like the internet ✓.

---

## Question 9 — Packet Switching and Circuit Switching 分组交换与电路交换 [8 marks]

**(a)** Packet switching. [4 marks]

**Preparation:** The data is divided/split into small units called packets. Each packet is given a header that contains the source and destination IP addresses, the packet sequence number, and other control information ✓.

**Transmission:** Each packet is sent independently across the network. Routers examine the destination address in each packet header and forward it along the best available route at that moment. Different packets from the same message may take different routes through the network ✓.

**Arrival at destination:** Packets may arrive out of order or at different times. At the destination, the packets are reassembled into the correct order using the sequence numbers in their headers ✓. If any packets are missing or corrupted, the destination device can request retransmission of those specific packets ✓.

---

**(b)** Circuit switching. [2 marks]

In circuit switching, a dedicated communication path/circuit is established between the sender and receiver before any data is transmitted ✓. This circuit remains exclusively reserved for the duration of the communication session. All data travels along this same path in order. When the communication is complete, the circuit is released/closed and the resources become available for other connections ✓.

---

**(c)** Advantages comparison. [2 marks]

**Advantage of packet switching over circuit switching:** Packet switching uses the network more efficiently because there is no dedicated line that sits idle during pauses in transmission. Multiple communications can share the same network links simultaneously ✓.

**Advantage of circuit switching over packet switching:** Circuit switching provides a guaranteed, consistent bandwidth/connection with no delay variation (jitter) or packet reordering, making it more suitable for real-time communication such as voice telephone calls ✓.

---

*Cambridge International AS Level Computer Science 9618 - Chapter 2 Homework Answers*
