# 🖥️ HƯỚNG DẪN CẤU HÌNH TOÀN BỘ MÁY TRẠM & SERVER (END-HOSTS) — LAB DAY 6

Tài liệu này cung cấp bảng thông số cấu hình mạng chi tiết (IP, Subnet Mask, Default Gateway, DNS) cho tất cả các máy trạm (PC), máy chủ kiểm thử (Server Farm ISP và VLAN) trong bài Lab Day 6 (`EIGRP — OSPF — VLAN Lab 2`).

---

## 1. BẢNG THÔNG SỐ CẤU HÌNH IP MÁY TRẠM & PHÂN VÙNG (END-HOSTS)

| Tên Thiết Bị | Cổng Cắm Vật Lý / Node | Vùng Quản Trị | Địa Chỉ IP | Subnet Mask | Default Gateway | DNS Server | Chức Năng Nghiệm Thu |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **PC-LAN1** (hoặc Loopback1) | WestGate `Loopback1` | EIGRP AS 66 | `172.21.0.10` | `255.255.224.0` (/19) | `172.21.0.1` | `8.8.8.8` | Kiểm tra thông mạng nội bộ phía Tây |
| **PC-LAN2** (hoặc Loopback2) | West `Loopback2` | EIGRP AS 66 | `172.21.32.10` | `255.255.224.0` (/19) | `172.21.32.1` | `8.8.8.8` | **Nguồn kiểm thử chính của ACL 101** |
| **PC-LAN3** (hoặc Loopback3) | Core `Loopback3` | EIGRP AS 99 | `172.22.0.10` | `255.255.224.0` (/19) | `172.22.0.1` | `8.8.8.8` | Kiểm tra mạng Lõi doanh nghiệp |
| **PC-West** | Cổng `Fa0/10` Switch Server | VLAN 2 ("west") | `172.22.32.10` | `255.255.240.0` (/20) | `172.22.32.2` | `8.8.8.8` | Kiểm tra Inter-VLAN & Truy cập Internet |
| **PC-East** / **Server-East** | Cổng `Fa0/10` Switch Client | VLAN 3 ("east") | `172.22.48.10` | `255.255.240.0` (/20) | `172.22.48.2` | `8.8.8.8` | **Đích đến kiểm thử ACL 101 (Bật Web/Telnet)** |
| **PC-LAN4** (hoặc Loopback4) | East `Loopback4` | OSPF Area 0 | `172.23.0.10` | `255.255.224.0` (/19) | `172.23.0.1` | `8.8.8.8` | Kiểm tra thông mạng nội bộ phía Đông |
| **PC-LAN5** (hoặc Loopback5) | East `Loopback5` | OSPF Area 0 | `172.23.32.10` | `255.255.224.0` (/19) | `172.23.32.1` | `8.8.8.8` | Kiểm tra thông mạng nội bộ phía Đông |
| **PC-LAN6** (hoặc Loopback6) | EastGate `Loopback6` | OSPF Area 0 | `172.23.64.10` | `255.255.224.0` (/19) | `172.23.64.1` | `8.8.8.8` | Kiểm tra thông mạng biên phía Đông |

---

## 2. BẢNG THÔNG SỐ SERVER FARM CỦA ISP WEST & ISP EAST (TRONG FILE .PKT)

| Tên Thiết Bị | Cổng Cắm Vật Lý | Vùng ISP | Địa Chỉ IP | Subnet Mask | Default Gateway | Dịch Vụ Cung Cấp |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Web Server** | ISP WEST `Fa0/0/0` | ISP Phía Tây | `10.2.0.2` | `255.255.0.0` (/16) | `10.2.0.1` | HTTP, HTTPS |
| **DNS Server** | ISP WEST `Fa0/0/1` | ISP Phía Tây | `10.2.0.3` | `255.255.0.0` (/16) | `10.2.0.1` | DNS Server |
| **Mail Server** | ISP WEST `Fa0/0/2` | ISP Phía Tây | `10.2.0.4` | `255.255.0.0` (/16) | `10.2.0.1` | SMTP, POP3 |
| **Web Server** | ISP EAST `Fa0/0/0` | ISP Phía Đông | `192.168.0.2` | `255.255.255.0` (/24) | `192.168.0.1` | HTTP, HTTPS |
| **DNS Server** | ISP EAST `Fa0/0/1` | ISP Phía Đông | `192.168.0.3` | `255.255.255.0` (/24) | `192.168.0.1` | DNS Server (8.8.8.8) |
| **Mail Server** | ISP EAST `Fa0/0/2` | ISP Phía Đông | `192.168.0.4` | `255.255.255.0` (/24) | `192.168.0.1` | SMTP, POP3 |

---

## 3. HƯỚNG DẪN THIẾT LẬP DỊCH VỤ TRÊN PC-EAST ĐỂ TEST ACL 101 (YÊU CẦU 8)

Để nghiệm thu yêu cầu: *"Do not allow LAN2 ping vlan 'east', except HTTP+TELNET access (two way); other traffics are allowed"*, bạn thực hiện cấu hình máy trạm/server **PC-East** trên Packet Tracer như sau:

### Cách 1: Sử dụng Thiết bị `Server-PT` làm PC-East (Khuyên Dùng)
1. Trong Packet Tracer, chọn thiết bị **Server-PT** đặt tên là `PC-East` (hoặc `Server-East`), cắm cáp thẳng vào cổng `Fa0/10` của **Switch Client**.
2. Nhấp vào thiết bị $\rightarrow$ chọn tab **Desktop** $\rightarrow$ **IP Configuration**:
   - IP Address: `172.22.48.10`
   - Subnet Mask: `255.255.240.0`
   - Default Gateway: `172.22.48.2` (hoặc `172.22.48.1` / `172.22.48.3`)
   - DNS Server: `8.8.8.8`
3. Chuyển sang tab **Services**:
   - Mục **HTTP**: Đảm bảo cả `HTTP` và `HTTPS` đều bật **On**. (Có thể sửa file `index.html` thêm dòng `Welcome to VLAN EAST Company DUT!`).
   - Mục **TELNET**: Bật **On**, tạo tài khoản `admin` / mật khẩu `cisco` (nếu có).

### Cách 2: Sử dụng Thiết bị `PC-PT`
1. Đặt IP như bảng trên (`172.22.48.10/20`).
2. Chú ý: Packet Tracer PC thông thường không hỗ trợ HTTP daemon cục bộ; do đó việc dùng **Server-PT** cho PC-East là giải pháp tối ưu nhất để thầy chấm demo trực quan qua trình duyệt Web.

---

## 4. KỊCH BẢN KIỂM THỬ HỘP TRẮNG TỪ PC-LAN2 (HOẶC ROUTER WEST)

Trên máy trạm **PC-LAN2** (`172.21.32.10`) hoặc trên **Router West** (`ping 172.22.48.10 source loopback2`), thực thi lần lượt 3 kịch bản:

### Kịch bản 1: Ping sang VLAN "east" (BẮT BUỘC BỊ CHẶN)
```text
C:\> ping 172.22.48.10
Pinging 172.22.48.10 with 32 bytes of data:
Request timed out.
Request timed out.
Request timed out.
Request timed out.
Ping statistics for 172.22.48.10:
    Packets: Sent = 4, Received = 0, Lost = 4 (100% loss)
```
👉 **ĐÁNH GIÁ: THÀNH CÔNG (Pass ACL Rule 3: Deny ICMP Echo)**.

### Kịch bản 2: Truy cập Web sang VLAN "east" (BẮT BUỘC THÀNH CÔNG)
1. Trên **PC-LAN2**, mở **Web Browser**.
2. Nhập URL: `http://172.22.48.10`
3. Nhấn **Go** $\longrightarrow$ Trang Web của Cisco hiện ra ngay lập tức!
👉 **ĐÁNH GIÁ: THÀNH CÔNG (Pass ACL Rule 1: Permit TCP port 80/www)**.

### Kịch bản 3: Ping ra ngoài Internet và các VLAN khác (BẮT BUỘC THÔNG SUỐT)
```text
C:\> ping 10.10.10.10   (Loopback ISP Tây)
Reply from 10.10.10.10: bytes=32 time=12ms TTL=253 ... (100% Success)

C:\> ping 8.8.8.8       (Loopback ISP Đông)
Reply from 8.8.8.8: bytes=32 time=15ms TTL=253 ... (100% Success)

C:\> ping 172.22.32.10 (PC-West thuộc VLAN 2)
Reply from 172.22.32.10: bytes=32 time=8ms TTL=127 ... (100% Success)
```
👉 **ĐÁNH GIÁ: THÀNH CÔNG (Pass ACL Rule 4: Permit IP any any - Other traffics allowed)**.
