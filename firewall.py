from scapy.all import * 

rules = [ {"protocol": "TCP", "port": 22}, #blocks SSH
    {"protocol": "UDP", "port": 53}, #blocks DNS
    {"ip": "172.16.5.20"} ] #blocks a specific generic IP

def packet_matches_rule(pkt, rule): #returns true if a packet goes against one of the rules
    #matches the IP 
    if "ip" in rule and pkt.haslayer(IP): 
        if pkt[IP].src == rule["ip"] or pkt[IP].dst == rule["ip"]:
            return True

    #matches the protocool and port
    if "protocol" in rule and "port" in rule: 
        proto = rule["protocol"] 
        port = rule["port"]

        if proto == "TCP" and pkt.haslayer(TCP): 
            if pkt[TCP].sport == port or pkt[TCP].dport == port:
                return True

        if proto == "UDP" and pkt.haslayer(UDP): 
            if pkt[UDP].sport == port or pkt[UDP].dport == port:
                return True

    return False

def packet_check(pkt):
    for rule in rules: #iterates through each rule 
        if packet_matches_rule(pkt, rule): 
            print(f"BLOCKED {pkt.summary()}")
            return  #this is so that the packet gets ignored 

    # If no rule matched, allow it
    print(f"ALLOWED {pkt.summary()}")

def firewall_main():
    print("Firewall has started up.") #informing user that firewall has started
    sniff(prn=packet_check, store=False) #doesn't store packet