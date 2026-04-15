# Chapter 6: Security, Privacy & Data Integrity - Homework Answers

> Total: 58 marks

---

## Question 1 [6 marks]

**(a)** Explain the difference between **symmetric encryption** and **asymmetric encryption**. [4 marks]

**Answer:**

**Symmetric encryption:**
✓ Uses a single shared secret key for both encryption and decryption
✓ Both the sender and recipient must possess the same key; the key must be securely shared between them before communication can take place

**Asymmetric encryption:**
✓ Uses a pair of mathematically related keys — a public key and a private key
✓ Data encrypted with the public key can only be decrypted with the corresponding private key (and vice versa); the public key can be freely distributed, while the private key is kept secret by its owner

**(b)** Give **one** situation where asymmetric encryption would be preferred. Justify your answer. [2 marks]

**Answer:**

✓ Asymmetric encryption is preferred when two parties need to communicate securely over the internet without having previously shared a secret key — e.g. online shopping / e-commerce transactions
✓ Justification: There is no need to securely exchange a shared key beforehand; the recipient simply publishes their public key, and anyone can use it to encrypt messages that only the recipient can decrypt with their private key

---

## Question 2 [4 marks]

**(a)** Describe what a firewall does. [2 marks]

**Answer:**

✓ A firewall monitors and filters incoming and outgoing network traffic based on a set of predefined security rules
✓ It acts as a barrier between a trusted internal network and untrusted external networks (e.g. the internet), blocking unauthorised access while allowing legitimate traffic to pass through

**(b)** Explain **two** limitations of using only a firewall for network security. [2 marks]

**Answer:**

✓ A firewall cannot protect against threats that originate from inside the network (e.g. a disgruntled employee or malware introduced via a USB drive)
✓ A firewall cannot detect or prevent all types of malware — e.g. malware hidden within encrypted traffic or within email attachments that pass through permitted ports may not be detected

---

## Question 3 [6 marks]

**(a)** Explain what is meant by **authentication**. [1 mark]

**Answer:**

✓ Authentication is the process of verifying/confirming the identity of a user, device, or system before granting access to resources

**(b)** Describe **three** different methods of authentication. [3 marks]

**Answer:**

✓ **Something you know** (knowledge-based) — e.g. the bank requires the customer to enter a password or PIN to log in to their online banking account
✓ **Something you have** (possession-based) — e.g. the bank sends a one-time passcode (OTP) to the customer's registered mobile phone, or provides a physical security token/card reader that generates a code
✓ **Something you are** (biometric-based) — e.g. the bank's mobile app uses fingerprint recognition or facial recognition to verify the customer's identity

**(c)** Explain why **two-factor authentication** is more secure than a single method. [2 marks]

**Answer:**

✓ Two-factor authentication (2FA) requires the user to provide evidence from two different categories (e.g. something they know AND something they have), so even if one factor is compromised (e.g. a password is stolen), the attacker still cannot gain access without the second factor
✓ This significantly reduces the risk of unauthorised access because an attacker would need to compromise two independent authentication methods simultaneously, which is much more difficult

---

## Question 4 [8 marks]

| Type of malware | Description | How it spreads/operates |
|----------------|-------------|------------------------|
| Virus | ✓ A piece of malicious code that attaches itself to a legitimate program or file and executes when the host program is run | ✓ Spreads when infected files are shared between users (e.g. via email attachments, USB drives, file downloads); requires user action to activate by running the infected program |
| Worm | ✓ A standalone malicious program that replicates itself to spread to other computers without needing to attach to a host program | ✓ Spreads automatically across networks by exploiting security vulnerabilities in operating systems or software; does not require user action to propagate |
| Trojan horse | ✓ Malware that is disguised as legitimate or useful software, tricking users into installing it | ✓ Does not self-replicate; relies on users being deceived into downloading and running it; once installed, it may open a backdoor, steal data, or allow remote control of the system |
| Ransomware | ✓ Malware that encrypts the victim's files or locks them out of their system, then demands a ransom payment (often in cryptocurrency) in exchange for the decryption key | ✓ Often spreads via phishing emails with malicious attachments or links, or through drive-by downloads from compromised websites; once executed, it rapidly encrypts files on the local system and may spread to network drives |

---

## Question 5 [6 marks]

**(a)** Identify the type of cyber attack described above. [1 mark]

**Answer:**

✓ Phishing

**(b)** Explain the difference between **phishing** and **pharming**. [4 marks]

**Answer:**

**Phishing:**
✓ A social engineering attack where the attacker sends fraudulent communications (typically emails) that appear to come from a trusted source
✓ The aim is to trick the victim into clicking a malicious link and entering sensitive information (e.g. login credentials, credit card details) on a fake website

**Pharming:**
✓ An attack that redirects a legitimate website's traffic to a fake/fraudulent website, typically by modifying DNS settings or poisoning the DNS cache
✓ The user types the correct website address but is unknowingly redirected to a fake site that looks identical; unlike phishing, the user does not need to click a link — the redirection happens automatically

**(c)** State **one** method of social engineering other than phishing and pharming. [1 mark]

**Answer:**

✓ Pretexting / shoulder surfing / baiting / tailgating / vishing (voice phishing) — e.g. an attacker telephones a victim while pretending to be a bank employee and persuades them to reveal their account details

---

## Question 6 [6 marks]

**(a)** Explain the difference between **verification** and **validation**. [2 marks]

**Answer:**

✓ **Verification** is the process of checking that data has been accurately transferred/copied from one source to another — e.g. checking that data entered into a system matches the original source document (double entry, screen/visual check)
✓ **Validation** is the process of checking that data entered is reasonable, sensible, and conforms to specified rules — it does not guarantee that the data is correct, only that it is plausible (e.g. a range check, type check)

**(b)** Validation checks: [4 marks]

| Data item | Validation check | How it works |
|-----------|-----------------|--------------|
| Student age (must be between 11 and 18) | ✓ Range check | Checks that the value entered falls within a specified range (11 to 18 inclusive); rejects any value below 11 or above 18 |
| Student email address | ✓ Format check | Checks that the data matches a predefined pattern/format — e.g. must contain an "@" symbol followed by a domain name with a "." (such as name@domain.com) |
| Student name (must not be left empty) | ✓ Presence check | Checks that a value has been entered into the field; rejects the entry if the field is left blank/empty |
| Student ID (a 6-digit code ending in a calculated digit) | ✓ Check digit | The last digit is calculated from the other digits using a predefined algorithm; when the ID is entered, the check digit is recalculated and compared to the one entered — if they do not match, the data is rejected |

---

## Question 7 [6 marks]

**(a)** Describe how a **digital signature** is created and verified. [4 marks]

**Answer:**

**Creation:**
✓ The sender creates a hash/message digest of the original document/message using a hashing algorithm
✓ The sender encrypts this hash using their own private key — this encrypted hash is the digital signature, which is sent along with the original message

**Verification:**
✓ The recipient decrypts the digital signature using the sender's public key to obtain the original hash
✓ The recipient independently hashes the received message using the same hashing algorithm and compares the two hashes — if they match, the message has not been tampered with and the sender's identity is confirmed

**(b)** Explain the purpose of a **digital certificate** and what information it contains. [2 marks]

**Answer:**

✓ A digital certificate is an electronic document issued by a trusted Certificate Authority (CA) that verifies the identity of the holder and binds their identity to their public key, enabling trust in online communications
✓ It contains: the owner's name/identity, the owner's public key, the issuing Certificate Authority's name, the certificate's serial number, the expiry date, and the digital signature of the CA

---

## Question 8 [4 marks]

Describe **four** methods of access control.

**Answer:**

✓ **User IDs and passwords** — each user is assigned a unique username and password; they must enter valid credentials to log in and access the system
✓ **Access control lists (ACLs) / file permissions** — each resource (file, folder, database) has an associated list specifying which users or groups have what level of access (e.g. read, write, execute, no access)
✓ **User privilege levels / user groups** — users are assigned to different groups (e.g. administrator, standard user, guest), each with different levels of access rights; this ensures users can only access resources appropriate to their role
✓ **Physical access controls** — using locked doors, key cards, biometric scanners, or security guards to restrict physical access to servers and computer rooms

---

## Question 9 [6 marks]

**(a)** Explain **two** threats to the **privacy** of the patient data. [2 marks]

**Answer:**

✓ **Hacking / unauthorised access** — an external attacker could exploit vulnerabilities in the hospital's network to gain access to patient records and steal sensitive personal/medical information
✓ **Insider threat** — a hospital employee with legitimate access could intentionally or accidentally view, copy, or disclose patient data to unauthorised individuals

**(b)** Describe **two** measures the hospital could take to maintain the **integrity** of the data. [2 marks]

**Answer:**

✓ **Regular backups** — the hospital should perform regular (e.g. daily) backups of the database so that if data is corrupted or accidentally modified, it can be restored to a correct previous state
✓ **Access controls with audit logs** — restricting write/edit access to authorised staff only and maintaining logs of all changes made to records (who changed what and when), so that any unauthorised or accidental modifications can be detected and reversed

**(c)** Explain why **spyware** is a particular threat to patient data privacy and how it can be prevented. [2 marks]

**Answer:**

✓ Spyware secretly monitors and records user activity (e.g. keystrokes, screen content, files accessed) and transmits this data to an attacker; in a hospital setting, this could expose sensitive patient records, login credentials, and confidential medical information without anyone being aware
✓ Prevention: install and regularly update anti-spyware/anti-malware software on all hospital computers, keep operating systems and applications patched with the latest security updates, and educate staff not to download software from untrusted sources or click on suspicious links

---

## Question 10 [6 marks]

**Discussion of security measures for a business handling online payments:**

**Encryption:**
✓ The business should use SSL/TLS (HTTPS) to encrypt all data transmitted between the customer's browser and the server, ensuring that credit card details cannot be intercepted and read by attackers during transmission
✓ Sensitive data stored on the server (e.g. customer payment details) should be encrypted at rest using strong encryption algorithms, so that even if an attacker gains access to the database, the data is unreadable without the decryption key

**Authentication:**
✓ The business should implement strong authentication for customer accounts — e.g. requiring strong passwords and offering two-factor authentication (2FA) to verify customer identity
✓ The server should use a digital certificate issued by a trusted Certificate Authority to authenticate itself to customers, proving that the website is genuine and not a fraudulent copy

**Access control:**
✓ The business should restrict access to customer data to authorised employees only, using role-based access control (RBAC) so that staff can only access the data they need for their job
✓ Administrative access to the server and database should be protected with strong credentials, audit logging, and physical security measures; regular security audits should be conducted to identify and address vulnerabilities

---

**--- END OF ANSWERS ---**
