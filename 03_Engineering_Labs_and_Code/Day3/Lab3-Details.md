# LAB3 Cao đẳng Banana

## 1. Dữ kiện bài toán
- **Lớp:** 969 sinh viên $\times$ 2
- **Phòng thí nghiệm:** 400 máy tính
- **Văn phòng:** 69 sinh viên $\times$ 2
- **Mạng tổng:** $10.0.0.0/u$
- **Điều kiện:** $s \le 2^n \ ; \ h \le 2^{32-u-n} - 2$

---

## 2. Các bước giải và phân bổ Subnet Mask

Số mạng con cần chia: $s = 3 \le 2^n$

### a. Lớp
- Số host yêu cầu: $h = 969 \cdot 2 \le 2^{32-u-n} - 2$ *(1 SV = 2 thiết bị)*
- Chọn $n = 2 \Rightarrow 1938 \le 2^{30-u} - 2$
- Ta có: $2048 \text{ IPs} = 2^{11} \Leftrightarrow 2^{30-u} \ge 1940 \Leftrightarrow 2^{30-19} \ge 1940$
- $\Rightarrow u \ge 19 \Leftrightarrow u_1 = 21 \text{ (chọn)}$

### b. LAB
- Tìm $n$ cho LAB: Start IP: $\text{NA}_1 \ \& \ u_1 = 21$
- $h_1 = 400 \le 2^{32-u_1-n_1} - 2$
- $\Rightarrow 2^{11-n_1} \ge 400$
- Chọn $2^{11-n_1} = 512 \text{ IPs} = 2^9 > 400 \Rightarrow n_1 = 2$
- $\Rightarrow /21 \xrightarrow{+2} /23$
- $\Rightarrow u_2 = 23$

### c. OFFICE
- Tìm $n$ cho OFFICE: Start IP: $\text{NA}_1 \ \& \ u_2 = 23$
- $h_2 = 69 \cdot 2 = 138 \le 2^{32-u_2-n_2} - 2$
- $\Rightarrow 2^{9-n_2} \ge 138 \Leftrightarrow 2^{9-1} = 256 \text{ IPs} \Leftrightarrow 2^8 > 138$
- $\Rightarrow n_2 = 1$
- $\Rightarrow /23 \xrightarrow{+1} /24$

---

## 3. Phân bổ dải IP chi tiết

- **Subnet masks:** Lớp: `/21` ; LAB: `/23` ; OFFICE: `/24`
- Mạng tổng: $10.0.0.0/u$. Chọn theo thứ tự từ khu có số lượng host lớn nhất đến nhỏ nhất:

### • Lớp (1938 hosts)
- **DG (Default Gateway):** `10.0.0.1`
- **SERVER:** `10.0.0.2`
- **AP:** `10.0.0.3` $\rightarrow$ `10.0.0.30`
- Với prefix `/21` $\Leftrightarrow 2048 \text{ IP}$
  - Số IP còn lại cho DHCP: $2048 - 2 - 30 = 2016$
- **DHCP scope:** `10.0.0.31` $\xrightarrow{2016 \text{ IP}}$ `10.0.7.254`

### • LAB
- **DG (Default Gateway):** `10.0.8.1`
- **SERVER:** `10.0.8.2`
- **AP:** `10.0.8.3` $\rightarrow$ `10.0.8.30`
- Với prefix `/23` $\Leftrightarrow 512 \text{ IP}$
  - Số IP còn lại cho DHCP: $512 - 2 - 30 = 480$
- **DHCP scope:** `10.0.8.31` $\xrightarrow{480 \text{ IP}}$ `10.0.9.254`

### • OFFICE
- **DG (Default Gateway):** `10.0.10.1`
- **SERVER:** `10.0.10.2`
- **AP:** `10.0.10.3` $\rightarrow$ `10.0.10.30`
- Với prefix `/24` $\Leftrightarrow 256 \text{ IP}$
  - Số IP còn lại cho DHCP: $256 - 2 - 30 = 224$
- **DHCP scope:** `10.0.10.31` $\xrightarrow{224 \text{ IP}}$ `10.0.10.254`

*(Ghi chú: Giả sử số lượng IP dành cho AP bằng nhau cho cả 3 phòng ban. Nếu thực tế hơn thì nên để dải AP của LAB và OFFICE ít lại để số lượng IP cho DHCP nhiều hơn).*

---

## 4. Ghi chú & Giải thích công thức

**Công thức tính số lượng IP DHCP:**
$$\text{①}: 2048 - 2 - 30 = 2016$$

- **$2048$:** Tổng số IP mà Subnet cung cấp.
- **$- 2$:** Trừ 2 địa chỉ IP dành riêng gồm Network Address (NA) và Broadcast Address (BA).
- **$- 30$:** Trừ các IP gán tĩnh cho Default Gateway, Server, và Access Point (AP - các thiết bị phần cứng như cục phát Wi-Fi).

**Định nghĩa:**
- **DHCP scope:** Là dải địa chỉ IP cấp phát tự động cho các thiết bị thuộc mạng (laptop, điện thoại,...).