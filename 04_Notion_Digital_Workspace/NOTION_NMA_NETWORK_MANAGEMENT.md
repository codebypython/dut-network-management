# 📡 MASTER WORKSPACE: QUẢN TRỊ MẠNG (NMA-DUT)
# Đại học Bách khoa — Đại học Đà Nẵng | Semester 7

> 🏛️ **Mã học phần**: NMA-DUT (Quản trị Mạng & Hệ thống)
> ⏱️ **Thời lượng**: 15 tuần (3TC lý thuyết + 1.5TC thực hành)
> 🎯 **CLOs**: FCAPS → DHCP/DNS/VLAN → AD/GPO/LDAP → Web/File/Mail → SNMP/Firewall/VPN/Backup

---

## 📊 I. COURSE PROGRESS TRACKER — THEO DÕI TIẾN ĐỘ 15 TUẦN

> 💡 **Notion**: Convert thành Database → Tạo **Board View** theo `Giai đoạn` và **Timeline View** theo `Tuần`.

| Tuần | Chủ Đề | Module | CLO | Lý Thuyết | Lab | Báo Cáo Lab | Trạng Thái | Ghi Chú |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- |
| W1 | Tổng quan QTM, FCAPS, Thiết lập Lab | Mod-1 | CLO-1 | ⬜ | ⬜ Lab 01 | ⬜ | 🔲 Chưa bắt đầu | VMware + Packet Tracer + GNS3 |
| W2 | VLSM/CIDR, VLAN 802.1Q, Trunking | Mod-2 | CLO-2 | ⬜ | ⬜ Lab 02 | ⬜ | 🔲 Chưa bắt đầu | VLAN 10/20/30, Trunk |
| W3 | Inter-VLAN Routing, Static/OSPF | Mod-2 | CLO-2 | ⬜ | ⬜ Lab 03 | ⬜ | 🔲 Chưa bắt đầu | Router-on-a-Stick vs L3 SVI |
| W4 | DHCP Server & Relay Agent | Mod-2 | CLO-2 | ⬜ | ⬜ Lab 04 | ⬜ | 🔲 Chưa bắt đầu | DORA, Split Scope 80/20 |
| W5 | DNS Server & Phân giải tên miền | Mod-2 | CLO-2 | ⬜ | ⬜ Lab 05 | ⬜ | 🔲 Chưa bắt đầu | Forward/Reverse Zone, Bind9 |
| W6 | Active Directory DS & Domain Controller | Mod-3 | CLO-3 | ⬜ | ⬜ Lab 06 | ⬜ | 🔲 Chưa bắt đầu | FSMO, Kerberos, Join Domain |
| W7 | Group Policy Objects (GPO) | Mod-3 | CLO-3 | ⬜ | ⬜ Lab 07 | ⬜ | 🔲 Chưa bắt đầu | LSDOU, Security Filtering |
| W8 | OpenLDAP & SAMBA Domain | Mod-3 | CLO-3 | ⬜ | ⬜ Lab 08 | ⬜ | 🔲 Chưa bắt đầu | LDAP, sssd, realmd |
| **W9** | **THI GIỮA KỲ** | **—** | **CLO 1-3** | **—** | **🧪 Live Lab 90p** | **—** | 🔲 Chưa bắt đầu | **Toàn bộ Module 1-3** |
| W10 | Web Server & SSL/TLS (HTTPS) | Mod-4 | CLO-4 | ⬜ | ⬜ Lab 09 | ⬜ | 🔲 Chưa bắt đầu | IIS + Nginx, Virtual Host |
| W11 | File Server, NTFS/Share, Quota | Mod-4 | CLO-4 | ⬜ | ⬜ Lab 10 | ⬜ | 🔲 Chưa bắt đầu | ABE, FSRM, NFS |
| W12 | Mail Server, MX, SPF, DKIM | Mod-4 | CLO-4 | ⬜ | ⬜ Lab 11 | ⬜ | 🔲 Chưa bắt đầu | Postfix + Dovecot + Roundcube |
| W13 | SNMP, Syslog & Wireshark | Mod-5 | CLO-5 | ⬜ | ⬜ Lab 12 | ⬜ | 🔲 Chưa bắt đầu | Zabbix, Rsyslog, SNMPv3 |
| W14 | Firewall (iptables) & VPN (IPsec) | Mod-5 | CLO-5 | ⬜ | ⬜ Lab 13 | ⬜ | 🔲 Chưa bắt đầu | iptables chains, OpenVPN |
| W15 | Backup/DR & Bảo vệ Đồ án | Mod-5 | CLO-5,6 | ⬜ | ⬜ Lab 14 | ⬜ | 🔲 Chưa bắt đầu | 3-2-1 Rule, AD Restore |

---

## 🧠 II. FLASHCARD & ACTIVE RECALL DATABASE (Spaced Repetition)

> 💡 **Notion**: Convert thành Database → Filter view: `Cần Ôn Hôm Nay? = ⚠️ Cần ôn`.
> **Notion Formula 2.0** cho cột `Cần Ôn?`:
> ```javascript
> if(empty(prop("Lần Ôn Gần Nhất")), true,
>    dateAdd(prop("Lần Ôn Gần Nhất"), prop("Chu Kỳ (Ngày)"), "days") <= now())
> ```

| Khái Niệm | Module | Tầng OSI | Bloom | Ưu Tiên 80/20 | Trạng Thái | Lần Ôn Gần Nhất | Chu Kỳ (Ngày) | Cần Ôn? | Lệnh CLI / Công Thức |
| :--- | :---: | :--- | :---: | :--- | :--- | :--- | :---: | :--- | :--- |
| **Mô hình FCAPS** (5 chữ cái) | Mod-1 | N/A (Framework) | C2 | 🔥 Trọng tâm | 🔴 Chưa thuộc | — | 1 | ⚠️ Cần ôn | Fault, Config, Accounting, Performance, Security |
| **HA / SLA / MTBF / MTTR** | Mod-1 | N/A (Metrics) | C2 | ⚡ Phụ | 🔴 Chưa thuộc | — | 1 | ⚠️ Cần ôn | SLA = Uptime %, MTBF = Mean Time Between Failures |
| **VLSM/CIDR — Chia subnet** | Mod-2 | Layer 3 | C3 | 🔥 Trọng tâm | 🔴 Chưa thuộc | — | 1 | ⚠️ Cần ôn | Hosts = 2^(32-prefix) - 2 |
| **VLAN 802.1Q & Trunking** | Mod-2 | Layer 2 | C3 | 🔥 Trọng tâm | 🔴 Chưa thuộc | — | 1 | ⚠️ Cần ôn | `switchport mode trunk`, Native VLAN |
| **Inter-VLAN: Router-on-a-Stick** | Mod-2 | Layer 3 | C3 | 🔥 Trọng tâm | 🔴 Chưa thuộc | — | 1 | ⚠️ Cần ôn | `encapsulation dot1Q <vlan-id>` |
| **Inter-VLAN: L3 Switch SVI** | Mod-2 | Layer 3 | C3 | ⚡ Phụ | 🔴 Chưa thuộc | — | 1 | ⚠️ Cần ôn | `interface vlan <id>`, `ip routing` |
| **DHCP DORA 4 bước** | Mod-2 | Layer 7 (UDP 67/68) | C3 | 🔥 Trọng tâm | 🔴 Chưa thuộc | — | 1 | ⚠️ Cần ôn | Discover → Offer → Request → Acknowledge |
| **DHCP Options (3, 6, 15, 66/67)** | Mod-2 | Layer 7 | C2 | ⚡ Phụ | 🔴 Chưa thuộc | — | 1 | ⚠️ Cần ôn | 3=Gateway, 6=DNS, 15=Domain, 66/67=PXE |
| **DHCP Relay Agent (ip helper-address)** | Mod-2 | Layer 3→7 | C3 | 🔥 Trọng tâm | 🔴 Chưa thuộc | — | 1 | ⚠️ Cần ôn | `ip helper-address <DHCP-Server-IP>` |
| **DHCP Split Scope 80/20** | Mod-2 | Layer 7 | C4 | ⚡ Phụ | 🔴 Chưa thuộc | — | 2 | ⚠️ Cần ôn | Server A: 80% scope, Server B: 20% scope |
| **DNS — Cây phân cấp (Root→TLD→SLD)** | Mod-2 | Layer 7 (UDP/TCP 53) | C2 | 🔥 Trọng tâm | 🔴 Chưa thuộc | — | 1 | ⚠️ Cần ôn | Root `.` → .vn → edu.vn → dut.edu.vn |
| **DNS — Recursive vs Iterative Query** | Mod-2 | Layer 7 | C2 | 🔥 Trọng tâm | 🔴 Chưa thuộc | — | 1 | ⚠️ Cần ôn | Recursive: DNS server trả lời hộ client |
| **DNS Record Types (A, AAAA, CNAME, MX, NS, PTR, SOA, SRV)** | Mod-2 | Layer 7 | C3 | 🔥 Trọng tâm | 🔴 Chưa thuộc | — | 1 | ⚠️ Cần ôn | A=IPv4, MX=Mail, PTR=Reverse, SRV=Service |
| **DNS Zone Transfer (Primary → Secondary)** | Mod-2 | Layer 7 | C3 | ⚡ Phụ | 🔴 Chưa thuộc | — | 2 | ⚠️ Cần ôn | AXFR (full) vs IXFR (incremental) |
| **AD DS — Forest / Tree / Domain / OU** | Mod-3 | Layer 7 (LDAP/Kerberos) | C2 | 🔥 Trọng tâm | 🔴 Chưa thuộc | — | 1 | ⚠️ Cần ôn | Forest > Tree > Domain > OU |
| **AD DS — 5 FSMO Roles** | Mod-3 | Layer 7 | C4 | 🔥 Trọng tâm | 🔴 Chưa thuộc | — | 1 | ⚠️ Cần ôn | Schema, Domain Naming, RID, PDC Emulator, Infrastructure |
| **Kerberos v5 (KDC, TGT, TGS)** | Mod-3 | Layer 7 (TCP 88) | C4 | 🔥 Trọng tâm | 🔴 Chưa thuộc | — | 1 | ⚠️ Cần ôn | AS-REQ → AS-REP(TGT) → TGS-REQ → TGS-REP |
| **GPO — Thứ tự LSDOU** | Mod-3 | Layer 7 | C3 | 🔥 Trọng tâm | 🔴 Chưa thuộc | — | 1 | ⚠️ Cần ôn | Local → Site → Domain → OU (gần nhất thắng) |
| **GPO — Block Inheritance vs Enforced** | Mod-3 | Layer 7 | C4 | ⚡ Phụ | 🔴 Chưa thuộc | — | 2 | ⚠️ Cần ôn | Enforced (No Override) > Block Inheritance |
| **LDAP — Base DN, CN, OU, DC** | Mod-3 | Layer 7 (TCP 389/636) | C2 | 🔥 Trọng tâm | 🔴 Chưa thuộc | — | 1 | ⚠️ Cần ôn | `cn=admin,dc=dut,dc=local` |
| **SAMBA — SMB/CIFS & sssd/realmd** | Mod-3 | Layer 7 (TCP 445) | C3 | ⚡ Phụ | 🔴 Chưa thuộc | — | 2 | ⚠️ Cần ôn | `realm join --verbose dut.local` |
| **Web Server — IIS vs Apache vs Nginx** | Mod-4 | Layer 7 (TCP 80/443) | C3 | 🔥 Trọng tâm | 🔴 Chưa thuộc | — | 1 | ⚠️ Cần ôn | IIS=Process Model, Nginx=Event-driven |
| **SSL/TLS — Chứng chỉ X.509 & CA** | Mod-4 | Layer 6/7 | C4 | 🔥 Trọng tâm | 🔴 Chưa thuộc | — | 1 | ⚠️ Cần ôn | openssl req → openssl x509, TLS 1.3 Handshake |
| **File Server — NTFS vs Share Permissions** | Mod-4 | Layer 7 (SMB) | C3 | 🔥 Trọng tâm | 🔴 Chưa thuộc | — | 1 | ⚠️ Cần ôn | Effective = Most Restrictive |
| **FSRM — Quota & File Screening** | Mod-4 | Layer 7 | C3 | ⚡ Phụ | 🔴 Chưa thuộc | — | 2 | ⚠️ Cần ôn | Hard Quota vs Soft Quota |
| **Mail — SMTP/POP3/IMAP Ports** | Mod-4 | Layer 7 | C2 | 🔥 Trọng tâm | 🔴 Chưa thuộc | — | 1 | ⚠️ Cần ôn | SMTP:25/587, POP3:110/995, IMAP:143/993 |
| **Mail — SPF, DKIM, DMARC** | Mod-4 | Layer 7 (DNS TXT) | C4 | 🔥 Trọng tâm | 🔴 Chưa thuộc | — | 1 | ⚠️ Cần ôn | SPF=IP whitelist, DKIM=Digital sign, DMARC=Policy |
| **SNMP — NMS/Agent, MIB, OID** | Mod-5 | Layer 7 (UDP 161/162) | C3 | 🔥 Trọng tâm | 🔴 Chưa thuộc | — | 1 | ⚠️ Cần ôn | SNMPv2c: Community String, SNMPv3: auth+priv |
| **Syslog — RFC 5424, 8 Severity Levels** | Mod-5 | Layer 7 (UDP 514) | C2 | 🔥 Trọng tâm | 🔴 Chưa thuộc | — | 1 | ⚠️ Cần ôn | 0:Emergency → 7:Debug |
| **iptables — Tables & Chains** | Mod-5 | Layer 3/4 | C3 | 🔥 Trọng tâm | 🔴 Chưa thuộc | — | 1 | ⚠️ Cần ôn | Filter(INPUT/OUTPUT/FORWARD), NAT(PRE/POST) |
| **IPsec — IKE Phase 1 & 2** | Mod-5 | Layer 3 | C4 | 🔥 Trọng tâm | 🔴 Chưa thuộc | — | 1 | ⚠️ Cần ôn | Phase1=ISAKMP SA, Phase2=IPsec SA, AH vs ESP |
| **VPN — Site-to-Site vs Remote Access** | Mod-5 | Layer 3 | C3 | 🔥 Trọng tâm | 🔴 Chưa thuộc | — | 1 | ⚠️ Cần ôn | S2S=2 routers, RA=Client dial-in |
| **Backup — Chiến lược 3-2-1** | Mod-5 | N/A (Strategy) | C2 | 🔥 Trọng tâm | 🔴 Chưa thuộc | — | 1 | ⚠️ Cần ôn | 3 bản sao, 2 loại media, 1 offsite |
| **Backup — Full vs Differential vs Incremental** | Mod-5 | N/A (Strategy) | C3 | 🔥 Trọng tâm | 🔴 Chưa thuộc | — | 1 | ⚠️ Cần ôn | Full=All, Diff=Since last Full, Inc=Since last Any |
| **RPO & RTO** | Mod-5 | N/A (Metrics) | C2 | 🔥 Trọng tâm | 🔴 Chưa thuộc | — | 1 | ⚠️ Cần ôn | RPO=Max data loss, RTO=Max downtime |

---

## 🔴 III. LAB ERROR JOURNAL — NHẬT KÝ LỖI SAI THỰC HÀNH

> 💡 **Notion**: Convert thành Database → Tạo **Gallery View** grouped by `Module` để xem visual.

| Mã Lỗi | Tuần / Lab | Thiết Bị | Tầng OSI | Nguyên Nhân Gốc Rễ (Root Cause) | Config Sai | Config Đúng | Mức Độ | Module |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :---: |
| ERR-001 | W2 / Lab02 | Cisco Switch 2960 | Layer 2 | Quên tạo VLAN trước khi gán port | `switchport access vlan 10` (VLAN 10 chưa tồn tại) | Chạy `vlan 10` + `name IT` trước, rồi mới gán port | 🚨 Nguy hiểm | Mod-2 |
| ERR-002 | W3 / Lab03 | Router 2911 | Layer 3 | Quên `no shutdown` trên cổng vật lý g0/0 | Chỉ config sub-interface g0/0.10 | `interface g0/0` → `no shutdown` trước | 🚨 Nguy hiểm | Mod-2 |
| ERR-003 | W4 / Lab04 | Router 2911 | Layer 7 | DHCP không cấp IP cho VLAN khác Router | Thiếu `ip helper-address` trên interface VLAN | Trên L3 interface/SVI: `ip helper-address <DHCP-IP>` | 🚨 Nguy hiểm | Mod-2 |
| ERR-004 | W5 / Lab05 | Windows DNS | Layer 7 | Client không resolve được domain nội bộ | Quên cấu hình DNS Server IP trên client/DHCP | Thêm DNS Option 6 vào DHCP Scope hoặc set thủ công | ⚠️ Thường gặp | Mod-2 |
| ERR-005 | W6 / Lab06 | Win Server DC | Layer 7 | Client không join domain | DNS client không trỏ về DC (DC = DNS Server) | `ipconfig /all` → Preferred DNS = IP của DC | 🚨 Nguy hiểm | Mod-3 |
| _Template_ | W_ / Lab_ | _Thiết bị_ | _Layer ?_ | _Phân tích nguyên nhân..._ | _Cấu hình đã thử (sai)_ | _Cấu hình chuẩn (đúng)_ | _⚠️/🚨_ | _Mod-?_ |

---

## 📖 IV. KNOWLEDGE BASE — FEYNMAN NOTES (TOGGLE BLOCKS)

> 💡 **Notion**: Các block `<details>` sẽ tự convert thành **Toggle Heading** khi import.

<details>
<summary><b>📦 Module 1: Cơ sở Quản trị Mạng & FCAPS</b></summary>

### 🔑 FCAPS — 5 Trụ Cột Quản Trị Mạng

**Ẩn dụ Feynman**: Hãy tưởng tượng bạn quản lý một toàn nhà 50 tầng. FCAPS giống như 5 phòng ban quản lý:
- **F**ault (Sự cố) = Đội bảo trì — phát hiện ống nước vỡ, đèn cháy
- **C**onfiguration (Cấu hình) = Đội kiến trúc — ai ở phòng nào, lắp thiết bị gì
- **A**ccounting (Kế toán) = Bảng ghi sử dụng — phòng nào dùng bao nhiêu điện/nước
- **P**erformance (Hiệu năng) = Đội đo đạc — thang máy chạy bao nhanh, nhiều người xếp hàng không
- **S**ecurity (An ninh) = Đội bảo vệ — ai được vào, kẻ lạ bị chặn

### 📐 Chỉ số Hạ tầng
- **SLA** = Cam kết uptime (99.99% = downtime chỉ 52 phút/năm)
- **MTBF** = Trung bình bao lâu thiết bị hỏng 1 lần
- **MTTR** = Trung bình sửa hỏng mất bao lâu

</details>

<details>
<summary><b>📦 Module 2: Hạ tầng Cốt lõi (DHCP, DNS, VLAN, Routing)</b></summary>

### 🔑 VLAN — Tại sao cần?
**Ẩn dụ**: Một tòa nhà văn phòng mà tất cả phòng ban đều dùng chung 1 hành lang → Bất kỳ ai nói lớn (broadcast) cả tòa nhà đều nghe.
VLAN = **Xây tường ngăn** giữa các phòng ban trên cùng 1 switch vật lý.

### 🔑 DHCP DORA — 4 Bước Bắt Tay
1. **D**iscover: Client broadcast "Ai là DHCP Server?"
2. **O**ffer: Server trả lời "Tôi đây, IP này cho bạn!"
3. **R**equest: Client "OK, tôi chọn IP này"
4. **A**ck: Server "Xác nhận! IP là của bạn trong X giờ"

> ⚠️ **Bẫy quan trọng**: Broadcast DHCP Discover KHÔNG thể vượt qua Router/L3 boundary → Cần `ip helper-address`!

### 🔑 DNS — Recursive vs Iterative
- **Recursive**: Client hỏi DNS Server → DNS Server tự đi hỏi khắp nơi rồi trả về kết quả cuối cùng (như gọi 113 nhờ tìm số điện thoại)
- **Iterative**: DNS Server chỉ nói "Tôi không biết, nhưng hỏi ông kia thử đi" → Client tự đi hỏi tiếp (như hỏi đường mà mỗi người chỉ bạn đi hướng tiếp theo)

</details>

<details>
<summary><b>📦 Module 3: Định danh & Thư mục (AD DS, GPO, LDAP)</b></summary>

### 🔑 Active Directory — Tại sao cần?
**Ẩn dụ**: Workgroup giống như mỗi phòng có 1 cuốn sổ danh bạ riêng → 100 phòng = 100 sổ, thêm 1 nhân viên phải ghi vào cả 100 cuốn.
AD DS = **1 cuốn sổ danh bạ trung tâm** (Domain Controller) → Thêm 1 lần, tất cả phòng đều biết.

### 🔑 Kerberos — Quy Trình Xác Thực
1. Client gửi AS-REQ → KDC (Key Distribution Center)
2. KDC trả AS-REP chứa **TGT** (Ticket Granting Ticket) — như vé vào công viên
3. Client dùng TGT gửi TGS-REQ → KDC xin vé cho dịch vụ cụ thể (File Server, Web,...)
4. KDC trả TGS-REP chứa **Service Ticket** — như vé cho từng trò chơi riêng

### 🔑 GPO — LSDOU
Thứ tự áp dụng: **L**ocal → **S**ite → **D**omain → **OU**
Chính sách ở OU **gần nhất** sẽ **ghi đè** chính sách ở cấp cao hơn (trừ khi Enforced).

</details>

<details>
<summary><b>📦 Module 4: Dịch vụ Ứng dụng & Lưu trữ (Web, File, Mail)</b></summary>

### 🔑 NTFS vs Share Permissions
- **NTFS**: Áp dụng cả khi truy cập local lẫn qua mạng
- **Share**: Chỉ áp dụng khi truy cập qua mạng
- **Effective Permission** = Quyền hạn chế nhất giữa NTFS ∩ Share

**Ví dụ**: User A có NTFS Full Control + Share Read → Qua mạng chỉ được Read.

### 🔑 Mail Server — Luồng Email
```
Người gửi → MUA (Outlook) → MTA (Postfix/SMTP:587) → DNS(MX lookup)
→ MTA đích → MDA (Dovecot) → Mailbox → MUA người nhận (IMAP:993)
```

### 🔑 SPF / DKIM / DMARC — Bộ 3 Chống Giả Mạo
- **SPF**: "Chỉ các IP này được gửi email thay mặt domain tôi"
- **DKIM**: "Email này có chữ ký số xác thực từ domain tôi"
- **DMARC**: "Nếu SPF/DKIM fail → reject/quarantine/none"

</details>

<details>
<summary><b>📦 Module 5: Giám sát & An ninh (SNMP, Firewall, VPN, Backup)</b></summary>

### 🔑 SNMP — 3 Phiên Bản
| Tiêu chí | v1 | v2c | v3 |
|:---------|:---|:----|:---|
| Bảo mật | Community String (plaintext) | Community String (plaintext) | USM (auth + priv) |
| Mã hóa | ❌ | ❌ | ✅ AES/DES |
| Sử dụng | Cũ, không dùng | Phổ biến nhất | Khuyến nghị |

### 🔑 iptables — Luồng Xử Lý
```
Incoming → PREROUTING(NAT) → Routing Decision
  ├── Đến máy local → INPUT(Filter) → Application
  └── Forward sang máy khác → FORWARD(Filter) → POSTROUTING(NAT) → Out

Application → OUTPUT(Filter) → POSTROUTING(NAT) → Out
```

### 🔑 IPsec VPN — 2 Phase
- **Phase 1 (ISAKMP SA)**: Hai bên thỏa thuận thuật toán mã hóa, xác thực nhau → Tạo đường hầm quản lý
- **Phase 2 (IPsec SA)**: Thỏa thuận cách bảo vệ dữ liệu thực tế → Tạo đường hầm dữ liệu
- **AH** = Chỉ xác thực (Authentication Header), không mã hóa
- **ESP** = Vừa xác thực vừa mã hóa (Encapsulating Security Payload) → **Dùng ESP!**

### 🔑 Backup 3-2-1
- **3** bản sao dữ liệu (1 gốc + 2 backup)
- **2** loại phương tiện lưu trữ khác nhau (ổ cứng + tape/cloud)
- **1** bản ở nơi khác (offsite/cloud)

</details>

---

## 🧪 V. LAB CLI QUICK REFERENCE

<details>
<summary><b>💻 Template: Cisco Router — Inter-VLAN + DHCP</b></summary>

```cisco
! === BƯỚC 1: BẬT CỔNG VẬT LÝ ===
Router> enable
Router# configure terminal
Router(config)# interface GigabitEthernet0/0
Router(config-if)# no ip address
Router(config-if)# no shutdown
Router(config-if)# exit

! === BƯỚC 2: SUB-INTERFACE CHO TỪNG VLAN ===
Router(config)# interface g0/0.10
Router(config-subif)# encapsulation dot1Q 10
Router(config-subif)# ip address 192.168.10.1 255.255.255.0
Router(config-subif)# exit

Router(config)# interface g0/0.20
Router(config-subif)# encapsulation dot1Q 20
Router(config-subif)# ip address 192.168.20.1 255.255.255.0
Router(config-subif)# exit

! === BƯỚC 3: DHCP SERVER ===
Router(config)# ip dhcp excluded-address 192.168.20.1 192.168.20.10
Router(config)# ip dhcp pool POOL_VLAN20
Router(dhcp-config)# network 192.168.20.0 255.255.255.0
Router(dhcp-config)# default-router 192.168.20.1
Router(dhcp-config)# dns-server 8.8.8.8
Router(dhcp-config)# lease 0 8 0
Router(dhcp-config)# exit
```

</details>

<details>
<summary><b>💻 Template: Cisco Switch — VLAN & Trunk</b></summary>

```cisco
Switch> enable
Switch# configure terminal

! === TẠO VLAN ===
Switch(config)# vlan 10
Switch(config-vlan)# name IT_Dept
Switch(config)# vlan 20
Switch(config-vlan)# name Sales_Dept
Switch(config)# exit

! === CỔNG TRUNK ===
Switch(config)# interface g0/1
Switch(config-if)# switchport mode trunk
Switch(config-if)# exit

! === CỔNG ACCESS ===
Switch(config)# interface range fa0/1-10
Switch(config-if-range)# switchport mode access
Switch(config-if-range)# switchport access vlan 10
Switch(config-if-range)# spanning-tree portfast
Switch(config-if-range)# exit
```

</details>

<details>
<summary><b>💻 Template: Windows Server — AD DS Promotion</b></summary>

```powershell
# === CÀI ĐẶT ROLE AD DS ===
Install-WindowsFeature -Name AD-Domain-Services -IncludeManagementTools

# === NÂNG CẤP THÀNH DOMAIN CONTROLLER ===
Install-ADDSForest `
    -DomainName "dut.local" `
    -DomainNetbiosName "DUT" `
    -ForestMode "WinThreshold" `
    -DomainMode "WinThreshold" `
    -InstallDns:$true `
    -SafeModeAdministratorPassword (ConvertTo-SecureString "P@ssw0rd!" -AsPlainText -Force) `
    -Force:$true

# === TẠO OU CẤU TRÚC ===
New-ADOrganizationalUnit -Name "DUT_Company" -Path "DC=dut,DC=local"
New-ADOrganizationalUnit -Name "IT" -Path "OU=DUT_Company,DC=dut,DC=local"
New-ADOrganizationalUnit -Name "HR" -Path "OU=DUT_Company,DC=dut,DC=local"
New-ADOrganizationalUnit -Name "Sales" -Path "OU=DUT_Company,DC=dut,DC=local"

# === TẠO USER MẪU ===
New-ADUser -Name "Nguyen Van A" -SamAccountName "nguyenvana" `
    -UserPrincipalName "nguyenvana@dut.local" `
    -Path "OU=IT,OU=DUT_Company,DC=dut,DC=local" `
    -AccountPassword (ConvertTo-SecureString "User@123" -AsPlainText -Force) `
    -Enabled $true
```

</details>

<details>
<summary><b>💻 Template: Linux — DHCP/DNS/LDAP</b></summary>

```bash
# === CÀI ĐẶT ISC DHCP SERVER (Ubuntu) ===
sudo apt update && sudo apt install -y isc-dhcp-server
sudo nano /etc/dhcp/dhcpd.conf
# subnet 192.168.20.0 netmask 255.255.255.0 {
#   range 192.168.20.50 192.168.20.200;
#   option routers 192.168.20.1;
#   option domain-name-servers 8.8.8.8, 1.1.1.1;
#   default-lease-time 7200;  # 2 giờ
# }
sudo systemctl restart isc-dhcp-server
sudo systemctl enable isc-dhcp-server

# === CÀI ĐẶT BIND9 DNS SERVER ===
sudo apt install -y bind9 bind9utils
sudo nano /etc/bind/named.conf.local
# zone "dut.edu.vn" { type master; file "/etc/bind/db.dut.edu.vn"; };
sudo systemctl restart bind9

# === JOIN LINUX VÀO AD DOMAIN ===
sudo apt install -y realmd sssd adcli krb5-user
sudo realm discover dut.local
sudo realm join --verbose dut.local -U Administrator
```

</details>

<details>
<summary><b>💻 Lệnh Kiểm Tra & Xác Thực (Verification Commands)</b></summary>

```bash
# === NETWORK BASIC ===
ping 192.168.10.1                     # Kiểm tra kết nối L3
traceroute 192.168.20.1               # Truy vết đường đi
nslookup web.dut.edu.vn               # Phân giải DNS (Windows/Linux)
dig web.dut.edu.vn @192.168.10.1      # Phân giải DNS (Linux chi tiết)

# === CISCO SHOW COMMANDS ===
show ip interface brief                # Tổng quan interface
show vlan brief                        # Danh sách VLAN
show ip route                          # Bảng định tuyến
show ip dhcp binding                   # IP đã cấp
show ip dhcp pool                      # Thống kê DHCP pool

# === WINDOWS ===
ipconfig /all                          # Xem cấu hình mạng
gpupdate /force                        # Cập nhật GPO ngay lập tức
gpresult /r                            # Xem GPO đang áp dụng
Get-ADUser -Filter * | Select Name     # Liệt kê user AD
Test-NetConnection -Port 443 web.dut.edu.vn  # Test kết nối TCP

# === LINUX ===
systemctl status <service>             # Trạng thái dịch vụ
journalctl -u <service> -f            # Xem log realtime
ss -tulnp                             # Danh sách port đang listen
tcpdump -i eth0 port 53               # Bắt gói DNS
```

</details>

---

## 🎯 VI. EXAM PREP ZONE

### ✅ Checklist Giữa Kỳ (Tuần 9 — Live Lab 90 phút)

- [ ] Chia subnet VLSM cho 3+ phòng ban
- [ ] Cấu hình VLAN + Trunk trên Switch
- [ ] Cấu hình Inter-VLAN Routing (Router-on-a-Stick)
- [ ] Cấu hình DHCP Server + DHCP Relay Agent
- [ ] Dựng DNS Server (Forward + Reverse Zone)
- [ ] Nâng cấp Windows Server → Domain Controller
- [ ] Join Client vào Domain
- [ ] Tạo OU + User + Group
- [ ] Áp dụng tối thiểu 2 GPO (Password Policy + Drive Map)
- [ ] Kiểm tra bằng: `ping`, `nslookup`, `gpresult /r`

### ✅ Checklist Đồ Án Cuối Kỳ (Tuần 15 — Enterprise Multi-Site)

- [ ] Thiết kế topo mạng 2 chi nhánh (Đà Nẵng + TP.HCM/Hà Nội)
- [ ] VLAN theo phòng ban + Trunking 802.1Q
- [ ] OSPF kết nối WAN giữa 2 chi nhánh
- [ ] DHCP Relay cho tất cả VLAN
- [ ] Primary DC + Additional DC đồng bộ
- [ ] Tối thiểu 5 GPO thiết thực
- [ ] Web Server HTTPS (CA nội bộ)
- [ ] File Server + NTFS/Share + Quota + ABE
- [ ] Mail Server gửi nhận an toàn
- [ ] Tường lửa iptables/Windows Firewall
- [ ] Site-to-Site IPsec VPN
- [ ] Zabbix/Syslog giám sát 24/7
- [ ] Kế hoạch Backup 3-2-1 tự động

---

## 🗓️ VII. DAILY SOP — QUY TRÌNH HỌC HÀNG NGÀY

- [ ] 🌅 **Sáng (15 phút)**: Mở DB Flashcard → Lọc `Cần Ôn? = ⚠️` → Tự recall trước khi xem đáp án → Cập nhật `Lần Ôn` + điều chỉnh `Chu Kỳ`
- [ ] 🌤️ **Chiều/Tối (60 phút)**: Mở Packet Tracer/VMware → Thực hành Lab theo tuần hiện tại → Gõ CLI từng dòng, không copy-paste
- [ ] 🌃 **Đêm (15 phút)**: Ghi mọi lỗi gặp vào DB Error Journal → Phân tích Root Cause → Viết 1 câu "Nguyên tắc khắc cốt ghi tâm"

---

### ❌ TEMPLATE GHI CHÉP LỖI SAI

```
### ❌ [SỰ CỐ LAB] - [Tên Dịch Vụ]
- ❓ Hiện tượng: [Mô tả triệu chứng cụ thể]
- 🔴 Config Sai: [Cấu hình đã thử]
- 🟢 Config Đúng: [Cấu hình chuẩn]
- 🔍 ROOT CAUSE:
  * Tầng OSI: [Layer ?]
  * Tại sao sai: [Giải thích bản chất]
  * Lệnh phát hiện nhanh: [show/debug/tcpdump...]
- 💡 Quy tắc ghi nhớ: [1 câu ngắn gọn]
```

---

> 🏁 **Mỗi tuần ôn xong, quay lại Mục I để tick ✅ tiến độ. Không để tuần nào trống!**
