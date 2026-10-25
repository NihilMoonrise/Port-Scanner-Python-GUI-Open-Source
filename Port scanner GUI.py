#Open source Python port scanner written fully by Nihil
#MIT LICENSED
#"THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND... IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY..."

#A simple port scanner that scans for the ports 1337, 4444 and 8080 but it also shows other open ports
#port 1337 and 4444 are usually used by malware

#Unauthorized port scanning may violate applicable laws, policies and terms of service. Use this tool responsibly.
#The IP address is where the tool is pointed at and it is pretty much the equivalent of walking up to someone's house and testing the doors and windows to see whether they are locked or not.
#It is maybe not breaking in but it is the first step that malicious actors take.

#Only scan systems you own or have explicit permission to test.

import socket
import tkinter as tk

root = tk.Tk()
root.configure(bg="black")
root.title("Port Scanner")
root.geometry("500x400")

name_label = tk.Label(root, text="Port Scanner", bg="black", fg="white")
name_label.pack()

name_entry = tk.Entry(root, bg="#222222", fg="white", insertbackground="white")
name_entry.insert(0, "127.0.0.1")
name_entry.pack()

def scan_port(host, port):
    a = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    a.settimeout(0.5)
    c = a.connect_ex((host, port))
    a.close()
    if c == 0:
        return True
    else:
        return False

targeted_ports_scan = [1337, 4444, 8080]

flagged_ports = {
    1337: "Port usually used by classic backdoors (malware)",
    4444: "A port usually used by malware and security researchers (Metasploit)",
    8080: "Alternate web server or proxy port, USUALLY legitimate"
}

def start_scan():
    results.delete("1.0", tk.END)
    host = name_entry.get()
    results.insert(tk.END, host + "\n")
    open_ports = []
    for port in targeted_ports_scan:
        resultaat = scan_port(host, port)
        if resultaat:
            open_ports.append(port)
    if not open_ports:
        results.insert(tk.END, "No open ports were found\n")
    else:
        for port in open_ports:
            if port in flagged_ports:
                results.insert(tk.END, f"[!] Port {port} open - {flagged_ports[port]}\n")
            else:
                results.insert(tk.END, f"[+] Port {port} open\n")

scan_button = tk.Button(root, text="Scan", bg="#222222", fg="white", command=start_scan)
scan_button.pack()

results = tk.Text(root, height=16, width=60, bg="#222222", fg="white", insertbackground="white")
results.pack()

root.mainloop()

