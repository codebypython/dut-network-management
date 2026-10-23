# 📘 TÀI LIỆU MASTER: HƯỚNG DẪN HOÀN CHỈNH & BẢO VỆ 10/10 LAB DAY 5
## Đề bài: Multi Area OSPF — EIGRP — VLAN Lab (DUT IT Faculty)
> **Giảng viên phụ trách**: Thầy Nguyễn Thế Xuân Ly — Bộ môn Mạng & Truyền thông, Khoa CNTT, Trường Đại học Bách Khoa (DUT)  
> **Môi trường thực hành**: Cisco Packet Tracer 8.2.2  
> **Tệp mô phỏng đi kèm**: [`03_Engineering_Labs_and_Code/Day5/ISP service.pkt`](file:///d:/Development/DUT/courses/03_Company_Network_Management_NMA/03_Engineering_Labs_and_Code/Day5/ISP%20service.pkt)

---

## MỤC LỤC
1. [Phần I: Phân Tích Toàn Diện Yêu Cầu Của Đề Bài](#phần-i-phân-tích-toàn-diện-yêu-cầu-của-đề-bài)
2. [Phần II: Bản Đồ Quy Hoạch IP VLSM Chuẩn Xác](#phần-ii-bản-đồ-quy-hoạch-ip-vlsm-chuẩn-xác)
3. [Phần III: Sơ Đồ Đấu Nối Vật Lý & Cổng Giao Tiếp](#phần-iii-sơ-đồ-đấu-nối-vật-lý--cổng-giao-tiếp)
4. [Phần IV: Kịch Bản Lệnh CLI Triển Khai Toàn Diện (7 Giai Đoạn)](#phần-iv-kịch-bản-lệnh-cli-triển-khai-toàn-diện-7-giai-đoạn)
5. [Phần V: Quy Trình Nghiệm Thu & Kiểm Thử Hộp Trắng (5 Bước)](#phần-v-quy-trình-nghiệm-thu--kiểm-thử-hộp-trắng-5-bước)
6. [Phần VI: Cẩm Nang Vấn Đáp Chuyên Sâu Bảo Vệ Điểm 10/10](#phần-vi-cẩm-nang-vấn-đáp-chuyên-sâu-bảo-vệ-điểm-1010)

---

# PHẦN I: PHÂN TÍCH TOÀN DIỆN YÊU CẦU CỦA ĐỀ BÀI

Bài Lab Day 5 là bài thực hành nâng cao tích hợp đa công nghệ doanh nghiệp (Hybrid Enterprise Network) với độ phức tạp cao nhất trong học phần Mạng máy tính / Quản trị mạng tại DUT. Đề bài đặt ra 6 nhóm yêu cầu kỹ thuật đan xen chặt chẽ:

### 1. Phân bổ địa chỉ IP (VLSM)
- Vùng OSPF: Mạng chính `172.23.0.0/16`.
- Vùng EIGRP: Mạng chính `172.22.0.0/16`.
- 5 cổng Loopback (`lo1` đến `lo5`): Mỗi nhánh yêu cầu **8000 nodes**.
- 2 VLAN (`mars` và `venus`): Mỗi VLAN yêu cầu **4000 nodes**.
- Các đường WAN Point-to-Point nối các Router: Tự quy hoạch subnet `/30` (4 IP, 2 host khả dụng).
- Mạng nối Internet (Neptune ra ISP): Cố định `192.168.0.0/24`.

### 2. Chuyển mạch Layer 2 (VLAN, VTP & Trunking)
- 2 Switch: `Server` (VTP Server) và `Client` (VTP Client).
- VTP Configuration: `domain = planet`, `password = solar`.
- VLAN Database: VLAN 2 (tên `mars`), VLAN 3 (tên `venus`).
- Cấu hình Trunking (chuẩn IEEE 802.1Q) trên các cổng liên kết Switch-Switch và Switch-Router.

### 3. Định tuyến liên VLAN (Inter-VLAN Routing)
- Cấu hình Sub-interfaces (Router-on-a-Stick) trên cả 3 Router: **Earth, Mars, Venus**.
- Cả 3 Router này đều có chân cắm vào hệ thống Switch L2 để cùng tham gia định tuyến cho VLAN 2 và VLAN 3.

### 4. Định tuyến nội bộ lai (Multi-Area OSPF & EIGRP)
- **OSPF Đa vùng**:
  - `Area 0 (Backbone)`: Nằm ở trung tâm kết nối giữa Earth và các Sub-interface VLAN của Mars và Venus.
  - `Area 1`: Chạy giữa Venus và Mecury (kèm Loopback 3 của Venus).
  - `Area 2`: Chạy giữa Mars và Jupiter (kèm Loopback 2 của Mars và Loopback 4 của Jupiter).
  - **Mars** và **Venus** đóng vai trò **ABR (Area Border Router)** liên kết Area 0 với Area 1/2.
- **EIGRP AS 69**:
  - Chạy trên tam giác phía Đông: **Jupiter**, **Mecury**, **Neptune** (kèm Loopback 5 của Mecury).

### 5. Tái phân phối (Redistribution) & Cổng biên Internet (Edge NAT)
- **ASBR (Autonomous System Boundary Router)**: Đặt tại **Jupiter** và **Mecury** (chạy đồng thời OSPF và EIGRP AS 69).
- Tái phân phối 2 chiều (Mutual Redistribution) OSPF $\leftrightarrow$ EIGRP.
- **Cảnh báo cốt tử từ đề bài**: `(beware of default route)` — Yêu cầu kiểm soát độ tin cậy tuyến (Administrative Distance) để chống Routing Loop giữa OSPF External (AD 110) và EIGRP External (AD 170).
- **Edge Router Neptune**:
  - Trỏ Default Route `0.0.0.0/0` ra Gateway ISP (`192.168.0.1`).
  - Cấu hình NAT với IP Public Pool: `192.168.0.11` đến `192.168.0.22/24`.
  - Quảng bá Default Route vào mạng nội bộ EIGRP.

### 6. Tùy chọn xác thực bảo mật (Authentication)
- OSPF Authentication: Sử dụng mã hóa MD5, mật khẩu `cat`.
- EIGRP Authentication: Sử dụng Key-chain `11`, mật khẩu `mouse`.

---

# PHẦN II: BẢN ĐỒ QUY HOẠCH IP VLSM CHUẨN XÁC

### 1. Phép tính độ dài tiền tố (Prefix Length Calculation)
- **8000 nodes/nhánh (Loopback `lo1` - `lo5`)**:
  $$2^h - 2 \ge 8000 \implies 2^{13} = 8192 \implies h = 13 \text{ host bits} \implies \text{Prefix} = 32 - 13 = \mathbf{/19} \quad (\text{Bước nhảy } = 32)$$
  $$\text{Subnet Mask: } \mathbf{255.255.224.0}$$
- **4000 nodes/nhánh (VLAN `mars`, `venus`)**:
  $$2^h - 2 \ge 4000 \implies 2^{12} = 4096 \implies h = 12 \text{ host bits} \implies \text{Prefix} = 32 - 12 = \mathbf{/20} \quad (\text{Bước nhảy } = 16)$$
  $$\text{Subnet Mask: } \mathbf{255.255.240.0}$$
- **Đường WAN Point-to-Point (Serial)**:
  $$\text{Prefix} = \mathbf{/30} \quad (\text{Bước nhảy } = 4) \quad \text{Subnet Mask: } \mathbf{255.255.255.252}$$

---

### 2. Bảng Phân Bổ Chi Tiết Toàn Bộ 12 Subnet

| STT | Vùng Mạng / Giao Thức | Mục Đích Sử Dụng | Network ID | Subnet Mask | Dải IP Khả Dụng (Usable Range) | Broadcast IP |
|:---:|:---|:---|:---|:---|:---|:---|
| **1** | OSPF (172.23.0.0/16) | `lo1` (Router Earth) | `172.23.0.0/19` | 255.255.224.0 | `172.23.0.1` – `172.23.31.254` | `172.23.31.255` |
| **2** | OSPF (172.23.0.0/16) | `lo2` (Router Mars) | `172.23.32.0/19` | 255.255.224.0 | `172.23.32.1` – `172.23.63.254` | `172.23.63.255` |
| **3** | OSPF (172.23.0.0/16) | `lo3` (Router Venus) | `172.23.64.0/19` | 255.255.224.0 | `172.23.64.1` – `172.23.95.254` | `172.23.95.255` |
| **4** | OSPF (172.23.0.0/16) | `lo4` (Router Jupiter) | `172.23.96.0/19` | 255.255.224.0 | `172.23.96.1` – `172.23.127.254` | `172.23.127.255` |
| **5** | OSPF (172.23.0.0/16) | **VLAN 2 (mars)** | `172.23.128.0/20` | 255.255.240.0 | `172.23.128.1` – `172.23.143.254` | `172.23.143.255` |
| **6** | OSPF (172.23.0.0/16) | **VLAN 3 (venus)** | `172.23.144.0/20` | 255.255.240.0 | `172.23.144.1` – `172.23.159.254` | `172.23.159.255` |
| **7** | EIGRP (172.22.0.0/16) | `lo5` (Router Mecury) | `172.22.0.0/19` | 255.255.224.0 | `172.22.0.1` – `172.22.31.254` | `172.22.31.255` |
| **8** | OSPF WAN /30 | Serial Mars $\leftrightarrow$ Jupiter | `172.23.255.0/30` | 255.255.255.252 | `172.23.255.1` (Mars) – `172.23.255.2` (Jup) | `172.23.255.3` |
| **9** | OSPF WAN /30 | Serial Venus $\leftrightarrow$ Mecury | `172.23.255.4/30` | 255.255.255.252 | `172.23.255.5` (Venus) – `172.23.255.6` (Mec) | `172.23.255.7` |
| **10** | EIGRP WAN /30 | Serial Jupiter $\leftrightarrow$ Neptune | `172.22.255.0/30` | 255.255.255.252 | `172.22.255.1` (Jup) – `172.22.255.2` (Nep) | `172.22.255.3` |
| **11** | EIGRP WAN /30 | Serial Mecury $\leftrightarrow$ Neptune | `172.22.255.4/30` | 255.255.255.252 | `172.22.255.5` (Mec) – `172.22.255.6` (Nep) | `172.22.255.7` |
| **12** | ISP External WAN | Neptune $\leftrightarrow$ ISP Gateway | `192.168.0.0/24` | 255.255.255.0 | `192.168.0.1` (ISP) – `192.168.0.10` (Nep) | `192.168.0.255` |

---

# PHẦN III: SƠ ĐỒ ĐẤU NỐI VẬT LÝ & CỔNG GIAO TIẾP

### 1. Phân vùng Chuyển mạch LAN (Cáp thẳng Ethernet)
- **Earth** `Gig0/0` $\longleftrightarrow$ `Fa0/1` **Switch Server** (Trunk)
- **Switch Server** `Fa0/3` $\longleftrightarrow$ `Gig0/0` **Router Mars** (Trunk)
- **Switch Server** `Fa0/2` $\longleftrightarrow$ `Fa0/1` **Switch Client** (Trunk liên Switch)
- **Switch Client** `Fa0/2` $\longleftrightarrow$ `Gig0/0` **Router Venus** (Trunk)
- **Switch Client** `Fa0/10` $\longleftrightarrow$ `FastEthernet0` **PC0** (VLAN 2 `mars`: IP `172.23.128.10/20`, Gateway `172.23.128.1`)

### 2. Phân vùng Định tuyến WAN (Cáp Serial Ziczac - Đỏ)
> **Quy ước đầu cáp DCE/DTE**: Phía đầu có biểu tượng đồng hồ (Clock) là đầu **DCE**, bắt buộc phải cấu hình lệnh `clock rate 64000`. Phía đầu **DTE** chỉ cần cấu hình IP và `no shutdown`.

- **Mars** `Se0/3/0` *(DCE)* $\longleftrightarrow$ `Se0/3/0` *(DTE)* **Jupiter**
- **Venus** `Se0/3/0` *(DCE)* $\longleftrightarrow$ `Se0/3/0` *(DTE)* **Mecury**
- **Neptune** `Se0/3/1` *(DCE)* $\longleftrightarrow$ `Se0/3/1` *(DTE)* **Jupiter**
- **Neptune** `Se0/3/0` *(DCE)* $\longleftrightarrow$ `Se0/3/1` *(DTE)* **Mecury**
- **Neptune** `Gig0/0` $\longleftrightarrow$ **DSL Modem** `Port 1` $\longleftrightarrow$ **DSL Cloud** $\longleftrightarrow$ `Fa0/0` **Router ISP**

### 3. Phân vùng Máy chủ Dịch vụ Internet (Phía sau Router ISP)
- **Router ISP** `Fa0/0/0` (VLAN 69) $\longleftrightarrow$ `Fa0` **Google DNS** (`8.8.8.8/24`, Gateway `8.8.8.9`)
- **Router ISP** `Fa0/0/1` (VLAN 69) $\longleftrightarrow$ `Fa0` **Google Mail** (`8.8.8.10/24`, Gateway `8.8.8.9`)
- **Router ISP** `Fa0/0/2` (VLAN 69) $\longleftrightarrow$ `Fa0` **Web Server** (`8.8.8.11/24`, Gateway `8.8.8.9`)

---

# PHẦN IV: KỊCH BẢN LỆNH CLI TRIỂN KHAI TOÀN DIỆN

### GIAI ĐOẠN 1: CẤU HÌNH LAYER 2 (SWITCHES)

#### 1. Trên Switch `Server`
```cisco
enable
configure terminal
hostname Server

! Khởi tạo VTP Server
vtp domain planet
vtp password solar
vtp mode server

! Khai báo VLANs
vlan 2
 name mars
vlan 3
 name venus
exit

! Bật Trunking chuẩn 802.1Q
interface range FastEthernet0/1 - 3
 switchport mode trunk
 switchport trunk allowed vlan 1,2,3
 no shutdown
exit
```

#### 2. Trên Switch `Client`
```cisco
enable
configure terminal
hostname Client

! Khởi tạo VTP Client
vtp domain planet
vtp password solar
vtp mode client

! Bật Trunking nối Switch Server và Router Venus
interface range FastEthernet0/1 - 2
 switchport mode trunk
 switchport trunk allowed vlan 1,2,3
 no shutdown
exit

! Gán cổng Fa0/10 cho PC0 kiểm thử (thuộc VLAN 2 mars - chuẩn xác theo topo Packet Tracer)
interface FastEthernet0/10
 switchport mode access
 switchport access vlan 2
 no shutdown
exit
```

---

### GIAI ĐOẠN 2: CẤU HÌNH LAYER 3 & ĐỊNH TUYẾN NỘI BỘ (IGP)

#### 1. Router `Earth` (Vùng Backbone OSPF Area 0)
```cisco
enable
configure terminal
hostname Earth

interface loopback 1
 ip address 172.23.0.1 255.255.224.0
exit

interface Gig0/0
 no shutdown
exit

interface Gig0/0.2
 encapsulation dot1Q 2
 ip address 172.23.128.1 255.255.240.0
exit

interface Gig0/0.3
 encapsulation dot1Q 3
 ip address 172.23.144.1 255.255.240.0
 ! Đặt Cost = 10 trên cổng VLAN 3 (để cổng VLAN 2 giữ Cost 1 mặc định giành quyền ưu tiên tuyệt đối, triệt tiêu ECMP)
 ip ospf cost 10
exit

router ospf 1
 router-id 1.1.1.1
 network 172.23.0.0 0.0.31.255 area 0
 network 172.23.128.0 0.0.15.255 area 0
 network 172.23.144.0 0.0.15.255 area 0
exit
```

#### 2. Router `Mars` (ABR: Area 0 $\longleftrightarrow$ Area 2)
```cisco
enable
configure terminal
hostname Mars

interface loopback 2
 ip address 172.23.32.1 255.255.224.0
exit

interface Gig0/0
 no shutdown
exit

interface Gig0/0.2
 encapsulation dot1Q 2
 ip address 172.23.128.2 255.255.240.0
exit

interface Gig0/0.3
 encapsulation dot1Q 3
 ip address 172.23.144.2 255.255.240.0
exit

interface Serial0/3/0
 ip address 172.23.255.1 255.255.255.252
 clock rate 64000
 no shutdown
exit

router ospf 1
 router-id 2.2.2.2
 network 172.23.128.0 0.0.15.255 area 0
 network 172.23.144.0 0.0.15.255 area 0
 network 172.23.32.0 0.0.31.255 area 2
 network 172.23.255.0 0.0.0.3 area 2
exit
```

#### 3. Router `Venus` (ABR: Area 0 $\longleftrightarrow$ Area 1)
```cisco
enable
configure terminal
hostname Venus

interface loopback 3
 ip address 172.23.64.1 255.255.224.0
exit

interface Gig0/0
 no shutdown
exit

interface Gig0/0.2
 encapsulation dot1Q 2
 ip address 172.23.128.3 255.255.240.0
exit

interface Gig0/0.3
 encapsulation dot1Q 3
 ip address 172.23.144.3 255.255.240.0
exit

interface Serial0/3/0
 ip address 172.23.255.5 255.255.255.252
 clock rate 64000
 no shutdown
exit

router ospf 1
 router-id 3.3.3.3
 network 172.23.128.0 0.0.15.255 area 0
 network 172.23.144.0 0.0.15.255 area 0
 network 172.23.64.0 0.0.31.255 area 1
 network 172.23.255.4 0.0.0.3 area 1
exit
```

#### 4. Router `Jupiter` (ASBR: OSPF Area 2 & EIGRP AS 69)
```cisco
enable
configure terminal
hostname Jupiter

interface loopback 4
 ip address 172.23.96.1 255.255.224.0
exit

interface Serial0/3/0
 ip address 172.23.255.2 255.255.255.252
 no shutdown
exit

interface Serial0/3/1
 ip address 172.22.255.1 255.255.255.252
 no shutdown
exit

router ospf 1
 router-id 4.4.4.4
 network 172.23.96.0 0.0.31.255 area 2
 network 172.23.255.0 0.0.0.3 area 2
exit

router eigrp 69
 no auto-summary
 network 172.22.255.0 0.0.0.3
exit
```

#### 5. Router `Mecury` (ASBR: OSPF Area 1 & EIGRP AS 69)
```cisco
enable
configure terminal
hostname Mecury

interface loopback 5
 ip address 172.22.0.1 255.255.224.0
exit

interface Serial0/3/0
 ip address 172.23.255.6 255.255.255.252
 no shutdown
exit

interface Serial0/3/1
 ip address 172.22.255.5 255.255.255.252
 no shutdown
exit

router ospf 1
 router-id 5.5.5.5
 network 172.23.255.4 0.0.0.3 area 1
exit

router eigrp 69
 no auto-summary
 network 172.22.0.0 0.0.31.255
 network 172.22.255.4 0.0.0.3
exit
```

#### 6. Router `Neptune` (EIGRP AS 69 & Biên Internet)
```cisco
enable
configure terminal
hostname Neptune

interface Serial0/3/1
 ip address 172.22.255.2 255.255.255.252
 clock rate 64000
 no shutdown
exit

interface Serial0/3/0
 ip address 172.22.255.6 255.255.255.252
 clock rate 64000
 no shutdown
exit

interface Gig0/0
 ip address 192.168.0.10 255.255.255.0
 no shutdown
exit

router eigrp 69
 no auto-summary
 network 172.22.255.0 0.0.0.3
 network 172.22.255.4 0.0.0.3
exit
```

---

### GIAI ĐOẠN 3: TÁI PHÂN PHỐI & CHỐNG BẪY ROUTING LOOP

#### 1. Trên Router `Neptune` (Đẩy Default Route vào EIGRP & Cấu hình NAT)
```cisco
enable
configure terminal

! 1. Tuyến ngầm định ra ISP
ip route 0.0.0.0 0.0.0.0 192.168.0.1

! 2. Bể địa chỉ NAT Public (12 IP)
ip nat pool ISP-POOL 192.168.0.11 192.168.0.22 netmask 255.255.255.0

! 3. ACL bắt các dải mạng nội bộ
access-list 1 permit 172.22.0.0 0.0.255.255
access-list 1 permit 172.23.0.0 0.0.255.255

! 4. Bật NAT Overload (PAT)
ip nat inside source list 1 pool ISP-POOL overload

! 5. Gán chiều Inside/Outside
interface Gig0/0
 ip nat outside
exit
interface Serial0/3/0
 ip nat inside
exit
interface Serial0/3/1
 ip nat inside
exit

! 6. Bơm tuyến Default Route vào EIGRP kèm 5 thông số Seed Metric chuẩn mực
router eigrp 69
 redistribute static metric 10000 100 255 1 1500
 no redistribute connected
exit
```

#### 2. Trên Router `Jupiter` (Redistribution & Sửa Administrative Distance)
```cisco
enable
configure terminal

! Bơm OSPF vào EIGRP
router eigrp 69
 redistribute ospf 1 metric 10000 100 255 1 1500
exit

! Bơm EIGRP vào OSPF và triệt tiêu bẫy Loop bằng cách hạ độ ưu tiên External Route
router ospf 1
 redistribute eigrp 69 subnets
 distance ospf external 175
 default-information originate
exit
```

#### 3. Trên Router `Mecury` (Tái phân phối EIGRP <-> OSPF)
```cisco
enable
configure terminal

! Bơm OSPF vào EIGRP
router eigrp 69
 redistribute ospf 1 metric 10000 100 255 1 1500
exit

! Bơm EIGRP vào OSPF và triệt tiêu bẫy Loop
! LƯU Ý THEO ĐÚNG GỢI Ý CỦA THẦY: Chỉ có Jupiter chạy default-information originate, Mecury KHÔNG chạy để tránh loop
router ospf 1
 redistribute eigrp 69 subnets
 distance ospf external 175
exit
```

---

### GIAI ĐOẠN 4: THIẾT LẬP ROUTER ISP ĐỂ TEST NAT & INTERNET

```cisco
enable
configure terminal
hostname ISP

! 1. Cổng WAN nối về Cloud DSL / Router Neptune
interface FastEthernet0/0
 description LINK TO DSL CLOUD
 ip address 192.168.0.1 255.255.255.0
 no shutdown
exit

! 2. Cấu hình VLAN 69 làm Gateway cho các Server Internet (Google DNS, Mail, Web)
interface Vlan69
 ip address 8.8.8.9 255.255.255.0
 no shutdown
exit

! 3. Gán các cổng Switch tích hợp (HWIC-4ESW) vào VLAN 69
interface FastEthernet0/0/0
 description NOI GOOGLE DNS (8.8.8.8)
 switchport access vlan 69
 switchport mode access
 spanning-tree portfast
 no shutdown
exit

interface FastEthernet0/0/1
 description NOI GOOGLE MAIL (8.8.8.10)
 switchport access vlan 69
 switchport mode access
 spanning-tree portfast
 no shutdown
exit

interface FastEthernet0/0/2
 description NOI WEB SERVER (8.8.8.11)
 switchport access vlan 69
 switchport mode access
 spanning-tree portfast
 no shutdown
exit

! 4. (Tùy chọn phụ) Loopback 0 bổ trợ
interface Loopback0
 ip address 8.8.8.8 255.255.255.255
 no shutdown
exit
```

---

### GIAI ĐOẠN 5: CẤU HÌNH XÁC THỰC BẢO MẬT (AUTHENTICATION)

#### 1. Xác thực EIGRP MD5 (Key-chain 11, chuỗi "mouse")

- **Trên Neptune**:
```cisco
enable
configure terminal
key chain EIGRP_KEY
 key 11
  key-string mouse
exit
interface Serial0/3/0
 ip authentication mode eigrp 69 md5
 ip authentication key-chain eigrp 69 EIGRP_KEY
exit
interface Serial0/3/1
 ip authentication mode eigrp 69 md5
 ip authentication key-chain eigrp 69 EIGRP_KEY
exit
```

- **Trên Jupiter**:
```cisco
enable
configure terminal
key chain EIGRP_KEY
 key 11
  key-string mouse
exit
interface Serial0/3/1
 ip authentication mode eigrp 69 md5
 ip authentication key-chain eigrp 69 EIGRP_KEY
exit
```

- **Trên Mecury**:
```cisco
enable
configure terminal
key chain EIGRP_KEY
 key 11
  key-string mouse
exit
interface Serial0/3/1
 ip authentication mode eigrp 69 md5
 ip authentication key-chain eigrp 69 EIGRP_KEY
exit
```

#### 2. Xác thực OSPF MD5 (Password "cat")

- **Trên Earth**:
```cisco
enable
configure terminal
interface Gig0/0.2
 ip ospf message-digest-key 1 md5 cat
exit
interface Gig0/0.3
 ip ospf message-digest-key 1 md5 cat
exit
router ospf 1
 area 0 authentication message-digest
exit
```

- **Trên Mars**:
```cisco
enable
configure terminal
interface Gig0/0.2
 ip ospf message-digest-key 1 md5 cat
exit
interface Gig0/0.3
 ip ospf message-digest-key 1 md5 cat
exit
interface Serial0/3/0
 ip ospf message-digest-key 1 md5 cat
exit
router ospf 1
 area 0 authentication message-digest
 area 2 authentication message-digest
exit
```

- **Trên Venus**:
```cisco
enable
configure terminal
interface Gig0/0.2
 ip ospf message-digest-key 1 md5 cat
exit
interface Gig0/0.3
 ip ospf message-digest-key 1 md5 cat
exit
interface Serial0/3/0
 ip ospf message-digest-key 1 md5 cat
exit
router ospf 1
 area 0 authentication message-digest
 area 1 authentication message-digest
exit
```

- **Trên Jupiter**:
```cisco
enable
configure terminal
interface Serial0/3/0
 ip ospf message-digest-key 1 md5 cat
exit
router ospf 1
 area 2 authentication message-digest
exit
```

- **Trên Mecury**:
```cisco
enable
configure terminal
interface Serial0/3/0
 ip ospf message-digest-key 1 md5 cat
exit
router ospf 1
 area 1 authentication message-digest
exit
```

---

# PHẦN V: QUY TRÌNH NGHIỆM THU & KIỂM THỬ HỘP TRẮNG

Để bảo vệ bài lab đạt điểm 10/10, bạn không chỉ dừng lại ở lệnh `ping`, mà phải trình bày được dữ liệu thực nghiệm thông qua 5 lệnh kiểm thử "hộp trắng":

### 1. Kiểm tra chống lặp Routing Loop bằng `tracert`
- **Vị trí**: Command Prompt trên `PC0` (`172.23.128.10`).
- **Thực thi**: `tracert 192.168.0.1`
- **Kết quả chuẩn mực**: Gói tin đi thẳng qua 5 trạm không bị lặp:
  1. `172.23.128.1` (Default Gateway trên Earth)
  2. `172.23.255.x` (Qua Mars hoặc Venus)
  3. `172.23.255.y` (Qua Jupiter hoặc Mecury)
  4. `172.22.255.z` (Qua Neptune)
  5. `192.168.0.1` (Cổng ISP)

### 2. Soi ký hiệu định tuyến trong `show ip route`
- **Trên Earth / Mars / Venus**:
  - Phải thấy các tuyến liên vùng: ký hiệu `O IA` (Inter-Area).
  - Phải thấy các tuyến ngoại lai EIGRP bơm sang: ký hiệu `O E2` (OSPF External Type 2) cho dải `172.22.0.0/16`.
  - Phải thấy tuyến ngầm định ra Internet: `O*E2 0.0.0.0/0`.
- **Trên Neptune**:
  - Phải thấy các tuyến OSPF bơm sang EIGRP: ký hiệu `D EX` (EIGRP External) cho dải `172.23.0.0/16`.

### 3. Kiểm tra bảng dịch địa chỉ NAT (`show ip nat translations`)
- **Vị trí**: Router `Neptune`.
- **Thao tác**: Sau khi từ PC0 ping ra `192.168.0.1`, gõ `show ip nat translations`.
- **Kết quả chuẩn mực**: Xuất hiện phiên dịch ánh xạ giữa `Inside Local` (`172.23.128.10:icmp`) sang `Inside Global` (`192.168.0.11` kèm port PAT).

### 4. Kiểm tra trạng thái láng giềng bảo mật
- **OSPF**: Gõ `show ip ospf neighbor` trên Earth/Mars/Venus/Jupiter/Mecury $\longrightarrow$ Cột `State` phải đạt trạng thái **`FULL/BDR`** hoặc **`FULL/DR`**.
- **EIGRP**: Gõ `show ip eigrp neighbors` trên Jupiter/Mecury/Neptune $\longrightarrow$ Bảng liệt kê đầy đủ IP hàng xóm.

### 5. Kiểm tra VTP & Trunking
- Gõ `show vtp status` trên Server/Client: Chung domain `planet`, Revision Number đồng bộ.
- Gõ `show interfaces trunk`: Cả 3 cổng nối đều ở trạng thái `trunking` với allowed VLAN `1,2,3`.

---

# PHẦN VI: CẨM NANG VẤN ĐÁP CHUYÊN SÂU BẢO VỆ ĐIỂM 10/10

Đây là các câu hỏi "bẫy" mà giảng viên DUT (thầy Ly) thường hỏi để phân loại sinh viên xuất sắc:

### Câu 1: Tại sao trong đề bài có lưu ý "(beware of default route)" và thầy giáo gợi ý "chỉ lựa chọn 1 trong 2 (Jupiter hoặc Mercury) để cấu hình default-information originate"?
> **Trả lời:**  
> - **Nguyên nhân sinh ra Loop**:  
>   - Khi Neptune đẩy Default Route (`0.0.0.0/0`) vào EIGRP, tuyến này có độ tin cậy $AD = 170$ (EIGRP External).
>   - Nếu **cả Jupiter và Mecury** cùng bật `default-information originate` để bơm vào OSPF, tuyến này sẽ biến thành OSPF External với độ tin cậy mặc định $AD = 110$.
>   - Router Mecury lúc này đứng trước 2 nguồn tin về Default Route:
>     1. Từ Neptune (nối trực tiếp qua Serial) với $AD = 170$.
>     2. Từ Jupiter (bơm qua mạng OSPF) với $AD = 110$.
>   - Do quy tắc chọn đường ưu tiên $AD$ nhỏ hơn ($110 < 170$), Mecury sẽ bỏ rơi đường nối trực tiếp với Neptune để định tuyến vòng qua OSPF Jupiter $\implies$ **Sinh ra Routing Loop (hiện tượng ping gói được, gói mất)!**
> - **Giải pháp tối ưu theo chuẩn của Thầy giáo**:  
>   - **Chỉ cấu hình `default-information originate` trên DUY NHẤT 1 Router ASBR (chọn Jupiter)**. Mecury vẫn chạy `redistribute eigrp 69 subnets` để chia sẻ các subnet nội bộ, nhưng **tuyệt đối không chạy** `default-information originate`.
>   - Khi đó, trong toàn bộ mạng OSPF chỉ có duy nhất Jupiter là điểm xuất phát tuyến $0.0.0.0/0$. Mecury không phát default route vào OSPF nên không bao giờ có sự cạnh tranh hay xung đột luồng dữ liệu, triệt tiêu bẫy loop ngay từ gốc rễ!

---

### Câu 2: Tại sao khi đứng tại Router Earth gõ `ping 8.8.8.8` thì tỷ lệ thành công ban đầu chỉ đạt khoảng 40% – 60% (rớt 2-3 gói), trong khi đứng tại PC0 ping thì đạt 100%?
> **Trả lời:**  
> - Đây là hệ quả của hiện tượng **Xung đột phiên NAT (NAT PAT Collision) kết hợp với Cơ chế Cân bằng tải (ECMP)**:
>   1. **4 đường ECMP trên Earth**: Earth nối vào hệ thống qua 2 Sub-interface VLAN 2 (`172.23.128.1`) và VLAN 3 (`172.23.144.1`). Ở phía đối diện có cả Mars (`.2`) và Venus (`.3`) với Cost bằng nhau. Khi cả 2 hướng đi ra Internet có Cost bằng nhau, OSPF nhân chéo tạo ra **4 đường đi Default Route có Cost bằng nhau**.
>   2. **Tráo đổi Source IP liên tục**: Khi ping 5 gói tin từ CLI của Earth mà không chỉ định nguồn, Router sẽ lấy IP của cổng mà gói tin chui ra làm Source IP. Do chia bài luân phiên qua các đường, gói 1 mang IP nguồn `172.23.128.1`, nhưng gói 2 lại mang IP nguồn `172.23.144.1`.
>   3. **Đụng độ ICMP ID tại Neptune**: Cả 5 gói tin này sinh ra từ cùng một phiên Ping nên mang cùng một mã `ICMP Sequence / ICMP ID`. Khi Neptune nhận gói 1, nó ghi bảng NAT cho IP `172.23.128.1`. Phần ngàn giây sau, gói 2 ập tới với cùng ICMP ID nhưng lại mang IP `172.23.144.1`. Neptune bị xung đột định danh phiên nên drop gói tin hoặc ghi đè, khiến gói Reply từ 8.8.8.8 không thể định tuyến về đúng cổng!
> - Trong khi đó, **PC0** là máy trạm chỉ có duy nhất 1 card mạng và 1 IP tĩnh cố định (`172.23.128.10`), không có hiện tượng nhảy IP nguồn nên NAT mượt mà đạt 100%.

---

### Câu 3: Làm thế nào để giải quyết triệt để hiện tượng rớt gói từ Earth (Nên chọn cấu hình Redistribution hay Nâng/Hạ Cost)?
> **Trả lời:**  
> **Giải pháp hoàn hảo nhất là KẾT HỢP CẢ HAI KỸ THUẬT**:
> 1. **Cấu hình Redistribution theo thầy (Loại bỏ 2 đường qua Venus)**:
>    - Chỉ bật `default-information originate` trên Jupiter (Area 2).
>    - Khi đó, đường đi qua Mars sang Jupiter có metric ngắn hơn hẳn so với việc đi vòng qua Venus sang Mecury (vì Mecury không còn phát default route). Earth lập tức loại bỏ 2 đường qua Venus, bảng định tuyến từ 4 đường giảm xuống còn 2 đường (qua Mars).
> 2. **Can thiệp OSPF Cost trên Earth (Loại bỏ nốt đường qua VLAN 3)**:
>    - Trên Router Earth, ta cấu hình `ip ospf cost 10` cho sub-interface `Gig0/0.3` (VLAN 3), trong khi giữ nguyên `Gig0/0.2` (VLAN 2) ở Cost mặc định là `1`.
>    - Lúc này, OSPF so sánh Cost: $1 < 10 \implies$ Earth loại bỏ hoàn toàn đường đi qua VLAN 3, co bảng định tuyến Default Route về **ĐÚNG 1 ĐƯỜNG DUY NHẤT**: `via 172.23.128.2, GigabitEthernet0/0.2`.
>    - Vì chỉ còn 1 cổng xuất duy nhất, Source IP cố định 100% ở `172.23.128.1`, Neptune xử lý NAT không bị xung đột phiên, **lệnh ping thường từ Earth đạt 100% (5/5) xanh rờn ngay lập tức!**
> 3. **(Tùy chọn phụ khi bảo vệ)**: Sinh viên cũng có thể biểu diễn lệnh `ping 8.8.8.8 source Loopback1` để chứng minh cho thầy thấy bản chất của hiện tượng là do thay đổi IP nguồn của gói ICMP.

---

### Câu 4: Tại sao trên Router Neptune cần gỡ bỏ lệnh `redistribute connected` (`no redistribute connected`)?
> **Trả lời:**  
> - Cổng `Gig0/0` của Neptune nối với ISP mang dải IP Public `192.168.0.0/24` (mạng Connected).
> - Nếu để `redistribute connected`, dải mạng của ISP sẽ bị bơm ngược vào bảng định tuyến nội bộ của toàn bộ các Router Earth, Mars, Venus...
> - Trong thiết kế mạng chuẩn doanh nghiệp, các Router nội bộ **không bao giờ được phép học đích danh subnet ngoài của ISP**, mà tất cả lưu lượng đi ra ngoài đều phải đi qua **Tuyến ngầm định (Default Route `0.0.0.0/0`)**. Việc gỡ bỏ lệnh này giúp bảng định tuyến nội bộ sạch sẽ, bảo mật và đúng chuẩn kiến trúc ISP-Enterprise.

---

### Câu 5: Tại sao khi tái phân phối vào EIGRP bắt buộc phải có 5 thông số Metric, trong khi vào OSPF bắt buộc phải có từ khóa `subnets`?
> **Trả lời:**  
> - **Đối với EIGRP**: Metric mặc định (Seed Metric) khi lấy từ giao thức khác vào là **vô cực ($\infty$)**. Nếu không gán thủ công 5 giá trị Vector Metric: Bandwidth ($K_1$), Delay ($K_3$), Reliability ($K_4$), Load ($K_2$), MTU ($K_5$), EIGRP sẽ coi tuyến đó là không thể tiếp cận (unreachable) và không bao giờ đưa vào bảng định tuyến.
> - **Đối với OSPF**: Mặc định OSPF coi mọi tuyến nhận từ bên ngoài là mạng lớp đầy đủ (Classful: /8, /16, /24). Nếu mạng của ta đã được chia nhỏ theo kỹ thuật VLSM (như các subnet /19, /20, /30 trong đề) mà không có từ khóa `subnets`, OSPF sẽ tự động lọc bỏ toàn bộ các mạng con này và không quảng bá.
