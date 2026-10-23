
## 1. WORKING MEMORY & NETWORK CONTEXT
- Môn học: Quản trị mạng DUT (NetAdmin Corp) | Tuần [X]
- Thiết bị tác nghiệp: [Router Cisco 2911 / Switch 2960 / Windows Server 2022 / Ubuntu Server 22.04]
- Giao thức liên quan: [DHCP Relay / DNS Forwarder / Inter-VLAN SVI / AD DS GPO]

## 2. NEGATIVE CONSTRAINTS (BẮT BUỘC TUÂN THỦ)
1. CẤM TUYỆT ĐỐI đưa ra câu lệnh cấu hình mà không có Bảng phân bổ IP và Topo mạng rõ ràng.
2. MỌI khối lệnh Cisco IOS hoặc PowerShell bắt buộc phải có chú thích giải thích từng tham số ở từng dòng.
3. BẮT BUỘC cung cấp danh sách lệnh kiểm tra trạng thái (`show ...` hoặc `Get-... / Test-...`).
4. TUYỆT ĐỐI KHÔNG hướng dẫn tắt tường lửa (`netsh advfirewall set allprofiles state off` hoặc `ufw disable`) như một giải pháp xử lý sự cố chính thức.

## 3. NHIỆM VỤ CHI TIẾT
[
Sinh viên muốn học cho tới khi thành thạo bài tự làm bài này:
[1] Thiết kế, triển khai và quản trị quán Cafe WIFI
Yêu cầu:
1. Quán Coffee có 2 tầng. Tính toán bán kính vùng phủ sóng để triển khai ít nhất 2 Access Point (AP) thích hợp nhằm đảm bảo không có điểm chết. Số liệu tính toán dựa vào kích thước của quán. Từ đó suy ra chọn chuẩn WIFI nào (5, 6 hay 7).
2. Tính toán số IP để cấp đủ cho số lượng các thiết bị lúc cao điểm (ví dụ: xem Champion League hoặc giải Ngoại hang Anh)
3. Tính toán băng thông Internet thuê bao thích hợp để phát được ít nhất Video Youtube với chuẩn FullHD.
4. Chọn thiết bị Access Point (AP) thích hợp đảm bảo chịu tải tối đa khi cao điểm.
5. Sau khi thiết kế xong (trên giấy/word) thì triển khai sơ đồ với Packet Tracer. Làm thế nào để khi triển khai nhiều AP thì hạn chế nhiễu? Bảo mật WIFI với WPA2 Personal (PSK: Pre-shared Key)


 ]

## 4. CẤU TRÚC ĐẦU RA YÊU CẦU
- 🗺️ **Sơ đồ Topo & Bảng IP**: Bảng Markdown liệt kê Interface, IP Address, Subnet Mask, VLAN ID.
- ⚙️ **Khối lệnh cấu hình (CLI/PowerShell)**: Có comment chi tiết từng dòng.
- 🔍 **Quy trình kiểm thử & Bắt gói tin**: Lệnh ping, traceroute hoặc bộ lọc Wireshark để xác thực luồng tin.
- ⚠️ **Lỗi phổ biến sinh viên hay gặp**: Nêu ít nhất 2 lỗi cấu hình kinh điển (Quên `no shutdown`, sai encapsulation dot1Q, lệch Default Gateway).
- 💡 **Micro-quiz**: 1 câu hỏi phản biện về hoạt động của giao thức.