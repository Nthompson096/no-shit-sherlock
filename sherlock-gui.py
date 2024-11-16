import tkinter as tk
from tkinter import ttk, scrolledtext, filedialog
import subprocess
import threading

class SherlockGUI:
    def __init__(self, master):
        self.master = master
        master.title("Sherlock GUI")
        master.geometry("800x600")

        # Username input
        self.username_label = ttk.Label(master, text="Username:")
        self.username_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.username_entry = ttk.Entry(master, width=50)
        self.username_entry.grid(row=0, column=1, columnspan=2, padx=5, pady=5)

        # Options
        self.verbose_var = tk.BooleanVar()
        self.verbose_check = ttk.Checkbutton(master, text="Verbose", variable=self.verbose_var)
        self.verbose_check.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        self.csv_var = tk.BooleanVar()
        self.csv_check = ttk.Checkbutton(master, text="CSV Output", variable=self.csv_var)
        self.csv_check.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        self.xlsx_var = tk.BooleanVar()
        self.xlsx_check = ttk.Checkbutton(master, text="XLSX Output", variable=self.xlsx_var)
        self.xlsx_check.grid(row=1, column=2, padx=5, pady=5, sticky="w")

        self.tor_var = tk.BooleanVar()
        self.tor_check = ttk.Checkbutton(master, text="Use Tor", variable=self.tor_var)
        self.tor_check.grid(row=2, column=0, padx=5, pady=5, sticky="w")

        self.unique_tor_var = tk.BooleanVar()
        self.unique_tor_check = ttk.Checkbutton(master, text="Unique Tor", variable=self.unique_tor_var)
        self.unique_tor_check.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        self.dump_response_var = tk.BooleanVar()
        self.dump_response_check = ttk.Checkbutton(master, text="Dump Response", variable=self.dump_response_var)
        self.dump_response_check.grid(row=2, column=2, padx=5, pady=5, sticky="w")

        self.no_txt_var = tk.BooleanVar()
        self.no_txt_check = ttk.Checkbutton(master, text="No TXT File", variable=self.no_txt_var)
        self.no_txt_check.grid(row=3, column=0, padx=5, pady=5, sticky="w")

        self.nsfw_var = tk.BooleanVar()
        self.nsfw_check = ttk.Checkbutton(master, text="Include NSFW Sites", variable=self.nsfw_var)
        self.nsfw_check.grid(row=3, column=1, padx=5, pady=5, sticky="w")

        self.print_all_var = tk.BooleanVar()
        self.print_all_check = ttk.Checkbutton(master, text="Print All Sites", variable=self.print_all_var)
        self.print_all_check.grid(row=3, column=2, padx=5, pady=5, sticky="w")

        self.print_found_var = tk.BooleanVar()
        self.print_found_check = ttk.Checkbutton(master, text="Print Found Sites", variable=self.print_found_var)
        self.print_found_check.grid(row=4, column=0, padx=5, pady=5, sticky="w")

        self.no_color_var = tk.BooleanVar()
        self.no_color_check = ttk.Checkbutton(master, text="No Color Output", variable=self.no_color_var)
        self.no_color_check.grid(row=4, column=1, padx=5, pady=5, sticky="w")

        self.browse_var = tk.BooleanVar()
        self.browse_check = ttk.Checkbutton(master, text="Browse Results", variable=self.browse_var)
        self.browse_check.grid(row=4, column=2, padx=5, pady=5, sticky="w")

        self.local_var = tk.BooleanVar()
        self.local_check = ttk.Checkbutton(master, text="Use Local Data", variable=self.local_var)
        self.local_check.grid(row=5, column=0, padx=5, pady=5, sticky="w")

        self.timeout_label = ttk.Label(master, text="Timeout:")
        self.timeout_label.grid(row=6, column=0, padx=5, pady=5, sticky="w")
        self.timeout_entry = ttk.Entry(master, width=10)
        self.timeout_entry.insert(0, "60")  # Default value
        self.timeout_entry.grid(row=6, column=1, padx=5, pady=5, sticky="w")

        self.site_label = ttk.Label(master, text="Site:")
        self.site_label.grid(row=7, column=0, padx=5, pady=5, sticky="w")
        self.site_entry = ttk.Entry(master, width=50)
        self.site_entry.grid(row=7, column=1, columnspan=2, padx=5, pady=5)

        self.proxy_label = ttk.Label(master, text="Proxy URL:")
        self.proxy_label.grid(row=8, column=0, padx=5, pady=5, sticky="w")
        self.proxy_entry = ttk.Entry(master, width=50)
        self.proxy_entry.grid(row=8, column=1, columnspan=2, padx=5, pady=5)

        self.json_label = ttk.Label(master, text="JSON File:")
        self.json_label.grid(row=9, column=0, padx=5, pady=5, sticky="w")
        self.json_entry = ttk.Entry(master, width=50)
        self.json_entry.grid(row=9, column=1, columnspan=2, padx=5, pady=5)

        self.output_button = ttk.Button(master, text="Select Output File", command=self.select_output)
        self.output_button.grid(row=10, column=0, padx=5, pady=5, sticky="w")
        self.output_label = ttk.Label(master, text="No file selected")
        self.output_label.grid(row=10, column=1, columnspan=2, padx=5, pady=5, sticky="w")

        # Search button
        self.search_button = ttk.Button(master, text="Search", command=self.run_search)
        self.search_button.grid(row=11, column=0, columnspan=3, pady=10)

        # Results display
        self.results_text = scrolledtext.ScrolledText(master, height=20, width=80)
        self.results_text.grid(row=12, column=0, columnspan=3, padx=5, pady=5)

    def select_output(self):
        filename = filedialog.asksaveasfilename(defaultextension=".txt")
        if filename:
            self.output_label.config(text=filename)

    def run_search(self):
        username = self.username_entry.get()
        if not username:
            self.results_text.insert(tk.END, "Please enter a username.\n")
            return

        self.results_text.delete('1.0', tk.END)
        self.results_text.insert(tk.END, f"Searching for username: {username}\n\n")
        
        thread = threading.Thread(target=self.sherlock_search, args=(username,))
        thread.start()

    def sherlock_search(self, username):
        try:
            command = ['sherlock', username]
            
            if self.verbose_var.get():
                command.append('--verbose')
            if self.csv_var.get():
                command.append('--csv')
            if self.xlsx_var.get():
                command.append('--xlsx')
            if self.tor_var.get():
                command.append('--tor')
            if self.unique_tor_var.get():
                command.append('--unique-tor')
            if self.dump_response_var.get():
                command.append('--dump-response')
            if self.no_txt_var.get():
                command.append('--no-txt')
            if self.nsfw_var.get():
                command.append('--nsfw')
            if self.print_all_var.get():
                command.append('--print-all')
            if self.print_found_var.get():
                command.append('--print-found')
            if self.no_color_var.get():
                command.append('--no-color')
            if self.browse_var.get():
                command.append('--browse')
            if self.local_var.get():
                command.append('--local')

            timeout = self.timeout_entry.get()
            if timeout:
                command.extend(['--timeout', timeout])
            
            site = self.site_entry.get()
            if site:
                command.extend(['--site', site])
            
            proxy = self.proxy_entry.get()
            if proxy:
                command.extend(['--proxy', proxy])
            
            json_file = self.json_entry.get()
            if json_file:
                command.extend(['--json', json_file])
            
            output_file = self.output_label.cget("text")
            if output_file != "No file selected":
                command.extend(['--output', output_file])

            process = subprocess.Popen(command, 
                                       stdout=subprocess.PIPE, 
                                       stderr=subprocess.PIPE,
                                       text=True)
            
            for line in process.stdout:
                self.results_text.insert(tk.END, line)
                self.results_text.see(tk.END)
                self.results_text.update()

            process.wait()

            if process.returncode != 0:
                error_output = process.stderr.read()
                self.results_text.insert(tk.END, f"Error: {error_output}\n")
            
            self.results_text.insert(tk.END, "\nSearch completed.\n")
        except Exception as e:
            self.results_text.insert(tk.END, f"An error occurred: {str(e)}\n")

root = tk.Tk()
gui = SherlockGUI(root)
root.mainloop()
