![[{B64BC9B2-94FB-4711-9C0E-F0BA9910258D}.png]]
# TÓM TẮT ĐỀ LAB: Multi Area OSPF - EIGRP - VLAN

## 1. Quy hoạch không gian IP (VLSM)

- **Vùng OSPF:** Sử dụng dải mạng chính `172.23.0.0/16`.

- **Vùng EIGRP:** Sử dụng dải mạng chính `172.22.0.0/16`.

- **Yêu cầu Host:**
    - Các Loopback (`lo1` -> `lo5`): **8000 nodes/nhánh** $\rightarrow$ Cần Subnet `/19`.
    - Các VLAN (`mars`, `venus`): **4000 nodes/nhánh** $\rightarrow$ Cần Subnet `/20`.

- _(Tự tính toán thêm IP Point-to-Point `/30` cho các đoạn cáp nối giữa các Router)._

## 2. Cấu hình Layer 2 (Switching & VLAN)

- **VLAN:** Tạo VLAN 2 (tên: `mars`) và VLAN 3 (tên: `venus`).

- **VTP:** Domain = `planet`, Password = `solar`.

- **Trunking:** Các đường nối giữa 2 Switch (Server - Client) và đường lên Router (Earth) phải cấu hình Trunking (`T`).
## 3. Cấu hình Layer 3 (Định tuyến nội bộ - IGP)

- **Inter-VLAN Routing:** Triển khai trên các Router **Earth, Mars, Venus** để định tuyến cho VLAN.

- **OSPF (Đa vùng):**
    - Area 0 (Backbone): Nằm ở Earth, Client, Server.
    - Area 1: Nằm ở Venus, Mecury.
    - Area 2: Nằm ở Mars, Jupiter.
    - _Mars và Venus đóng vai trò ABR (Định tuyến liên vùng - Inter-area)._

- **EIGRP:** Chạy AS **69** trên khu vực Jupiter, Mecury, Neptune.
## 4. Tái phân phối (Redistribution) & Cấu hình Biên (Edge)

- **Redistribution:** Thực hiện trên **Jupiter** và **Mecury** (chuyển đổi qua lại giữa OSPF và EIGRP).
    - _Lưu ý từ đề bài:_ Chú ý cẩn thận với Default Route (để tránh bẫy Routing Loop).

- **Neptune (Router giao tiếp ISP):**
    - Cấu hình **NAT** với Pool IP public: `192.168.0.11` đến `192.168.0.22/24`.
    - Cấu hình **Default Route** trỏ ra ISP.
    - Quảng bá tuyến mặc định vào trong mạng nội bộ (**Default network**).
## 5. Tùy chọn Bảo mật (Authentication)

- **OSPF:** Dùng mã hóa MD5, password = `cat`.

- **EIGRP:** Dùng key chain = `11`, key-string = `mouse`.


### BẢN ĐỒ KẾT NỐI VẬT LÝ
**1. Vùng Mạng LAN (Cáp thẳng - Gigabit/FastEthernet):**

- **Earth** `Gig0/0` $\leftrightarrow$ `Fa0/1` **Server**
    
- **Server** `Fa0/3` $\leftrightarrow$ `Gig0/0` **Mars**
    
- **Server** `Fa0/2` $\leftrightarrow$ `Fa0/1` **Client**
    
- **Client** `Fa0/2` $\leftrightarrow$ `Gig0/0` **Venus**

**2. Vùng Định Tuyến WAN (Cáp Ziczac Đỏ - Serial):**

- **Mars** `Se0/3/0` _(DCE)_ $\leftrightarrow$ `Se0/3/0` **Jupiter**
    
- **Venus** `Se0/3/0` _(DCE)_ $\leftrightarrow$ `Se0/3/0` **Mecury**
    
- **Jupiter** `Se0/3/1` $\leftrightarrow$ `Se0/3/1` _(DCE)_ **Neptune**
    
- **Mecury** `Se0/3/1` $\leftrightarrow$ `Se0/3/0` _(DCE)_ **Neptune**

### Subnets như sau:
- **5 subnets cho các mạng LAN ảo (Loopback):** Lần lượt là `lo1`, `lo2`, `lo3`, `lo4`, và `lo5`.

- **2 subnets cho các VLAN:** Mạng `vlan mars` và `vlan venus`. (vlan 2,3)

- **4 subnets cho các đường trục WAN (:** Gồm các đoạn kết nối trực tiếp Mars - Jupiter, Jupiter - Neptune, Venus - Mecury, và Mecury - Neptune.

- **1 subnet kết nối Internet:** Đoạn cáp nối từ Router Neptune ra ISP (sử dụng dải IP `192.168.0.0/24`).

Tổng cộng: $5 + 2 + 4 + 1 = 12$ subnets.
	Vậy 1 Router sẽ có tổng cộng 12 subnets, riêng cục router nối ra internet (Neptune) ra 13 vì tính thêm 1 tuyến ngầm định

Còn về câu hỏi **tại sao không thấy khai báo Cost của OSPF** thì vẫn áp dụng nguyên lý mặc định của Cisco mà tôi đã giải thích nhé: Khi tái phân phối (Redistribute), OSPF sẽ âm thầm tự "bơm" một cái Seed Metric (Cost) mặc định bằng 20, nên anh em mình đỡ được một bước gõ tay trong code.

![[{B0F2D86A-2CF9-4810-A45D-5C5BFB95096E}.png]]
Neptune > show ip route:
![[{3623DD44-E267-4F96-8619-5B2E30EC5037}.png]]

Jupiter > show ip route:
![[{235E27DE-64EE-4A37-8289-55F085B390B6}.png]]

Mercury > show ip route:
![[{0E3492C9-3C85-4F68-8BD1-5724C6596E43}.png]]

Mars > show ip route:
![[{A4E2850A-488C-4844-9CBF-82AA9B52DD13}.png]]

Venus > show ip route
![[{C957CCA1-83CC-4B64-80A6-87B779F2F229}.png]]

Earth > show ip route
![[{9F542CFE-E04A-45D8-85A0-50B7B56F3AF5}.png]]Tuy nhiên, trong thực tế thiết kế (và đúng với ý đồ của thầy giáo), các Router nằm sâu bên trong nội bộ (như Earth, Mars, Jupiter...) **không cần thiết phải học đích danh** dải mạng của ISP. Bởi vì chúng ta đã có **Tuyến ngầm định (Default Route `0.0.0.0/0`)** đóng vai trò "hứng" tất cả các IP lạ rồi. Việc tống thêm dải Connected của ISP vào bảng định tuyến nội bộ chỉ làm dư thừa một dòng không đáng có.

Để "gọt" lại bảng định tuyến cho gọn gàng và khớp 100% với bài chuẩn,  chỉ cần lên con **Neptune** gỡ lệnh đó ra:

Cisco CLI
```
enable
configure terminal
router eigrp 69
 no redistribute connected
exit
```
Gõ xong, đợi vài giây cho mạng hội tụ lại, sau đó quay về con **Earth** gõ `show ip route`.

Earth > show ip route (after)
![[{5167BBBA-D694-4FED-A64A-47C011BFE654}.png]]

Tiếp tục là test ở PC0:
Test lần lượt:
tracert 192.168.0.1
ping 192.168.0.1
![[{9AFFD3CC-DCFA-4D4B-9D2B-6C307707E17F}.png]]