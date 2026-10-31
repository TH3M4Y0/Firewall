from scapy.all import * 
import time

stats = { #counts the number of incoming packets, the blocked packets and allowed ones
    "total": 0,
    "allowed": 0,
    "blocked": 0
}

global packet_count #used for counting packets per second to get network traffic
packet_count = 0
start_time = time.time()

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
    stats["total"] += 1
    time_difference = time.time() - start_time

    for rule in rules: #iterates through each rule 
        if packet_matches_rule(pkt, rule): 
            stats["blocked"] += 1
            print(f"BLOCKED {pkt.summary()}")
            return  #this is so that the packet gets ignored 

    if time_difference >= 1:
        pps = packet_count/time_difference #calculates total incoming packets per second

        #resets time_difference and packet_count
        packet_count = 0 
        start_time = time.time()

    stats["allowed"] += 1
    print(f"ALLOWED {pkt.summary()}") # Ifno rules matched allow it

def firewall_main():
    print("Firewall has started up.") #informing user that firewall has started
    sniff(prn=packet_check, store=False) #doesn't store packet