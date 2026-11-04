#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DUT Day 6 Lab - EIGRP / OSPF / VLAN / NAT Automated Configuration Auditor
Verifies all technical requirements across the 9 device configuration files.
"""

import os
import re
import sys

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8', errors='backslashreplace')

CONFIG_DIR = r"d:\NEXUS\02_Academic_DUT\Courses\03_Company_Network_Management_NMA\03_Engineering_Labs_and_Code\Day6\device_configs"

def read_cfg(filename):
    path = os.path.join(CONFIG_DIR, filename)
    if not os.path.exists(path):
        return ""
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()

def audit():
    print("===============================================================")
    print("       DUT DAY 6 LAB AUTOMATED CONFIGURATION AUDIT REPORT      ")
    print("===============================================================")

    tests = []

    # 1. Switch Server
    sw_s = read_cfg("01_Server_Switch.cfg")
    tests.append(("Server", "VTP Domain 'business'", "vtp domain business" in sw_s))
    tests.append(("Server", "VTP Password 'goodluck'", "vtp password goodluck" in sw_s))
    tests.append(("Server", "VTP Mode Server", "vtp mode server" in sw_s))
    tests.append(("Server", "VLAN 2 (name west)", "vlan 2" in sw_s and "name west" in sw_s))
    tests.append(("Server", "VLAN 3 (name east)", "vlan 3" in sw_s and "name east" in sw_s))
    tests.append(("Server", "Trunking on connected ports", "switchport mode trunk" in sw_s))
    tests.append(("Server", "Access VLAN 2 on Fa0/10", "switchport access vlan 2" in sw_s))

    # 2. Switch Client
    sw_c = read_cfg("02_Client_Switch.cfg")
    tests.append(("Client", "VTP Domain 'business'", "vtp domain business" in sw_c))
    tests.append(("Client", "VTP Password 'goodluck'", "vtp password goodluck" in sw_c))
    tests.append(("Client", "VTP Mode Client", "vtp mode client" in sw_c))
    tests.append(("Client", "Trunking on connected ports", "switchport mode trunk" in sw_c))
    tests.append(("Client", "Access VLAN 3 on Fa0/10", "switchport access vlan 3" in sw_c))

    # 3. Router Core
    core = read_cfg("03_Core_Router.cfg")
    tests.append(("Core", "LAN3 Subnet (172.22.0.1/19)", "172.22.0.1 255.255.224.0" in core))
    tests.append(("Core", "Sub-interface Gig0/0.2 (172.22.32.2/20)", "172.22.32.2 255.255.240.0" in core and "dot1Q 2" in core))
    tests.append(("Core", "Sub-interface Gig0/0.3 (172.22.48.2/20)", "172.22.48.2 255.255.240.0" in core and "dot1Q 3" in core))
    tests.append(("Core", "EIGRP AS 99 Process", "router eigrp 99" in core and "no auto-summary" in core))
    tests.append(("Core", "EIGRP 99 Network 172.22.0.0", "network 172.22.0.0" in core))
    tests.append(("Core", "EIGRP 99 Network VLAN 2 & 3", "network 172.22.32.0 0.0.15.255" in core and "network 172.22.48.0 0.0.15.255" in core))

    # 4. Router West
    west = read_cfg("04_West_Router.cfg")
    tests.append(("West", "LAN2 Subnet (172.21.32.1/19)", "172.21.32.1 255.255.224.0" in west))
    tests.append(("West", "ACL 101 Inbound on LAN2", "ip access-group 101 in" in west))
    tests.append(("West", "Sub-interfaces Gig0/0.2 & Gig0/0.3", "172.22.32.1 255.255.240.0" in west and "172.22.48.1 255.255.240.0" in west))
    tests.append(("West", "WAN Serial Se0/3/0 (172.21.255.2/30)", "172.21.255.2 255.255.255.252" in west))
    tests.append(("West", "EIGRP AS 66 & AS 99 Redistribution", "router eigrp 66" in west and "router eigrp 99" in west))
    tests.append(("West", "Redistribute Default Route into EIGRP 99", "redistribute static metric" in west))
    tests.append(("West", "ACL 101: Permit HTTP (www)", "permit tcp 172.21.32.0 0.0.31.255 172.22.48.0 0.0.15.255 eq www" in west))
    tests.append(("West", "ACL 101: Permit TELNET (telnet)", "permit tcp 172.21.32.0 0.0.31.255 172.22.48.0 0.0.15.255 eq telnet" in west))
    tests.append(("West", "ACL 101: Deny Ping (icmp echo)", "deny icmp 172.21.32.0 0.0.31.255 172.22.48.0 0.0.15.255 echo" in west))
    tests.append(("West", "ACL 101: Permit other traffics", "permit ip any any" in west))

    # 5. Router East
    east = read_cfg("05_East_Router.cfg")
    tests.append(("East", "LAN4 Subnet (172.23.0.1/19)", "172.23.0.1 255.255.224.0" in east))
    tests.append(("East", "LAN5 Subnet (172.23.32.1/19)", "172.23.32.1 255.255.224.0" in east))
    tests.append(("East", "Sub-interfaces Gig0/0.2 & Gig0/0.3", "172.22.32.3 255.255.240.0" in east and "172.22.48.3 255.255.240.0" in east))
    tests.append(("East", "WAN Serial Se0/3/0 (172.23.255.1/30)", "172.23.255.1 255.255.255.252" in east))
    tests.append(("East", "OSPF Area 0 Configuration", "router ospf 1" in east and "area 0" in east))
    tests.append(("East", "Redistribute EIGRP 99 into OSPF", "redistribute eigrp 99 subnets" in east))
    tests.append(("East", "Redistribute OSPF into EIGRP 99", "redistribute ospf 1 metric" in east))

    # 6. Router WestGate
    wg = read_cfg("06_WestGate_Router.cfg")
    tests.append(("WestGate", "LAN1 Subnet (172.21.0.1/19)", "172.21.0.1 255.255.224.0" in wg))
    tests.append(("WestGate", "WAN Serial Se0/3/0 (172.21.255.1/30 DCE 64000)", "172.21.255.1 255.255.255.252" in wg and "clock rate 64000" in wg))
    tests.append(("WestGate", "Gig0/0 External IP (10.2.200.200/16)", "10.2.200.200 255.255.0.0" in wg))
    tests.append(("WestGate", "NAT Inside & Outside Interfaces", "ip nat inside" in wg and "ip nat outside" in wg))
    tests.append(("WestGate", "NAT Pool WEST-POOL (10.2.200.201~.203)", "ip nat pool WEST-POOL 10.2.200.201 10.2.200.203" in wg))
    tests.append(("WestGate", "NAT Overload", "ip nat inside source list 1 pool WEST-POOL overload" in wg))
    tests.append(("WestGate", "ip default-network 10.0.0.0 (Thầy gợi ý)", "ip default-network 10.0.0.0" in wg))
    tests.append(("WestGate", "EIGRP 66 Network 10.0.0.0 (Thầy gợi ý)", "network 10.0.0.0" in wg and "router eigrp 66" in wg))

    # 7. Router EastGate
    eg = read_cfg("07_EastGate_Router.cfg")
    tests.append(("EastGate", "LAN6 Subnet (172.23.64.1/19)", "172.23.64.1 255.255.224.0" in eg))
    tests.append(("EastGate", "WAN Serial Se0/3/0 (172.23.255.2/30 DCE 64000)", "172.23.255.2 255.255.255.252" in eg and "clock rate 64000" in eg))
    tests.append(("EastGate", "Gig0/0 External IP (192.168.0.10/24)", "192.168.0.10 255.255.255.0" in eg))
    tests.append(("EastGate", "NAT Inside & Outside Interfaces", "ip nat inside" in eg and "ip nat outside" in eg))
    tests.append(("EastGate", "NAT Pool EAST-POOL (192.168.0.11~.15)", "ip nat pool EAST-POOL 192.168.0.11 192.168.0.15" in eg))
    tests.append(("EastGate", "NAT Overload", "ip nat inside source list 1 pool EAST-POOL overload" in eg))
    tests.append(("EastGate", "Static Default Route ra ISP Đông", "ip route 0.0.0.0 0.0.0.0 192.168.0.1" in eg))
    tests.append(("EastGate", "OSPF Area 0 Configuration", "router ospf 1" in eg and "area 0" in eg))
    tests.append(("EastGate", "default-information originate (Yêu cầu 5)", "default-information originate" in eg))

    # 8. Router ISP-West
    isp_w = read_cfg("08_ISP_West_Router.cfg")
    tests.append(("ISP-West", "Fa0/0 Gateway (10.2.0.1/16)", "10.2.0.1 255.255.0.0" in isp_w))
    tests.append(("ISP-West", "Loopback0 Internet Server (10.10.10.10/32)", "10.10.10.10 255.255.255.255" in isp_w))

    # 9. Router ISP-East
    isp_e = read_cfg("09_ISP_East_Router.cfg")
    tests.append(("ISP-East", "Fa0/0 Gateway (192.168.0.1/24)", "192.168.0.1 255.255.255.0" in isp_e))
    tests.append(("ISP-East", "Loopback0 Google DNS (8.8.8.8/32)", "8.8.8.8 255.255.255.255" in isp_e))

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
    success = audit()
    exit(0 if success else 1)
