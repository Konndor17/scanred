import scapy.all as scapy
# instalar esta libreria pip install scapy
def escanear(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    dispositivos = []
    for elemento in answered_list:
        dispositivo = {"ip": elemento[1].psrc, "mac": elemento[1].hwsrc}
        dispositivos.append(dispositivo)
    return dispositivos

def mostrar_dispositivos(dispositivos):
    print("Dirección IP\t\tDirección MAC")
    print("------------------------------------------")
    for dispositivo in dispositivos:
        print(dispositivo["ip"] + "\t\t" + dispositivo["mac"])

def mostrar_banner():
    banner = """
 _______ _     _ _______  ______ _     _ _______  ______
|    ___|_____| |   _   ||    ___|  _  |   _   ||    _ |
|    ___|   _   |       ||    ___| | | |       ||   | ||
|   |   |_______|   _   | |   |   | | | |   _   | \   |_|
|___|            |_______||___|   |_| |_|__| |__|  |______|

    Escaneo de Dispositivos en la Red Local - IP y MAC

    """
    print(banner)

if __name__ == "__main__":
    mostrar_banner()
    ip_rango = "192.168.1.1/24"  # Ajusta este rango a tu red local
    dispositivos_en_red = escanear(ip_rango)
    mostrar_dispositivos(dispositivos_en_red)
