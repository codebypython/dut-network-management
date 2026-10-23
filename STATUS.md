# 📊 PROJECT STATUS DASHBOARD — NetAdmin Corp (CORP-03-NMA)

> **Cập nhật lần cuối**: 2026-10-20 | **Tuần hiện tại**: Tuần 5 (Multi Area OSPF, EIGRP & Redistribution)  
> **Mentor chuyên trách**: DUT Network Admin Mentor (`01_Strategy_and_Curriculum/AGENT_PROFILE.md`)

---

## Current Phase: 🔵 PHASE 1 — INFRASTRUCTURE & CORE SERVICES (Tuần 1-5)

Tập trung vào quy hoạch IP, Subnetting VLSM, cấu hình định tuyến cơ bản, VLAN/Trunking, Multi-Area OSPF, EIGRP AS 69, Route Redistribution và dịch vụ lõi DHCP/NAT.

---

## Implementation & Lab Progress

### Module 1: Cơ Sở Hạ Tầng & Dịch Vụ Mạng Cốt Lõi
- [x] Quy hoạch Bảng phân bổ IP & Topo mạng doanh nghiệp mẫu (Lab 1)
- [x] Cấu hình DHCP Server (DORA, Scope, Reservation, Relay Agent - Lab 3/4)
- [x] Định tuyến tĩnh & Inter-VLAN Routing (Router-on-a-stick / SVI - Lab 4)
- [x] Định tuyến nâng cao OSPF Đa vùng, EIGRP AS 69 & Tái phân phối (Redistribution - Lab Day 5)
- [ ] Cấu hình DNS Server (Forward/Reverse Lookup, MX, CNAME, Root Hints)

### Module 2: Định Danh & Thư Mục (Directory Services)
- [ ] Cài đặt Windows Server 2022 Active Directory Domain Services (AD DS)
- [ ] Thiết kế Organizational Units (OU), User/Group & Group Policy Objects (GPO)
- [ ] Tích hợp máy trạm Windows 10/11 và Ubuntu Linux vào Domain

### Module 3: Dịch Vụ Ứng Dụng & Giám Sát
- [ ] Triển khai Web Server IIS / Nginx (SSL/TLS HTTPS)
- [ ] File Server SMB/NFS & Phân quyền ma trận NTFS vs Share Permissions
- [ ] Giám sát mạng với SNMPv3, Syslog Server & Bắt gói tin Wireshark

---

## Known Issues & Blockers

| # | Vấn đề | Mức độ | Ghi chú |
|:-:|:---|:---:|:---|
| 1 | File máy ảo Windows Server 2022 dung lượng lớn | 🟡 Medium | Cần dọn dẹp dung lượng ổ đĩa trước khi clone |

---

## Last Session
- **Date**: 2026-10-20
- **Work Done**: 
  - Giải mã và hạ cấp chữ ký tương thích thành công cho file `03_Engineering_Labs_and_Code/Day5/ISP service.pkt` từ bản 9.0.1.0858 xuống 8.2.2.0400 bằng Twofish/EAX Repacket, bảo đảm mở mượt mà trên Cisco Packet Tracer 8.2.2 của sinh viên.
  - Tinh chỉnh và chuẩn hóa cấu trúc thư mục Day 5: Dọn dẹp các thư mục trùng lặp, tạo thư mục `device_configs/` gồm 9 file `.cfg` độc lập cho từng thiết bị (`Server`, `Client`, `Earth`, `Mars`, `Venus`, `Jupiter`, `Mecury`, `Neptune`, `ISP`) và lưu trữ bản nháp cũ vào `raw_notes/`.
  - Phát hiện và hiệu chỉnh các điểm cốt tử trong topology: Cổng kết nối PC0 là `Client Fa0/10` (thay vì Fa0/3), kiến trúc Gateway VLAN 69 và 3 máy chủ Internet (`Google DNS 8.8.8.8`, `Google Mail 8.8.8.10`, `Web 8.8.8.11`) trên ISP.
  - Xây dựng công cụ kiểm toán tự động `05_Troubleshooting_and_Toolkits/audit_day5_pkt.py` quét toàn bộ cấu trúc XML/PKT: **Đạt 41/41 tiêu chí kỹ thuật (100.0% PASSED)**.
  - Xuất bản Cẩm nang Master duy nhất `HUONG_DAN_HOAN_CHINH_LAB_5_MULTI_AREA_OSPF_EIGRP_VLAN.md` tích hợp toàn bộ kiến trúc, bảng VLSM, CLI 7 giai đoạn, quy trình kiểm thử 5 bước và cẩm nang vấn đáp điểm 10/10.
- **Next Priority (P0)**: Sinh viên mở file `ISP service.pkt` trực tiếp trên Cisco Packet Tracer 8.2.2 và thực hiện các bước ping/tracert nghiệm thu.
