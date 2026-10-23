#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DUT Day 5 Lab - Multi Area OSPF & EIGRP Automated Compliance Auditor
Verifies all 41 technical requirements against Cisco Packet Tracer XML/PKT source.
"""

import xml.etree.ElementTree as ET
import sys
import os

def audit_lab(xml_path):
    if not os.path.exists(xml_path):
        print(f"Error: {xml_path} not found.")
        return False

    tree = ET.parse(xml_path)
    root = tree.getroot()

    def get_dev_lines(dev_name):
        for d in root.findall('.//DEVICE'):
            name = d.findtext('.//NAME')
            if name == dev_name:
                return [el.text for el in d.iter() if el.tag == 'LINE' and el.text]
        return []

    print("===============================================================")
    print("        DUT DAY 5 LAB AUTOMATED TECHNICAL AUDIT REPORT         ")
    print("===============================================================")

    checklist = []

    # 1. Earth
    e_str = ' '.join(get_dev_lines('Earth'))
    checklist.append(('Earth', 'Loopback 1 (172.23.0.1/19)', '172.23.0.1 255.255.224.0' in e_str))
    checklist.append(('Earth', 'Gig0/0.2 (172.23.128.1/20 dot1Q 2)', '172.23.128.1 255.255.240.0' in e_str and 'dot1Q 2' in e_str))
    checklist.append(('Earth', 'Gig0/0.3 (172.23.144.1/20 dot1Q 3)', '172.23.144.1 255.255.240.0' in e_str and 'dot1Q 3' in e_str))
    checklist.append(('Earth', 'OSPF Cost 10 on Gig0/0.3 (ECMP Elimination)', 'ip ospf cost 10' in e_str))
    checklist.append(('Earth', 'OSPF Area 0 configured', 'network 172.23.0.0 0.0.31.255 area 0' in e_str))
    checklist.append(('Earth', 'OSPF MD5 Authentication (cat)', 'message-digest-key 1 md5 cat' in e_str))

    # 2. Mars
    m_str = ' '.join(get_dev_lines('Mars'))
    checklist.append(('Mars', 'Loopback 2 (172.23.32.1/19)', '172.23.32.1 255.255.224.0' in m_str))
    checklist.append(('Mars', 'Gig0/0.2 & Gig0/0.3 Sub-interfaces', '172.23.128.2' in m_str and '172.23.144.2' in m_str))
    checklist.append(('Mars', 'Serial0/3/0 (172.23.255.1/30 DCE 64000)', '172.23.255.1 255.255.255.252' in m_str and 'clock rate 64000' in m_str))
    checklist.append(('Mars', 'OSPF ABR (Area 0 and Area 2)', 'area 0' in m_str and 'area 2' in m_str))
    checklist.append(('Mars', 'OSPF MD5 Authentication', 'message-digest-key 1 md5 cat' in m_str))

    # 3. Venus
    v_str = ' '.join(get_dev_lines('Venus'))
    checklist.append(('Venus', 'Loopback 3 (172.23.64.1/19)', '172.23.64.1 255.255.224.0' in v_str))
    checklist.append(('Venus', 'Gig0/0.2 & Gig0/0.3 Sub-interfaces', '172.23.128.3' in v_str and '172.23.144.3' in v_str))
    checklist.append(('Venus', 'Serial0/3/0 (172.23.255.5/30)', '172.23.255.5 255.255.255.252' in v_str))
    checklist.append(('Venus', 'OSPF ABR (Area 0 and Area 1)', 'area 0' in v_str and 'area 1' in v_str))
    checklist.append(('Venus', 'OSPF MD5 Authentication', 'message-digest-key 1 md5 cat' in v_str))

    # 4. Jupiter
    j_str = ' '.join(get_dev_lines('Jupiter'))
    checklist.append(('Jupiter', 'Loopback 4 (172.23.96.1/19)', '172.23.96.1 255.255.224.0' in j_str))
    checklist.append(('Jupiter', 'Serial0/3/0 OSPF (172.23.255.2/30)', '172.23.255.2 255.255.255.252' in j_str))
    checklist.append(('Jupiter', 'Serial0/3/1 EIGRP (172.22.255.1/30)', '172.22.255.1 255.255.255.252' in j_str))
    checklist.append(('Jupiter', 'Redistribute OSPF -> EIGRP (Metric 5 params)', 'redistribute ospf 1 metric 10000 100 255 1 1500' in j_str))
    checklist.append(('Jupiter', 'Redistribute EIGRP -> OSPF (subnets)', 'redistribute eigrp 69 subnets' in j_str))
    checklist.append(('Jupiter', 'Loop Prevention (distance ospf external 175)', 'distance ospf external 175' in j_str))
    checklist.append(('Jupiter', 'EIGRP Authentication (key 11 / mouse)', 'key 11' in j_str and 'mouse' in j_str))

    # 5. Mecury
    mec_str = ' '.join(get_dev_lines('Mecury'))
    checklist.append(('Mecury', 'Loopback 5 (172.22.0.1/19 in EIGRP)', '172.22.0.1 255.255.224.0' in mec_str))
    checklist.append(('Mecury', 'Serial0/3/0 OSPF (172.23.255.6/30)', '172.23.255.6 255.255.255.252' in mec_str))
    checklist.append(('Mecury', 'Serial0/3/1 EIGRP (172.22.255.5/30)', '172.22.255.5 255.255.255.252' in mec_str))
    checklist.append(('Mecury', 'Redistribute OSPF <-> EIGRP', 'redistribute ospf 1 metric' in mec_str and 'redistribute eigrp 69 subnets' in mec_str))
    checklist.append(('Mecury', 'Teacher Rule: NO default-originate (Anti-loop)', 'default-information originate' not in mec_str))
    checklist.append(('Mecury', 'Loop Prevention (distance ospf external 175)', 'distance ospf external 175' in mec_str))
    checklist.append(('Mecury', 'EIGRP Authentication (key 11 / mouse)', 'key 11' in mec_str and 'mouse' in mec_str))

    # 6. Neptune
    n_str = ' '.join(get_dev_lines('Neptune'))
    checklist.append(('Neptune', 'Serial0/3/0 (172.22.255.6/30 DCE 64000)', '172.22.255.6 255.255.255.252' in n_str and 'clock rate 64000' in n_str))
    checklist.append(('Neptune', 'Serial0/3/1 (172.22.255.2/30 DCE 64000)', '172.22.255.2 255.255.255.252' in n_str and 'clock rate 64000' in n_str))
    checklist.append(('Neptune', 'Gig0/0 Outside (192.168.0.10/24)', '192.168.0.10 255.255.255.0' in n_str and 'ip nat outside' in n_str))
    checklist.append(('Neptune', 'Default Route (0.0.0.0/0 -> 192.168.0.1)', 'ip route 0.0.0.0 0.0.0.0 192.168.0.1' in n_str))
    checklist.append(('Neptune', 'NAT Pool (192.168.0.11~.22/24)', 'ip nat pool ISP-POOL 192.168.0.11 192.168.0.22' in n_str))
    checklist.append(('Neptune', 'NAT Access-list (172.22 & 172.23)', 'permit 172.22.0.0' in n_str and 'permit 172.23.0.0' in n_str))
    checklist.append(('Neptune', 'EIGRP Default Route Redistribution', 'redistribute static metric' in n_str))
    checklist.append(('Neptune', 'EIGRP Authentication (key 11 / mouse)', 'key 11' in n_str and 'mouse' in n_str))

    # 7. Switches
    srv_str = ' '.join(get_dev_lines('Server'))
    checklist.append(('Server', 'Trunking on Fa0/1, Fa0/2, Fa0/3', 'switchport mode trunk' in srv_str and 'allowed vlan 2-3' in srv_str))

    cli_str = ' '.join(get_dev_lines('Client'))
    checklist.append(('Client', 'Trunking on Fa0/1, Fa0/2', 'switchport mode trunk' in cli_str and 'allowed vlan 2-3' in cli_str))
    checklist.append(('Client', 'Access Port for PC0 on Fa0/10 (VLAN 2)', 'switchport access vlan 2' in cli_str))

    # 8. ISP
    isp_str = ' '.join(get_dev_lines('ISP'))
    checklist.append(('ISP', 'Fa0/0 (192.168.0.1/24 to Neptune)', '192.168.0.1 255.255.255.0' in isp_str))
    checklist.append(('ISP', 'Vlan69 (8.8.8.9/24 Gateway for Servers)', '8.8.8.9 255.255.255.0' in isp_str))

    passed = 0
    for dev, item, ok in checklist:
        status = '[PASS]' if ok else '[FAIL]'
        if ok: passed += 1
        print(f"{status} {dev:10} | {item}")

    print('---------------------------------------------------------------')
    rate = (passed / len(checklist)) * 100
    print(f"AUDIT SUMMARY: {passed}/{len(checklist)} CHECKS PASSED ({rate:.1f}%)")
    print("===============================================================")
    return passed == len(checklist)

if __name__ == '__main__':
    default_xml = os.path.join(
        os.path.dirname(__file__),
        '..', '03_Engineering_Labs_and_Code', 'Day5', 'ISP_service_source.xml'
    )
    xml_path = sys.argv[1] if len(sys.argv) > 1 else default_xml
    audit_lab(xml_path)
