# Chapter 6: Security, Privacy & Data Integrity - Paper 1 Mark Scheme Answers

> Topics: Encryption, security threats (phishing, malware, hacking), firewalls, authentication, data verification/validation, digital signatures, data integrity, data privacy

---

## 2024 May/June (9618/12)

### Question 3(a) (Security measures)

(i) Identify one other security measure that helps to protect the server from hackers. Describe how it works. [3 marks]

✓ **Firewall** (identification - 1 mark)
✓ A firewall monitors/filters incoming and outgoing network traffic based on predetermined security rules
✓ It examines data packets and blocks unauthorised access / suspicious traffic from reaching the server, while allowing legitimate traffic through

> 提示：防火墙 - 监控和过滤网络流量，根据安全规则阻止未授权访问，允许合法流量通过

*Alternative acceptable answers: intrusion detection system, access control lists, etc.*

---

(ii) Identify one security measure that helps to protect the data when it is being transmitted. Describe how it works. [3 marks]

✓ **Encryption** (identification - 1 mark)
✓ The data is converted from plaintext into ciphertext using an encryption algorithm and a key before transmission
✓ Only the intended recipient who has the correct decryption key can convert the ciphertext back into readable plaintext, so even if the data is intercepted it cannot be read

> 提示：加密 - 用加密算法和密钥将明文转为密文传输，只有拥有解密密钥的接收方才能还原数据；即使被截获也无法读取

*Alternative: SSL/TLS, VPN -- with appropriate description*

---

## 2024 Oct/Nov (9618/12)

### Question 4(c) (Security during email transfer)

- Security method: ✓ **Encryption**
- Explanation:

✓ The program code file is encrypted before being sent by email, converting the data into ciphertext using an encryption algorithm and key
✓ If the email is intercepted during transmission, the encrypted data cannot be read/understood without the decryption key
✓ Only the intended recipient with the correct key can decrypt and access the original program code

> 提示：加密保护邮件传输 - 发送前加密成密文，截获也无法读取，只有持有密钥的接收方能解密

*1 mark for identification + 2 marks for explanation = 3 marks*

*Alternative acceptable: digital signature (verifies sender identity and ensures data has not been tampered with)*

---

## 2023 Oct/Nov (9618/12)

### Question 5

(a) State the meaning of privacy of data. [1 mark]

✓ Privacy of data means that data is only accessible to / can only be viewed by those who are authorised to access it / data is used only for the purpose for which it was collected

> 提示：数据隐私 = 数据只能被授权人员访问/查看，只用于收集时的目的

---

(b) State the meaning of integrity of data. [1 mark]

✓ Integrity of data means that the data is accurate / correct / complete / up-to-date / has not been altered or corrupted (either accidentally or deliberately)

> 提示：数据完整性 = 数据准确、正确、完整、未被意外或故意篡改/损坏

---

(c) Describe the following threats to a computer system. [4 marks]

**Phishing email:**
✓ A fraudulent email that appears to come from a legitimate/trusted source (e.g. a bank)
✓ The email attempts to trick the user into revealing personal/sensitive information (such as passwords, bank details) or clicking a malicious link that installs malware

> 提示：钓鱼邮件 - 伪装成合法来源的欺诈邮件，诱骗用户泄露个人信息或点击恶意链接

**Spyware:**
✓ Malicious software that is installed on a computer without the user's knowledge/consent
✓ It secretly monitors/records the user's activity (e.g. keystrokes, browsing history, personal data) and sends this information to a third party

> 提示：间谍软件 - 未经用户同意安装，秘密监控用户活动（如键盘记录、浏览历史），将信息发送给第三方

*2 marks per threat = 4 marks*

---

### Question 2(b) (Database security)
Describe other methods that a DBMS can use to improve the security of a database. [4 marks]

✓ **Access rights / access levels** -- different users are given different levels of access (e.g. read-only, read-write, no access) to different parts of the database, limiting what data they can view or modify
✓ **Encryption** -- data stored in the database is encrypted so that even if unauthorised access occurs, the data cannot be read without the decryption key
✓ **Database views** -- virtual tables are created that show only certain fields/records to specific users, hiding sensitive data from unauthorised users
✓ **Audit trail / logging** -- the DBMS records all actions performed on the database (who accessed what, when, and what changes were made) to detect and investigate unauthorised activity
✓ **Backup and recovery** -- regular backups are made so data can be restored if it is lost, corrupted, or compromised

> 提示：DBMS安全方法 - 访问权限控制、数据加密、数据库视图（限制可见字段）、审计日志、备份恢复

*Any 4 points for 4 marks (1 mark per described method)*

---

## 2022 Oct/Nov (9618/12)

### Question 4

(a) State the difference between data verification and data validation. [1 mark]

✓ **Verification** checks that data has been accurately copied/transferred from one source to another (e.g. data entry matches the original), while **validation** checks that data is reasonable / sensible / within acceptable limits / of the correct type before it is accepted by the system

> 提示：验证（Verification）= 检查数据是否准确复制/转录；校验（Validation）= 检查数据是否合理、符合规则

---

(b) Describe how a checksum is used to detect errors during data transmission. [3 marks]

✓ Before transmission, a mathematical calculation / algorithm is performed on the data to produce a checksum value
✓ The checksum value is sent/transmitted along with the data to the receiving end
✓ The receiving end performs the same calculation on the received data and compares its calculated checksum with the transmitted checksum
✓ If the two values do not match, an error has occurred during transmission and the data is requested to be re-sent

> 提示：校验和 - 发送前计算校验值并随数据发送；接收方重新计算并比较；不匹配则说明传输出错，请求重发

*Any 3 points for 3 marks*

---

(c) Describe two other validation methods that can be used to validate non-numeric data. [2 marks]

✓ **Length check** -- checks that the data entered has the correct number of characters / is within an acceptable length range (e.g. a password must be at least 8 characters)
✓ **Presence check** -- checks that data has been entered into a field and the field has not been left empty *(note: already given in question, do not use)*
✓ **Format check / input mask** -- checks that the data follows a specific pattern/format (e.g. an email address must contain "@" and a domain)
✓ **Lookup check / list check** -- checks that the data entered matches one of a set of predefined acceptable values in a list

> 提示：非数字数据校验 - 长度检查（字符数是否正确）、格式检查（是否符合特定模式如邮箱格式）、查找检查（是否在预定义列表中）

*Any 2 different methods for 2 marks*

---

### Question 6(a) (Security)

(i) Explain how a digital signature ensures the email is authentic. [2 marks]

✓ The sender creates a hash/digest of the message and encrypts it using their private key to create the digital signature
✓ The recipient decrypts the digital signature using the sender's public key and compares the resulting hash with a newly computed hash of the received message -- if they match, the email is authentic (it came from the claimed sender and has not been tampered with)

> 提示：数字签名 - 发送方用私钥加密消息摘要（哈希值）；接收方用发送方公钥解密并比较哈希值，匹配则证明邮件真实且未被篡改

---

(ii) Describe how a firewall protects the data on the computer. [3 marks]

✓ A firewall can be software-based or hardware-based and is positioned between the computer/network and the internet
✓ It monitors/examines all incoming and outgoing network traffic / data packets
✓ It applies a set of predefined rules to determine whether to allow or block specific traffic
✓ It blocks unauthorised access attempts / prevents hackers from gaining access to the computer / blocks suspicious or malicious data packets

> 提示：防火墙 - 位于计算机和网络之间，监控所有进出流量，根据预定规则允许或阻止数据包，防止未授权访问

*Any 3 points for 3 marks*

---

## 2021 May/June (9618/12)

### Question 8

(a) Describe the difference between the security and privacy of data. [2 marks]

✓ **Security** of data refers to the measures/methods taken to protect data from unauthorised access, theft, corruption or loss (e.g. firewalls, encryption, passwords)
✓ **Privacy** of data refers to ensuring that personal/sensitive data is only accessible to authorised individuals and is used only for its intended purpose / relates to the rights of individuals regarding their personal data

> 提示：安全性 = 保护数据免受未授权访问/盗窃/损坏的措施；隐私性 = 确保个人数据仅被授权人访问并仅用于既定目的

---

(b) Identify one other software-based measure that could be used to restrict access to data. [1 mark]

✓ Firewall
✓ Encryption
✓ Anti-malware / anti-virus software
✓ Access control lists / access rights

> 提示：其他软件安全措施 - 防火墙、加密、杀毒软件、访问控制列表（任选一个）

*Any 1 for 1 mark*

---

(c) Identify two threats to the data that are posed by networks and the internet. [2 marks]

✓ Hacking / unauthorised access
✓ Malware / viruses / spyware / ransomware
✓ Phishing attacks
✓ Denial of service (DoS) attacks
✓ Man-in-the-middle attacks / data interception / eavesdropping

> 提示：网络威胁 - 黑客入侵、恶意软件/病毒、钓鱼攻击、拒绝服务攻击、数据拦截（任选两个）

*Any 2 for 2 marks*
