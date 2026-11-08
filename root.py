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
root.configure(background = "#1E1E1E")

style = ttk.Style() #styling of all the widgets in the app
style.configure("TFrame", background="#252526")
style.configure("TLabel", background="#252526", foreground ="#FFFFFF", font=("Consolas", 16) )
style.configure("Start.TButton", font=("Consolas", 14), background="#252526", relief = "flat" )

style.map(
    "Start.TButton",
    background=[
        ("active", "#252526"),
        ("pressed", "#1e7e34")
    ],
)

start_frame = ttk.Frame(root, height = 110, width = 900, style = "TFrame") #frame to have all the packet counts in
start_frame.place(x=0, y=530)

start_button = ttk.Button(start_frame, text = "Start Firewall", style = "Start.TButton", command = lambda: threading.Thread(target = firewall.firewall_main, daemon = True).start()) #button to start the firewall
start_button.place(x=180, y=10, width=170, height=50)

exit_button = ttk.Button(start_frame, text = 'Stop Firewall', style = "Start.TButton", command = lambda: root.quit()) #button to quit the window
exit_button.place(x=480, y=10, width=170, height=50)

count_frame = ttk.Frame(root, height = 100, width = 900) #frame to have all the packet counts in
count_frame.place(x=0, y=0)

total_label = ttk.Label(count_frame, text="Total Packets: 0", style = "TLabel") #text for the total packets
total_label.place(x = 100, y = 18)

allowed_label = ttk.Label(count_frame, text="Allowed: 0", style = "TLabel", foreground="#28A745") # text for the allowed packets
allowed_label.place(x = 370, y = 18)

blocked_label = ttk.Label(count_frame, text="Blocked: 0", style = "TLabel", foreground="#DC3545")#text for the blocked packets
blocked_label.place(x = 590, y = 18)

pps_label = ttk.Label(count_frame, text="PPS: 0", style = "TLabel")# text for the PPS
pps_label.place(x = 590, y = 52)

update()
root.mainloop() #runs the window 