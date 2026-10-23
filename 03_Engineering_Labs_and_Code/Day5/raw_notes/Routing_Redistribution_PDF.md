Dưới đây là bản tóm tắt chi tiết và có hệ thống các kiến thức cốt lõi từ tài liệu "Routing Redistribution_2.pdf", được chia thành 4 chủ đề chính để ông dễ dàng áp dụng thẳng vào bài Lab đang làm:
### 1. Tái phân phối định tuyến (Route Redistribution)

Tái phân phối là quá trình một Router biên (Boundary Router) học các tuyến đường từ một giao thức định tuyến này và "bơm" (quảng bá) chúng sang một giao thức định tuyến khác.

**Nguyên tắc Seed Metric (Metric hạt giống):** Khi đưa route từ giao thức này sang giao thức khác, Router không hiểu Metric của nhau (ví dụ: RIP đếm hop, OSPF tính cost, EIGRP tính K-values). Do đó, phải gán một **Seed Metric** mặc định. Seed metric nên được thiết lập sao cho tuyến đường tái phân phối trông "tệ" hơn các tuyến nội bộ để tránh lặp (routing loop).

**Cú pháp cấu hình cho từng giao thức:**

- **Vào RIP:** Metric mặc định là vô cực (infinity), phải khai báo metric thủ công.
    - `Router(config-router)# redistribute ospf 1 metric 3`

- **Vào OSPF:** Metric mặc định là 20, loại Type 2 (E2). **Cực kỳ lưu ý:** Mặc định OSPF không tái phân phối các mạng chia nhỏ (subnets), bắt buộc phải thêm từ khóa `subnets`.
    - `Router(config-router)# redistribute eigrp 100 subnets metric-type 1`

- **Vào EIGRP:** Metric mặc định là vô cực, bắt buộc phải khai báo 5 tham số Seed Metric (Bandwidth, Delay, Reliability, Load, MTU).
    - `Router(config-router)# redistribute ospf 1 metric 10000 100 255 1 1500`

### 2. Kiểm soát cập nhật định tuyến (Controlling Routing Updates)

Để tránh quảng bá sai hoặc lọc bớt các tuyến đường không cần thiết, tài liệu cung cấp 3 công cụ:
- **Passive-interface:** Ngăn Router gửi các bản tin cập nhật định tuyến ra một cổng cụ thể (thường dùng cho cổng nối xuống mạng LAN/PC).

- **Distribute-list:** Sử dụng Access Control List (ACL) để cho phép (permit) hoặc chặn (deny) các tuyến đường cụ thể khi nhận vào (in) hoặc gửi đi (out).

- **Route Map:** Công cụ cực kỳ mạnh mẽ hoạt động như ngôn ngữ lập trình (If - Then). Dùng lệnh `match` để xét điều kiện và lệnh `set` để thay đổi thông số (ví dụ: đổi metric).
### 3. Khoảng cách quản trị (Administrative Distance - AD)

AD là độ tin cậy của một nguồn định tuyến. Khi Router học được cùng 1 mạng đích từ nhiều nguồn, nó sẽ ưu tiên nguồn có AD nhỏ nhất.

Bảng giá trị AD cần nhớ:
- Kết nối trực tiếp (Connected): 0
- Tuyến tĩnh (Static route): 1
- EIGRP nội bộ (Internal EIGRP): 90
- OSPF: 110
- RIPv1, RIPv2: 120
- EIGRP ngoại lai (External EIGRP - Hàng Redistribute): 170

**Sửa đổi AD (Modifying AD):** Trong các bài Lab có từ 2 điểm Redistribution trở lên (như con Jupiter và Mecury của ông), mạng rất dễ bị lặp vòng (Routing Loop) do Router học nhầm tuyến đường có AD thấp hơn nhưng lại đi đường vòng. Giải pháp là ép đổi giá trị AD của các giao thức.
- Cú pháp: `Router(config-router)# distance <trị-số-AD> <IP-nguồn> <Wildcard-mask> <ACL>`

### 4. Cấu hình dịch vụ DHCP & IP Helper

Thiết bị Cisco IOS có thể đóng vai trò làm DHCP Server (cấp IP), Client (nhận IP), hoặc Relay Agent (chuyển tiếp).

Cấu hình DHCP Server:
1. Loại trừ IP (thường là Gateway/Server): `ip dhcp excluded-address 192.168.1.1 192.168.1.10`

2. Tạo Pool: `ip dhcp pool <tên>`

3. Cấp mạng: `network 192.168.1.0 255.255.255.0`

4. Cấp Gateway: `default-router 192.168.1.1`

5. Cấp DNS: `dns-server 8.8.8.8`


Cấu hình DHCP Relay Agent (IP Helper): Khi máy trạm nằm khác mạng (khác Broadcast Domain) với DHCP Server, bản tin xin IP (Broadcast) sẽ bị Router chặn lại. Tính năng IP Helper sẽ tóm bản tin Broadcast này, đóng gói thành Unicast và gửi thẳng đến IP của DHCP Server.
- Cách dùng: Chui vào cổng (interface) đang trực tiếp nối với máy trạm và gõ lệnh: `Router(config-if)# ip helper-address <IP-của-DHCP-Server>`.