from scapy.all import sniff, IP

def packet_callback(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = packet[IP].proto
        print(f"[+] Packet captured: {src_ip} -> {dst_ip} | Protocol: {protocol}")

print("🔍 Sniffing started on the default interface. Press Ctrl+C to stop.\n")
sniff(prn=packet_callback, store=False)
