# 📡 BÀI TRÌNH BÀY KỸ THUẬT: TÍNH TOÁN VÙNG PHỦ SÓNG & LỰA CHỌN CHUẨN WI-FI CHO QUÁN CAFE 2 TẦNG

> **Học phần**: Quản trị Mạng (NMA-DUT) — Đại học Bách khoa – ĐH Đà Nẵng  
> **Đề bài**: Thiết kế, triển khai và quản trị Quán Cafe Wi-Fi  
> **Yêu cầu giải quyết**: Yêu cầu 1 — Tính toán bán kính vùng phủ sóng, triển khai ít nhất 2 AP đảm bảo không có điểm chết, từ đó suy ra chọn chuẩn Wi-Fi nào (5, 6 hay 7).  
> **Ngày thực hiện**: 11/08/2026

---

## MỤC LỤC

1. [Phần A: Khảo sát mặt bằng và xác định thông số đầu vào](#phần-a-khảo-sát-mặt-bằng-và-xác-định-thông-số-đầu-vào)
2. [Phần B: Tính toán bán kính phủ sóng hình học](#phần-b-tính-toán-bán-kính-phủ-sóng-hình-học)
3. [Phần C: Kiểm chứng bằng mô hình suy hao sóng vô tuyến (RF Link Budget)](#phần-c-kiểm-chứng-bằng-mô-hình-suy-hao-sóng-vô-tuyến)
4. [Phần D: Chứng minh bắt buộc dùng ≥ 2 AP (Phân tích suy hao xuyên tầng)](#phần-d-chứng-minh-bắt-buộc-dùng--2-ap)
5. [Phần E: Biện luận lựa chọn chuẩn Wi-Fi (5, 6 hay 7)](#phần-e-biện-luận-lựa-chọn-chuẩn-wi-fi)
6. [Phần F: Tổng hợp kết quả và bản vẽ bố trí AP](#phần-f-tổng-hợp-kết-quả-và-bản-vẽ-bố-trí-ap)

---

## PHẦN A: KHẢO SÁT MẶT BẰNG VÀ XÁC ĐỊNH THÔNG SỐ ĐẦU VÀO

### A.1. Bản vẽ mặt bằng quán cafe

Quán cafe giả định có quy mô tiêu chuẩn nhà phố kinh doanh khu vực đô thị Đà Nẵng:

```
╔═══════════════════════════════════════════════════════════╗
║                    MẶT BẰNG MỖI TẦNG                      ║
║                                                           ║
║   (0,8) ┌──────────────────────────────────────┐ (15,8)   ║
║         │               W = 8 mét              │          ║
║         │                                      │          ║
║         │                                      │          ║
║         │              ● AP                    │          ║
║         │          (7.5 , 4.0)                 │          ║
║         │                                      │          ║
║         │                                      │          ║
║   (0,0) └──────────────────────────────────────┘ (15,0)   ║
║                    L = 15 mét                             ║
╚═══════════════════════════════════════════════════════════╝
```

### A.2. Bảng thông số đầu vào

| STT | Thông số | Ký hiệu | Giá trị | Đơn vị | Ghi chú / Nguồn |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | Chiều dài mỗi tầng | $L$ | $15$ | mét | Theo bản vẽ khảo sát thực tế |
| 2 | Chiều rộng mỗi tầng | $W$ | $8$ | mét | Theo bản vẽ khảo sát thực tế |
| 3 | Diện tích mỗi tầng | $S$ | $120$ | m² | $S = L \times W = 15 \times 8$ |
| 4 | Chiều cao từ sàn đến trần | $H_{\text{trần}}$ | $3.5$ | mét | Trần bê tông trát phẳng |
| 5 | Độ dày sàn bê tông giữa 2 tầng | $t_{\text{sàn}}$ | $0.20$ | mét | Sàn bê tông cốt thép |
| 6 | Số tầng | — | $2$ | tầng | Tầng 1 (quầy bar) + Tầng 2 (khu ngồi chính) |
| 7 | Độ cao gắn AP (tính từ sàn) | $h_{\text{AP}}$ | $3.3$ | mét | Gắn áp trần, cách trần $0.2\text{m}$ |
| 8 | Độ cao thiết bị người dùng | $h_{\text{user}}$ | $1.0$ | mét | Điện thoại khi đặt trên bàn cafe |

### A.3. Xác định vị trí đặt AP tối ưu

**Nguyên lý**: Để diện tích hình tròn phủ sóng bao trọn hình chữ nhật mặt sàn, vị trí tâm hình tròn phải trùng với **tâm hình học của hình chữ nhật** (giao điểm 2 đường chéo).

Tọa độ tâm đặt AP trên mỗi tầng:

$$x_0 = \frac{L}{2} = \frac{15}{2} = 7.5 \text{ mét}$$

$$y_0 = \frac{W}{2} = \frac{8}{2} = 4.0 \text{ mét}$$

$$z_0 = h_{\text{AP}} = 3.3 \text{ mét (tính từ sàn tầng đó)}$$

---

## PHẦN B: TÍNH TOÁN BÁN KÍNH PHỦ SÓNG HÌNH HỌC

### B.1. Bài toán hình học: AP phải phủ kín toàn bộ sàn

Khi AP đặt tại tâm hình chữ nhật, điểm xa nhất mà sóng phải tới được chính là **4 góc** của căn phòng. Khoảng cách từ tâm tới góc xa nhất chính bằng **một nửa đường chéo** hình chữ nhật.

```
   Góc A ─────────────────── Góc B
   (0,8)                    (15,8)
     \                       /
      \    d_2D             /
       \  ┌──────┐        /
        \ │      │       /
         \│  AP  │ 4.0m /
          │(7.5,4)│     /
          │      │    /
          └──┬───┘   /
         7.5m│      /
             │     /
   Góc D ────┴──────────── Góc C
   (0,0)                  (15,0)
```

### B.2. Bước tính 1 — Bán kính phủ sóng mặt phẳng 2D ($d_{\text{2D}}$)

Áp dụng **Định lý Pythagoras** trong tam giác vuông tạo bởi nửa chiều dài, nửa chiều rộng và đường chéo:

$$d_{\text{2D}} = \sqrt{\left(\frac{L}{2}\right)^2 + \left(\frac{W}{2}\right)^2}$$

Thay số:

$$d_{\text{2D}} = \sqrt{(7.5)^2 + (4.0)^2}$$

$$d_{\text{2D}} = \sqrt{56.25 + 16.00}$$

$$d_{\text{2D}} = \sqrt{72.25}$$

$$\boxed{d_{\text{2D}} \approx 8.50 \text{ mét}}$$

**Ý nghĩa vật lý**: Nếu nhìn từ trên xuống (2D), sóng Wi-Fi từ AP phải lan tỏa đủ xa ít nhất $8.50\text{m}$ theo mọi hướng trên mặt sàn mới tới được 4 góc phòng.

### B.3. Bước tính 2 — Bán kính phủ sóng không gian 3D ($d_{\text{3D}}$)

Trong thực tế, AP gắn trên trần ($h_{\text{AP}} = 3.3\text{m}$) còn người dùng cầm điện thoại ở độ cao mặt bàn ($h_{\text{user}} = 1.0\text{m}$). Chênh lệch độ cao:

$$\Delta h = h_{\text{AP}} - h_{\text{user}} = 3.3 - 1.0 = 2.3 \text{ mét}$$

Khoảng cách thực tế trong không gian 3D từ AP đến thiết bị người dùng ở góc xa nhất:

$$d_{\text{3D}} = \sqrt{d_{\text{2D}}^2 + (\Delta h)^2}$$

$$d_{\text{3D}} = \sqrt{(8.50)^2 + (2.3)^2}$$

$$d_{\text{3D}} = \sqrt{72.25 + 5.29}$$

$$d_{\text{3D}} = \sqrt{77.54}$$

$$\boxed{d_{\text{3D}} \approx 8.81 \text{ mét}}$$

### B.4. Kết luận Bước tính hình học

| Đại lượng | Giá trị tính toán | Giá trị làm tròn lên (Safety Margin) |
| :--- | :---: | :---: |
| Bán kính phủ sóng 2D ($d_{\text{2D}}$) | $8.50\text{ m}$ | $9\text{ m}$ |
| Bán kính phủ sóng 3D ($d_{\text{3D}}$) | $8.81\text{ m}$ | $9\text{ m}$ |

> **Yêu cầu kỹ thuật**: Mỗi Access Point cần có bán kính phủ sóng hiệu dụng tối thiểu $R_{\text{min}} \ge 9\text{ mét}$ để đảm bảo $100\%$ không có điểm chết trên mặt sàn $15\text{m} \times 8\text{m}$.

---

## PHẦN C: KIỂM CHỨNG BẰNG MÔ HÌNH SUY HAO SÓNG VÔ TUYẾN

Sau khi tính được bán kính hình học ($\approx 9\text{m}$), chúng ta cần **kiểm chứng** xem tại khoảng cách đó, tín hiệu Wi-Fi còn đủ mạnh để truyền dữ liệu Full HD hay không. Đây là bước tính vật lý sóng RF.

### C.1. Các thông số RF của thiết bị

| STT | Thông số | Ký hiệu | Giá trị | Đơn vị | Ghi chú |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | Công suất phát AP (Transmit Power) | $P_{\text{Tx}}$ | $20$ | dBm | Tương đương $100\text{mW}$, chuẩn AP doanh nghiệp |
| 2 | Độ lợi anten AP (AP Antenna Gain) | $G_{\text{Tx}}$ | $3$ | dBi | Anten Omni-directional tích hợp bên trong |
| 3 | Độ lợi anten smartphone (Client Gain) | $G_{\text{Rx}}$ | $0$ | dBi | Anten tích hợp trong smartphone |
| 4 | Suy hao tham chiếu tại $d_0 = 1\text{m}$ (5GHz) | $PL_0$ | $47$ | dB | Theo FSPL $= 20\log_{10}(f) + 20\log_{10}(d) + 32.44$ |
| 5 | Hệ số suy hao môi trường trong nhà (Path Loss Exponent) | $n$ | $3.0$ | — | Quán cafe: bàn ghế gỗ, người đi lại, tường kính |
| 6 | Ngưỡng cường độ tối thiểu chấp nhận được (Sensitivity Threshold) | $RSSI_{\text{min}}$ | $-65$ | dBm | Ngưỡng doanh nghiệp cho truyền video HD mượt |

### C.2. Bước tính 3 — Tính suy hao đường truyền tại góc xa nhất (Path Loss)

Áp dụng **Mô hình suy hao khoảng cách logarit trong nhà** (Indoor Log-Distance Path Loss Model):

$$PL(d) = PL_0 + 10 \cdot n \cdot \log_{10}\!\left(\frac{d}{d_0}\right)$$

Trong đó:
- $PL_0 = 47\text{ dB}$ (Suy hao tại khoảng cách tham chiếu $d_0 = 1\text{m}$, băng tần $5\text{GHz}$).
- $n = 3.0$ (Hệ số suy hao môi trường quán cafe).
- $d = d_{\text{3D}} = 8.81\text{m}$ (Khoảng cách thực tế từ AP đến góc xa nhất).

Thay số vào:

$$PL(8.81) = 47 + 10 \times 3.0 \times \log_{10}(8.81)$$

Tính $\log_{10}(8.81)$:

$$\log_{10}(8.81) = \log_{10}\!\left(\frac{881}{100}\right) = \log_{10}(881) - 2 \approx 2.9450 - 2 = 0.9450$$

Thay lại:

$$PL(8.81) = 47 + 30 \times 0.9450$$

$$PL(8.81) = 47 + 28.35$$

$$\boxed{PL(8.81) = 75.35 \text{ dB}}$$

### C.3. Bước tính 4 — Tính cường độ tín hiệu nhận được tại góc xa nhất ($RSSI$)

Áp dụng **phương trình Quỹ đường truyền (Link Budget Equation)**:

$$RSSI = P_{\text{Tx}} + G_{\text{Tx}} + G_{\text{Rx}} - PL(d)$$

Thay số:

$$RSSI = 20 + 3 + 0 - 75.35$$

$$\boxed{RSSI_{\text{góc xa nhất (cùng tầng)}} = -52.35 \text{ dBm}}$$

### C.4. Bước tính 5 — Đánh giá chất lượng tín hiệu

So sánh kết quả $RSSI$ vừa tính được với các ngưỡng tiêu chuẩn doanh nghiệp:

| Mức chất lượng | Dải RSSI | Ý nghĩa thực tế |
| :--- | :--- | :--- |
| 🟢 **Xuất sắc (Excellent)** | $RSSI \ge -50\text{ dBm}$ | Tốc độ tối đa, xem video 4K mượt |
| 🟢 **Rất tốt (Very Good)** | $-50 > RSSI \ge -60\text{ dBm}$ | Xem Full HD 1080p ổn định |
| 🟡 **Trung bình (Fair)** | $-60 > RSSI \ge -67\text{ dBm}$ | Xem video 720p, lướt web |
| 🟠 **Yếu (Weak)** | $-67 > RSSI \ge -75\text{ dBm}$ | Lướt web chậm, video bị buffer |
| 🔴 **Điểm chết (Dead Zone)** | $RSSI < -80\text{ dBm}$ | Mất kết nối |

Kết quả tính toán:

$$RSSI = -52.35\text{ dBm} \quad \longrightarrow \quad \text{Nằm trong mức } \mathbf{🟢 \text{ Xuất sắc (Excellent)}}$$

$$-52.35\text{ dBm} \gg -65\text{ dBm (ngưỡng tối thiểu cho Full HD)}$$

> **Kết luận Phần C**: Với AP đặt đúng vị trí tâm trần mỗi tầng, cường độ tín hiệu tại góc xa nhất **cùng tầng** đạt $-52.35\text{ dBm}$, vượt xa ngưỡng yêu cầu. AP đơn phủ kín tuyệt đối $100\%$ diện tích mặt sàn $120\text{m}^2$ mỗi tầng.

---

## PHẦN D: CHỨNG MINH BẮT BUỘC DÙNG ≥ 2 AP

### D.1. Đặt vấn đề

Câu hỏi then chốt: *"Nếu 1 AP phủ tốt 1 tầng rồi, vậy có thể dùng 1 AP duy nhất phát xuyên sàn để phủ cả 2 tầng không?"*

Để trả lời, chúng ta phải tính **suy hao khi sóng xuyên qua sàn bê tông cốt thép** giữa 2 tầng.

### D.2. Hệ số suy hao xuyên sàn (Floor Attenuation Factor — FAF)

Theo dữ liệu thực nghiệm của **ITU-R P.1238** (Mô hình truyền sóng trong nhà) và các nghiên cứu tiêu chuẩn:

| Vật liệu kết cấu | Băng tần 2.4 GHz | Băng tần 5 GHz |
| :--- | :---: | :---: |
| Sàn gỗ nhẹ (gỗ ván ép) | $-5\text{ dB}$ | $-8\text{ dB}$ |
| Sàn bê tông nhẹ (không cốt thép) | $-12\text{ dB}$ | $-15\text{ dB}$ |
| **Sàn bê tông cốt thép (dày 20cm)** | **$-18\text{ dB}$** | **$-22\text{ dB}$** |
| Sàn bê tông kép có lớp cách âm | $-25\text{ dB}$ | $-30\text{ dB}$ |

Với quán cafe có sàn bê tông cốt thép dày $20\text{cm}$, ở băng tần $5\text{GHz}$:

$$\boxed{FAF = -22 \text{ dB}}$$

### D.3. Bước tính 6 — Tính RSSI tại Tầng 2 nếu chỉ dùng 1 AP ở Tầng 1

Khoảng cách xuyên tầng từ AP Tầng 1 (trần T1) đến thiết bị ở góc xa nhất Tầng 2:

Chiều dọc xuyên tầng: $\Delta h_{\text{xuyên tầng}} = t_{\text{sàn}} + (H_{\text{trần}} - h_{\text{AP}}) + (H_{\text{trần}} - h_{\text{user}}) = 0.20 + 0.20 + 2.50 = 2.90\text{m}$

*(Đơn giản hóa: khoảng cách thẳng đứng giữa AP Tầng 1 (gần trần T1) và thiết bị trên bàn Tầng 2 là khoảng $h_{\text{trần}} - h_{\text{AP}} + t_{\text{sàn}} + h_{\text{trần}} - h_{\text{user}} = 0.2 + 0.2 + 2.5 = 2.9\text{m}$)*

Khoảng cách 3D xuyên tầng:

$$d_{\text{xuyên tầng}} = \sqrt{d_{\text{2D}}^2 + \Delta h_{\text{xuyên tầng}}^2} = \sqrt{(8.50)^2 + (2.90)^2} = \sqrt{72.25 + 8.41} = \sqrt{80.66} \approx 8.98\text{m}$$

Suy hao đường truyền (không tính sàn):

$$PL(8.98) = 47 + 30 \times \log_{10}(8.98) = 47 + 30 \times 0.9533 = 47 + 28.60 = 75.60\text{ dB}$$

**Tổng suy hao khi xuyên qua sàn bê tông**:

$$PL_{\text{tổng}} = PL(d) + FAF = 75.60 + 22 = \mathbf{97.60 \text{ dB}}$$

Cường độ tín hiệu nhận được tại Tầng 2:

$$RSSI_{\text{Tầng 2}} = P_{\text{Tx}} + G_{\text{Tx}} + G_{\text{Rx}} - PL_{\text{tổng}}$$

$$RSSI_{\text{Tầng 2}} = 20 + 3 + 0 - 97.60$$

$$\boxed{RSSI_{\text{Tầng 2}} = -74.60 \text{ dBm}}$$

### D.4. Đánh giá kết quả

$$RSSI_{\text{Tầng 2}} = -74.60\text{ dBm} \quad < \quad -65\text{ dBm} \text{ (Ngưỡng tối thiểu cho Full HD)}$$

| Vị trí | RSSI tính toán | Mức chất lượng | Xem Full HD 1080p? |
| :--- | :---: | :--- | :---: |
| Góc xa nhất **cùng tầng** với AP | $-52.35\text{ dBm}$ | 🟢 Xuất sắc | ✅ Mượt mà |
| Góc xa nhất **khác tầng** (xuyên sàn bê tông) | $-74.60\text{ dBm}$ | 🟠 Yếu | ❌ Buffer liên tục |

### D.5. Phân tích hậu quả kỹ thuật nếu ép dùng 1 AP

Khi tín hiệu giảm xuống $-74.60\text{ dBm}$, xảy ra hiệu ứng dây chuyền:

```
Bước 1:  RSSI giảm → SNR (Signal-to-Noise Ratio) giảm xuống còn ~5-10 dB
                ↓
Bước 2:  Hệ thống tự hạ cấp điều chế (MCS Fallback)
         MCS 9 (256-QAM, ~866 Mbps) → MCS 1 (QPSK, ~13 Mbps)
                ↓
Bước 3:  Tốc độ thực tế giảm về còn 5-8 Mbps (Gần bằng 3G)
                ↓
Bước 4:  Gói tin truyền lại liên tục (Retransmission > 30%)
                ↓
Bước 5:  Chiếm kênh truyền lâu hơn → Ảnh hưởng toàn bộ
         client CẢ 2 TẦNG (Protocol Fairness Problem)
```

### D.6. Kết luận Phần D

> **CHỨNG MINH HOÀN TẤT**: Với sàn bê tông cốt thép, suy hao xuyên tầng $FAF = -22\text{dB}$ khiến tín hiệu tụt từ $-52.35\text{dBm}$ (Xuất sắc) xuống $-74.60\text{dBm}$ (Yếu). **Bắt buộc phải triển khai ít nhất 2 Access Point, mỗi tầng 1 AP riêng biệt.**

---

## PHẦN E: BIỆN LUẬN LỰA CHỌN CHUẨN WI-FI

### E.1. Xác định yêu cầu kỹ thuật đặc thù của quán cafe

Trước khi so sánh các chuẩn Wi-Fi, cần liệt kê rõ các yêu cầu kỹ thuật mà chuẩn Wi-Fi phải đáp ứng:

| STT | Yêu cầu kỹ thuật | Mô tả chi tiết | Mức độ |
| :---: | :--- | :--- | :---: |
| 1 | **Mật độ kết nối đồng thời cao** | Giờ cao điểm xem bóng đá: $\ge 120$ thiết bị/tầng đồng thời. | BẮT BUỘC |
| 2 | **Hỗ trợ băng tần 5 GHz** | Giảm nhiễu với thiết bị lân cận (quán bên cạnh, nhà dân). | BẮT BUỘC |
| 3 | **Cơ chế phục vụ đồng thời nhiều client** | Tránh hiện tượng "xếp hàng chờ" khi đông người. | BẮT BUỘC |
| 4 | **Chống nhiễu giữa 2 AP (Co-Channel)** | 2 AP cùng tòa nhà cách nhau 1 sàn bê tông, sóng vẫn có thể rò rỉ. | QUAN TRỌNG |
| 5 | **Bán kính phủ sóng $\ge 9$ mét (5GHz)** | Theo kết quả tính toán ở Phần B. | BẮT BUỘC |
| 6 | **Thiết bị đầu cuối phải tương thích rộng rãi** | $\ge 90\%$ smartphone của khách phải hỗ trợ chuẩn Wi-Fi đó. | BẮT BUỘC |
| 7 | **Chi phí đầu tư hợp lý cho hộ kinh doanh** | Ngân sách thiết bị AP vừa phải (dưới $5$ triệu VNĐ/AP). | QUAN TRỌNG |

### E.2. Bảng đối chiếu 3 chuẩn Wi-Fi theo từng yêu cầu

| Yêu cầu | Wi-Fi 5 (802.11ac) | Wi-Fi 6 (802.11ax) | Wi-Fi 7 (802.11be) |
| :--- | :---: | :---: | :---: |
| **(1) Mật độ cao ($\ge 120$ client/AP)** | ❌ Nghẽn nặng khi $> 30\text{-}40$ client | ✅ Thiết kế tối ưu cho $\ge 100$ client | ✅ Tối ưu |
| **(2) Hỗ trợ 5 GHz** | ✅ Có | ✅ Có (cả 2.4 + 5 GHz) | ✅ Có (thêm 6 GHz) |
| **(3) Phục vụ đồng thời (OFDMA)** | ❌ Không có (chỉ OFDM đơn kênh) | ✅ **OFDMA**: chia kênh $\rightarrow$ phục vụ $\le 37$ client/khung | ✅ OFDMA nâng cao |
| **(4) Chống nhiễu giữa 2 AP (BSS Coloring)** | ❌ Không có | ✅ **BSS Coloring**: đánh dấu gói tin theo AP, loại bỏ nhiễu | ✅ Có |
| **(5) Bán kính $\ge 9\text{m}$ ở 5 GHz** | ✅ Đạt (~$12\text{m}$) | ✅ Đạt (~$12\text{m}$, tốt hơn nhờ Target Wake Time) | ✅ Đạt |
| **(6) Tỷ lệ smartphone hỗ trợ (2026)** | ✅ $99\%$ | ✅ **$\ge 95\%$** | ❌ $< 20\%$ (quá mới) |
| **(7) Giá thiết bị AP** | $\approx 1\text{-}2$ triệu VNĐ | $\approx 2\text{-}4$ triệu VNĐ | $\approx 8\text{-}15$ triệu VNĐ |
| **TỔNG ĐIỂM ĐẠT** | **3/7** | **7/7** ✅ | **5/7** |

### E.3. Phân tích loại trừ từng chuẩn

**❌ Loại Wi-Fi 5 (802.11ac)** — Lý do:
- Không có OFDMA: Tại mỗi thời điểm phát sóng, toàn bộ kênh $80\text{MHz}$ chỉ phục vụ đúng 1 client. Với $120$ thiết bị, thời gian chờ trung bình tăng tuyến tính, gây ra độ trễ $> 200\text{ms}$ (video giật/buffer).
- Không có BSS Coloring: 2 AP trong cùng tòa nhà sẽ "nghe thấy" sóng của nhau qua sàn bê tông (dù yếu), dẫn tới cả 2 AP đều dừng phát sóng chờ nhau (**CCA Contention**), giảm thông lượng $30\text{-}50\%$.

**❌ Loại Wi-Fi 7 (802.11be)** — Lý do:
- Tỷ lệ smartphone hỗ trợ quá thấp ($< 20\%$ năm 2026). Đa số khách mang iPhone 14/15/16 hoặc Samsung Galaxy S23/S24 chỉ hỗ trợ tối đa Wi-Fi 6/6E.
- Giá thiết bị AP Wi-Fi 7 gấp $3\text{-}5$ lần Wi-Fi 6, không phù hợp ngân sách quán cafe.
- Băng tần $6\text{GHz}$ cần cấp phép riêng và bán kính phủ sóng ngắn hơn $5\text{GHz}$.

**✅ Chọn Wi-Fi 6 (802.11ax)** — Lý do tổng hợp:
- **OFDMA** giải quyết triệt để vấn đề mật độ cao: Chia kênh $80\text{MHz}$ thành $37$ Resource Units (RU), phục vụ song song $37$ thiết bị trong cùng 1 khung truyền.
- **BSS Coloring** loại bỏ can nhiễu giữa 2 AP.
- **Target Wake Time (TWT)**: Điều phối lịch trình thức/ngủ cho từng client, tiết kiệm pin điện thoại và giảm tranh chấp kênh vô tuyến.
- Tương thích ngược hoàn toàn với Wi-Fi 5 và Wi-Fi 4.
- Giá thành AP doanh nghiệp hợp lý ($2\text{-}4$ triệu VNĐ/thiết bị).

---

## PHẦN F: TỔNG HỢP KẾT QUẢ VÀ BẢN VẼ BỐ TRÍ AP

### F.1. Bảng tổng hợp kết quả toàn bộ tính toán

| STT | Đại lượng / Kết quả | Giá trị | Ghi chú |
| :---: | :--- | :---: | :--- |
| 1 | Diện tích mỗi tầng | $120\text{ m}^2$ | $15\text{m} \times 8\text{m}$ |
| 2 | Bán kính phủ sóng 2D cần thiết | $8.50\text{ m}$ | Nửa đường chéo hình chữ nhật |
| 3 | Bán kính phủ sóng 3D cần thiết | $8.81\text{ m}$ | Tính đến chênh lệch độ cao AP - User |
| 4 | Bán kính thiết kế (làm tròn lên) | $9\text{ m}$ | Có hệ số dự phòng an toàn |
| 5 | Suy hao đường truyền tại góc xa nhất (cùng tầng) | $75.35\text{ dB}$ | Mô hình Log-Distance, $n=3.0$ |
| 6 | RSSI tại góc xa nhất (cùng tầng) | $-52.35\text{ dBm}$ | 🟢 Mức Xuất sắc, Full HD mượt |
| 7 | Suy hao xuyên sàn bê tông 5GHz (FAF) | $-22\text{ dB}$ | Sàn BTCT dày $20\text{cm}$ |
| 8 | RSSI tại Tầng 2 nếu chỉ dùng 1 AP Tầng 1 | $-74.60\text{ dBm}$ | 🟠 Mức Yếu, **không đạt** yêu cầu |
| 9 | **Số lượng AP tối thiểu** | **2 AP** | **1 AP / tầng** |
| 10 | **Chuẩn Wi-Fi lựa chọn** | **Wi-Fi 6 (802.11ax)** | Đạt 7/7 tiêu chí kỹ thuật |

### F.2. Bản vẽ bố trí cuối cùng

```
╔══════════════════════════════════════════════════════════════╗
║                        TẦNG 2                               ║
║   ┌──────────────────────────────────────────────────┐      ║
║   │                                                  │      ║
║   │                 📡 AP-02                         │      ║
║   │            (Wi-Fi 6, 802.11ax)                   │      ║
║   │         Tọa độ: (7.5m, 4.0m, 3.3m)             │      ║
║   │         Kênh 2.4G: Channel 6                     │      ║
║   │         Kênh 5G: Channel 149                     │      ║
║   │         Bảo mật: WPA2-PSK (AES)                 │      ║
║   │         RSSI tại góc: -52.35 dBm 🟢             │      ║
║   │                                                  │      ║
║   └──────────────────────────────────────────────────┘      ║
║              🧱 SÀN BÊ TÔNG CỐT THÉP (FAF = -22dB)        ║
║                        TẦNG 1                               ║
║   ┌──────────────────────────────────────────────────┐      ║
║   │                                                  │      ║
║   │                 📡 AP-01                         │      ║
║   │            (Wi-Fi 6, 802.11ax)                   │      ║
║   │         Tọa độ: (7.5m, 4.0m, 3.3m)             │      ║
║   │         Kênh 2.4G: Channel 1                     │      ║
║   │         Kênh 5G: Channel 36                      │      ║
║   │         Bảo mật: WPA2-PSK (AES)                 │      ║
║   │         RSSI tại góc: -52.35 dBm 🟢             │      ║
║   │                                                  │      ║
║   └──────────────────────────────────────────────────┘      ║
╚══════════════════════════════════════════════════════════════╝
```

---

## PHỤ LỤC: BẢNG TRA CỨU CÔNG THỨC ĐÃ SỬ DỤNG

| STT | Tên Công thức | Biểu thức | Mục đích sử dụng |
| :---: | :--- | :--- | :--- |
| 1 | Định lý Pythagoras 2D | $d_{\text{2D}} = \sqrt{(L/2)^2 + (W/2)^2}$ | Tính nửa đường chéo mặt sàn |
| 2 | Khoảng cách không gian 3D | $d_{\text{3D}} = \sqrt{d_{\text{2D}}^2 + \Delta h^2}$ | Tính khoảng cách thực từ AP đến góc xa nhất |
| 3 | Suy hao Log-Distance (Indoor) | $PL(d) = PL_0 + 10 \cdot n \cdot \log_{10}(d/d_0)$ | Tính suy hao tín hiệu RF theo khoảng cách |
| 4 | Quỹ đường truyền (Link Budget) | $RSSI = P_{\text{Tx}} + G_{\text{Tx}} + G_{\text{Rx}} - PL(d)$ | Tính cường độ tín hiệu thực tế tại mọi điểm |
| 5 | Suy hao xuyên sàn | $PL_{\text{tổng}} = PL(d) + FAF$ | Xác định chất lượng sóng khi AP phát xuyên tầng |
