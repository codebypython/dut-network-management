# 📊 PROJECT STATUS DASHBOARD — NetAdmin Corp (CORP-03-NMA)

> **Cập nhật lần cuối**: 2026-11-03 | **Tuần hiện tại**: Tuần 6 (EIGRP, OSPF, Inter-VLAN, Dual-ISP NAT & Redistribution)  
> **Mentor chuyên trách**: DUT Network Admin Mentor (`01_Strategy_and_Curriculum/AGENT_PROFILE.md`)

---

## Current Phase: 🔵 PHASE 1 — INFRASTRUCTURE & CORE SERVICES (Tuần 1-6)

Tập trung vào quy hoạch IP, Subnetting VLSM, cấu hình định tuyến cơ bản, VLAN/Trunking, Multi-Area OSPF, EIGRP AS 66 & 99, Route Redistribution, Dual-ISP NAT Overload và ACL bảo mật.

---

## Implementation & Lab Progress

### Module 1: Cơ Sở Hạ Tầng & Dịch Vụ Mạng Cốt Lõi
- [x] Quy hoạch Bảng phân bổ IP & Topo mạng doanh nghiệp mẫu (Lab 1)
- [x] Cấu hình DHCP Server (DORA, Scope, Reservation, Relay Agent - Lab 3/4)
- [x] Định tuyến tĩnh & Inter-VLAN Routing (Router-on-a-stick / SVI - Lab 4)
- [x] Định tuyến nâng cao OSPF Đa vùng, EIGRP AS 69 & Tái phân phối (Redistribution - Lab Day 5)
- [x] Định tuyến tích hợp EIGRP 66/99, OSPF Area 0, Dual-ISP NAT & Extended ACL 101 (Lab Day 6)
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
- **Date**: 2026-11-03
- **Work Done**: 
  - Phân tích và phát hiện xung đột phân vùng định tuyến trong bản nháp cũ của Day 6: Chuẩn hóa Vùng Tây (`EIGRP AS 66` - `172.21.0.0/16`), Vùng Giữa (`EIGRP AS 99` - `172.22.0.0/16`), Vùng Đông (`OSPF Area 0` - `172.23.0.0/16`), bảo đảm lệnh `default-information originate` trên `EastGate` đúng 100% cú pháp gốc OSPF.
  - Chuẩn hóa kỹ thuật quảng bá Tuyến ngầm định trên `WestGate` theo yêu cầu/gợi ý của Thầy: Sử dụng `ip default-network 10.0.0.0` kết hợp quảng bá `network 10.0.0.0` trong `router eigrp 66` (hoàn toàn không dùng `ip route 0.0.0.0 0.0.0.0` hay `redistribute static`).
  - Cập nhật và đồng bộ toàn bộ 9 file cấu hình trong `03_Engineering_Labs_and_Code/Day6/device_configs/` (`01_Server_Switch.cfg` đến `09_ISP_East_Router.cfg`).
  - Xây dựng tài liệu cấu hình máy trạm `10_End_Hosts_PC_Configurations.md` cho 8 PC/Server, hướng dẫn bật Web/Telnet trên `PC-East` để kiểm thử hộp trắng ACL 101.
  - Xuất bản Cẩm nang Master toàn diện `HUONG_DAN_HOAN_CHINH_LAB_6_EIGRP_OSPF_VLAN_NAT.md` tích hợp VLSM 12 subnets, ma trận đấu nối vật lý, CLI 8 giai đoạn, quy trình nghiệm thu và cẩm nang vấn đáp điểm 10/10.
  - Xây dựng công cụ kiểm toán tự động `05_Troubleshooting_and_Toolkits/audit_day6_configs.py`: **Đạt 56/56 tiêu chí kỹ thuật (100.0% PASSED)**.
- **Next Priority (P0)**: Sinh viên mở Cisco Packet Tracer 8.2.2, tạo topology theo ma trận cổng và copy-paste cấu hình CLI vào từng thiết bị.
