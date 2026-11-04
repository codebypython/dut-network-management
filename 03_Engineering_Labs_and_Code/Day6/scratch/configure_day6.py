import xml.etree.ElementTree as ET
import os
import sys

sys.path.append(r"d:\NEXUS\02_Academic_DUT\Courses\03_Company_Network_Management_NMA\05_Troubleshooting_and_Toolkits\Unpacket")
from repacket import compress_qt, obf_stage2, obf_stage1
from Decipher.twofish import Twofish
from Decipher.eax import EAX

SOURCE_XML = r"d:\NEXUS\02_Academic_DUT\Courses\03_Company_Network_Management_NMA\03_Engineering_Labs_and_Code\Day6\day6_source.xml"
OUTPUT_XML = r"d:\NEXUS\02_Academic_DUT\Courses\03_Company_Network_Management_NMA\03_Engineering_Labs_and_Code\Day6\day6_configured.xml"
OUTPUT_PKT = r"d:\NEXUS\02_Academic_DUT\Courses\03_Company_Network_Management_NMA\03_Engineering_Labs_and_Code\Day6\ISP service.pkt"
BACKUP_PKT = r"d:\NEXUS\02_Academic_DUT\Courses\03_Company_Network_Management_NMA\03_Engineering_Labs_and_Code\Day6\Lab6_EIGRP_OSPF_VLAN_NAT_Completed.pkt"

def build_configs():
    cfgs = {}

    cfgs['WestGate'] = """!
version 15.1
service timestamps log datetime msec
service timestamps debug datetime msec
no service password-encryption
!
hostname WestGate
!
ip cef
no ipv6 cef
!
spanning-tree mode pvst
!
interface Loopback1
 ip address 172.21.0.1 255.255.224.0
!
interface GigabitEthernet0/0
 ip address 10.2.200.200 255.255.0.0
 ip nat outside
 duplex auto
 speed auto
 no shutdown
!
interface GigabitEthernet0/1
 no ip address
 duplex auto
 speed auto
 shutdown
!
interface GigabitEthernet0/2
 no ip address
 duplex auto
 speed auto
 shutdown
!
interface Serial0/3/0
 ip address 172.21.255.1 255.255.255.252
 ip nat inside
 clock rate 64000
 no shutdown
!
interface Serial0/3/1
 no ip address
 clock rate 2000000
 shutdown
!
interface Vlan1
 no ip address
 shutdown
!
router eigrp 66
 network 10.0.0.0
 network 172.21.0.0
 no auto-summary
!
ip nat pool WEST-POOL 10.2.200.201 10.2.200.203 netmask 255.255.0.0
ip nat inside source list 1 pool WEST-POOL overload
!
ip classless
ip default-network 10.0.0.0
!
access-list 1 permit 172.21.0.0 0.0.255.255
access-list 1 permit 172.22.0.0 0.0.255.255
access-list 1 permit 172.23.0.0 0.0.255.255
!
line con 0
line aux 0
line vty 0 4
 login
!
end"""

    cfgs['West'] = """!
version 15.1
service timestamps log datetime msec
service timestamps debug datetime msec
no service password-encryption
!
hostname West
!
ip cef
no ipv6 cef
!
spanning-tree mode pvst
!
interface Loopback2
 ip address 172.21.32.1 255.255.224.0
 ip access-group 101 in
!
interface GigabitEthernet0/0
 no ip address
 duplex auto
 speed auto
 no shutdown
!
interface GigabitEthernet0/0.2
 encapsulation dot1Q 2
 ip address 172.22.32.1 255.255.240.0
 no shutdown
!
interface GigabitEthernet0/0.3
 encapsulation dot1Q 3
 ip address 172.22.48.1 255.255.240.0
 no shutdown
!
interface GigabitEthernet0/1
 no ip address
 duplex auto
 speed auto
 shutdown
!
interface GigabitEthernet0/2
 no ip address
 duplex auto
 speed auto
 shutdown
!
interface Serial0/3/0
 ip address 172.21.255.2 255.255.255.252
 no shutdown
!
interface Serial0/3/1
 no ip address
 clock rate 2000000
 shutdown
!
interface Vlan1
 no ip address
 shutdown
!
router eigrp 66
 redistribute eigrp 99 metric 10000 100 255 1 1500
 network 172.21.0.0
 no auto-summary
!
router eigrp 99
 redistribute eigrp 66 metric 10000 100 255 1 1500
 redistribute static metric 10000 100 255 1 1500
 network 172.22.0.0
 network 172.22.32.0 0.0.15.255
 network 172.22.48.0 0.0.15.255
 no auto-summary
!
ip classless
ip route 0.0.0.0 0.0.0.0 172.21.255.1
!
access-list 101 permit tcp 172.21.32.0 0.0.31.255 172.22.48.0 0.0.15.255 eq www
access-list 101 permit tcp 172.21.32.0 0.0.31.255 172.22.48.0 0.0.15.255 eq telnet
access-list 101 deny icmp 172.21.32.0 0.0.31.255 172.22.48.0 0.0.15.255 echo
access-list 101 permit ip any any
!
line con 0
line aux 0
line vty 0 4
 login
!
end"""

    cfgs['Core'] = """!
version 15.1
service timestamps log datetime msec
service timestamps debug datetime msec
no service password-encryption
!
hostname Core
!
ip cef
no ipv6 cef
!
spanning-tree mode pvst
!
interface Loopback3
 ip address 172.22.0.1 255.255.224.0
!
interface GigabitEthernet0/0
 no ip address
 duplex auto
 speed auto
 no shutdown
!
interface GigabitEthernet0/0.2
 encapsulation dot1Q 2
 ip address 172.22.32.2 255.255.240.0
 no shutdown
!
interface GigabitEthernet0/0.3
 encapsulation dot1Q 3
 ip address 172.22.48.2 255.255.240.0
 no shutdown
!
interface GigabitEthernet0/1
 no ip address
 duplex auto
 speed auto
 shutdown
!
interface GigabitEthernet0/2
 no ip address
 duplex auto
 speed auto
 shutdown
!
interface Serial0/3/0
 no ip address
 clock rate 2000000
 shutdown
!
interface Serial0/3/1
 no ip address
 clock rate 2000000
 shutdown
!
interface Vlan1
 no ip address
 shutdown
!
router eigrp 99
 network 172.22.0.0
 network 172.22.32.0 0.0.15.255
 network 172.22.48.0 0.0.15.255
 no auto-summary
!
ip classless
!
line con 0
line aux 0
line vty 0 4
 login
!
end"""

    cfgs['East'] = """!
version 15.1
service timestamps log datetime msec
service timestamps debug datetime msec
no service password-encryption
!
hostname East
!
ip cef
no ipv6 cef
!
spanning-tree mode pvst
!
interface Loopback4
 ip address 172.23.0.1 255.255.224.0
!
interface Loopback5
 ip address 172.23.32.1 255.255.224.0
!
interface GigabitEthernet0/0
 no ip address
 duplex auto
 speed auto
 no shutdown
!
interface GigabitEthernet0/0.2
 encapsulation dot1Q 2
 ip address 172.22.32.3 255.255.240.0
 no shutdown
!
interface GigabitEthernet0/0.3
 encapsulation dot1Q 3
 ip address 172.22.48.3 255.255.240.0
 no shutdown
!
interface GigabitEthernet0/1
 no ip address
 duplex auto
 speed auto
 shutdown
!
interface GigabitEthernet0/2
 no ip address
 duplex auto
 speed auto
 shutdown
!
interface Serial0/3/0
 ip address 172.23.255.1 255.255.255.252
 no shutdown
!
interface Serial0/3/1
 no ip address
 clock rate 2000000
 shutdown
!
interface Vlan1
 no ip address
 shutdown
!
router eigrp 99
 redistribute ospf 1 metric 10000 100 255 1 1500
 redistribute static metric 10000 100 255 1 1500
 network 172.22.0.0
 network 172.22.32.0 0.0.15.255
 network 172.22.48.0 0.0.15.255
 no auto-summary
!
router ospf 1
 log-adjacency-changes
 redistribute eigrp 99 subnets
 network 172.23.0.0 0.0.255.255 area 0
!
ip classless
ip route 0.0.0.0 0.0.0.0 172.23.255.2
!
line con 0
line aux 0
line vty 0 4
 login
!
end"""

    cfgs['EastGate'] = """!
version 15.1
service timestamps log datetime msec
service timestamps debug datetime msec
no service password-encryption
!
hostname EastGate
!
ip cef
no ipv6 cef
!
spanning-tree mode pvst
!
interface Loopback6
 ip address 172.23.64.1 255.255.224.0
 ip nat inside
!
interface GigabitEthernet0/0
 ip address 192.168.0.10 255.255.255.0
 ip nat outside
 duplex auto
 speed auto
 no shutdown
!
interface GigabitEthernet0/1
 no ip address
 duplex auto
 speed auto
 shutdown
!
interface GigabitEthernet0/2
 no ip address
 duplex auto
 speed auto
 shutdown
!
interface Serial0/3/0
 ip address 172.23.255.2 255.255.255.252
 ip nat inside
 clock rate 64000
 no shutdown
!
interface Serial0/3/1
 no ip address
 clock rate 2000000
 shutdown
!
interface Vlan1
 no ip address
 shutdown
!
router ospf 1
 log-adjacency-changes
 network 172.23.0.0 0.0.255.255 area 0
 default-information originate
!
ip nat pool EAST-POOL 192.168.0.11 192.168.0.15 netmask 255.255.255.0
ip nat inside source list 1 pool EAST-POOL overload
!
ip classless
ip route 0.0.0.0 0.0.0.0 192.168.0.1
!
access-list 1 permit 172.21.0.0 0.0.255.255
access-list 1 permit 172.22.0.0 0.0.255.255
access-list 1 permit 172.23.0.0 0.0.255.255
!
line con 0
line aux 0
line vty 0 4
 login
!
end"""

    cfgs['Server'] = """!
version 15.0
no service timestamps log datetime msec
no service timestamps debug datetime msec
no service password-encryption
!
hostname Server
!
spanning-tree mode pvst
spanning-tree extend system-id
!
vtp domain business
vtp password goodluck
vtp mode server
!
vlan 2
 name west
!
vlan 3
 name east
!
interface FastEthernet0/1
 switchport mode trunk
 switchport trunk allowed vlan 1,2,3
 no shutdown
!
interface FastEthernet0/2
 switchport mode trunk
 switchport trunk allowed vlan 1,2,3
 no shutdown
!
interface FastEthernet0/3
 switchport mode trunk
 switchport trunk allowed vlan 1,2,3
 no shutdown
!
interface FastEthernet0/10
 switchport access vlan 2
 switchport mode access
 spanning-tree portfast
 no shutdown
!
interface GigabitEthernet0/1
 switchport mode trunk
 switchport trunk allowed vlan 1,2,3
 no shutdown
!
interface GigabitEthernet0/2
 switchport mode trunk
 switchport trunk allowed vlan 1,2,3
 no shutdown
!
interface Vlan1
 no ip address
 shutdown
!
line con 0
line vty 0 4
 login
line vty 5 15
 login
!
end"""

    cfgs['Client'] = """!
version 15.0
no service timestamps log datetime msec
no service timestamps debug datetime msec
no service password-encryption
!
hostname Client
!
spanning-tree mode pvst
spanning-tree extend system-id
!
vtp domain business
vtp password goodluck
vtp mode client
!
interface FastEthernet0/1
 switchport mode trunk
 switchport trunk allowed vlan 1,2,3
 no shutdown
!
interface FastEthernet0/2
 switchport mode trunk
 switchport trunk allowed vlan 1,2,3
 no shutdown
!
interface FastEthernet0/10
 switchport access vlan 3
 switchport mode access
 spanning-tree portfast
 no shutdown
!
interface GigabitEthernet0/1
 switchport mode trunk
 switchport trunk allowed vlan 1,2,3
 no shutdown
!
interface GigabitEthernet0/2
 shutdown
!
interface Vlan1
 no ip address
 shutdown
!
line con 0
line vty 0 4
 login
line vty 5 15
 login
!
end"""

    cfgs['ISP WEST'] = """!
version 12.4
no service timestamps log datetime msec
no service timestamps debug datetime msec
no service password-encryption
!
hostname ISP-West
!
ip cef
no ipv6 cef
!
spanning-tree mode pvst
!
interface Loopback0
 ip address 10.10.10.10 255.255.255.255
 no shutdown
!
interface FastEthernet0/0
 description LINK TO WESTGATE
 ip address 10.2.0.1 255.255.0.0
 duplex auto
 speed auto
 no shutdown
!
interface FastEthernet0/1
 no ip address
 duplex auto
 speed auto
 shutdown
!
interface FastEthernet0/0/0
 switchport access vlan 69
 switchport mode access
 spanning-tree portfast
 no shutdown
!
interface FastEthernet0/0/1
 switchport access vlan 69
 switchport mode access
 spanning-tree portfast
 no shutdown
!
interface FastEthernet0/0/2
 switchport access vlan 69
 switchport mode access
 spanning-tree portfast
 no shutdown
!
interface FastEthernet0/0/3
 switchport access vlan 69
 switchport mode access
 spanning-tree portfast
 shutdown
!
interface Vlan1
 no ip address
 shutdown
!
interface Vlan69
 ip address 10.2.0.254 255.255.0.0
 no shutdown
!
ip classless
!
line con 0
line aux 0
line vty 0 4
 login
!
end"""

    cfgs['ISP EAST'] = """!
version 12.4
no service timestamps log datetime msec
no service timestamps debug datetime msec
no service password-encryption
!
hostname ISP-East
!
ip cef
no ipv6 cef
!
spanning-tree mode pvst
!
interface Loopback0
 ip address 8.8.8.8 255.255.255.255
 no shutdown
!
interface FastEthernet0/0
 description LINK TO EASTGATE
 ip address 192.168.0.1 255.255.255.0
 duplex auto
 speed auto
 no shutdown
!
interface FastEthernet0/1
 no ip address
 duplex auto
 speed auto
 shutdown
!
interface FastEthernet0/0/0
 switchport access vlan 69
 switchport mode access
 spanning-tree portfast
 no shutdown
!
interface FastEthernet0/0/1
 switchport access vlan 69
 switchport mode access
 spanning-tree portfast
 no shutdown
!
interface FastEthernet0/0/2
 switchport access vlan 69
 switchport mode access
 spanning-tree portfast
 no shutdown
!
interface FastEthernet0/0/3
 switchport access vlan 69
 switchport mode access
 spanning-tree portfast
 shutdown
!
interface Vlan1
 no ip address
 shutdown
!
interface Vlan69
 ip address 192.168.0.254 255.255.255.0
 no shutdown
!
ip classless
!
line con 0
line aux 0
line vty 0 4
 login
!
end"""

    return cfgs

def apply_configs_to_xml():
    tree = ET.parse(SOURCE_XML)
    root = tree.getroot()
    cfgs = build_configs()

    for dev_name, cfg_text in cfgs.items():
        found = False
        for d in root.findall('.//DEVICE'):
            if d.findtext('.//NAME') == dev_name:
                found = True
                print(f"Applying configuration to '{dev_name}'...")
                
                # Update hostname in SYS_NAME
                sys_name = d.find('.//SYS_NAME')
                if sys_name is not None:
                    sys_name.text = cfg_text.split('hostname ')[1].split('\n')[0].strip()

                # Update RUNNINGCONFIG
                rc = d.find('.//RUNNINGCONFIG')
                if rc is not None:
                    rc.clear()
                    for line in cfg_text.strip().split('\n'):
                        line_el = ET.SubElement(rc, 'LINE')
                        line_el.text = line
                
                # Update STARTUPCONFIG
                sc = d.find('.//STARTUPCONFIG')
                if sc is not None:
                    sc.clear()
                    for line in cfg_text.strip().split('\n'):
                        line_el = ET.SubElement(sc, 'LINE')
                        line_el.text = line
        if not found:
            print(f"Warning: Device '{dev_name}' not found in XML!")

    # Configure ISP West servers (Google DNS 2, Google Mail 2, Web 2)
    west_servers = {
        'Google DNS 2': ('10.2.0.2', '255.255.0.0', '10.2.0.1', '10.10.10.10'),
        'Google Mail 2': ('10.2.0.3', '255.255.0.0', '10.2.0.1', '10.10.10.10'),
        'Web 2': ('10.2.0.4', '255.255.0.0', '10.2.0.1', '10.10.10.10'),
    }
    east_servers = {
        'Google DNS': ('192.168.0.2', '255.255.255.0', '192.168.0.1', '8.8.8.8'),
        'Google Mail': ('192.168.0.3', '255.255.255.0', '192.168.0.1', '8.8.8.8'),
        'Web': ('192.168.0.4', '255.255.255.0', '192.168.0.1', '8.8.8.8'),
    }

    all_servers = {**west_servers, **east_servers}
    for d in root.findall('.//DEVICE'):
        name = d.findtext('.//NAME')
        if name in all_servers:
            ip, mask, gw, dns = all_servers[name]
            port = d.find('.//PORT')
            if port is not None:
                p_ip = port.find('IP')
                if p_ip is not None: p_ip.text = ip
                p_sub = port.find('SUBNET')
                if p_sub is not None: p_sub.text = mask
                p_gw = port.find('PORT_GATEWAY')
                if p_gw is not None: p_gw.text = gw
                p_dns = port.find('PORT_DNS')
                if p_dns is not None: p_dns.text = dns
            print(f"Configured server '{name}' with IP {ip}")

    # Save output XML
    tree.write(OUTPUT_XML, encoding='utf-8', xml_declaration=True)
    print(f"[+] Saved configured XML to '{OUTPUT_XML}'")

def encrypt_to_pkt(xml_file, pkt_file):
    with open(xml_file, "rb") as f:
        xml_data = f.read()

    print(f"[*] Compressing data ({len(xml_data)} bytes)...")
    comp = compress_qt(xml_data)

    print("[*] Applying Stage 2 Obfuscation...")
    s2 = obf_stage2(comp)

    print("[*] Encrypting (Twofish/EAX)...")
    key = bytes([137]) * 16
    iv = bytes([16]) * 16
    tf = Twofish(key)
    eax = EAX(tf.encrypt)
    ct, tag = eax.encrypt(nonce=iv, plaintext=s2)
    eax_blob = ct + tag

    print("[*] Applying Stage 1 Obfuscation...")
    s1 = obf_stage1(eax_blob)

    with open(pkt_file, "wb") as f:
        f.write(s1)
    print(f"[+] Successfully wrote PKT to '{pkt_file}' ({len(s1)} bytes)")

if __name__ == "__main__":
    apply_configs_to_xml()
    encrypt_to_pkt(OUTPUT_XML, OUTPUT_PKT)
    encrypt_to_pkt(OUTPUT_XML, BACKUP_PKT)
    print("\n[SUCCESS] Day 6 Lab PKT has been completely built and configured!")

