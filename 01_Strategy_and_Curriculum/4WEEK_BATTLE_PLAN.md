# ⚡ KẾ HOẠCH TÁC CHIẾN 4 TUẦN: CÔNG TY QUẢN TRỊ MẠNG (ENTERPRISE NETADMIN)
## 4-Week Tactical Execution Plan — Network Management & Administration (NMA)

> **Mã Doanh Nghiệp:** `CORP-03-NMA`  
> **Cố vấn chuyên môn:** **DUT Network Admin Mentor**  
> **Người thực thi:** Kỹ Sư Trưởng Handmade (`HM-00` / Bạn)

---

## 🎯 MỤC TIÊU THÁNG 1
Hoàn thành Chuyên đề 1 (Quy hoạch IP & Topo doanh nghiệp) và Chuyên đề 2 (Hạ tầng mạng lõi DHCP/DNS/Routing); thực hiện phân tích gói tin DORA trên Wireshark theo đúng chuẩn mực sư phạm DUT.

---

## 📅 LỘ TRÌNH CHI TIẾT TỪNG TUẦN

### Tuần 1: Thiết Kế Topo Doanh Nghiệp 3 Tầng & Bảng Phân Bổ IP (VLSM)
- **Lý thuyết**: Mô hình quản trị FCAPS, Kiến trúc mạng doanh nghiệp 3 tầng (Core - Distribution - Access), Kỹ thuật chia mạng con theo độ dài mặt nạ thay đổi (VLSM).
- **Thực hành (Lab)**:
  - Dựng Topo trên Cisco Packet Tracer: 1 Router Cisco 2911, 2 Switch Layer 3 Catalyst 3560, 4 Switch Access Catalyst 2960.
  - Phân bổ dải IP `192.168.10.0/24` cho 4 phòng ban:
    - VLAN 10 (Kế Toán - 30 hosts): `192.168.10.0/27`
    - VLAN 20 (Kinh Doanh - 60 hosts): `192.168.10.64/26`
    - VLAN 30 (Kỹ Thuật - 20 hosts): `192.168.10.128/27`
    - VLAN 99 (Quản Trị Native - 10 hosts): `192.168.10.160/28`
- **Sản phẩm bàn giao**: File Topo `03_Engineering_Labs_and_Code/Enterprise_Topology_3Tier.pkt` kèm file bảng phân bổ IP Markdown.
- **KPI nghiệm thu**: Bảng phân bổ IP không bị chồng lấn (No overlapping subnets); đúng chuẩn DUT Network Admin Mentor.

---

### Tuần 2: Cấu Hình Chuyển Mạch VLAN Đa Tầng, Trunking & SVI
- **Lý thuyết**: Chuẩn đóng gói 802.1Q (VLAN Tagging 4 bytes), Giao thức VTP v2/v3, Định tuyến liên VLAN bằng Router-on-a-stick và Switch Virtual Interface (SVI).
- **Thực hành (Lab)**:
  - Cấu hình Cisco CLI chuẩn:
    ```cisco
    ! Trên Switch Access: Tạo VLAN & gán cổng
    vlan 10
     name KeToan
    interface fastEthernet 0/1
     switchport mode access
     switchport access vlan 10
    ! Cấu hình cổng Trunk nối lên Switch L3
    interface gigabitEthernet 0/1
     switchport mode trunk
     switchport trunk allowed vlan 10,20,30,99
    ```
  - Bật định tuyến IP trên Switch Layer 3 (`ip routing`) và tạo các Interface VLAN làm Default Gateway.
- **Sản phẩm bàn giao**: File cấu hình `running-config` đã lưu của Switch L3 và Switch Access.
- **KPI nghiệm thu**: Các PC thuộc các VLAN khác nhau ping thông 100% qua Switch L3; lệnh `show vlan brief` hiển thị đúng tên.

---

### Tuần 3: Dịch Vụ Cấp Phát IP Động (DHCP) & Cấu Hình DHCP Relay Agent
- **Lý thuyết**: Quá trình bắt tay 4 bước DHCP (Discover, Offer, Request, Acknowledge), Cổng UDP 67 (Server) và UDP 68 (Client), Cơ chế Relay Agent vượt qua ranh giới broadcast của Router.
- **Thực hành (Lab)**:
  - Cấu hình DHCP Server tập trung trên Router Core cho 3 VLAN.
  - Trên các Interface SVI của Switch L3, cấu hình lệnh `ip helper-address <IP_DHCP_Server>` để chuyển tiếp gói tin DHCP Broadcast thành Unicast.
  - Mở Wireshark bắt và phân tích bản tin DHCP DORA tại cổng Router.
- **Sản phẩm bàn giao**: Ảnh chụp màn hình Wireshark 4 gói tin dán vào `04_Notion_Digital_Workspace/` và log lệnh cấu hình.
- **KPI nghiệm thu**: 100% PC ở các VLAN nhận đúng dải IP, Subnet Mask, Gateway và DNS Server được gán.

---

### Tuần 4: Máy Chủ Tên Miền (DNS) & Định Tuyến Động OSPF Đơn Vùng
- **Lý thuyết**: Cơ chế phân giải tên miền đệ quy (Recursive) vs lặp (Iterative), Các bản ghi Resource Records (A, CNAME, PTR, MX), Giao thức định tuyến trạng thái liên kết OSPF Area 0.
- **Thực hành (Lab)**:
  - Dựng máy chủ DNS Server (BIND9 trên máy ảo Linux hoặc Windows Server); cấu hình phân giải tên miền nội bộ `portal.dut.corp`.
  - Cấu hình định tuyến OSPF trên Router Biên và Switch L3:
    ```cisco
    router ospf 1
     router-id 1.1.1.1
     network 192.168.10.0 0.0.0.255 area 0
     network 10.0.0.0 0.0.0.3 area 0
    ```
- **Sản phẩm bàn giao**: File nhật ký kiểm thử lệnh `nslookup portal.dut.corp` và bảng định tuyến `show ip route ospf`.
- **KPI nghiệm thu**: Máy trạm truy cập được web nội bộ qua tên miền; bảng định tuyến hội tụ không có loop.
