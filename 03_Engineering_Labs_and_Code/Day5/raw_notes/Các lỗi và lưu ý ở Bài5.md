CLick để xem lại [[Bài 5]]

Thầy muốn hỏi thêm
"Earth>ping 8.8.8.8
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 8.8.8.8, timeout is 2 seconds:
..!!!
Success rate is 60 percent (3/5), round-trip min/avg/max = 55/58/64 ms" 

Tại sao khi ping 8.8.8.8 ở earth thì tỉ lệ luôn luôn là ~ 40-60% ? nghĩa là bị rớt 2-3 gói ?

--- 

Câu hỏi mở rộng này của thầy giáo thực sự là một "cú lừa" cực kỳ đẳng cấp, đào rất sâu vào bản chất của ba cơ chế: Ping, Cân bằng tải (ECMP), và NAT. 

Hiện tượng rớt 2-3 gói tin (hiệu suất 40-60%) khi ping trực tiếp từ Earth hoàn toàn **không phải do cấu hình sai**, mà xuất phát từ **Sự cố ghi đè phiên NAT (NAT PAT Collision) do IP nguồn thay đổi liên tục**.


Sự xung đột này diễn ra theo chuỗi logic sau:

- **Cơ chế Cân bằng tải (ECMP):** Như bảng định tuyến ông đã phân tích, Earth đang có 4 tuyến đường đi ra Default Route với Cost bằng nhau (2 đường xuất phát qua cổng Gig0/0.2, 2 đường qua cổng Gig0/0.3). Khi ông thực hiện lệnh Ping 5 gói tin, Earth sẽ chia bài: gói thứ nhất xuất qua Gig0/0.2, gói thứ hai xuất qua Gig0/0.3, gói thứ ba quay lại Gig0/0.2, v.v.

- **Cơ chế chọn IP Nguồn của Router:** Theo nguyên tắc của Cisco, nếu không chỉ định rõ nguồn, Router sẽ tự động lấy IP của **cổng vật lý mà gói tin vừa chui ra** làm Source IP. Do sự phân tải ở trên, gói số 1 sẽ mang IP nguồn là `172.23.128.1` (của Gig0/0.2), nhưng gói số 2 lại mang IP nguồn `172.23.144.1` (của Gig0/0.3).

- **Điểm nghẽn tại trạm NAT (Neptune):** Kỹ thuật NAT Overload (PAT) ông thiết lập trên Neptune phân biệt các phiên Ping bằng **Mã định danh ICMP (ICMP ID)**. Do cả 5 gói tin này đều sinh ra từ cùng một dòng lệnh Ping duy nhất trên Earth, chúng đều mang chung một ICMP ID.

- **Bảng NAT bị "ngáo":** Khi gói 1 tới, Neptune ghi vào bảng NAT: "Đang dịch ICMP ID 1234 cho IP nội bộ `172.23.128.1`". Ngay phần ngàn giây sau, gói 2 ập tới cũng mang ICMP ID 1234, nhưng nguồn lại là `172.23.144.1`. Lúc này Neptune bị bối rối vì thấy hai IP nội bộ khác nhau lại đang cố dùng chung một định danh phiên cùng một thời điểm. Hậu quả là nó sẽ ghi đè bản dịch NAT hoặc trực tiếp loại bỏ (drop) gói tin, khiến gói tin phản hồi (Reply) từ 8.8.8.8 không biết đường tìm về đúng đích.

Đó chính là lý do vì sao khi ông Ping từ máy khách **PC0** (máy tính chỉ có 1 cổng, 1 IP cố định duy nhất), tỉ lệ thành công luôn là tĩnh lặng tuyệt đối 100%.

Để xử lý triệt để hiện tượng này và chứng minh cho thầy giáo thấy ông hiểu rõ cơ chế lõi, ông chỉ cần ép con Earth sử dụng **duy nhất một IP nguồn** cho toàn bộ quá trình Ping.

# Solutions

### 1. Phân tích "4 tuyến đường đi ra Default Route" của Earth

Ông mở lại bảng định tuyến của con **Earth** và nhìn vào dòng `O*E2 0.0.0.0/0` ở dưới cùng. Nó liệt kê chính xác 4 địa chỉ IP ở phần `via` (thông qua).
```
O*E2 0.0.0.0/0 
[110/1] via 172.23.128.3, 00:09:29, GigabitEthernet0/0.2
[110/1] via 172.23.144.3, 00:09:29, GigabitEthernet0/0.3
[110/1] via 172.23.128.2, 00:09:29, GigabitEthernet0/0.2
[110/1] via 172.23.144.2, 00:09:29, GigabitEthernet0/0.3
```
Sở dĩ có đến 4 đường là do sự kết hợp của sơ đồ vật lý và cấu hình VLAN  tạo ra một ma trận đối xứng

- Earth kết nối với hệ thống thông qua 2 cánh cửa ảo là **VLAN 2 (mars - mạng 128.x)** và **VLAN 3 (venus - mạng 144.x)**.
- Ở đầu bên kia của 2 VLAN này, có 2 con Router đang vẫy tay đón gói tin là **Mars (IP đuôi .2)** và **Venus (IP đuôi .3)**.
- Cả Mars và Venus đều có khoảng cách (Cost) đi ra Internet bằng y hệt nhau.

Do đó, OSPF nhân chéo lên và tạo ra 4 lựa chọn (4 equal-cost paths) để cân bằng tải:

1. Đi qua **Venus** bằng đường **VLAN mars** (`via 172.23.128.3, GigabitEthernet0/0.2`).

2. Đi qua **Venus** bằng đường **VLAN venus** (`via 172.23.144.3, GigabitEthernet0/0.3`).

3. Đi qua **Mars** bằng đường **VLAN mars** (`via 172.23.128.2, GigabitEthernet0/0.2`).

4. Đi qua **Mars** bằng đường **VLAN venus** (`via 172.23.144.2, GigabitEthernet0/0.3`).

Chính vì có 4 đường này, mỗi khi ông Ping 5 gói, con Earth sẽ "chia bài" xoay vòng: Gói 1 đi đường 1, gói 2 đi đường 2, gói 3 đi đường 3, gói 4 đi đường 4, gói 5 lại quay về đường 1. Việc đổi đường liên tục khiến IP nguồn bị đổi theo (từ 128.1 sang 144.1), dẫn đến việc con Neptune bị lú lẫn khi dịch NAT PAT và đánh rơi 2-3 gói tin.

### 2. 

Lệnh đúng nếu gõ 1 dòng:
`ping 8.8.8.8 source Loopback1` (hoặc `source 172.23.0.1`)

  
**Tuy nhiên, cách khắc phục chuyên nghiệp (và 99% là "mảng miếng" thầy giáo sẽ dạy vào tuần sau) chính là tính năng Extended Ping (Ping mở rộng).**

Trong thực tế doanh nghiệp, các kỹ sư mạng không bao giờ gõ lệnh Ping kèm cụm `source` dài loằng ngoằng. Họ dùng trình đơn tương tác của Extended Ping để khóa cứng IP nguồn. Cách làm như sau:

1. Tại Router Earth, ông chỉ gõ chữ `ping` rồi bấm **Enter**.

2. Nó sẽ hiện ra một loạt các câu hỏi, ông nhập như sau (cái nào để trống nghĩa là cứ bấm Enter để lấy mặc định):

    - Protocol [ip]: _(Bấm Enter)_

    - Target IP address: **8.8.8.8**

    - Repeat count [5]: _(Bấm Enter)_

    - Datagram size [100]: _(Bấm Enter)_

    - Timeout in seconds [2]: _(Bấm Enter)_

    - **Extended commands [n]: y** _(Gõ chữ y để kích hoạt chế độ mở rộng)_

    - **Source address or interface: 172.23.0.1** _(Gõ IP của Loopback 1 vào đây)_

    - Type of service [0]: _(Bấm Enter)_

    - Set DF bit in IP header? [no]: _(Bấm Enter)_

    - Validate reply data? [no]: _(Bấm Enter)_

    - Data pattern [0xABCD]: _(Bấm Enter)_

    - Loose, Strict, Record, Timestamp, Verbose[none]: _(Bấm Enter)_

    - Sweep range of sizes [n]: _(Bấm Enter)_


Bởi vì  đã trói chặt IP nguồn là `172.23.0.1`. Dù con Earth có ném gói tin đi qua 4 con đường nào đi chăng nữa, thì IP nguồn vẫn không hề thay đổi. 

Con Neptune khi nhận được sẽ chỉ thấy duy nhất 1 IP đến, nó sẽ lập bảng NAT rất mượt và trả gói tin về đúng đích, triệt tiêu hoàn toàn lỗi NAT Collision! 