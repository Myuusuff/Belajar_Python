import os
import re

def get_ip_from_mac(mac_address):
    # Jalankan perintah arp -a untuk mendapatkan daftar IP-MAC di jaringan lokal
    result = os.popen('arp -a').read()
    
    # Cari MAC address dalam hasil ARP
    pattern = re.compile(r"(\d+\.\d+\.\d+\.\d+)\s+.*\s+" + mac_address)
    match = pattern.search(result)
    
    if match:
        return match.group(1)  # Mengembalikan IP lokal yang terkait dengan MAC address
    else:
        return "MAC address tidak ditemukan dalam tabel ARP."

# Ganti dengan MAC address yang ingin kamu cek
mac_address = "28:31:66:8C:68:9B"
ip = get_ip_from_mac(mac_address)
print(f"IP lokal untuk MAC {mac_address} adalah: {ip}")
