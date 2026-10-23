# Unpacket


**Unpacket** is a pure-Python reverse-engineering tool that decrypts Cisco Packet Tracer (`.pkt`) files and converts them into their original XML representation.


The project reimplements the complete proprietary cryptographic and obfuscation pipeline used by Packet Tracer, allowing offline analysis of lab files without relying on the official application.


It is intended for security researchers, reverse engineers, and network analysts who want to inspect, diff, or version-control Packet Tracer topologies at a structural level.


## Features


- **Pure Python, No External Dependencies**


    No OpenSSL, no PyCrypto, no third-party crypto libraries.
- **Full Cryptographic Stack Reimplementation**


    Twofish block cipher (128-bit)


    CMAC (OMAC) authentication


    CTR mode counter engine


    EAX authenticated encryption (AEAD)
- **Proprietary Obfuscation Handling**


    Stage-1 reverse/XOR transformation


    Stage-2 positional XOR mask
- **Qt Compression Support**


    Automatic qCompress / zlib decompression
- **Command Line Interface**


Simple CLI for `.pkt → .xml` conversion (and reverse in `repacket`)

## Installation


Clone the repository and ensure Python >= 3.8 is available:


```bash
git clone https://github.com/Punkcake21/Unpacket.git
cd Unpacket

```

No additional packages are required.


## Usage


### Decrypt .pkt to .xml


```bash
python3 unpacket.py lab.pkt

```

Output will be written as:


```text
lab.xml
```

Custom output path:


```bash
python3 unpacket.py lab.pkt -o decrypted.xml
```

### Repack .xml to .pkt


```bash
python3 repacket.py lab.xml
```

Optional output file:


```bash
python3 repacket.py lab.xml -o rebuilt.pkt
```

## Command Line Options


### Unpacket


| Option | Description |
| ---- | ---- |
| input_file | Input .pkt file |
| -o, --output | Output XML path |
| -h, --help | Show help |


### Repacket


| Option | Description |
| ---- | ---- |
| input_file | Input .xml file |
| -o, --output | Output .pkt path |
| -h, --help | Show help |


## Cryptographic Pipeline


Packet Tracer files use a layered protection scheme:


1. **Stage-1 Obfuscation**
  Reverse order + positional XOR mask.
2. **Authenticated Decryption**
Twofish in EAX mode:

  - CMAC used for OMAC(0/1/2)
  - CTR keystream seeded with nonce MAC
  - Tag verification (AEAD integrity)
3. **Stage-2 Deobfuscation**
  Secondary XOR with decreasing counter.
4. **Qt Compression Layer**
  zlib stream with big-endian length prefix (`qCompress` format).

The final output is a valid XML topology file identical to the one used internally by Packet Tracer.


## Legal Notice


This software is provided for **educational, research, and interoperability purposes only**.


Cisco Packet Tracer and all related trademarks are property of Cisco Systems, Inc.
This project is not affiliated with or endorsed by Cisco.


## License


MIT License
