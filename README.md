# 🌐 DUT Network Management (Quản Trị Mạng & Hạ Tầng Doanh Nghiệp)
### Academic Vault: Quy Hoạch Mạng Doanh Nghiệp, Định Tuyến OSPF/EIGRP & Windows Server AD DS

[![DUT CNTT](https://img.shields.io/badge/DUT-Khoa%20CNTT-0052cc.svg)](https://dut.udn.vn)
[![Course](https://img.shields.io/badge/Course-Network%20Management-0077b6.svg)](https://github.com/codebypython/dut-network-management)
[![Simulator](https://img.shields.io/badge/Simulator-Cisco%20Packet%20Tracer%208.2.2-005073.svg)](https://netacad.com)
[![Routing Protocols](https://img.shields.io/badge/Routing-OSPF%20%7C%20EIGRP%20%7C%20VLAN-1d3557.svg)](https://cisco.com)
[![Directory Services](https://img.shields.io/badge/Server-Windows%20Server%20AD%20DS-0078d4.svg)](https://microsoft.com)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> **Kho lưu trữ học thuật chính quy học phần Quản trị Mạng (Network Management)**  
> **Trường Đại học Bách Khoa — Đại học Đà Nẵng (DUT)**  
> **Sinh viên thực hiện:** Nguyễn Trung Kiên (`codebypython` | `kien1152005@gmail.com`)

---

## 📌 1. TỔNG QUAN HỌC PHẦN (COURSE OVERVIEW)

Học phần **Quản trị Mạng** trang bị kiến thức chuyên sâu về thiết kế, triển khai và vận hành hệ thống mạng doanh nghiệp quy mô vừa và lớn. Nội dung bao phủ từ phân hoạch địa chỉ IP (VLSM Subnetting), định tuyến động nâng cao (Multi-Area OSPF, EIGRP, Redistribution) trên thiết bị Cisco, đến cấu hình hạ tầng dịch vụ mạng (DHCP, DNS, NAT/PAT) và quản trị thư mục tập trung Active Directory Domain Services (AD DS) trên Windows Server.

---

## 🏛️ 2. NỘI DUNG CHUYÊN ĐỀ & BÀI THỰC HÀNH (SYLLABUS & LABS)

### 🔹 Module 1: Hạ Tầng Mạng & Định Tuyến Nâng Cao (Routing & Switching)
- **Quy hoạch IP & VLSM:** Phân chia subnet tối ưu, chống lãng phí không gian địa chỉ IPv4.
- **Inter-VLAN Routing:** Phân chia mạng cục bộ ảo (VLAN), cấu hình 802.1Q Trunking, cơ chế Router-on-a-stick và Switch Virtual Interface (SVI).
- **Định tuyến động OSPF & EIGRP:** Cấu hình OSPF Đa vùng (Area 0 Backbone & Stub Areas), EIGRP AS 69 với metric K-values, và Tái phân phối tuyến (Route Redistribution).

### 🔹 Module 2: Dịch Vụ Mạng Cốt Lõi (Core Network Services)
- **DHCP Service:** Quy trình 4 bước DORA, cấp phát IP Scope động, DHCP Reservation theo MAC và DHCP Relay Agent liên phân đoạn mạng.
- **NAT / PAT:** Chuyển dịch địa chỉ mạng tĩnh (Static NAT), động (Dynamic NAT) và quá tải cổng (Port Address Translation) ra môi trường ISP.

### 🔹 Module 3: Quản Trị Hệ Thống & Thư Mục (Directory Services & SysAdmin)
- **Active Directory Domain Services (AD DS):** Cài đặt Domain Controller, thiết kế cây thư mục Đơn vị tổ chức (OU), quản trị User, Group và bảo mật mật khẩu.
- **Group Policy Objects (GPO):** Triển khai chính sách khóa máy trạm, phân quyền ổ đĩa mạng SMB/NFS và tự động hóa cập nhật.

---

## 📁 3. CẤU TRÚC THƯ MỤC (REPOSITORY LAYOUT)

```
dut-network-management/
├── 01_Strategy_and_Curriculum/         # Đề cương chi tiết học phần, thang điểm & kế hoạch
├── 02_Lectures_and_Raw_Materials/      # Slide bài giảng lý thuyết & tài liệu tham khảo
├── 03_Engineering_Labs_and_Code/       # File mô phỏng Cisco Packet Tracer (.pkt) & Configs (.cfg)
│   ├── Day1_VLSM_IP_Planning/          # Quy hoạch IP & topo mẫu
│   ├── Day3_DHCP_Services/             # Cấu hình DHCP Server & Relay
│   ├── Day4_InterVLAN_Routing/         # Định tuyến VLAN & Trunking
│   └── Day5_MultiArea_OSPF_EIGRP/      # OSPF Đa vùng, EIGRP AS 69 & ISP Simulation
├── 04_Notion_Digital_Workspace/        # Bản ghi Notion số hóa & Cheat-sheets
├── 05_Troubleshooting_and_Toolkits/    # Tool audit tự động XML/PKT & cẩm nang xử lý lỗi
├── AGENT_PROTOCOL.md                   # Điều lệ điều phối AI Mentor
├── STATUS.md                           # Dashboard tiến độ thực tế 15 tuần
├── .gitignore                          # Loại trừ file cài đặt exe nặng, ISO và máy ảo
└── README.md                           # Đặc tả học thuật chính thức
```

---

## ⚡ 4. KHỞI CHẠY LAB & KIỂM TOÁN TỰ ĐỘNG

```powershell
# 1. Chạy script kiểm toán cấu hình Packet Tracer Day 5
python 05_Troubleshooting_and_Toolkits/audit_day5_pkt.py

# 2. Mở file mô phỏng trên Cisco Packet Tracer 8.2.2:
#    03_Engineering_Labs_and_Code/Day5/ISP service.pkt
```

---

## 👤 5. THÔNG TIN HỌC THUẬT

- **Sinh viên:** Nguyễn Trung Kiên
- **GitHub:** [@codebypython](https://github.com/codebypython)
- **Trường:** Đại học Bách Khoa — Đại học Đà Nẵng (DUT)
- **Giấy phép:** [MIT License](LICENSE)
