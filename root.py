import tkinter as tk
from tkinter import ttk #for themed widgets
from firewall import firewall_main
import threading

root = tk.Tk() #creates the window 
TITLE = root.title(' Firewall Window ')
root.geometry('800x600+575+175') # configures the window size and position
root.resizable(False, False)

start_firewall_button = ttk.Button(root, text = "Start Firewall", command = lambda: threading.Thread(target = firewall_main, daemon = True).start()) #button to start the firewall
start_firewall_button.place(x=300, y=200)

exit_button = ttk.Button(root, text = 'Stop', command = lambda: root.quit()) #button to quit the window
exit_button.place(x=450, y=200)

root.mainloop() #runs the window 