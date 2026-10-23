## GIAI ĐOẠN 1: BẢNG PHÂN BỔ IP (VLSM)

**Dải OSPF (172.23.0.0/16) - Cấp cho khu vực bên trái:**
- **lo1 (Earth):** 8000 hosts -> `/19` -> `172.23.0.0/19`
- **lo2 (Mars):** 8000 hosts -> `/19` -> `172.23.32.0/19`
- **lo3 (Venus):** 8000 hosts -> `/19` -> `172.23.64.0/19`
- **lo4 (Jupiter):** 8000 hosts -> `/19` -> `172.23.96.0/19`
- **VLAN 2 (mars):** 4000 hosts -> `/20` -> `172.23.128.0/20`
- **VLAN 3 (venus):** 4000 hosts -> `/20` -> `172.23.144.0/20`

**Dải EIGRP (172.22.0.0/16) - Cấp cho khu vực bên phải:**
- **lo5 (Mecury):** 8000 hosts -> `/19` -> `172.22.0.0/19`

*(Các mạng Point-to-Point nối Router sử dụng Subnet `/30` cắt từ cuối dải IP)*




# BẮT ĐẦU CẤU HÌNH

## GIAI ĐOẠN 2: CẤU HÌNH LAYER 2 (SWITCHES)

_Mục tiêu: Đẩy VTP, tạo VLAN 2, 3 và bật chế độ Trunking trên toàn bộ các cổng nối đến Router._

**1. Trên Switch "Server":**

Cisco CLI

```
enable
configure terminal
hostname Server

! Cấu hình VTP
vtp domain planet
vtp password solar
vtp mode server

! Tạo VLAN
vlan 2
 name mars
vlan 3
 name venus
exit

! Cấu hình Trunking cho 3 cổng kết nối
interface range FastEthernet0/1 - 3
 switchport mode trunk
 switchport trunk allowed vlan 2,3
 no shutdown
exit
```

**2. Trên Switch "Client":**

Cisco CLI

```
enable
configure terminal
hostname Client

! Cấu hình VTP Client
vtp domain planet
vtp password solar
vtp mode client

! Cấu hình Trunking cho 2 cổng kết nối
interface range FastEthernet0/1 - 2
 switchport mode trunk
 switchport trunk allowed vlan 2,3
 no shutdown
exit
```

## GIAI ĐOẠN 3: CẤU HÌNH LAYER 3 (INTER-VLAN & OSPF/EIGRP)

_Mục tiêu: Đặt IP Sub-interface cho VLAN, đặt IP Serial và cấu hình giao thức OSPF/EIGRP chạy bên dưới._

**1. Router Earth (Vùng OSPF Area 0):**

Cisco CLI

```
enable
configure terminal
hostname Earth

! Cổng Loopback 1
interface loopback 1
 ip address 172.23.0.1 255.255.224.0
exit

! Bật cổng vật lý Gig0/0
interface Gig0/0
 no shutdown
exit

! Sub-interface cho VLAN 2 (mars)
interface Gig0/0.2
 encapsulation dot1Q 2
 ip address 172.23.128.1 255.255.240.0
exit

! Sub-interface cho VLAN 3 (venus)
interface Gig0/0.3
 encapsulation dot1Q 3
 ip address 172.23.144.1 255.255.240.0
exit

! Chạy OSPF Area 0
router ospf 1
 network 172.23.0.0 0.0.31.255 area 0
 network 172.23.128.0 0.0.15.255 area 0
 network 172.23.144.0 0.0.15.255 area 0
exit
```

**2. Router Mars (ABR - Giữa Area 0 và Area 2):**

Cisco CLI

```
enable
configure terminal
hostname Mars

! Cổng Loopback 2
interface loopback 2
 ip address 172.23.32.1 255.255.224.0
exit

! Bật cổng vật lý Gig0/0
interface Gig0/0
 no shutdown
exit

! Sub-interface cho VLAN 2
interface Gig0/0.2
 encapsulation dot1Q 2
 ip address 172.23.128.2 255.255.240.0
exit

! Sub-interface cho VLAN 3
interface Gig0/0.3
 encapsulation dot1Q 3
 ip address 172.23.144.2 255.255.240.0
exit

! Cổng Serial nối Jupiter (DCE cấp Clock)
interface Serial0/3/0
 ip address 172.23.255.1 255.255.255.252
 clock rate 64000
 no shutdown
exit

! Chạy OSPF
router ospf 1
 ! Đẩy các mạng VLAN vào Area 0
 network 172.23.128.0 0.0.15.255 area 0
 network 172.23.144.0 0.0.15.255 area 0
 ! Đẩy mạng Serial và Loopback vào Area 2
 network 172.23.32.0 0.0.31.255 area 2
 network 172.23.255.0 0.0.0.3 area 2
exit
```

**3. Router Venus (ABR - Giữa Area 0 và Area 1):**

Cisco CLI

```
enable
configure terminal
hostname Venus

! Cổng Loopback 3
interface loopback 3
 ip address 172.23.64.1 255.255.224.0
exit

! Bật cổng vật lý Gig0/0
interface Gig0/0
 no shutdown
exit

! Sub-interface cho VLAN 2
interface Gig0/0.2
 encapsulation dot1Q 2
 ip address 172.23.128.3 255.255.240.0
exit

! Sub-interface cho VLAN 3
interface Gig0/0.3
 encapsulation dot1Q 3
 ip address 172.23.144.3 255.255.240.0
exit

! Cổng Serial nối Mecury (DCE cấp Clock)
interface Serial0/3/0
 ip address 172.23.255.5 255.255.255.252
 clock rate 64000
 no shutdown
exit

! Chạy OSPF
router ospf 1
 ! Đẩy VLAN vào Area 0
 network 172.23.128.0 0.0.15.255 area 0
 network 172.23.144.0 0.0.15.255 area 0
 ! Đẩy Serial và Loopback vào Area 1
 network 172.23.64.0 0.0.31.255 area 1
 network 172.23.255.4 0.0.0.3 area 1
exit
```

**4. Router Jupiter (Điểm Tái phân phối - Chạy cả OSPF và EIGRP):**

Cisco CLI

```
enable
configure terminal
hostname Jupiter

! Cổng Loopback 4
interface loopback 4
 ip address 172.23.96.1 255.255.224.0
exit

! Cổng Serial nối về Mars
interface Serial0/3/0
 ip address 172.23.255.2 255.255.255.252
 no shutdown
exit

! Cổng Serial nối về Neptune
interface Serial0/3/1
 ip address 172.22.255.1 255.255.255.252
 no shutdown
exit

! Chạy OSPF Area 2
router ospf 1
 network 172.23.96.0 0.0.31.255 area 2
 network 172.23.255.0 0.0.0.3 area 2
exit

! Chạy EIGRP AS 69
router eigrp 69
 no auto-summary
 network 172.22.255.0 0.0.0.3
exit
```

**5. Router Mecury (Điểm Tái phân phối - Chạy cả OSPF và EIGRP):**

Cisco CLI

```
enable
configure terminal
hostname Mecury

! Cổng Loopback 5
interface loopback 5
 ip address 172.22.0.1 255.255.224.0
exit

! Cổng Serial nối về Venus
interface Serial0/3/0
 ip address 172.23.255.6 255.255.255.252
 no shutdown
exit

! Cổng Serial nối về Neptune
interface Serial0/3/1
 ip address 172.22.255.5 255.255.255.252
 no shutdown
exit

! Chạy OSPF Area 1
router ospf 1
 network 172.23.255.4 0.0.0.3 area 1
exit

! Chạy EIGRP AS 69
router eigrp 69
 no auto-summary
 network 172.22.0.0 0.0.31.255
 network 172.22.255.4 0.0.0.3
exit
```

**6. Router Neptune (Vùng EIGRP & Ra Internet):**

Cisco CLI

```
enable
configure terminal
hostname Neptune

! Cổng Serial nối Jupiter (DCE cấp Clock)
interface Serial0/3/1
 ip address 172.22.255.2 255.255.255.252
 clock rate 64000
 no shutdown
exit

! Cổng Serial nối Mecury (DCE cấp Clock)
interface Serial0/3/0
 ip address 172.22.255.6 255.255.255.252
 clock rate 64000
 no shutdown
exit

! Cổng nối ra ISP
interface Gig0/0
 ip address 192.168.0.10 255.255.255.0
 no shutdown
exit

! Chạy EIGRP
router eigrp 69
 no auto-summary
 network 172.22.255.0 0.0.0.3
 network 172.22.255.4 0.0.0.3
exit
```

Lưu ý về: **Giai đoạn 4: Tái phân phối và NAT**. 
Đây là phần tinh hoa nhất của bài này vì nó chứa cái bẫy "chết người" mà thầy giáo đã ghi chú trong đề: **"(beware of default route)"**.

**Tại sao lại có bẫy ở đây?** Khi Neptune đẩy tuyến mặc định (Default route) vào EIGRP, nó sẽ có AD = 170 (External EIGRP). Khi Jupiter lấy tuyến đó bơm vào OSPF, nó biến thành OSPF External (AD = 110). Lúc này, con Mecury sẽ nhận được tuyến mặc định từ 2 hướng: từ Neptune (AD = 170) và từ Jupiter (AD = 110). Do 110 < 170, Mecury sẽ "ngu ngốc" vứt bỏ đường nối trực tiếp với Neptune để chạy vòng qua Jupiter. Thế là sinh ra Routing Loop!

**Cách giải quyết:** Áp dụng kiến thức sửa AD ở slide 40-46. Ta sẽ ép OSPF trên Jupiter và Mecury hạ độ ưu tiên của hàng External xuống (đổi AD từ 110 thành 175) để nó luôn ưu tiên đường EIGRP (170) ra Internet.

## GIAI ĐOẠN 4: REDISTRIBUTION & NAT

**1. Router Neptune (Cấu hình NAT & Default Route ra Internet):**

Cisco CLI

```
enable
configure terminal

! 1. Tạo tuyến mặc định trỏ ra ISP (Giả sử IP của ISP là 192.168.0.1)
ip route 0.0.0.0 0.0.0.0 192.168.0.1

! 2. Cấu hình NAT Pool (192.168.0.11 đến .22)
ip nat pool ISP-POOL 192.168.0.11 192.168.0.22 netmask 255.255.255.0

! 3. ACL cho phép 2 dải mạng OSPF và EIGRP được phép NAT ra mạng
access-list 1 permit 172.22.0.0 0.0.255.255
access-list 1 permit 172.23.0.0 0.0.255.255

! 4. Bật NAT Inside -> Outside
ip nat inside source list 1 pool ISP-POOL

! 5. Gán cổng Outside (hướng ra ISP)
interface Gig0/0
 ip nat outside
exit

! 6. Gán cổng Inside (hướng về nội bộ)
interface Serial0/3/0
 ip nat inside
exit
interface Serial0/3/1
 ip nat inside
exit

! 7. Quảng bá tuyến mặc định (Default Route) vào mạng nội bộ EIGRP
router eigrp 69
 redistribute static metric 10000 100 255 1 1500
exit
```

**2. Router Jupiter (Tái phân phối - Giải quyết bẫy Loop):**

Cisco CLI

```
enable
configure terminal

! Tái phân phối từ OSPF sang EIGRP
router eigrp 69
 redistribute ospf 1 metric 10000 100 255 1 1500
exit

! Tái phân phối từ EIGRP sang OSPF
router ospf 1
 redistribute eigrp 69 subnets
 ! Sửa AD để chống Routing Loop cho Default Route
 distance ospf external 175
exit
```

**3. Router Mecury (Tái phân phối - Giải quyết bẫy Loop):**

Cisco CLI

```
enable
configure terminal

! Tái phân phối từ OSPF sang EIGRP
router eigrp 69
 redistribute ospf 1 metric 10000 100 255 1 1500
exit

! Tái phân phối từ EIGRP sang OSPF
router ospf 1
 redistribute eigrp 69 subnets
 ! Sửa AD để chống Routing Loop cho Default Route
 distance ospf external 175
exit
```

Nếu Ping thông ra tới IP của ISP (`192.168.0.1`). thì làm tiếp 

 Kết quả ping thành công (0% loss) ở ảnh 1 khẳng định thuật toán định tuyến OSPF/EIGRP, cơ chế Tái phân phối (Redistribution) và việc chặn Routing Loop của ông đã hoạt động hoàn hảo.

Để hoàn thiện phần kiểm tra NAT và chuyển sang Giai đoạn 5, chúng ta cần cấp IP cho cổng của con Router ISP.
### Bước 1: Kích hoạt Router ISP để kiểm tra NAT

Nhìn vào ảnh 2, Router ISP kết nối với DSL Modem qua cổng `Fa0/0`. Mở tab CLI của con **Router ISP** và dán đoạn lệnh sau để gán IP Default Gateway (`192.168.0.1`):

Cisco CLI

```
enable
configure terminal
interface FastEthernet0/0
 ip address 192.168.0.1 255.255.255.0
 no shutdown
exit
```

**Cách xác minh NAT:** Quay lại PC0, gõ lệnh `ping 192.168.0.1`. Nếu kết quả trả về `Reply from 192.168.0.1`, hệ thống NAT trên Neptune đã dịch IP thành công và mạng nội bộ đã thông ra Internet.

### GIAI ĐOẠN 5: CẤU HÌNH BẢO MẬT (AUTHENTICATION)

Đây là yêu cầu cuối cùng của đề bài: OSPF dùng `md5`, password là `cat`; EIGRP dùng key `11`, password là `mouse`. Lưu ý dán code đồng loạt để tránh mạng bị rớt do sai lệch mật khẩu giữa các thiết bị.

**1. Bảo mật EIGRP (Áp dụng cho Jupiter, Mecury, Neptune)**

Trên **Neptune**:

Cisco CLI

```
enable
configure terminal
key chain EIGRP_KEY
 key 11
  key-string mouse
exit
interface Serial0/3/0
 ip authentication mode eigrp 69 md5
 ip authentication key-chain eigrp 69 EIGRP_KEY
exit
interface Serial0/3/1
 ip authentication mode eigrp 69 md5
 ip authentication key-chain eigrp 69 EIGRP_KEY
exit
```


Trên **Jupiter**:

Cisco CLI

```
enable
configure terminal
key chain EIGRP_KEY
 key 11
  key-string mouse
exit
interface Serial0/3/1
 ip authentication mode eigrp 69 md5
 ip authentication key-chain eigrp 69 EIGRP_KEY
exit
```

Trên **Mecury**:

Cisco CLI

```
enable
configure terminal
key chain EIGRP_KEY
 key 11
  key-string mouse
exit
interface Serial0/3/1
 ip authentication mode eigrp 69 md5
 ip authentication key-chain eigrp 69 EIGRP_KEY
exit
```

**2. Bảo mật OSPF (Áp dụng cho Earth, Mars, Venus, Jupiter, Mecury)**

Trên **Earth**:

Cisco CLI

```
enable
configure terminal
interface Gig0/0.2
 ip ospf message-digest-key 1 md5 cat
exit
interface Gig0/0.3
 ip ospf message-digest-key 1 md5 cat
exit
router ospf 1
 area 0 authentication message-digest
exit
```


Trên **Mars**:

Cisco CLI

```
enable
configure terminal
interface Gig0/0.2
 ip ospf message-digest-key 1 md5 cat
exit
interface Gig0/0.3
 ip ospf message-digest-key 1 md5 cat
exit
interface Serial0/3/0
 ip ospf message-digest-key 1 md5 cat
exit
router ospf 1
 area 0 authentication message-digest
 area 2 authentication message-digest
exit
```


Trên **Venus**:

Cisco CLI

```
enable
configure terminal
interface Gig0/0.2
 ip ospf message-digest-key 1 md5 cat
exit
interface Gig0/0.3
 ip ospf message-digest-key 1 md5 cat
exit
interface Serial0/3/0
 ip ospf message-digest-key 1 md5 cat
exit
router ospf 1
 area 0 authentication message-digest
 area 1 authentication message-digest
exit
```


Trên **Jupiter**:

Cisco CLI

```
enable
configure terminal
interface Serial0/3/0
 ip ospf message-digest-key 1 md5 cat
exit
router ospf 1
 area 2 authentication message-digest
exit
```


Trên **Mecury**:

Cisco CLI

```
enable
configure terminal
interface Serial0/3/0
 ip ospf message-digest-key 1 md5 cat
exit
router ospf 1
 area 1 authentication message-digest
exit
```

Dán xong toàn bộ, đợi khoảng 15 giây để các Router thiết lập lại kết nối láng giềng. Hãy dùng lệnh `ping 192.168.0.1` một lần nữa từ PC0. Nếu ping vẫn thông báo `Reply`, bài Lab của ông đã hoàn thành xuất sắc 100%. Lệnh nào báo lỗi thì phản hồi lại cấu hình hoặc ảnh chụp màn hình để điều chỉnh.


#### NHẬT KÝ XỬ LÝ SỰ CỐ (TROUBLESHOOTING LOG)

**Sự cố 1: Bảng định tuyến OSPF mất tuyến mặc định (Default Route)**
- **Hiện tượng:** Máy PC0 ping ra cổng Outside của Neptune (192.168.0.10) báo lỗi `Destination host unreachable`.
- **Nguyên nhân:** Lệnh Tái phân phối (Redistribute) mặc định không tự động đẩy tuyến 0.0.0.0/0 từ EIGRP sang OSPF. Ngoài ra, mạng nối ra ISP trên Neptune là mạng Connected, chưa được phân phối.
- **Cách khắc phục:** 
  1. Thêm lệnh `default-information originate` vào tiến trình OSPF trên 2 Router biên (Jupiter, Mecury).
  2. Thêm lệnh `redistribute connected` vào EIGRP trên Neptune.

**Sự cố 2: Lỗi Local Loop khi test NAT trong Packet Tracer**
- **Hiện tượng:** Khi ping thẳng vào IP Outside của Neptune (192.168.0.10) từ PC0 thì xuất hiện lỗi `Request timed out` (dù gói tin đã đi tới nơi).
- **Nguyên nhân:** Khi Router Neptune nhận gói tin và NAT, nó cố gắng trả lời lại IP ảo vừa được NAT trên cùng một cổng, gây ra lỗi vòng lặp cục bộ (đặc thù của mô phỏng Packet Tracer).
- **Cách khắc phục:** Dựng IP thực tế cho Router ISP (`192.168.0.1`) và cho PC0 ping thẳng ra IP của ISP. Kết quả thông suốt 0% loss.

#### CÁC LỆNH KIỂM TRA (VERIFICATION)
- Kiểm tra láng giềng OSPF/EIGRP: `show ip ospf neighbor` / `show ip eigrp neighbors`
- Kiểm tra bảng định tuyến (phải có đủ tuyến O*E2 và D EX): `show ip route`
- Kiểm tra bảng dịch NAT (sau khi ping Internet): `show ip nat translations`