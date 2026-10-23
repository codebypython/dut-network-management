Ping chỉ là bề nổi (Black-box testing) để biết gói tin có đi đến đích hay không. Để chấm điểm hoặc tự kiểm chứng xem "nội công" bên trong mạng của ông có chuẩn 100% như thầy giáo yêu cầu hay không, chúng ta phải dùng kỹ thuật **White-box testing** bằng các lệnh `show` và `traceroute`.

Dưới đây là 5 chiêu kiểm tra (Verification) "tủ" mà các giảng viên mạng hay dùng nhất để soi lỗi, ông lưu lại để bỏ túi nhé:

### 1. Dùng lệnh `tracert` để kiểm tra bẫy Routing Loop (Trên PC0)

Đây là cách trực quan nhất để xem gói tin có bị chạy vòng tròn giữa Jupiter và Mecury hay không.

- **Thao tác:** Mở Command Prompt trên PC0, gõ: `tracert 192.168.0.1`

- **Kết quả đúng:** Ông sẽ thấy một danh sách các trạm (hop) mà gói tin đi qua. Ví dụ:
    1. `172.23.128.1` (Gateway ở Earth)
    
    2. `172.23.255.x` (Qua Mars)
    
    3. `172.23.255.y` (Qua Jupiter)
    
    4. `172.22.255.z` (Qua Neptune)
    
    5. `192.168.0.1` (Tới ISP)

- **Kết quả sai (Bị Loop):** Nếu ông thấy gói tin nhảy qua nhảy lại giữa 2 IP của Jupiter và Mecury đến tận 30 lần rồi "Request timed out", nghĩa là lệnh sửa AD (distance 175) của ông chưa ăn.

### 2. Soi bảng định tuyến chéo (Trên các Router)

- **Thao tác:** Vào CLI của Earth, Mars, Mecury, gõ `show ip route`.

- **Kết quả đúng cần thấy:**

    - **Trên Earth/Mars:** Phải thấy các tuyến có ký hiệu `O IA` (Inter-Area - ví dụ mạng của Area 1 và Area 2).

    - **Trên Earth/Mars/Venus:** Phải thấy ký hiệu `O E2` (OSPF External Type 2) cho các mạng của EIGRP (dải `172.22.x.x`) và tuyến mặc định `0.0.0.0/0`.

    - **Trên Neptune:** Phải thấy ký hiệu `D EX` (EIGRP External) chứa các mạng của vùng OSPF (dải `172.23.x.x`).
### 3. Kiểm tra Hệ thống Dịch địa chỉ NAT (Trên Router Neptune)

- **Thao tác:** Từ PC0 ping ra `192.168.0.1` khoảng 2-3 gói. Ngay sau đó, mở CLI của Neptune lên gõ `show ip nat translations`.

- **Kết quả đúng:** Bảng NAT hiện ra rõ ràng việc IP nội bộ của PC0 (`172.23.128.10`) đã được "dịch" thành một IP Public trong Pool (ví dụ `192.168.0.11` hoặc `.12`). Nếu bảng này trống trơn dù ping vẫn thông, nghĩa là NAT tịt, gói tin chạy bằng routing thông thường.

### 4. Kiểm tra Mật khẩu & Quan hệ láng giềng (Trên các Router)

Việc cấu hình MD5 (OSPF) và Key-chain (EIGRP) nếu chỉ cần sai 1 ký tự là 2 Router sẽ "nghỉ chơi" với nhau.

- **Thao tác:** Gõ lệnh `show ip ospf neighbor` (đối với OSPF) và `show ip eigrp neighbors` (đối với EIGRP).

- **Kết quả đúng:** Bảng phải liệt kê IP của các Router hàng xóm và cột State (với OSPF) phải hiện chữ **FULL**. Nếu gõ lệnh này ra mà bảng trống lốc, chắc chắn cấu hình Authentication (Giai đoạn 5) đã bị gõ sai chữ `cat` hoặc `mouse` ở đâu đó.

### 5. Kiểm tra VTP và Trunking (Trên Switch Server và Client)

- **Kiểm tra VTP:** Gõ `show vtp status`.

    - _Chờ đợi:_ Switch Server có `VTP Operating Mode: Server`, Switch Client là `Client`. Cả 2 có chung `VTP Domain Name: planet`. `Configuration Revision` phải giống nhau (hoặc Client lớn hơn/bằng).

- **Kiểm tra Trunking:** Gõ `show interfaces trunk`.

    - _Chờ đợi:_ Cột Status hiện `trunking`, và cột VLANs allowed and active phải liệt kê rõ `1-3` (hoặc `2,3`).

