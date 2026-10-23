chi tiết 4 vấn đề

- **1. Bản chất 4 địa chỉ `via` từ 2 VLAN:** Nhìn vào sơ đồ thiết kế, Router Earth cắm thẳng xuống Switch Server. Trong khi đó, cả Router Mars và Venus đều được cắm cáp kết nối vào hệ thống Switch Layer 2 này. Do ông đã cấu hình Trunking cho cả VLAN 2 (`mars`) và VLAN 3 (`venus`) chạy thông suốt toàn bộ hệ thống Switch, nên từ góc nhìn của Earth, để đi đến đích nó sẽ thấy: 2 ngả đường đi qua Mars (một ngả qua IP VLAN 2, một ngả qua IP VLAN 3) và 2 ngả đường đi qua Venus (cũng qua IP VLAN 2 và VLAN 3). Tổng cộng là 4 con đường có mức ưu tiên (Cost) bằng y hệt nhau, nên OSPF đưa cả 4 vào bảng định tuyến để chạy cân bằng tải.
    
      
    
- **2. Sự thật về lệnh Ping kèm cụm `source`:** Ông thấy gõ `ping 8.8.8.8 source Loopback1` tiện hơn là hoàn toàn chính xác. Trên các thiết bị Cisco thực tế chạy hệ điều hành IOS đời mới, mọi người đều gõ một dòng như vậy cho nhanh. Câu nói "kỹ sư không gõ vậy" là để ám chỉ trong môi trường giả lập (như Packet Tracer mô phỏng IOS đời cũ) hoặc các kỳ thi chứng chỉ khắt khe, lệnh gộp này hay bị báo lỗi cú pháp (như lỗi dấu `^` ông gặp). Khi đó, kỹ năng dùng Extended Ping (chỉ gõ chữ `ping` rồi Enter để trả lời từng câu hỏi) là "võ công" bắt buộc phải biết vì nó chạy mượt trên 100% mọi đời máy.
    
      
    
- **3. Thời điểm cấp IP Nguồn (Source IP):** Suy luận của ông rất chuẩn. Khi Earth tự khởi tạo lệnh Ping mà không bị ép IP nguồn, nó sẽ chờ đến phần ngàn giây cuối cùng khi gói tin bị đẩy ra khỏi cổng vật lý nào, nó sẽ lấy luôn IP của cổng ảo tương ứng (VLAN 2 hoặc VLAN 3) làm IP nguồn. Do Earth đang chia bài qua 4 đường luân phiên, IP nguồn liên tục bị tráo đổi, làm con Neptune bị loạn bảng dịch NAT dẫn đến đánh rơi gói tin.
    
      
    
- **4. Mánh khóe của thầy giáo:** Sự nghi ngờ của ông rất có cơ sở. Nếu thầy biểu diễn gõ đúng lệnh `ping 8.8.8.8` đơn giản mà 5 gói đi trót lọt 100%, thì thầy đã âm thầm **can thiệp vào OSPF Cost để triệt tiêu tính năng cân bằng tải (ECMP)**. Cụ thể, thầy sẽ vào cấu hình 1 trong 4 cổng ảo (ví dụ cổng VLAN 2 hướng đi Mars) và hạ Cost xuống thấp nhất. Lúc đó bảng định tuyến của Earth sẽ xóa 3 đường kia đi, dồn toàn bộ lưu lượng vào 1 cửa duy nhất. Khi chỉ còn 1 đường ra, IP nguồn sẽ đứng im không đổi, NAT sẽ hoạt động hoàn hảo và ping xanh rờn ngay lập tức.

cấu hình Trunking, 