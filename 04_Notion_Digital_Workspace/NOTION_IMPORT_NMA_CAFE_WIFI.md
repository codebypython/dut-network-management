# 📘 Master Notion Workspace: Quản Trị Mạng (NMA-DUT)
# ☕ Chuyên Đề: Thiết Kế & Quản Trị Wi-Fi Quán Cafe High-Density

> 🏛️ **Đơn vị**: Đại học Bách khoa – ĐH Đà Nẵng (DUT)  
> 🏷️ **Mã học phần**: NMA-DUT (Quản trị Mạng)  
> 👤 **Mentor**: DUT Network Admin Mentor  
> 🎯 **Mục tiêu học phần**: Làm chủ lý thuyết sóng RF, tính toán dung lượng mạng, phân bổ Subnetting /23, cấp phát DHCP, QoS Bandwidth và bảo mật WPA2-PSK trên Cisco Packet Tracer.

---

## 📊 I. MASTER DATABASES

### 🗂️ Database 1: Active Recall & Spaced Repetition (Kiến Thức Cốt Lõi)

| Tên Thuật Ngữ / Khái Niệm | Tầng OSI / Giao Thức | Mức Độ (Bloom) | Ưu Tiên (80/20) | Trạng Thái | Lần Ôn Gần Nhất | Chu Kỳ (Ngày) | Cần Ôn Hôm Nay? | Lệnh CLI / Công Thức Cốt Lõi |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **OFDMA trong Wi-Fi 6 (802.11ax)** | Layer 1/2 (RF/MAC) | Mức 2 (Hiểu) | 🔥 Trọng tâm (80%) | 🔴 Chưa thuộc | 2026-08-11 | 1 | ⚠️ Cần ôn | Chia kênh thành các Resource Units (RU) |
| **Kênh không chồng lấn 2.4GHz (1, 6, 11)** | Layer 1 (Physical/RF) | Mức 3 (Vận dụng) | 🔥 Trọng tâm (80%) | 🔴 Chưa thuộc | 2026-08-11 | 1 | ⚠️ Cần ôn | Kênh rộng 20MHz, cách nhau 25MHz |
| **Chia Subnet /23 & DHCP Lease Time** | Layer 3/7 (IP/DHCP) | Mức 3 (Vận dụng) | 🔥 Trọng tâm (80%) | 🟡 Tạm thuộc | 2026-08-11 | 2 | 🟢 Chưa tới lịch | `lease 0 2 0`, Mask: `255.255.254.0` |
| **Tính toán Băng thông YouTube 1080p** | Layer 4/7 (QoS/Perf) | Mức 3 (Vận dụng) | 🔥 Trọng tâm (80%) | 🟡 Tạm thuộc | 2026-08-11 | 2 | 🟢 Chưa tới lịch | $BW = 5\text{M} \times N_{\text{vid}} + 1\text{M} \times N_{\text{web}}$ |
| **Bảo mật WPA2-Personal (AES-CCMP)** | Layer 2 (Security) | Mức 2 (Hiểu) | 🔥 Trọng tâm (80%) | 🟢 Thành thạo | 2026-08-08 | 5 | 🟢 Chưa tới lịch | 4-Way Handshake (PMK $\rightarrow$ PTK/GTK) |
| **Inter-VLAN Sub-interface (802.1Q)** | Layer 3 (Routing) | Mức 3 (Vận dụng) | ⚡ Phụ (20%) | 🟢 Thành thạo | 2026-08-05 | 7 | 🟢 Chưa tới lịch | `encapsulation dot1Q <vlan-id>` |
| **Cơ chế Captive Portal (AAA)** | Layer 7 (HTTP/Auth) | Mức 3 (Vận dụng) | ⚡ Phụ (20%) | 🔴 Chưa thuộc | 2026-08-11 | 1 | ⚠️ Cần ôn | HTTP Redirect Port 80 $\rightarrow$ Splash Page |

> 💡 **Notion Formula 2.0 cho cột `[Cần Ôn Hôm Nay?]`:**
> ```javascript
> if(empty(prop("Lần Ôn Gần Nhất")), true, dateAdd(prop("Lần Ôn Gần Nhất"), prop("Chu Kỳ (Ngày)"), "days") <= now())
> ```

---

### 🗂️ Database 2: Nhật Ký Lỗi Sai Thực Hành (Reverse Engineering)

| Mã Sự Cố / Bài Lab | Thiết Bị Gặp Lỗi | Tầng OSI | Nguyên Nhân Gốc Rễ (Root Cause) | Cấu Hình Đã Làm (Sai) | Cấu Hình Chuẩn (Đúng) | Mức Độ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Lab Cafe - Lỗi 01: Mạng Wi-Fi rớt gói 40%** | AP Tầng 1 & AP Tầng 2 | Layer 1 (RF) | Nhiễu đồng kênh (Co-Channel Interference) | Cả 2 AP đều để Channel 1 | AP1: Ch 1 (2.4G) / Ch 36 (5G)<br/>AP2: Ch 6 (2.4G) / Ch 149 (5G) | 🚨 Cực kỳ nguy hiểm |
| **Lab Cafe - Lỗi 02: Kẹt "Obtaining IP..."** | Router DHCP Server | Layer 7 (DHCP) | Cạn kiệt IP do đặt Lease Time quá dài | Dùng /24 (254 IP) + Lease 8 ngày | Dùng /23 (510 IP) + Lease 2 giờ | 🚨 Cực kỳ nguy hiểm |
| **Lab Cafe - Lỗi 03: Khách scan thấy máy POS** | Cisco Switch 2960 | Layer 2 (VLAN) | Không phân tách mạng Khách và Nội bộ | Cắm tất cả vào VLAN 1 mặc định | POS: VLAN 10 (Access)<br/>AP Wi-Fi: VLAN 20 (Access) | 🚨 Lỗ hổng bảo mật |
| **Lab Cafe - Lỗi 04: 1 Khách kéo IDM sập mạng** | Router 2911 (QoS) | Layer 4/7 (Perf) | Không cấu hình giới hạn tốc độ người dùng | Mở không giới hạn băng thông | Giới hạn Per-IP: Down 6M / Up 2M | ⚠️ Ảnh hưởng vận hành |

---

## 📖 II. MASTER KNOWLEDGE BASE (FEYNMAN & 80/20)

<details>
<summary><b>▶ 1.1 Bản Chất Sóng RF, Vùng Phủ Sóng & Chuẩn Wi-Fi 6</b></summary>

- **Ẩn dụ Feynman:**
  - **Wi-Fi 5 (OFDM cũ) giống như xe taxi chỉ chở 1 người/chuyến**: Mỗi lần phát sóng chỉ phục vụ đúng 1 máy điện thoại, các máy khác phải xếp hàng chờ $\rightarrow$ Quán đông 100 người sẽ bị nghẽn tắc hàng đợi.
  - **Wi-Fi 6 (OFDMA mới) giống như xe bus chở nhiều người**: Một khung truyền sóng được chia thành nhiều ngăn nhỏ (**Resource Units - RU**), chở đồng thời dữ liệu cho 10-20 điện thoại cùng một lúc $\rightarrow$ Triệt tiêu độ trễ.
- **Quy luật Suy hao Sóng (Attenuation):**
  - Sàn bê tông cốt thép giữa tầng 1 và tầng 2 làm suy hao $\approx 20\text{dB}$ (mất $99\%$ năng lượng sóng).
  - *Quy tắc vàng*: **Không bao giờ dùng 1 AP phát xuyên tầng bê tông! Bắt buộc mỗi tầng 1 AP riêng.**
</details>

<details>
<summary><b>▶ 1.2 Công Thức Tính Toán Bắt Buộc (Capacity Planning Math)</b></summary>

1. **Bán kính Phủ sóng Hình chữ nhật ($15\text{m} \times 8\text{m}$):**
   $$R = \sqrt{\left(\frac{15}{2}\right)^2 + \left(\frac{8}{2}\right)^2} = \sqrt{7.5^2 + 4^2} \approx \mathbf{8.54 \text{ mét}}$$
2. **Số lượng IP Khả dụng Subnet `/23`:**
   $$\text{Số Host} = 2^{(32 - 23)} - 2 = 2^9 - 2 = \mathbf{510 \text{ IPs (Khả dụng)}}$$
3. **Băng thông Internet Đỉnh Điểm (Xem bóng đá Full HD):**
   $$BW_{\text{Total}} = (240 \times 20\% \times 5\text{ Mbps}) + (240 \times 80\% \times 1\text{ Mbps}) + 15\text{ Mbps} = \mathbf{447 \text{ Mbps}}$$
4. **Bộ 3 Kênh Không Chồng Lấn 2.4GHz:**
   - **Channel 1 (2.412 GHz)**, **Channel 6 (2.437 GHz)**, **Channel 11 (2.462 GHz)** (Độ rộng kênh: $20\text{MHz}$).
</details>

<details>
<summary><b>▶ 1.3 Quy Trình Triển Khai 4 Bước Chuẩn Doanh Nghiệp</b></summary>

1. **Bước 1 (Vật lý & RF)**: Gắn AP trần trung tâm mỗi tầng $\rightarrow$ Cài đặt kênh so le (T1: Ch 1/36; T2: Ch 6/149).
2. **Bước 2 (Phân hoạch L2/L3)**: Tạo VLAN 10 (Nội bộ/POS) và VLAN 20 (Wi-Fi Khách) $\rightarrow$ Gán Subnet `/23` cho VLAN 20.
3. **Bước 3 (Dịch vụ Mạng)**: Cấu hình DHCP Server với thời hạn mượn IP (Lease Time) ngắn ($2\text{ giờ}$).
4. **Bước 4 (Bảo mật & Kiểm thử)**: Cấu hình WPA2-Personal (AES) $\rightarrow$ Đo thông lượng và kiểm tra chuyển vùng (Roaming).
</details>

---

## 🧮 III. LAB THỰC HÀNH PACKET TRACER (PRACTICE LAB)

### 📋 Bảng Phân Bổ Địa Chỉ IP (IP Addressing Table)

| Thiết Bị (Device) | Interface | IP Address / Subnet | Default Gateway | VLAN ID | Chức Năng |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Router-2911** | `g0/0.10` | `192.168.10.1 /24` | N/A | VLAN 10 | Gateway Quản trị & Máy POS |
| **Router-2911** | `g0/0.20` | `192.168.20.1 /23` | N/A | VLAN 20 | Gateway Wi-Fi Khách (DHCP Server) |
| **Switch-2960** | `Vlan 10` | `192.168.10.2 /24` | `192.168.10.1` | VLAN 10 | Switch Management IP |
| **AP-Tang1** | `Port 0` | `192.168.10.11 /24` | `192.168.10.1` | VLAN 10 | AP Tầng 1 (Ch 1 / Ch 36) |
| **AP-Tang2** | `Port 0` | `192.168.10.12 /24` | `192.168.10.1` | VLAN 10 | AP Tầng 2 (Ch 6 / Ch 149) |
| **Máy POS** | `FastEth` | `192.168.10.50 /24` | `192.168.10.1` | VLAN 10 | Cố định IP tĩnh thu ngân |
| **Khách Tầng 1,2**| `Wireless`| *Cấp động qua DHCP* | `192.168.20.1` | VLAN 20 | Subnet `192.168.20.0/23` |

---

### 💻 1. Cấu hình Cisco Router 2911 (CLI)

```cisco
! === 1. BẬT CỔNG VẬT LÝ ===
Router> enable
Router# configure terminal
Router(config)# hostname Router-DUT-Coffee
Router-DUT-Coffee(config)# interface GigabitEthernet0/0
Router-DUT-Coffee(config-if)# no ip address
Router-DUT-Coffee(config-if)# no shutdown
Router-DUT-Coffee(config-if)# exit

! === 2. SUB-INTERFACE VLAN 10 (NỘI BỘ & POS) ===
Router-DUT-Coffee(config)# interface GigabitEthernet0/0.10
Router-DUT-Coffee(config-subif)# encapsulation dot1Q 10
Router-DUT-Coffee(config-subif)# ip address 192.168.10.1 255.255.255.0
Router-DUT-Coffee(config-subif)# exit

! === 3. SUB-INTERFACE VLAN 20 (WIFI KHÁCH SUBNET /23) ===
Router-DUT-Coffee(config)# interface GigabitEthernet0/0.20
Router-DUT-Coffee(config-subif)# encapsulation dot1Q 20
Router-DUT-Coffee(config-subif)# ip address 192.168.20.1 255.255.254.0
Router-DUT-Coffee(config-subif)# exit

! === 4. DỊCH VỤ DHCP SERVER CHO KHÁCH (LEASE 2 GIỜ) ===
Router-DUT-Coffee(config)# ip dhcp excluded-address 192.168.20.1 192.168.20.10
Router-DUT-Coffee(config)# ip dhcp pool GUEST_WIFI_POOL
Router-DUT-Coffee(dhcp-config)# network 192.168.20.0 255.255.254.0
Router-DUT-Coffee(dhcp-config)# default-router 192.168.20.1
Router-DUT-Coffee(dhcp-config)# dns-server 8.8.8.8 1.1.1.1
Router-DUT-Coffee(dhcp-config)# lease 0 2 0
Router-DUT-Coffee(dhcp-config)# exit
```

---

### 💻 2. Cấu hình Cisco Switch 2960 (CLI)

```cisco
Switch> enable
Switch# configure terminal
Switch(config)# hostname Switch-DUT-Coffee

! Khởi tạo VLAN
Switch-DUT-Coffee(config)# vlan 10
Switch-DUT-Coffee(config-vlan)# name POS_Internal
Switch-DUT-Coffee(config)# vlan 20
Switch-DUT-Coffee(config-vlan)# name Guest_Wifi
Switch-DUT-Coffee(config)# exit

! Cổng Trunk nối lên Router
Switch-DUT-Coffee(config)# interface GigabitEthernet0/1
Switch-DUT-Coffee(config-if)# switchport mode trunk
Switch-DUT-Coffee(config-if)# exit

! Cổng nối Máy POS (VLAN 10)
Switch-DUT-Coffee(config)# interface FastEthernet0/1
Switch-DUT-Coffee(config-if)# switchport mode access
Switch-DUT-Coffee(config-if)# switchport access vlan 10
Switch-DUT-Coffee(config-if)# spanning-tree portfast
Switch-DUT-Coffee(config-if)# exit

! Cổng nối 2 Access Point (VLAN 20)
Switch-DUT-Coffee(config)# interface range FastEthernet0/10, FastEthernet0/20
Switch-DUT-Coffee(config-if-range)# switchport mode access
Switch-DUT-Coffee(config-if-range)# switchport access vlan 20
Switch-DUT-Coffee(config-if-range)# spanning-tree portfast
Switch-DUT-Coffee(config-if-range)# exit
```

---

## 🎯 IV. TEMPLATE GHI CHÉP LỖI SAI (REVERSE ENGINEERING)

```markdown
### ❌ [SỰ CỐ LAB] - [Tên Dịch Vụ / Bài Tập]
- ❓ Hiện tượng / Triệu chứng: 
- 🔴 Cách cấu hình / Suy đoán ban đầu (Sai): 
- 🟢 Cách xử lý chuẩn (Đúng): 

- 🔍 PHÂN TÍCH GỐC RỄ (ROOT CAUSE ANALYSIS):
  * Tầng OSI bị lỗi: [Layer 1 / Layer 2 / Layer 3 / Layer 4 / Layer 7]
  * Tại sao cách cũ lại gây lỗi: 
  * Lệnh CLI kiểm tra nhanh: 

- 💡 Nguyên tắc khắc phục: 
```

---

## 🗓️ V. QUY TRÌNH HỌC TẬP HÀNG NGÀY (DAILY SOP)

- [ ] **Buổi Sáng (15 Phút)**: Mở Database 1 $\rightarrow$ Lọc `Cần Ôn Hôm Nay? = true` $\rightarrow$ Tự trả lời Flashcard trước khi mở đáp án.
- [ ] **Buổi Chiều/Tối (60 Phút)**: Mở Cisco Packet Tracer $\rightarrow$ Kéo thả thiết bị $\rightarrow$ Gõ lệnh cấu hình tại Mục III $\rightarrow$ Ping kiểm tra.
- [ ] **Buổi Đêm (15 Phút)**: Điền mọi lỗi sai gặp phải trong ngày vào Database 2.
