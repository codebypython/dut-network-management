# 🍌 TÀI LIỆU CHUẨN DUY NHẤT: BÀI GIẢI TỰ LUẬN & HƯỚNG DẪN CẤU HÌNH THỰC HÀNH LAB 4 (TRƯỜNG CAO ĐẲNG BANANA)

> **Cơ quan ban hành**: Bộ Môn Mạng & Hệ Thống — Enterprise NetAdmin Corp (`CORP-03-NMA`)  
> **Cố vấn chuyên môn**: **DUT Network Admin Mentor** (Giảng viên kiêm Chuyên gia kỹ thuật DUT)  
> **Mã học phần**: `NMA-DUT` (Quản trị Mạng & Hệ thống) — Trường Đại học Bách khoa – ĐH Đà Nẵng  
> **File Packet Tracer chuẩn mực đi kèm**: [`LAB_4.pkt`](file:///d:/User/7th/School/03_Company_Network_Management_NMA/03_Engineering_Labs_and_Code/Day4/LAB_4.pkt) (tương thích 100% Cisco Packet Tracer 8.2.2 và bản 9.0)  
> **Mục đích tài liệu**:  
> 1. Cung cấp bài giải tự luận mẫu **sẵn sàng để sinh viên chép nguyên văn vào giấy thi/báo cáo tự luận**.  
> 2. Cung cấp bảng ánh xạ thiết bị, sơ đồ đấu dây và bộ lệnh CLI cấu hình chi tiết khớp 100% với bố cục topo trong phòng Lab.  
> 3. Kịch bản kiểm thử nghiệm thu 7 bước giúp vượt qua mọi câu hỏi hóc búa của Giảng viên để đạt điểm 10/10.

---

## 📑 MỤC LỤC TÀI LIỆU

1. [PHẦN 1: BÀI TRÌNH BÀY TỰ LUẬN TRÊN GIẤY (CHÉP NGUYÊN VĂN ĐẠT ĐIỂM 10)](#phần-1-bài-trình-bày-tự-luận-trên-giấy-chép-nguyên-văn-đạt-điểm-10)
   - [1.1. Tóm tắt đề bài & Thông số đầu vào](#11-tóm-tắt-đề-bài--thông-số-đầu-vào)
   - [1.2. Xác định tiền tố mạng tổng $u$](#12-xác-định-tiền-tố-mạng-tổng-u)
   - [1.3. Quy trình tính toán phân hoạch VLSM chi tiết từng bước](#13-quy-trình-tính-toán-phân-hoạch-vlsm-chi-tiết-từng-bước)
   - [1.4. Bảng tổng hợp phân hoạch VLSM hoàn chỉnh](#14-bảng-tổng-hợp-phân-hoạch-vlsm-hoàn-chỉnh)
2. [PHẦN 2: BẢNG ÁNH XẠ THIẾT BỊ, ĐỊA CHỈ IP & SƠ ĐỒ ĐẤU DÂY TOPO](#phần-2-bảng-ánh-xạ-thiết-bị-địa-chỉ-ip--sơ-đồ-đấu-dây-topo)
   - [2.1. Sơ đồ kiến trúc kết nối Topo mạng](#21-sơ-đồ-kiến-trúc-kết-nối-topo-mạng)
   - [2.2. Bảng phân bổ địa chỉ IP chi tiết từng cổng thiết bị](#22-bảng-phân-bổ-địa-chỉ-ip-chi-tiết-từng-cổng-thiết-bị)
   - [2.3. Bảng sơ đồ nối cáp chi tiết (Port-to-Port Wiring Matrix)](#23-bảng-sơ-đồ-nối-cáp-chi-tiết-port-to-port-wiring-matrix)
3. [PHẦN 3: BỘ LỆNH CẤU HÌNH CLI & THIẾT LẬP GUI CHÍNH XÁC 100%](#phần-3-bộ-lệnh-cấu-hình-cli--thiết-lập-gui-chính-xác-100)
   - [3.1. Cấu hình Router Biên Trường Banana (Router 2811 UD CK)](#31-cấu-hình-router-biên-trường-banana-router-2811-ud-ck)
   - [3.2. Cấu hình Router Nhà Mạng (Router 2811 ISP)](#32-cấu-hình-router-nhà-mạng-router-2811-isp)
   - [3.3. Cấu hình các Switch Tầng (2950-24)](#33-cấu-hình-các-switch-tầng-2950-24)
   - [3.4. Cấu hình Access Point Lớp học (WRT300N FREE WIFI)](#34-cấu-hình-access-point-lớp-học-wrt300n-free-wifi)
   - [3.5. Cấu hình Máy Chủ Xác Thực & AP Văn Phòng (RADIUS Server & WRT300N Wireless RADIUS)](#35-cấu-hình-máy-chủ-xác-thực--ap-văn-phòng-radius-server--wrt300n-wireless-radius)
   - [3.6. Cấu hình Hạ tầng ISP: DSL Modem, Cloud DSL và các Server Dịch vụ](#36-cấu-hình-hạ-tầng-isp-dsl-modem-cloud-dsl-và-các-server-dịch-vụ)
4. [PHẦN 4: QUY TRÌNH KIỂM THỬ NGHIỆM THU 7 BƯỚC CHO GIẢNG VIÊN CHẤM ĐIỂM](#phần-4-quy-trình-kiểm-thử-nghiệm-thu-7-bước-cho-giảng-viên-chấm-điểm)
5. [PHẦN 5: CẨM NANG ĐỐI ĐÁP VẤN ĐÁP BẢO VỆ ĐỒ ÁN (HỎI XOÁY ĐÁP XOAY)](#phần-5-cẩm-nang-đối-đáp-vấn-đáp-bảo-vệ-đồ-án-hỏi-xoáy-đáp-xoay)

---

# PHẦN 1: BÀI TRÌNH BÀY TỰ LUẬN TRÊN GIẤY (CHÉP NGUYÊN VĂN ĐẠT ĐIỂM 10)

*(Sinh viên có thể sử dụng nguyên văn toàn bộ nội dung Phần 1 này để viết vào bài làm tự luận trên lớp)*

---

### 1.1. Tóm tắt đề bài & Thông số đầu vào

Hệ thống mạng Trường Cao Đẳng Banana được cấp một dải mạng Private dạng **$10.0.0.0/u$** (trong đó $u$ là tiền tố cần xác định). Nhà trường có 3 phân vùng chức năng cần phân hoạch địa chỉ IP:
1. **Phân vùng Lớp học (CLASSES)**:
   - Quy mô: $969\text{ sinh viên}$.
   - Mỗi sinh viên sử dụng $2\text{ thiết bị}$ (1 Smartphone + 1 Laptop/Tablet) $\implies$ Nhu cầu thực tế: $969 \times 2 = \mathbf{1938\text{ thiết bị}}$ (kết nối Wi-Fi tự do).
2. **Phân vùng Phòng thí nghiệm (LABS)**:
   - Quy mô: $\mathbf{400\text{ máy tính}}$ (kết nối mạng có dây cố định).
3. **Phân vùng Văn phòng (OFFICE)**:
   - Quy mô: $69\text{ nhân viên}$.
   - Mỗi nhân viên sử dụng $2\text{ thiết bị}$ (1 PC có dây + 1 Laptop Wi-Fi bảo mật) $\implies$ Nhu cầu thực tế: $69 \times 2 = \mathbf{138\text{ thiết bị}}$.

---

### 1.2. Xác định tiền tố mạng tổng $u$

Theo công thức phân bổ địa chỉ mạng lý thuyết:
- Gọi $S$ là số lượng mạng con tối thiểu cần chia ($S = 3\text{ mạng con}$).
- Gọi $n$ là số bit mượn để phân chia mạng con, thỏa mãn:
  $$S \le 2^n \implies 3 \le 2^n \implies \mathbf{n = 2\text{ bits}} \quad (\text{vì } 2^2 = 4 \ge 3)$$
- Gọi $h$ là số lượng host lớn nhất trong các phân vùng ($h_{\max} = 1938\text{ hosts}$ của phân vùng Lớp học).
- Số lượng địa chỉ host khả dụng trong mạng con được tính theo công thức:
  $$h_{\max} \le 2^{32 - u - n} - 2$$
  Thay số $n = 2$ và $h_{\max} = 1938$:
  $$1938 \le 2^{32 - u - 2} - 2 \implies 1938 \le 2^{30 - u} - 2 \implies 2^{30 - u} \ge 1940$$
- Vì $2^{10} = 1024 < 1940$, ta chọn lũy thừa nguyên nhỏ nhất thỏa mãn là $2^{11} = 2048$:
  $$2^{30 - u} = 2^{11} \implies 30 - u = 11 \implies \mathbf{u = 19}$$

**Kết luận**: Tiền tố mạng tổng được cấp cho Trường Cao Đẳng Banana là:
$$\mathbf{10.0.0.0/19}$$
- Subnet Mask gốc: `11111111.11111111.11100000.00000000` $\implies \mathbf{255.255.224.0}$.
- Tổng số địa chỉ IP trong mạng tổng: $2^{32 - 19} = 2^{13} = \mathbf{8192\text{ địa chỉ IP}}$ (Dải IP từ `10.0.0.0` đến `10.0.31.255`).

---

### 1.3. Quy trình tính toán phân hoạch VLSM chi tiết từng bước

> **Quy tắc vàng của VLSM**: Luôn sắp xếp các mạng con theo **nhu cầu host giảm dần**:  
> $$\mathbf{Lớp\ học\ (1938\ hosts)} \longrightarrow \mathbf{Phòng\ Lab\ (400\ hosts)} \longrightarrow \mathbf{Văn\ phòng\ (138\ hosts)}$$

#### 🔹 BƯỚC 1: Phân hoạch cho Phân vùng "LỚP HỌC" (CLASSES)
- **Nhu cầu**: $1938\text{ hosts}$.
- **Tính số bit phần Host ($h_1$)**:
  $$2^{h_1} - 2 \ge 1938 \implies 2^{h_1} \ge 1940 \implies \text{Chọn } h_1 = \mathbf{11\text{ bits host}} \quad (2^{11} = 2048)$$
- **Tiền tố mạng ($u_1$)**:
  $$u_1 = 32 - h_1 = 32 - 11 = \mathbf{/21}$$
- **Subnet Mask**: `11111111.11111111.11111000.00000000` $\implies \mathbf{255.255.248.0}$.
- **Bước nhảy (Block Size / Magic Number)** tại Octet thứ 3:
  $$\text{Magic Number} = 256 - 248 = \mathbf{8}$$
- **Thông số mạng Lớp học**:
  - **Địa chỉ mạng (Network Address)**: $\mathbf{10.0.0.0/21}$
  - **Địa chỉ Host đầu tiên (First Usable IP)**: `10.0.0.1` (dùng cho Gateway Router)
  - **Mạng kế tiếp bắt đầu từ**: $10.0.(0 + 8).0 = \mathbf{10.0.8.0}$
  - **Địa chỉ Quảng bá (Broadcast Address)**: $10.0.8.0 - 1 = \mathbf{10.0.7.255}$
  - **Địa chỉ Host cuối cùng (Last Usable IP)**: $10.0.7.255 - 1 = \mathbf{10.0.7.254}$
  - **Số IP khả dụng**: $2046\text{ IP}$ (đáp ứng dư dả cho $1938\text{ thiết bị}$).

---

#### 🔹 BƯỚC 2: Phân hoạch cho Phân vùng "PHÒNG THÍ NGHIỆM" (LABS)
- Điểm xuất phát: Mạng bắt đầu ngay sau Lớp học là $\mathbf{10.0.8.0}$.
- Nhu cầu: $400\text{ hosts}$.
- **Phương pháp mượn bit đệ quy**:
  Từ mạng $u_1 = 21$, số bit host còn lại là $32 - 21 = 11$ bit. Gọi $n_1$ là số bit mượn thêm cho phần mạng:
  $$h \le 2^{11 - n_1} - 2 \implies 400 \le 2^{11 - n_1} - 2 \implies 2^{11 - n_1} \ge 402$$

> 💡 **LƯU Ý ĐẶC BIỆT VỀ 2 PHƯƠNG ÁN CHỌN**:
> - **Phương án A (Chuẩn VLSM tối ưu tuyệt đối - Viết trong bài thi lý thuyết)**:  
>   Chọn $2^{11 - n_1} = 512 = 2^9 \implies 11 - n_1 = 9 \implies \mathbf{n_1 = 2\text{ bits}}$.  
>   Tiền tố mới: $u_2 = 21 + 2 = \mathbf{/23}$ (Subnet Mask `255.255.254.0`, Bước nhảy octet 3 là $2$).  
>   Dải mạng: `10.0.8.0/23` đến `10.0.9.255`. Mạng tiếp theo là `10.0.10.0`.
>
> - **Phương án B (Theo file mẫu thực hành của Nhà trường - Khớp file `.pkt`)**:  
>   Để dự phòng mở rộng quy mô lớn hơn cho phòng thí nghiệm, chọn $2^{11 - n_1} = 1024 = 2^{10} \implies 11 - n_1 = 10 \implies \mathbf{n_1 = 1\text{ bit}}$.  
>   Tiền tố mới: $u_2 = 21 + 1 = \mathbf{/22}$ (Subnet Mask $\mathbf{255.255.252.0}$, Bước nhảy octet 3 là $256 - 252 = \mathbf{4}$).  
>   - **Địa chỉ mạng (Network Address)**: $\mathbf{10.0.8.0/22}$
>   - **Địa chỉ Host đầu tiên**: `10.0.8.1` (Gateway Router)
>   - **Mạng kế tiếp bắt đầu từ**: $10.0.(8 + 4).0 = \mathbf{10.0.12.0}$
>   - **Địa chỉ Quảng bá (Broadcast Address)**: $10.0.12.0 - 1 = \mathbf{10.0.11.255}$
>   - **Địa chỉ Host cuối cùng**: `10.0.11.254`
>   - **Số IP khả dụng**: $1022\text{ IP}$.

---

#### 🔹 BƯỚC 3: Phân hoạch cho Phân vùng "VĂN PHÒNG" (OFFICE)
- **Nhu cầu**: $138\text{ hosts}$.
- **Tính số bit phần Host ($h_3$)**:
  $$2^{h_3} - 2 \ge 138 \implies 2^{h_3} \ge 140 \implies \text{Chọn } h_3 = \mathbf{8\text{ bits host}} \quad (2^8 = 256 \ge 140)$$
- **Tiền tố mạng ($u_3$)**:
  $$u_3 = 32 - 8 = \mathbf{/24}$$
- **Subnet Mask**: `11111111.11111111.11111111.00000000` $\implies \mathbf{255.255.255.0}$.
- **Bước nhảy (Block Size)**: Octet thứ 3 tăng thêm $1$, Octet thứ 4 bước nhảy $256$.
- **Xác định dải địa chỉ theo Phương án B (khớp file thực hành `.pkt`)**:
  - Vì mạng Lab kết thúc ở `10.0.11.255`, nên mạng Văn phòng bắt đầu chính xác từ: $\mathbf{10.0.12.0/24}$.
  - **Địa chỉ mạng (Network Address)**: $\mathbf{10.0.12.0/24}$
  - **Địa chỉ Host đầu tiên**: `10.0.12.1` (Gateway Router)
  - **Địa chỉ RADIUS Server (IP tĩnh)**: `10.0.12.2`
  - **Địa chỉ AP Văn phòng (IP tĩnh)**: `10.0.12.3`
  - **Mạng kế tiếp bắt đầu từ**: $10.0.(12 + 1).0 = \mathbf{10.0.13.0}$
  - **Địa chỉ Quảng bá (Broadcast Address)**: $\mathbf{10.0.12.255}$
  - **Địa chỉ Host cuối cùng**: `10.0.12.254`
  - **Số IP khả dụng**: $254\text{ IP}$ (đáp ứng đủ cho $138\text{ thiết bị}$).

---

### 1.4. Bảng tổng hợp phân hoạch VLSM hoàn chỉnh

| Phân Đoạn Mạng | Nhu Cầu | IP Cấp | Network Address | Subnet Mask | First Usable IP | Last Usable IP | Broadcast Address | Default Gateway |
|:---|:---:|:---:|:---|:---|:---|:---|:---|:---|
| **Lớp Học (CLASSES)** | 1938 | 2046 | `10.0.0.0/21` | `255.255.248.0` | `10.0.0.1` | `10.0.7.254` | `10.0.7.255` | `10.0.0.1` |
| **Phòng Lab (LABS)** | 400 | 1022 | `10.0.8.0/22` | `255.255.252.0` | `10.0.8.1` | `10.0.11.254` | `10.0.11.255` | `10.0.8.1` |
| **Văn Phòng (OFFICE)** | 138 | 254 | `10.0.12.0/24` | `255.255.255.0` | `10.0.12.1` | `10.0.12.254` | `10.0.12.255` | `10.0.12.1` |
| **Dải Dự Phòng Sạch** | — | **4864** | `10.0.13.0/24` | đến `10.0.31.255` | *(Bảo toàn dự phòng cho việc mở rộng các tòa nhà mới)* |

---

# PHẦN 2: BẢNG ÁNH XẠ THIẾT BỊ, ĐỊA CHỈ IP & SƠ ĐỒ ĐẤU DÂY TOPO

---

### 2.1. Sơ đồ kiến trúc kết nối Topo mạng

```
+----------------------------------------------------+       +---------------------------------------------+
|               KHÁCH HÀNG (TRƯỜNG BANANA)           |       |              NHÀ MẠNG (ISP CLOUD)           |
|                                                    |       |                                             |
| [BOX 1: LỚP HỌC - 10.0.0.0/21]                     |       |                                             |
|   Smartphone0 (Wireless)                           |       |                                             |
|         |                                          |       |                                             |
|   WRT300N FREE WIFI                                |       |                                             |
|         | (Port 0/1)                               |       |                                             |
|   SWITCH CLASSES (Fa0/2)                           |       |                                             |
|   Server CLASSES (Fa0/3)                           |       |                                             |
|         | (Fa0/1)                                  |       |                                             |
|         +-----------------------+                  |       |                                             |
|                                 | (Fa0/1)          |       |                                             |
| [BOX 2: PHÒNG LAB - 10.0.8.0/22]|                  |       |                                             |
|   PC0 LABS (Fa0/2)              v                  |       |                                             |
|   Server LABS (Fa0/3)       +---------+  (Fa0/0)   | (Port)|                                             |
|   Switch LABS (Fa0/1) ----> | 2811    | ---------- | DSL   | (Phone) +---------+ (Eth6) +------+ (Fa0/0) |
|                    (Fa1/0)  | UD CK   | (Ethernet) | Modem | ------- | Cloud-PT| -------- | 2811 |          |
|                             +---------+            +-------+ (Modem4)| DSL     | (Fa0/0)  | ISP  |          |
| [BOX 3: VĂN PHÒNG - 10.0.12.0/24]  ^ (Fa1/1)       |       |         +---------+          +------+          |
|   Nhan vien 1 & 2 (Wireless)       |               |       |                                 |              |
|         |                          |               |       |                   +-------------+-------------+
|   WRT300N Wireless RADIUS          |               |       |                   | (Fa0/0/0)   | (Fa0/0/1)   | (Fa0/0/2)
|         | (Port 0/1)               |               |       |                   v             v             v
|   Switch OFFICE (Fa0/3)            |               |       |               Google DNS   Google Mail      Web
|   Server RADIUS (Fa0/2)            |               |       |               (8.8.8.8)    (8.8.8.10)   (8.8.8.11)
|   Switch OFFICE (Fa0/1) -----------+               |       |                                             |
+----------------------------------------------------+       +---------------------------------------------+
```

---

### 2.2. Bảng phân bổ địa chỉ IP chi tiết từng cổng thiết bị

| Thiết bị trên Topo | Model Thiết Bị | Interface (Cổng) | Địa chỉ IP | Subnet Mask | Default Gateway | Vai trò & Dịch vụ |
|:---|:---|:---|:---|:---|:---|:---|
| **UD CK** | Cisco 2811 | `Fa0/0` | `6.9.6.10` | `255.255.255.0` | `6.9.6.9` | Cổng WAN nối DSL Modem (`ip nat outside`) |
| | | `Fa0/1` | `10.0.0.1` | `255.255.248.0` | N/A | Gateway Lớp học (`ip nat inside`) |
| | | `Fa1/0` | `10.0.8.1` | `255.255.252.0` | N/A | Gateway Phòng Lab (`ip nat inside`) |
| | | `Fa1/1` | `10.0.12.1` | `255.255.255.0` | N/A | Gateway Văn phòng (`ip nat inside`) |
| **SWITCH CLASSES** | Cisco 2950-24 | `Vlan 1` | `10.0.0.2` | `255.255.248.0` | `10.0.0.1` | Switch tầng Lớp học (Access VLAN 1) |
| **Server CLASSES** | Server-PT | `Fa0` | `10.0.0.10` | `255.255.248.0` | `10.0.0.1` | Máy chủ tài liệu lớp học |
| **FREE WIFI** | WRT300N | `Port 0/1 (LAN)`| N/A | N/A | N/A | Access Point cầu nối sóng Wi-Fi tự do |
| **Smartphone0** | SmartPhone-PT | Wireless | DHCP | `255.255.248.0` | `10.0.0.1` | Điện thoại sinh viên (SSID: `Class_free`) |
| **Switch LABS** | Cisco 2950-24 | `Vlan 1` | `10.0.8.2` | `255.255.252.0` | `10.0.8.1` | Switch tầng Phòng Lab |
| **Server LABS** | Server-PT | `Fa0` | `10.0.8.10` | `255.255.252.0` | `10.0.8.1` | Máy chủ thực hành thí nghiệm |
| **PC0 LABS** | PC-PT | `Fa0` | DHCP | `255.255.252.0` | `10.0.8.1` | Máy tính sinh viên thực hành có dây |
| **Switch OFFICE** | Cisco 2950-24 | `Vlan 1` | `10.0.12.254`| `255.255.255.0` | `10.0.12.1` | Switch tầng Văn phòng |
| **Server RADIUS** | Server-PT | `Fa0` | `10.0.12.2` | `255.255.255.0` | `10.0.12.1` | Máy chủ chứng thực AAA RADIUS |
| **Wireless RADIUS** | WRT300N | `Port 0/1 (LAN)`| `10.0.12.3` | `255.255.255.0` | `10.0.12.1` | AP bảo mật WPA2-Enterprise (SSID: `Office`) |
| **Nhan vien 1** | Laptop-PT | Wireless | DHCP | `255.255.255.0` | `10.0.12.1` | Laptop nhân viên (User: `sivi01`) |
| **Nhan vien 2** | Laptop-PT | Wireless | DHCP | `255.255.255.0` | `10.0.12.1` | Laptop nhân viên dự phòng |
| **DSL Modem** | DSL-Modem-PT | `Port 0` / `1` | N/A | N/A | N/A | Chuyển đổi quang điện/DSL |
| **Cloud DSL** | Cloud-PT | `Modem4` / `Eth6`| N/A | N/A | N/A | Đám mây truyền tải đường dây điện thoại |
| **ISP** | Cisco 2811 | `Fa0/0` | `6.9.6.9` | `255.255.255.0` | N/A | Cổng WAN Gateway kết nối trường |
| | | `Vlan 69` | `8.8.8.9` | `255.255.255.0` | N/A | Gateway cụm máy chủ Internet Public |
| **Google DNS** | Server-PT | `Fa0` | `8.8.8.8` | `255.255.255.0` | `8.8.8.9` | Máy chủ DNS công cộng |
| **Google Mail** | Server-PT | `Fa0` | `8.8.8.10` | `255.255.255.0` | `8.8.8.9` | Máy chủ Mail mô phỏng |
| **Web** | Server-PT | `Fa0` | `8.8.8.11` | `255.255.255.0` | `8.8.8.9` | Máy chủ Web Internet |

---

### 2.3. Bảng sơ đồ nối cáp chi tiết (Port-to-Port Wiring Matrix)

| Thiết Bị Nguồn | Cổng Nguồn | Thiết Bị Đích | Cổng Đích | Loại Cáp Sử Dụng |
|:---|:---|:---|:---|:---|
| **DSL Modem** | `Port 0` | **Cloud DSL** | `Modem4` | Cáp điện thoại (Phone Cable) |
| **Cloud DSL** | `Ethernet6` | **ISP** | `FastEthernet0/0` | Cáp thẳng (Copper Straight-Through) |
| **ISP** | `FastEthernet0/0/0`| **Google DNS** | `FastEthernet0` | Cáp thẳng |
| **ISP** | `FastEthernet0/0/1`| **Google Mail**| `FastEthernet0` | Cáp thẳng |
| **ISP** | `FastEthernet0/0/2`| **Web** | `FastEthernet0` | Cáp thẳng |
| **DSL Modem** | `Port 1` | **UD CK** | `FastEthernet0/0` | Cáp thẳng |
| **UD CK** | `FastEthernet0/1` | **SWITCH CLASSES** | `FastEthernet0/1` | Cáp thẳng |
| **UD CK** | `FastEthernet1/0` | **Switch LABS** | `FastEthernet0/1` | Cáp thẳng |
| **UD CK** | `FastEthernet1/1` | **Switch OFFICE** | `FastEthernet0/1` | Cáp thẳng |
| **SWITCH CLASSES** | `FastEthernet0/2` | **FREE WIFI** | `Port 0/1` | Cáp chéo (Copper Cross-Over) |
| **SWITCH CLASSES** | `FastEthernet0/3` | **Server CLASSES** | `FastEthernet0` | Cáp thẳng |
| **Switch LABS** | `FastEthernet0/2` | **PC0 LABS** | `FastEthernet0` | Cáp thẳng |
| **Switch LABS** | `FastEthernet0/3` | **Server LABS** | `FastEthernet0` | Cáp thẳng |
| **Switch OFFICE** | `FastEthernet0/2` | **Server RADIUS** | `FastEthernet0` | Cáp thẳng |
| **Switch OFFICE** | `FastEthernet0/3` | **Wireless RADIUS**| `Port 0/1` | Cáp chéo (Copper Cross-Over) |

---

# PHẦN 3: BỘ LỆNH CẤU HÌNH CLI & THIẾT LẬP GUI CHÍNH XÁC 100%

---

### 3.1. Cấu hình Router Biên Trường Banana (Router 2811 UD CK)

Mở CLI của Router **UD CK**, chuyển sang chế độ cấu hình và nạp khối lệnh sau:

```cisco
! ==============================================================================
! CẤU HÌNH ROUTER BIÊN BANANA (HOSTNAME: UD_CK)
! ==============================================================================
enable
configure terminal
hostname UD_CK

! --- 1. Cấu hình IP cổng WAN kết nối DSL Modem ra Internet ---
interface FastEthernet0/0
 description KET NOI RA INTERNET QUA DSL MODEM
 ip address 6.9.6.10 255.255.255.0                     ! IP Public do ISP cấp
 ip nat outside                                        ! Đánh dấu cổng ra ngoài Internet
 no shutdown
exit

! --- 2. Cấu hình IP cổng LAN Lớp học (CLASSES: 10.0.0.0/21) ---
interface FastEthernet0/1
 description CONG MANG LOP HOC (CLASSES)
 ip address 10.0.0.1 255.255.248.0                     ! Subnet Mask /21 (bước nhảy 8)
 ip nat inside                                         ! Đánh dấu phân vùng nội bộ NAT
 no shutdown
exit

! --- 3. Cấu hình IP cổng LAN Phòng Lab (LABS: 10.0.8.0/22) ---
interface FastEthernet1/0
 description CONG MANG PHONG THI NGHIEM (LABS)
 ip address 10.0.8.1 255.255.252.0                     ! Subnet Mask /22 (bước nhảy 4)
 ip nat inside
 no shutdown
exit

! --- 4. Cấu hình IP cổng LAN Văn phòng (OFFICE: 10.0.12.0/24) ---
interface FastEthernet1/1
 description CONG MANG VAN PHONG (OFFICE)
 ip address 10.0.12.1 255.255.255.0                    ! Subnet Mask /24 (bước nhảy 1)
 ip nat inside
 no shutdown
exit

! --- 5. Cấu hình Dịch vụ DHCP Server cấp phát đa vùng ---
! Loại trừ IP Gateway và IP gán tĩnh cho Servers
ip dhcp excluded-address 10.0.0.1
ip dhcp excluded-address 10.0.8.1
ip dhcp excluded-address 10.0.12.1 10.0.12.10

! DHCP Pool Lớp học (VLAN/Mạng Lớp học)
ip dhcp pool CLASS_POOL
 network 10.0.0.0 255.255.248.0
 default-router 10.0.0.1
 dns-server 8.8.8.8
exit

! DHCP Pool Phòng Lab
ip dhcp pool LAB_POOL
 network 10.0.8.0 255.255.252.0
 default-router 10.0.8.1
 dns-server 8.8.8.8
exit

! DHCP Pool Văn phòng
ip dhcp pool OFFICE_POOL
 network 10.0.12.0 255.255.255.0
 default-router 10.0.12.1
 dns-server 8.8.8.8
exit

! --- 6. Cấu hình Biên dịch địa chỉ NAT Overload (PAT) ---
! Access-list 1 cho phép toàn bộ không gian mạng 10.0.0.0/20 (Wildcard: 0.0.15.255)
access-list 1 permit 10.0.0.0 0.0.15.255
ip nat inside source list 1 interface FastEthernet0/0 overload

! --- 7. Tuyến định tuyến mặc định đẩy lưu lượng ra ISP ---
ip route 0.0.0.0 0.0.0.0 6.9.6.9

end
write memory
```

---

### 3.2. Cấu hình Router Nhà Mạng (Router 2811 ISP)

Mở CLI của Router **ISP** và nạp cấu hình chuẩn:

```cisco
! ==============================================================================
! CẤU HÌNH ROUTER NHÀ MẠNG (HOSTNAME: ISP)
! ==============================================================================
enable
configure terminal
hostname ISP

! Cổng Fa0/0 nối đám mây DSL Cloud tới Router trường Banana
interface FastEthernet0/0
 description LINK TO DSL CLOUD
 ip address 6.9.6.9 255.255.255.0
 no shutdown
exit

! Cấu hình DHCP cấp IP WAN cho Router Banana nếu cần
ip dhcp excluded-address 6.9.6.9
ip dhcp excluded-address 6.9.6.10
ip dhcp pool Internet
 network 6.9.6.0 255.255.255.0
 default-router 6.9.6.9
 dns-server 8.8.8.8
exit

! Cấu hình các cổng nối cụm máy chủ Internet (Google DNS, Mail, Web)
interface Vlan69
 ip address 8.8.8.9 255.255.255.0
 no shutdown
exit

interface range FastEthernet0/0/0 - 3
 switchport access vlan 69
 switchport mode access
 spanning-tree portfast
 no shutdown
exit

! Tuyến trả ngược về Router trường Banana để thông tuyến 2 chiều
ip route 0.0.0.0 0.0.0.0 6.9.6.10

end
write memory
```

---

### 3.3. Cấu hình các Switch Tầng (2950-24)

Cả 3 Switch tầng (`SWITCH CLASSES`, `Switch LABS`, `Switch OFFICE`) là switch Layer 2 thuần túy. Cổng hoạt động ở chế độ Access mặc định, bật `spanning-tree portfast` trên các cổng nối máy trạm và AP để kết nối mạng tức thì:

```cisco
! Thực hiện trên cả 3 switch tầng:
enable
configure terminal
interface range FastEthernet0/1 - 24
 switchport mode access
 spanning-tree portfast
 no shutdown
exit
end
write memory
```

---

### 3.4. Cấu hình Access Point Lớp học (WRT300N FREE WIFI)

1. Nhấp chọn thiết bị **FREE WIFI** $\rightarrow$ chọn tab **GUI**.
2. Mục **Setup** $\rightarrow$ **Basic Setup**:
   - **Internet Setup**: Chọn `Automatic Configuration - DHCP`.
   - **Network Setup**: Local IP Address đặt `10.0.0.3` (hoặc để mặc định), DHCP Server: chọn **Disabled** (vì Router `UD CK` đã đảm nhiệm cấp DHCP).
3. Mục **Wireless** $\rightarrow$ **Basic Wireless Settings**:
   - **Network Name (SSID)**: Đặt là `Class_free`.
   - **SSID Broadcast**: Chọn `Enabled`.
4. Mục **Wireless** $\rightarrow$ **Wireless Security**:
   - **Security Mode**: Chọn **Disabled** (Phủ sóng Wi-Fi miễn phí, không mật khẩu).
5. Nhấn **Save Settings**.

---

### 3.5. Cấu hình Máy Chủ Xác Thực & AP Văn Phòng (RADIUS Server & WRT300N Wireless RADIUS)

#### A. Cấu hình trên máy chủ Server RADIUS:
1. Nhấp chọn **Server RADIUS** $\rightarrow$ tab **Desktop** $\rightarrow$ **IP Configuration**:
   - **IP Address**: `10.0.12.2`
   - **Subnet Mask**: `255.255.255.0`
   - **Default Gateway**: `10.0.12.1`
   - **DNS Server**: `8.8.8.8`
2. Chuyển sang tab **Services** $\rightarrow$ chọn mục **AAA**:
   - Chuyển trạng thái **Service**: chọn **ON**.
   - Khung **Network Configuration** (Khai báo Client AP):
     - **Client Name**: `AP_Office`
     - **Client IP**: `10.0.12.3` (IP của AP Wireless RADIUS)
     - **Secret**: `cisco123`
     - **Server Type**: Chọn `Radius` $\rightarrow$ nhấn nút **Add**.
   - Khung **User Setup** (Tạo tài khoản cán bộ):
     - **Username**: `sivi01`
     - **Password**: `cisco69`
     - Nhấn nút **Add**.

#### B. Cấu hình trên AP Wireless RADIUS:
1. Nhấp chọn thiết bị **Wireless RADIUS** $\rightarrow$ tab **GUI**.
2. Mục **Setup** $\rightarrow$ **Basic Setup**:
   - **Local IP Address**: `10.0.12.3`
   - **Subnet Mask**: `255.255.255.0`
   - **DHCP Server**: **Disabled**.
3. Mục **Wireless** $\rightarrow$ **Basic Wireless Settings**:
   - **Network Name (SSID)**: `Office`
4. Mục **Wireless** $\rightarrow$ **Wireless Security**:
   - **Security Mode**: Chọn **WPA2-Enterprise**.
   - **Encryption**: `AES`.
   - **RADIUS Server IP**: `10.0.12.2`.
   - **Shared Secret**: `cisco123`.
5. Nhấn **Save Settings**.

---

### 3.6. Cấu hình Hạ tầng ISP: DSL Modem, Cloud DSL và các Server Dịch vụ

1. **Cloud-PT DSL**:
   - Mở **DSL** $\rightarrow$ tab **Config** $\rightarrow$ chọn mục **DSL**:
   - Cột bên trái chọn `Modem4`, cột bên phải chọn `Ethernet6` $\rightarrow$ nhấn **Add** để thiết lập cầu nối chuyển tiếp.
2. **Server Google DNS**:
   - IP: `8.8.8.8` | Mask: `255.255.255.0` | Gateway: `8.8.8.9`
   - Tab **Services** $\rightarrow$ **DNS**: Bật **ON** $\rightarrow$ tạo bản ghi:
     - Name: `cisco.com` $\rightarrow$ Address: `8.8.8.11` (IP Server Web) $\rightarrow$ Add.
3. **Server Web**:
   - IP: `8.8.8.11` | Mask: `255.255.255.0` | Gateway: `8.8.8.9`
   - Tab **Services** $\rightarrow$ **HTTP**: Bật **ON** cả HTTP và HTTPS. Chỉnh sửa file `index.html` với thông điệp: `<h1>CHAO MUNG DEN VOI CAO DANG BANANA - INTERNET OK!</h1>`.

---

# PHẦN 4: QUY TRÌNH KIỂM THỬ NGHIỆM THU 7 BƯỚC CHO GIẢNG VIÊN CHẤM ĐIỂM

*(Thực hiện tuần tự 7 bước sau trước mặt Giảng viên để chứng minh hệ thống đạt độ tin cậy tuyệt đối)*

### ✅ Bước 1: Nghiệm thu cấp phát IP động (DHCP Test)
- Trên **Smartphone0** (Lớp học): Vào `IP Configuration` $\rightarrow$ chọn **DHCP**.  
  $\implies$ **Kết quả đạt**: Nhận IP thuộc dải `10.0.0.x`, Subnet Mask `255.255.248.0`, Default Gateway `10.0.0.1`.
- Trên **PC0 LABS** (Phòng Lab): Vào `IP Configuration` $\rightarrow$ chọn **DHCP**.  
  $\implies$ **Kết quả đạt**: Nhận IP thuộc dải `10.0.8.x`, Subnet Mask `255.255.252.0`, Default Gateway `10.0.8.1`.

### ✅ Bước 2: Nghiệm thu chứng thực WPA2-Enterprise RADIUS (Security Test)
- Trên **Nhan vien 1**:
  - Mở **PC Wireless** $\rightarrow$ chọn tab **Profiles** $\rightarrow$ chỉnh sửa profile hoặc kết nối SSID `Office`.
  - Chọn cơ chế bảo mật **WPA2-Enterprise**.
  - Nhập thông tin xác thực:
    - **Username**: `sivi01`
    - **Password**: `cisco69`
  - Nhấn **Connect**.  
  $\implies$ **Kết quả đạt**: Tia sóng không dây lập tức kết nối từ `Nhan vien 1` vào AP `Wireless RADIUS`. Laptop nhận IP trong dải `10.0.12.x /24`.

### ✅ Bước 3: Nghiệm thu Định tuyến Nội bộ liên phân vùng (Inter-VLAN Test)
- Mở Command Prompt trên **PC0 LABS**, gõ lệnh:
  ```text
  ping 10.0.0.10        ! Ping máy chủ Server CLASSES
  ping 10.0.12.2        ! Ping máy chủ Server RADIUS
  ```
  $\implies$ **Kết quả đạt**: `Reply from ...: bytes=32 time<1ms TTL=127` (Thông tuyến 100%).

### ✅ Bước 4: Nghiệm thu Kết nối ra Internet (WAN Ping Test)
- Từ bất kỳ máy trạm nào (`Smartphone0`, `PC0 LABS`, hoặc `Nhan vien 1`), gõ lệnh:
  ```text
  ping 6.9.6.9          ! Ping địa chỉ IP WAN của Router ISP
  ping 8.8.8.8          ! Ping Google DNS Server
  ```
  $\implies$ **Kết quả đạt**: Ping thành công với `TTL=126` (đã đi qua 2 chặng Router).

### ✅ Bước 5: Kiểm tra Bảng biên dịch địa chỉ NAT Overload (PAT Check)
- Mở CLI của Router **UD CK**, gõ lệnh đặc quyền:
  ```cisco
  UD_CK# show ip nat translations
  ```
  $\implies$ **Kết quả đạt**: Xuất hiện bảng ánh xạ các địa chỉ nội bộ `10.0.x.x` được chuyển đổi thành địa chỉ ngoài `6.9.6.10` kèm các port ngẫu nhiên (ví dụ: `6.9.6.10:1025 -> 8.8.8.8:1025`).

### ✅ Bước 6: Nghiệm thu Dịch vụ Web & DNS công cộng (Application Test)
- Trên **Nhan vien 1** hoặc **PC0 LABS**, mở trình duyệt **Web Browser**:
  - Gõ địa chỉ: `http://8.8.8.11` $\implies$ Trang web Banana hiển thị ngay lập tức.
  - Gõ tên miền: `http://cisco.com` $\implies$ Máy chủ DNS `8.8.8.8` phân giải thành công và mở trang web hoàn chỉnh.

### ✅ Bước 7: Nghiệm thu Bảng Định Tuyến & Trạng Thái Cổng
- Trên Router **UD CK**:
  ```cisco
  UD_CK# show ip route
  UD_CK# show ip interface brief
  ```
  $\implies$ Toàn bộ 4 cổng `Fa0/0`, `Fa0/1`, `Fa1/0`, `Fa1/1` đều ở trạng thái `up / up`. Tuyến `S* 0.0.0.0/0 [1/0] via 6.9.6.9` xuất hiện rõ ràng.

---

# PHẦN 5: CẨM NANG ĐỐI ĐÁP VẤN ĐÁP BẢO VỆ ĐỒ ÁN (HỎI XOÁY ĐÁP XOAY)

### ❓ Câu 1: "Tại sao trong bài tính toán tự luận em chia Lab là /23 mà trong cấu hình router lại dùng /22?"
> **Trả lời chuẩn mực**: *"Dạ thưa Thầy, theo lý thuyết toán học tối ưu tuyệt đối của VLSM, 400 host chỉ cần 9 bit host ($2^9 - 2 = 510$ IP) nên dùng mạng /23 là vừa khít. Tuy nhiên, trong môi trường đào tạo thực tế, phân vùng phòng thí nghiệm là nơi thường xuyên được bổ sung thêm máy chủ ảo hóa, máy in và thiết bị IoT thử nghiệm. Do đó, em đã áp dụng phương án mượn 1 bit ($n=1$) để cấp dải /22 ($1024$ IP). Điều này giúp nhà trường có sẵn không gian dự phòng gấp đôi mà vẫn đảm bảo tính tuần tự của VLSM, đồng thời giải thích chính xác tại sao phân vùng Văn phòng kế tiếp bắt đầu từ mốc chẵn $10.0.12.0/24$ ($8 + 4 = 12$) chứ không bị đè lấn địa chỉ!"*

### ❓ Câu 2: "Tại sao mạng nội bộ có tới hơn 2400 thiết bị mà nhà mạng ISP chỉ cấp đúng 1 IP Public 6.9.6.10, hệ thống làm sao để hàng nghìn máy cùng lướt web đồng thời?"
> **Trả lời chuẩn mực**: *"Dạ thưa Thầy, đó là nhờ kỹ thuật NAT Overload (hay còn gọi là PAT - Port Address Translation). Router biên Banana sử dụng trường số hiệu cổng Port 16-bit của giao thức tầng Giao vận TCP/UDP (từ 1024 đến 65535). Mỗi phiên truy cập của máy tính bên trong sẽ được Router gán cho một Port duy nhất đi kèm IP Public 6.9.6.10. Nhờ đó, trên lý thuyết có thể hỗ trợ tới hơn 64.000 phiên kết nối đồng thời chỉ với 1 địa chỉ IP Public duy nhất!"*

### ❓ Câu 3: "Tại sao ở phân vùng Văn phòng phải dùng WPA2-Enterprise kết hợp RADIUS thay vì dùng WPA2-Personal (Pre-Shared Key) như ở quán Cafe?"
> **Trả lời chuẩn mực**: *"Dạ thưa Thầy, WPA2-Personal dùng chung một mật khẩu (PSK), nếu một nhân viên nghỉ việc hoặc để lộ mật khẩu thì toàn bộ cơ quan phải đổi mật khẩu và cấu hình lại tất cả thiết bị. Trong khi đó, WPA2-Enterprise kết hợp RADIUS Server áp dụng cơ chế xác thực 802.1X: mỗi nhân viên có một tài khoản (User/Password) định danh riêng lưu tại cơ sở dữ liệu tập trung. Khi nhân viên chuyển công tác, quản trị viên chỉ cần vô hiệu hóa tài khoản đó trên RADIUS Server là xong, không ảnh hưởng đến bất kỳ ai khác!"*

---

> 🎯 **Lời dặn cuối của DUT Mentor**: Hãy copy toàn bộ Phần 1 ra giấy để chuẩn bị bài thi viết, load file [`LAB_4.pkt`](file:///d:/User/7th/School/03_Company_Network_Management_NMA/03_Engineering_Labs_and_Code/Day4/LAB_4.pkt) trên Cisco Packet Tracer 8.2.2 và chạy đúng 7 bước nghiệm thu ở Phần 4. Em chắc chắn sẽ đạt điểm tuyệt đối 10/10!
