# 📜 AGENT PROTOCOL: GIAO THỨC VẬN HÀNH ĐA TÁC NHÂN
> **Môn học / Đồ án:** 03_Company_Network_Management_NMA
> **Trường Đại học Bách Khoa - Đại học Đà Nẵng (DUT)**
> **Hệ thống Quản trị Trung tâm:** [D:\AgentPlatform](file:///D:/AgentPlatform)
> **Tác giả / Kỹ sư phụ trách:** Nguyen Trung Kien (kien1152005@gmail.com)

---

## 1. NGUYÊN TẮC HOẠT ĐỘNG CỐT LÕI
Mọi Tác nhân Trí tuệ Nhân tạo (AI Agent) khi tham gia nghiên cứu, giải bài tập hoặc phát triển đồ án trong môn học này **BẮT BUỘC** tuân thủ các điều khoản sau:

1. **Tuân thủ State Machine & DAG**: Không nhảy cóc các giai đoạn. Bắt đầu từ Khảo sát Đề cương $\rightarrow$ Lập WBS Task Plan DAG $\rightarrow$ Hiện thực hóa (TDD) $\rightarrow$ Kiểm định Cú pháp & Bảo mật $\rightarrow$ Nghiệm thu Học thuật.
2. **Tối thiểu hóa Context Rot & Infinite Loops**: Tự động giải phóng biến tạm sau mỗi phiên, không lặp lại quá 3 lần thao tác sửa lỗi cùng một module mà không báo cáo người dùng.
3. **Cơ chế Kiểm định Nghiêm ngặt (Definition of Done - DoD 100%)**: Không được đánh dấu một task là hoàn thành nếu chưa thỏa mãn toàn bộ tiêu chí nghiệm thu cơ học.

---

## 2. CẤU TRÚC PHÂN CẤP THỦ THƯ & NGUỒN LỰC
```
.
├── AGENT_PROTOCOL.md            # Giao thức vận hành chính thức (Tệp này)
├── README.md                    # Tổng quan môn học & tiến độ thực tế
├── docs/
│   ├── syllabus/                # Đề cương chi tiết, lịch trình & Prerequisites DAG
│   └── lectures/                # Ghi chú học thuật có liên kết Wikilinks [[concept]]
├── slides/                      # Slide thuyết trình chuẩn Marp (presentation.marp.md)
├── exercises/                   # Bài tập lý thuyết, quiz & câu hỏi Active Recall
├── labs/                        # Mã nguồn thực hành & kịch bản kiểm thử TDD
└── reports/                     # Báo cáo tiến độ, đồ án định kỳ & nghiệm thu cuối kỳ
```

---

## 3. CÁC CỔNG KIỂM SOÁT NGHIỆM THU (QUALITY GATES)

### 🚪 Cổng 1: Thiết kế & Kế hoạch (Architect & Task Plan Review)
* Yêu cầu: Bản đặc tả kiến trúc phân rã công việc WBS không có chu trình tuần hoàn (Acyclic).
* Điều kiện qua cổng: Người dùng (Human-In-The-Loop) ký duyệt checkpoint trạng thái.

### 🚪 Cổng 2: Kiểm định Kỹ thuật (AST & Test-Driven Gate)
* Yêu cầu:
  * Không có lỗi cú pháp Python/JS/C++ (AST Parse Clean).
  * 100% Bộ kiểm thử tự động (Unit Test / Integration Test) phải vượt qua (`PASSED`).
  * Đo lường độ bao phủ kiểm thử tối thiểu $\ge 80\%$.

### 🚪 Cổng 3: Báo cáo & Bảo vệ Học thuật (Academic Defense Gate)
* Yêu cầu:
  * Xuất slide Marp phục vụ bảo vệ đồ án: `marp --pdf slides/presentation.marp.md`.
  * Có biểu đồ chứng minh thực nghiệm (nếu là môn AI/Data) hoặc sơ đồ mạng/packet capture (nếu là môn Mạng/An toàn thông tin).

---

## 4. ĐIỀU PHỐI TỪ AGENT PLATFORM MASTER CLI
Để chạy kiểm toán tự động hoặc thực thi quy trình chuẩn cho môn học này, sử dụng:

```powershell
# Kiểm toán tuân thủ toàn cục môn học
powershell -ExecutionPolicy Bypass -File "D:\AgentPlatform\cli\agent-platform.ps1" audit

# Chạy quy trình kiểm tra SOP Release đồ án
powershell -ExecutionPolicy Bypass -File "D:\AgentPlatform\cli\agent-platform.ps1" run-sop -Template "release_deployment_audit"
```
