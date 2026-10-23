# 📐 BIỂU MẪU CHUẨN: TÍNH TOÁN & THIẾT KẾ PHÂN HOẠCH MẠNG VLSM (MASTER TEMPLATE)

> **Cơ quan ban hành**: NetAdmin Holdings — Trường Đại học Bách khoa – ĐH Đà Nẵng (DUT)  
> **Mã quy chuẩn**: `NMA-TEMPLATE-VLSM-PRO-v1.0`  
> **Mục đích**: Cung cấp khung mẫu kỹ thuật chuẩn hóa 100% để sinh viên/kỹ sư chỉ cần **thay số theo đề bài** là có ngay báo cáo thiết kế mạng VLSM hoàn chỉnh, bảng IP chuẩn mực và bộ lệnh cấu hình Cisco IOS không thể bắt bẻ.  
> **Áp dụng cho**: Mọi bài toán phân hoạch mạng con IPv4 từ cơ bản đến nâng cao (Lab thực hành, Đồ án môn học, Chứng chỉ CCNA/Enterprise).  

---

## 📑 MỤC LỤC BIỂU MẪU

1. [Bảng Tra Cứu Nhanh Thông Số Nhị Phân & Block Size (Cheat Sheet)](#1-bảng-tra-cứu-nhanh-thông-số-nhị-phân--block-size-cheat-sheet)
2. [Khung Thu Thập Dữ Kiện Đầu Bài (Input Parameter Matrix)](#2-khung-thu-thập-dữ-kiện-đầu-bài-input-parameter-matrix)
3. [Quy Trình Xác Định Tiền Tố Mạng Tổng $u$ (Nếu Đề Yêu Cầu Tìm $u$)](#3-quy-trình-xác-định-tiền-tố-mạng-tổng-u-nếu-đề-yêu-cầu-tìm-u)
4. [Quy Trình Phân Hoạch VLSM Chuẩn Mực 5 Bước (Điền Số Tự Động)](#4-quy-trình-phân-hoạch-vlsm-chuẩn-mực-5-bước-điền-số-tự-động)
5. [Bảng Tổng Hợp VLSM & Bảng Phân Bổ IP Chi Tiết (Sẵn Sàng Copy)](#5-bảng-tổng-hợp-vlsm--bảng-phân-bổ-ip-chi-tiết-sẵn-sàng-copy)
6. [Bộ Khung Lệnh Cấu Hình Cisco IOS Mẫu (Chỉ Cần Thay Biến)](#6-bộ-khung-lệnh-cấu-hình-cisco-ios-mẫu-chỉ-cần-thay-biến)
7. [Kịch Bản Kiểm Thử & Nghiệm Thu Bảng Định Tuyến](#7-kịch-bản-kiểm-thử--nghiệm-thu-bảng-định-tuyến)
8. [Checklist Tự Kiểm Tra Chống Lỗi Đè Mạng (Sanity Check)](#8-checklist-tự-kiểm-tra-chống-lỗi-đè-mạng-sanity-check)

---

## 1. BẢNG TRA CỨU NHANH THÔNG SỐ NHỊ PHÂN & BLOCK SIZE (CHEAT SHEET)

*Khi tính toán, chỉ cần tra bảng này để lấy ngay số bit host ($h$), tiền tố ($/Prefix$), Subnet Mask và Bước nhảy (Block Size):*

| Số bit Host ($h$) | Tổng IP ($2^h$) | IP Khả Dụng ($2^h - 2$) | Tiền tố ($/Prefix$) | Subnet Mask thập phân | Octet biến thiên | Bước nhảy (Block Size) |
| :---: | :---: | :---: | :---: | :--- | :---: | :---: |
| **$h = 1$** | 2 | 0 (Chỉ làm P2P /31 RFC 3021)| **/31** | `255.255.255.254` | Octet 4 | $2$ |
| **$h = 2$** | 4 | **2** (Đường truyền WAN) | **/30** | `255.255.255.252` | Octet 4 | $4$ |
| **$h = 3$** | 8 | 6 | **/29** | `255.255.255.248` | Octet 4 | $8$ |
| **$h = 4$** | 16 | 14 | **/28** | `255.255.255.240` | Octet 4 | $16$ |
| **$h = 5$** | 32 | 30 | **/27** | `255.255.255.224` | Octet 4 | $32$ |
| **$h = 6$** | 64 | 62 | **/26** | `255.255.255.192` | Octet 4 | $64$ |
| **$h = 7$** | 128 | 126 | **/25** | `255.255.255.128` | Octet 4 | $128$ |
| **$h = 8$** | 256 | 254 | **/24** | `255.255.255.0` | Octet 4 | $256$ (Bước nhảy 1 ở Octet 3) |
| **$h = 9$** | 512 | 510 | **/23** | `255.255.254.0` | **Octet 3** | $256 - 254 = \mathbf{2}$ |
| **$h = 10$** | 1024 | 1022 | **/22** | `255.255.252.0` | **Octet 3** | $256 - 252 = \mathbf{4}$ |
| **$h = 11$** | 2048 | 2046 | **/21** | `255.255.248.0` | **Octet 3** | $256 - 248 = \mathbf{8}$ |
| **$h = 12$** | 4096 | 4094 | **/20** | `255.255.240.0` | **Octet 3** | $256 - 240 = \mathbf{16}$ |
| **$h = 13$** | 8192 | 8190 | **/19** | `255.255.224.0` | **Octet 3** | $256 - 224 = \mathbf{32}$ |
| **$h = 14$** | 16384 | 16382 | **/18** | `255.255.192.0` | **Octet 3** | $256 - 192 = \mathbf{64}$ |
| **$h = 15$** | 32768 | 32766 | **/17** | `255.255.128.0` | **Octet 3** | $256 - 128 = \mathbf{128}$ |
| **$h = 16$** | 65536 | 65534 | **/16** | `255.255.0.0` | **Octet 3** | $256$ (Bước nhảy 1 ở Octet 2) |

---

## 2. KHUNG THU THẬP DỮ KIỆN ĐẦU BÀI (INPUT PARAMETER MATRIX)

*👉 **Hướng dẫn**: Đọc kỹ đề bài và điền vào bảng dưới đây trước khi bắt đầu tính.*

### 2.1. Dữ kiện Mạng Tổng
- **Dải mạng tổng ban đầu**: `[ĐIỀN_VÀO: Ví dụ 10.0.0.0 hoặc 172.16.0.0 hoặc 192.168.0.0]`
- **Tiền tố ban đầu ($/u$)**: `[ĐIỀN_VÀO: Đã cho trước /u hay Cần phải tìm u?]`
- **Địa chỉ WAN kết nối ISP**: `[ĐIỀN_VÀO: Ví dụ 203.0.113.2/30, Gateway ISP: 203.0.113.1]`

### 2.2. Ma trận Nhu cầu Thiết bị từng Phân đoạn (Sắp xếp theo thứ tự giảm dần)

| Thứ tự ưu tiên | Tên Phân Đoạn / Khu Vực | Đối tượng sử dụng | Số lượng nhân sự | Hệ số thiết bị/người | Nhu cầu IP thô ($N_{\text{raw}}$) | Dự phòng mở rộng (%) | Nhu cầu Host thực tế ($H_i$) | VLAN ID dự kiến |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **1 (Max)** | `[Ví dụ: Lớp học]` | `[Sinh viên]` | `[969]` | `[x2 thiết bị]` | `[1938]` | `[5%]` | **`[1938]`** | VLAN 10 |
| **2** | `[Ví dụ: Phòng Lab]` | `[Máy tính có dây]` | `[400]` | `[x1 thiết bị]` | `[400]` | `[0%]` | **`[400]`** | VLAN 20 |
| **3** | `[Ví dụ: Văn phòng]` | `[Cán bộ/Nhân viên]`| `[69]` | `[x2 thiết bị]` | `[138]` | `[0%]` | **`[138]`** | VLAN 30 |
| **4** | `[Ví dụ: Server/DMZ]` | `[Máy chủ nội bộ]` | `[30]` | `[x1 thiết bị]` | `[30]` | `[10%]` | **`[30]`** | VLAN 40 |
| **5** | `[Ví dụ: Đường WAN]` | `[Router - Router]` | `[2]` | `[x1]` | `[2]` | `[0%]` | **`[2]`** | N/A |
| **TỔNG** | — | — | — | — | — | — | **`[2476 Host]`** | — |

---

## 3. QUY TRÌNH XÁC ĐỊNH TIỀN TỐ MẠNG TỔNG $u$ (NẾU ĐỀ YÊU CẦU TÌM $u$)

*👉 **Hướng dẫn**: Nếu đề bài đã cho sẵn $10.0.0.0/19$ thì bỏ qua phần này. Nếu đề bài cho dạng $10.0.0.0/u$ và yêu cầu tìm $u$, chọn 1 trong 2 cách lập luận sau để trình bày:*

### 🔹 Cách 1: Phương pháp giảng viên trên lớp (Mượn bit cố định FLSM / Worst-case)
1. **Tìm số bit mượn $n$ theo số lượng mạng con $S$**:
   $$S \le 2^n \iff [SỐ\_SUBNET] \le 2^n \implies n = [SỐ\_BIT\_MƯỢN]$$
   *(Ví dụ: 3 subnet $\implies 3 \le 2^n \implies n = 2$)*.
2. **Thiết lập công thức dung lượng phân đoạn lớn nhất ($H_{\max}$)**:
   $$H_{\max} \le 2^{32 - u - n} - 2$$
3. **Thay số và giải bất phương trình**:
   $$[H_{\max}] + 2 \le 2^{(32 - n) - u}$$
   Tìm lũy thừa $2^k$ nhỏ nhất sao cho $2^k \ge [H_{\max}] + 2$.
   $$\implies (32 - n) - u = k \implies \mathbf{u = 32 - n - k}$$

---

### 🔹 Cách 2: Phương pháp tổng hợp dung lượng thực tế (VLSM Aggregation)
1. **Cộng tổng số IP khối nhị phân của tất cả các phân đoạn**:
   $$\text{Tổng IP Khối} = \sum \text{BlockSize}_i = \text{Block}_1 + \text{Block}_2 + \dots + \text{Block}_k$$
   *(Ví dụ: $2048 + 512 + 256 = 2816\text{ IP}$)*.
2. **Tìm $u$ để mạng tổng bao trọn tổng IP trên**:
   $$2^{32 - u} \ge \text{Tổng IP Khối}$$
   Chọn $32 - u = m$ (với $2^m$ là lũy thừa nhỏ nhất $\ge \text{Tổng IP Khối}$).
   $$\implies \mathbf{u = 32 - m}$$
   *(Ví dụ: $2^{12} = 4096 \ge 2816 \implies 32 - u = 12 \implies u = 20$)*.

---

## 4. QUY TRÌNH PHÂN HOẠCH VLSM CHUẨN MỰC 5 BƯỚC (ĐIỀN SỐ TỰ ĐỘNG)

*👉 **Quy tắc vàng**: Bắt buộc tính theo thứ tự từ phân đoạn cần NHIỀU IP NHẤT đến phân đoạn ÍT IP NHẤT.*

### 📋 MẪU TÍNH CHO PHÂN ĐOẠN 1: `[TÊN PHÂN ĐOẠN 1]` (Lớn Nhất)
- **Nhu cầu thực tế**: $H_1 = \mathbf{[SỐ\_HOST\_1]}$ thiết bị.
- **Tính số bit phần Host ($h_1$)**:
  $$2^{h_1} - 2 \ge [H_1] \implies 2^{h_1} \ge [H_1 + 2]$$
  Tra bảng cheat sheet $\implies h_1 = \mathbf{[SỐ\_BIT\_HOST\_1]}$.
- **Xác định Prefix & Subnet Mask**:
  - Tiền tố: $\text{Prefix}_1 = 32 - h_1 = \mathbf{/[PREFIX\_1]}$.
  - Subnet Mask: $\mathbf{[SUBNET\_MASK\_1]}$.
- **Xác định Bước nhảy (Block Size)**:
  - Nếu Prefix từ $/24$ đến $/30$: Bước nhảy tại Octet 4 là $\text{Block} = 2^{h_1}$.
  - Nếu Prefix từ $/16$ đến $/23$: Bước nhảy tại Octet 3 là $\text{Block} = 256 - [\text{Giá trị Octet 3 của Mask}]$.
  $\implies$ **Bước nhảy = $\mathbf{[BƯỚC\_NHẢY\_1]}$**.
- **Thông số mạng chi tiết**:
  - **Network Address**: `[MẠNG_GỐC_BẮT_ĐẦU]/[PREFIX_1]` (Ví dụ: `10.0.0.0/21`)
  - **First Usable IP (Default Gateway)**: `[NETWORK_IP + 1]` (Ví dụ: `10.0.0.1`)
  - **Last Usable IP**: `[BROADCAST_IP - 1]` (Ví dụ: `10.0.7.254`)
  - **Broadcast Address**: `[NETWORK_IP + BƯỚC_NHẢY - 1]` (Ví dụ: `10.0.7.255`)
  - **Mạng tiếp theo bắt đầu từ**: $\mathbf{[MẠNG\_TIẾP\_THEO\_1]}$ (Ví dụ: `10.0.8.0`).

---

### 📋 MẪU TÍNH CHO PHÂN ĐOẠN 2: `[TÊN PHÂN ĐOẠN 2]`
- **Nhu cầu thực tế**: $H_2 = \mathbf{[SỐ\_HOST\_2]}$ thiết bị.
- **Mạng bắt đầu**: Lấy từ mạng tiếp theo của Phân đoạn 1: $\mathbf{[MẠNG\_TIẾP\_THEO\_1]}$.
- **Tính số bit phần Host ($h_2$)**:
  $$2^{h_2} - 2 \ge [H_2] \implies h_2 = \mathbf{[SỐ\_BIT\_HOST\_2]}$$
- **Xác định Prefix, Mask & Bước nhảy**:
  - Tiền tố: $\text{Prefix}_2 = 32 - h_2 = \mathbf{/[PREFIX\_2]}$.
  - Subnet Mask: $\mathbf{[SUBNET\_MASK\_2]}$.
  - Bước nhảy (Block Size): $\mathbf{[BƯỚC\_NHẢY\_2]}$.
- **Thông số mạng chi tiết**:
  - **Network Address**: `[MẠNG_TIẾP_THEO_1]/[PREFIX_2]` (Ví dụ: `10.0.8.0/23`)
  - **First Usable IP (Default Gateway)**: `[NETWORK_IP + 1]` (Ví dụ: `10.0.8.1`)
  - **Last Usable IP**: `[BROADCAST_IP - 1]` (Ví dụ: `10.0.9.254`)
  - **Broadcast Address**: `[NETWORK_IP + BƯỚC_NHẢY - 1]` (Ví dụ: `10.0.9.255`)
  - **Mạng tiếp theo bắt đầu từ**: $\mathbf{[MẠNG\_TIẾP\_THEO\_2]}$ (Ví dụ: `10.0.10.0`).

---

### 📋 MẪU TÍNH CHO PHÂN ĐOẠN 3: `[TÊN PHÂN ĐOẠN 3]`
- **Nhu cầu thực tế**: $H_3 = \mathbf{[SỐ\_HOST\_3]}$ thiết bị.
- **Mạng bắt đầu**: Lấy từ mạng tiếp theo của Phân đoạn 2: $\mathbf{[MẠNG\_TIẾP\_THEO\_2]}$.
- **Tính số bit phần Host ($h_3$)**:
  $$2^{h_3} - 2 \ge [H_3] \implies h_3 = \mathbf{[SỐ\_BIT\_HOST\_3]}$$
- **Xác định Prefix, Mask & Bước nhảy**:
  - Tiền tố: $\text{Prefix}_3 = 32 - h_3 = \mathbf{/[PREFIX\_3]}$.
  - Subnet Mask: $\mathbf{[SUBNET\_MASK\_3]}$.
  - Bước nhảy (Block Size): $\mathbf{[BƯỚC\_NHẢY\_3]}$.
- **Thông số mạng chi tiết**:
  - **Network Address**: `[MẠNG_TIẾP_THEO_2]/[PREFIX_3]` (Ví dụ: `10.0.10.0/24`)
  - **First Usable IP (Default Gateway)**: `[NETWORK_IP + 1]` (Ví dụ: `10.0.10.1`)
  - **Last Usable IP**: `[BROADCAST_IP - 1]` (Ví dụ: `10.0.10.254`)
  - **Broadcast Address**: `[NETWORK_IP + BƯỚC_NHẢY - 1]` (Ví dụ: `10.0.10.255`)
  - **Mạng tiếp theo bắt đầu từ**: $\mathbf{[MẠNG\_TIẾP\_THEO\_3]}$ (Ví dụ: `10.0.11.0`).

*(Nếu có thêm Phân đoạn 4, 5... chỉ cần copy cấu trúc mẫu trên và tịnh tiến tiếp tục).*

---

## 5. BẢNG TỔNG HỢP VLSM & BẢNG PHÂN BỔ IP CHI TIẾT (SẴN SÀNG COPY)

### 5.1. Bảng Tổng Hợp Quy Hoạch VLSM

| STT | Tên Phân Đoạn (VLAN) | Host Cần | Host Cung Cấp | Network Address | Subnet Mask | Dải IP Khả Dụng (Usable Range) | Default Gateway | Broadcast Address |
| :---: | :--- | :---: | :---: | :--- | :--- | :--- | :--- | :--- |
| **1** | `[Phân đoạn 1]` (VLAN 10) | `[H1]` | `[2^h1 - 2]` | `[Network_1]/[P1]` | `[Mask_1]` | `[IP_Đầu_1]` – `[IP_Cuối_1]` | `[GW_1]` | `[BC_1]` |
| **2** | `[Phân đoạn 2]` (VLAN 20) | `[H2]` | `[2^h2 - 2]` | `[Network_2]/[P2]` | `[Mask_2]` | `[IP_Đầu_2]` – `[IP_Cuối_2]` | `[GW_2]` | `[BC_2]` |
| **3** | `[Phân đoạn 3]` (VLAN 30) | `[H3]` | `[2^h3 - 2]` | `[Network_3]/[P3]` | `[Mask_3]` | `[IP_Đầu_3]` – `[IP_Cuối_3]` | `[GW_3]` | `[BC_3]` |
| **-** | *Dải IP Dự Phòng Sạch* | — | `[Dư thừa]` | `[Mạng_tiếp_theo]` đến `[IP_Cuối_Mạng_Tổng]` | Dành cho việc mở rộng dự án trong tương lai |

---

### 5.2. Bảng Phân Bổ IP Chi Tiết Từng Cổng Thiết Bị

| Thiết Bị (Device) | Giao Diện (Interface) | Địa Chỉ IP / Prefix | Subnet Mask | Default Gateway | VLAN ID | Chức Năng / Vai Trò |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **ROUTER_GATEWAY** | `Fa0/0 (WAN)` | `[IP_WAN_ROUTER]/30` | `255.255.255.252`| `[IP_WAN_ISP]` | N/A | Cổng WAN ra Internet (`nat outside`) |
| | `Fa0/1 (LAN)` | Unassigned | N/A | N/A | N/A | Cổng vật lý Trunking nối Core Switch |
| | `Fa0/1.10` | `[GW_1]/[P1]` | `[Mask_1]` | N/A | VLAN 10 | Gateway Phân đoạn 1 (`nat inside`) |
| | `Fa0/1.20` | `[GW_2]/[P2]` | `[Mask_2]` | N/A | VLAN 20 | Gateway Phân đoạn 2 (`nat inside`) |
| | `Fa0/1.30` | `[GW_3]/[P3]` | `[Mask_3]` | N/A | VLAN 30 | Gateway Phân đoạn 3 (`nat inside`) |
| **CORE_SWITCH** | `Vlan 1 (Mgmt)` | `[IP_QUẢN_TRỊ_SW]/[P]`| `[Mask]` | `[GW]` | VLAN 1 | Quản trị thiết bị Switch từ xa |
| | `Fa0/1` | 802.1Q Trunk | N/A | N/A | 10,20,30 | Cáp Trunk nối Router Gateway |
| | `Fa0/2` | Access VLAN 10 | N/A | N/A | VLAN 10 | Nối thiết bị Phân đoạn 1 |
| | `Fa0/3` | Access VLAN 20 | N/A | N/A | VLAN 20 | Nối thiết bị Phân đoạn 2 |
| | `Fa0/4` | Access VLAN 30 | N/A | N/A | VLAN 30 | Nối thiết bị Phân đoạn 3 |
| **SERVER_CO_DINH** | `NIC` | `[IP_TĨNH]/[P]` | `[Mask]` | `[GW]` | VLAN tương ứng | Máy chủ / RADIUS / Máy in |
| **CLIENTS (DHCP)** | `Wired / Wireless` | *DHCP Assigned* | Theo Pool | Theo Subnet | VLAN tương ứng | Thiết bị người dùng cuối |

---

## 6. BỘ KHUNG LỆNH CẤU HÌNH CISCO IOS MẪU (CHỈ CẦN THAY BIẾN)

### 6.1. Cấu hình Core Switch (VLANs, Trunking & Access Ports)
```cisco
enable
configure terminal
hostname CORE_SWITCH

! 1. Khởi tạo danh sách VLAN
vlan 10
 name VLAN10_[TEN_PHAN_DOAN_1]
exit
vlan 20
 name VLAN20_[TEN_PHAN_DOAN_2]
exit
vlan 30
 name VLAN30_[TEN_PHAN_DOAN_3]
exit

! 2. Cấu hình cổng Trunk kết nối Router
interface FastEthernet0/1
 switchport mode trunk
 switchport trunk allowed vlan 10,20,30
 no shutdown
exit

! 3. Cấu hình các cổng Access cấp phát cho từng khu vực
interface FastEthernet0/2
 switchport mode access
 switchport access vlan 10
 spanning-tree portfast                  ! Tăng tốc chuyển mạch cho client/AP
 no shutdown
exit

interface FastEthernet0/3
 switchport mode access
 switchport access vlan 20
 spanning-tree portfast
 no shutdown
exit

interface FastEthernet0/4
 switchport mode access
 switchport access vlan 30
 spanning-tree portfast
 no shutdown
exit

end
write memory
```

---

### 6.2. Cấu hình Router Biên (Router-on-a-Stick, Multi-DHCP & NAT Overload)
```cisco
enable
configure terminal
hostname ROUTER_GATEWAY

! 1. Kích hoạt cổng vật lý cha kết nối Switch
interface FastEthernet0/1
 no ip address
 no shutdown                             ! BẮT BUỘC BẬT CỔNG CHA
exit

! 2. Cấu hình Sub-interfaces cho từng VLAN (Thay IP và Subnet Mask)
interface FastEthernet0/1.10
 encapsulation dot1Q 10
 ip address [GW_1] [SUBNET_MASK_1]
 ip nat inside
exit

interface FastEthernet0/1.20
 encapsulation dot1Q 20
 ip address [GW_2] [SUBNET_MASK_2]
 ip nat inside
exit

interface FastEthernet0/1.30
 encapsulation dot1Q 30
 ip address [GW_3] [SUBNET_MASK_3]
 ip nat inside
exit

! 3. Cấu hình cổng WAN kết nối nhà mạng ISP
interface FastEthernet0/0
 ip address [IP_WAN_ROUTER] 255.255.255.252
 ip nat outside
 no shutdown
exit

! 4. Tuyến định tuyến ngầm định ra Internet (Default Route)
ip route 0.0.0.0 0.0.0.0 [IP_WAN_ISP]

! 5. Loại trừ địa chỉ IP tĩnh để chống xung đột DHCP
ip dhcp excluded-address [GW_1] [IP_TĨNH_CUỐI_1]
ip dhcp excluded-address [GW_2] [IP_TĨNH_CUỐI_2]
ip dhcp excluded-address [GW_3] [IP_TĨNH_CUỐI_3]

! 6. Cấu hình DHCP Pools cho từng phân đoạn mạng con
ip dhcp pool POOL_PHAN_DOAN_1
 network [NETWORK_ADDRESS_1] [SUBNET_MASK_1]
 default-router [GW_1]
 dns-server 8.8.8.8 1.1.1.1
 lease 0 2 0                             ! Thời gian thuê: 2 giờ (chống cạn IP)
exit

ip dhcp pool POOL_PHAN_DOAN_2
 network [NETWORK_ADDRESS_2] [SUBNET_MASK_2]
 default-router [GW_2]
 dns-server 8.8.8.8 1.1.1.1
exit

ip dhcp pool POOL_PHAN_DOAN_3
 network [NETWORK_ADDRESS_3] [SUBNET_MASK_3]
 default-router [GW_3]
 dns-server 8.8.8.8 1.1.1.1
exit

! 7. Cấu hình NAT Overload (PAT) cho toàn bộ mạng nội bộ
access-list 1 permit [MẠNG_TỔNG_GỐC] [WILDCARD_MASK_MẠNG_TỔNG]
ip nat inside source list 1 interface FastEthernet0/0 overload

end
write memory
```

---

## 7. KỊCH BẢN KIỂM THỬ & NGHIỆM THU BẢNG ĐỊNH TUYẾN

Khi báo cáo hoặc giảng viên kiểm tra, thực hiện 4 lệnh CLI cốt lõi sau trên Router:

### Checkpoint 1: Kiểm tra Bảng Định Tuyến (Routing Table)
```cisco
ROUTER_GATEWAY# show ip route
```
*Dấu hiệu chấm điểm 10/10*: Dòng thông báo **`variably subnetted, X subnets, Y masks`** xuất hiện với đúng số lượng subnet và các Subnet Mask khác nhau (`/P1`, `/P2`, `/P3`). Nếu chỉ thấy `1 mask` nghĩa là bạn đã làm sai theo kiểu FLSM cố định!

### Checkpoint 2: Kiểm tra Cấp phát IP Động (DHCP Binding)
```cisco
ROUTER_GATEWAY# show ip dhcp binding
```
Xác nhận máy trạm ở mỗi VLAN nhận đúng dải IP và Gateway tương ứng.

### Checkpoint 3: Kiểm tra Biên dịch NAT Overload
```cisco
ROUTER_GATEWAY# show ip nat translations
```
Khi máy trạm ping ra Internet (`ping 8.8.8.8`), bảng NAT phải hiển thị phiên chuyển đổi qua IP Public của cổng WAN.

---

## 8. CHECKLIST TỰ KIỂM TRA CHỐNG LỖI ĐÈ MẠNG (SANITY CHECK)

Trước khi nộp bài, hãy tự rà soát 5 câu hỏi sau:
- [ ] **Thứ tự phân bổ**: Bạn đã xếp phân đoạn cần nhiều host nhất lên đầu tiên chưa?
- [ ] **Ranh giới mạng con (Network Boundary)**: Địa chỉ mạng Network Address của mạng sau có bằng chính xác `[Network Address Mạng Trước] + [Bước nhảy Block Size]` không?
- [ ] **Kiểm tra Broadcast**: Địa chỉ Broadcast của mạng trước có nhỏ hơn Network Address của mạng liền kề đúng 1 đơn vị không?
- [ ] **Mặt nạ cha trên Router**: Đã gõ đúng Subnet Mask tương ứng trong từng lệnh `ip address` ở từng sub-interface chưa?
- [ ] **Cổng cha vật lý**: Đã có lệnh `no shutdown` trên cổng cha vật lý nối Switch chưa?
