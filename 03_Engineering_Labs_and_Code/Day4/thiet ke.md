# LAB4: Hà Nội - Đà Nẵng - Sài Gòn

## 1. Dữ kiện bài toán
- **Hà Nội:** 200 nhân viên
- **Đà Nẵng:** 50 nhân viên
- **Sài Gòn:** 100 nhân viên
- **Mạng tổng:** `172.16.0.0/u`

**Ghi chú kèm theo:**
- Định tuyến nội bộ Cty: OSPF.
- HNội có 1 SVer web, NAT = mạng con nối từ ISP.
- (*giả sử 1 nhân viên = 1 máy tính)

---

## 2. Các bước giải và phân bổ Subnet Mask

Số mạng con cần chia: $s = 3 \le 2^n \Rightarrow n = 2$

### a. Hà Nội
- Số host yêu cầu: $h = 200 \le 2^{32-u-n} - 2$
- Với $n = 2 \Rightarrow 200 \le 2^{30-u} - 2$
- $\Rightarrow 2^{30-u} \ge 202$
- Ta có: $256 = 2^8 \Leftrightarrow 2^{30-22} \ge 202 \Leftrightarrow 2^8 \ge 202 \Rightarrow u_1 \ge 22$
- Chọn $u_1 = 24$ (ít dư IP)

### b. Sài Gòn
- Tìm $n_1$ cho SG. Start IP: $\text{NA} \ \& \ u_1 = 24$
- $h_1 = 100 \le 2^{32-u_1-n_1} - 2$
- $\Rightarrow 2^{8-n_1} \ge 102$
- Cho $2^{8-n_1} = 128 \text{ IPS} = 2^7 \Rightarrow n_1 = 1 \Rightarrow /24 \xrightarrow{+1} /25$
- $\Rightarrow u_2 = 25$

### c. Đà Nẵng
- Tìm $n_2$ cho ĐN. Start IP: $\text{NA} \ \& \ u_2 = 25$
- $h_2 = 50 \le 2^{32-u_2-n_2} - 2$
- $\Rightarrow 2^{7-n_2} \ge 52$
- Cho $2^{7-n_2} = 2^6 \Rightarrow n_2 = 1 \Rightarrow /25 \xrightarrow{+1} /26$
- $\Rightarrow u_3 = 26$

---

## 3. Phân bổ dải IP chi tiết

- **Subnet masks:** Hà Nội: `/24` (256) ; Đà Nẵng: `/26` (64) ; Sài Gòn: `/25` (128)
- Ta có mạng tổng: `172.16.0.0/u`
- Để xác định IP, chọn từ khu có số lượng host lớn nhất đến nhỏ nhất:

### ① Hà Nội: 200 NV. (Lớn nhất)
- **DG:** `172.16.0.1`
- **SVer:** `172.16.0.2`
- **AP:** (Ko cần vì dùng switch nối thẳng vào máy)
- **DHCP scope:** `172.16.0.3` $\xrightarrow{252 \text{ IP}}$ `172.16.0.254`

### ② Sài Gòn: 100 NV.
- **DG:** `172.16.1.1` ;
- **DHCP scope:** `172.16.1.2` $\xrightarrow{125 \text{ IP}}$ `172.16.1.126`

### ③ Đà Nẵng: 50 NV.
- **DG:** `172.16.1.129`
- **DHCP scope:** `172.16.1.130` $\xrightarrow{61 \text{ IP}}$ `172.16.1.191`