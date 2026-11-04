#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DUT Day 6 Lab - Automated Technical Compliance Auditor for 'ISP service.pkt'
Decodes Packet Tracer PKT and verifies all 8 lab requirements across all devices.
"""

import sys
import os
import xml.etree.ElementTree as ET

# Ensure UTF-8 output on Windows
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8', errors='backslashreplace')

TOOLKIT_DIR = r"d:\NEXUS\02_Academic_DUT\Courses\03_Company_Network_Management_NMA\05_Troubleshooting_and_Toolkits"
sys.path.append(os.path.join(TOOLKIT_DIR, "Unpacket"))
from Decipher.pt_crypto import decrypt_pkt

PKT_PATH = r"d:\NEXUS\02_Academic_DUT\Courses\03_Company_Network_Management_NMA\03_Engineering_Labs_and_Code\Day6\ISP service.pkt"

def audit_pkt():
    print("===============================================================")
    print("      DUT DAY 6 LAB AUTOMATED TECHNICAL AUDIT FOR .PKT FILE    ")
    print(f"File: {PKT_PATH}")
    print("===============================================================")

    if not os.path.exists(PKT_PATH):
        print(f"ERROR: File not found at {PKT_PATH}")
        return False

    with open(PKT_PATH, "rb") as f:
        xml_data = decrypt_pkt(f.read())

    root = ET.fromstring(xml_data)

    def get_lines(dev_name):
        for d in root.findall('.//DEVICE'):
            name = d.findtext('.//NAME')
            if name == dev_name:
                rc = d.find('.//RUNNINGCONFIG')
                if rc is not None:
                    return [l.text for l in rc.findall('LINE') if l.text]
        return []

    tests = []

    # 1. WestGate
    wg_str = ' '.join(get_lines('WestGate'))
    tests.append(('WestGate', 'Hostname WestGate', 'hostname WestGate' in wg_str))
    tests.append(('WestGate', 'Gig0/0 External IP (10.2.200.200/16)', '10.2.200.200 255.255.0.0' in wg_str))
    tests.append(('WestGate', 'Serial0/3/0 WAN (172.21.255.1/30 DCE 64000)', '172.21.255.1 255.255.255.252' in wg_str and 'clock rate 64000' in wg_str))
    tests.append(('WestGate', 'NAT Inside & Outside interfaces', 'ip nat inside' in wg_str and 'ip nat outside' in wg_str))
    tests.append(('WestGate', 'NAT Pool WEST-POOL (10.2.200.201~.203)', 'ip nat pool WEST-POOL 10.2.200.201 10.2.200.203' in wg_str))
    tests.append(('WestGate', 'NAT Overload enabled', 'ip nat inside source list 1 pool WEST-POOL overload' in wg_str))
    tests.append(('WestGate', 'ip default-network 10.0.0.0 (Candidate Default)', 'ip default-network 10.0.0.0' in wg_str))
    tests.append(('WestGate', 'EIGRP 66 network 10.0.0.0 advertised', 'network 10.0.0.0' in wg_str and 'router eigrp 66' in wg_str))

    # 2. West
    w_str = ' '.join(get_lines('West'))
    tests.append(('West', 'Hostname West', 'hostname West' in w_str))
    tests.append(('West', 'Loopback2 (172.21.32.1/19 LAN2)', '172.21.32.1 255.255.224.0' in w_str))
    tests.append(('West', 'ACL 101 Inbound on LAN2', 'ip access-group 101 in' in w_str))
    tests.append(('West', 'Sub-interface Gig0/0.2 (172.22.32.1/20 dot1Q 2)', '172.22.32.1 255.255.240.0' in w_str and 'dot1Q 2' in w_str))
    tests.append(('West', 'Sub-interface Gig0/0.3 (172.22.48.1/20 dot1Q 3)', '172.22.48.1 255.255.240.0' in w_str and 'dot1Q 3' in w_str))
    tests.append(('West', 'Serial0/3/0 (172.21.255.2/30)', '172.21.255.2 255.255.255.252' in w_str))
    tests.append(('West', 'EIGRP AS 66 & AS 99 Redistribution', 'redistribute eigrp 99' in w_str and 'redistribute eigrp 66' in w_str))
    tests.append(('West', 'Default Route redistributed to EIGRP 99', 'redistribute static metric' in w_str))
    tests.append(('West', 'ACL 101: Permit HTTP (www)', 'permit tcp 172.21.32.0 0.0.31.255 172.22.48.0 0.0.15.255 eq www' in w_str))
    tests.append(('West', 'ACL 101: Permit TELNET (telnet)', 'permit tcp 172.21.32.0 0.0.31.255 172.22.48.0 0.0.15.255 eq telnet' in w_str))
    tests.append(('West', 'ACL 101: Deny Ping ICMP Echo', 'deny icmp 172.21.32.0 0.0.31.255 172.22.48.0 0.0.15.255 echo' in w_str))
    tests.append(('West', 'ACL 101: Permit other traffics', 'permit ip any any' in w_str))

    # 3. Core
    c_str = ' '.join(get_lines('Core'))
    tests.append(('Core', 'Hostname Core', 'hostname Core' in c_str))
    tests.append(('Core', 'Loopback3 (172.22.0.1/19 LAN3)', '172.22.0.1 255.255.224.0' in c_str))
    tests.append(('Core', 'Sub-interface Gig0/0.2 (172.22.32.2/20)', '172.22.32.2 255.255.240.0' in c_str and 'dot1Q 2' in c_str))
    tests.append(('Core', 'Sub-interface Gig0/0.3 (172.22.48.2/20)', '172.22.48.2 255.255.240.0' in c_str and 'dot1Q 3' in c_str))
    tests.append(('Core', 'EIGRP AS 99 Process & Networks', 'router eigrp 99' in c_str and 'network 172.22.0.0' in c_str))

    # 4. East
    e_str = ' '.join(get_lines('East'))
    tests.append(('East', 'Hostname East', 'hostname East' in e_str))
    tests.append(('East', 'Loopback4 (172.23.0.1/19 LAN4)', '172.23.0.1 255.255.224.0' in e_str))
    tests.append(('East', 'Loopback5 (172.23.32.1/19 LAN5)', '172.23.32.1 255.255.224.0' in e_str))
    tests.append(('East', 'Sub-interface Gig0/0.2 (172.22.32.3/20)', '172.22.32.3 255.255.240.0' in e_str and 'dot1Q 2' in e_str))
    tests.append(('East', 'Sub-interface Gig0/0.3 (172.22.48.3/20)', '172.22.48.3 255.255.240.0' in e_str and 'dot1Q 3' in e_str))
    tests.append(('East', 'Serial0/3/0 (172.23.255.1/30)', '172.23.255.1 255.255.255.252' in e_str))
    tests.append(('East', 'OSPF Area 0 Configuration', 'router ospf 1' in e_str and 'area 0' in e_str))
    tests.append(('East', 'Redistribute EIGRP 99 into OSPF', 'redistribute eigrp 99 subnets' in e_str))
    tests.append(('East', 'Redistribute OSPF into EIGRP 99 (Matching West metric)', 'redistribute ospf 1 metric 10000 100 255 1 1500' in e_str))

    # 5. EastGate
    eg_str = ' '.join(get_lines('EastGate'))
    tests.append(('EastGate', 'Hostname EastGate', 'hostname EastGate' in eg_str))
    tests.append(('EastGate', 'Loopback6 (172.23.64.1/19 LAN6)', '172.23.64.1 255.255.224.0' in eg_str))
    tests.append(('EastGate', 'Gig0/0 External IP (192.168.0.10/24)', '192.168.0.10 255.255.255.0' in eg_str))
    tests.append(('EastGate', 'Serial0/3/0 (172.23.255.2/30 DCE 64000)', '172.23.255.2 255.255.255.252' in eg_str and 'clock rate 64000' in eg_str))
    tests.append(('EastGate', 'NAT Inside & Outside interfaces', 'ip nat inside' in eg_str and 'ip nat outside' in eg_str))
    tests.append(('EastGate', 'NAT Pool EAST-POOL (192.168.0.11~.15)', 'ip nat pool EAST-POOL 192.168.0.11 192.168.0.15' in eg_str))
    tests.append(('EastGate', 'Static Default Route ra ISP Đông', 'ip route 0.0.0.0 0.0.0.0 192.168.0.1' in eg_str))
    tests.append(('EastGate', 'default-information originate (Yêu cầu 5)', 'default-information originate' in eg_str))

    # 6. Switches
    sw_s_str = ' '.join(get_lines('Server'))
    tests.append(('Server', 'VTP Domain & Password (business / goodluck)', 'vtp domain business' in sw_s_str and 'vtp password goodluck' in sw_s_str))
    tests.append(('Server', 'VTP Mode Server & VLAN 2/3 declared', 'vtp mode server' in sw_s_str and 'vlan 2' in sw_s_str and 'vlan 3' in sw_s_str))
    tests.append(('Server', 'Trunking on connected ports', 'switchport mode trunk' in sw_s_str))

    sw_c_str = ' '.join(get_lines('Client'))
    tests.append(('Client', 'VTP Domain & Password (business / goodluck)', 'vtp domain business' in sw_c_str and 'vtp password goodluck' in sw_c_str))
    tests.append(('Client', 'VTP Mode Client', 'vtp mode client' in sw_c_str))
    tests.append(('Client', 'Trunking on connected ports', 'switchport mode trunk' in sw_c_str))

    # 7. ISPs
    isp_w_str = ' '.join(get_lines('ISP WEST'))
    tests.append(('ISP WEST', 'Gateway IP 10.2.0.1/16', '10.2.0.1 255.255.0.0' in isp_w_str))
    tests.append(('ISP WEST', 'Loopback0 10.10.10.10/32', '10.10.10.10 255.255.255.255' in isp_w_str))

    isp_e_str = ' '.join(get_lines('ISP EAST'))
    tests.append(('ISP EAST', 'Gateway IP 192.168.0.1/24', '192.168.0.1 255.255.255.0' in isp_e_str))
    tests.append(('ISP EAST', 'Loopback0 Google DNS 8.8.8.8/32', '8.8.8.8 255.255.255.255' in isp_e_str))

    passed = 0
    failed = 0
    for dev, desc, ok in tests:
        status = "[ PASS ]" if ok else "[ FAIL ]"
        if ok:
            passed += 1
        else:
            failed += 1
        print(f"{status} {dev:<10} | {desc}")

    total = len(tests)
    score = (passed / total) * 100
    print("===============================================================")
    print(f"AUDIT SUMMARY: {passed}/{total} Passed ({score:.1f}%) | {failed} Failed")
    print("===============================================================")

    return failed == 0

if __name__ == "__main__":
    success = audit_pkt()
    sys.exit(0 if success else 1)

