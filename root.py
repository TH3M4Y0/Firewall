import tkinter as tk
from tkinter import ttk #for themed widgets
import firewall
import threading
import time

def update(): #updates the gui with the correct packet counts
    total_label.config(text=f"Total Packets: {firewall.stats['total']}")
    allowed_label.config(text=f"Allowed: {firewall.stats['allowed']}")
    blocked_label.config(text=f"Blocked: {firewall.stats['blocked']}")
    pps_label.config(text=f"PPS: {firewall.stats['pps']}")
    root.after(800, update)


root = tk.Tk() #creates the window 
TITLE = root.title(' Firewall Window ')
root.geometry('800x600+575+175') # configures the window size and position
root.resizable(False, False)

start_firewall_button = ttk.Button(root, text = "Start Firewall", command = lambda: threading.Thread(target = firewall.firewall_main, daemon = True).start()) #button to start the firewall
start_firewall_button.place(x=300, y=200)

exit_button = ttk.Button(root, text = 'Stop', command = lambda: root.quit()) #button to quit the window
exit_button.place(x=450, y=200)

count_frame = tk.Frame(root, height = 200, width = 900, relief= 'raised') #frame to have all the packet counts in
count_frame.place(x=0, y=0)

total_label = tk.Label(count_frame, text="Total Packets: 0", font=("Arial", 12)) #text for the total packets
total_label.place(x = 0, y = 100)

allowed_label = tk.Label(count_frame, text="Allowed: 0", font=("Arial", 12)) # text for the allowed packets
allowed_label.place(x = 150, y = 100)

blocked_label = tk.Label(count_frame, text="Blocked: 0", font=("Arial", 12))#text for the blocked packets
blocked_label.place(x = 300, y = 100)

pps_label = tk.Label(count_frame, text="PPS: 0", font=("Arial", 12))# text for the PPS
pps_label.place(x = 450, y = 100)

update()
root.mainloop() #runs the window 