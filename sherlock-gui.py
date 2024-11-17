import tkinter as tk
from tkinter import ttk, scrolledtext, filedialog
import subprocess
import threading
import json
import os

class SherlockGUI:
    def __init__(self, master):
        self.master = master
        master.title("Sherlock GUI")
        master.geometry("670x830")
        master.resizable(False, False)  # Disable window resizing

        # Dark theme settings
        self.bg_color = "#2E2E2E"
        self.fg_color = "#FFFFFF"
        self.entry_bg_color = "#3C3C3C"
        self.entry_fg_color = "#3C3C3C"
        self.button_bg_color = "#555555"
        self.button_fg_color = "#FFFFFF"
        self.checkbutton_bg_color = "#2E2E2E"
        self.checkbutton_fg_color = "#FFFFFF"
        
        master.config(bg=self.bg_color)

        # Set ttk style for dark theme
        self.style = ttk.Style()
        self.style.configure("TButton", background=self.button_bg_color, foreground=self.button_fg_color)
        self.style.configure("TCheckbutton", background=self.checkbutton_bg_color, foreground=self.checkbutton_fg_color)
        self.style.configure("TLabel", background=self.bg_color, foreground=self.fg_color)
        self.style.configure("TEntry", background=self.entry_bg_color, foreground=self.entry_fg_color)

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

        # JSON File Label and Entry
        self.json_label = ttk.Label(master, text="JSON File:")
        self.json_label.grid(row=9, column=0, padx=5, pady=5, sticky="w")
        self.json_entry = ttk.Entry(master, width=50)
        self.json_entry.grid(row=9, column=1, columnspan=2, padx=5, pady=5)

        # Add a checkbox for selecting output file option
        self.output_checkbox_var = tk.BooleanVar(value=True)  # Default to True, meaning use file
        self.output_checkbox = ttk.Checkbutton(master, text="Save to file", variable=self.output_checkbox_var)
        self.output_checkbox.grid(row=10, column=0, columnspan=3, padx=5, pady=5, sticky="w")

        # Add a button for selecting the folder to output the results
        self.folder_button = ttk.Button(master, text="Select Output Folder", command=self.select_folder)
        self.folder_button.grid(row=11, column=0, columnspan=3, padx=5, pady=5, sticky="nsew")

        # Label to display the selected folder
        self.folder_label = ttk.Label(master, text="No folder selected")
        self.folder_label.grid(row=12, column=0, columnspan=3, padx=5, pady=5, sticky="w")

        # Output File Selection Button
        self.output_button = ttk.Button(master, text="Select Output File", command=self.select_output)
        self.output_button.grid(row=13, column=0, columnspan=3, padx=5, pady=5, sticky="nsew")

        self.output_label = ttk.Label(master, text="No file selected")
        self.output_label.grid(row=14, column=0, columnspan=3, padx=5, pady=5, sticky="w")

        # Save/Load buttons (Moved down to row 15 and 16 to avoid overlap)
        self.save_button = ttk.Button(master, text="Save Settings", command=self.save_settings)
        self.save_button.grid(row=15, column=0, padx=5, pady=5, sticky="nsew")

        self.load_button = ttk.Button(master, text="Load Settings", command=self.load_settings)
        self.load_button.grid(row=15, column=1, padx=5, pady=5, sticky="nsew")

        # Search button
        self.search_button = ttk.Button(master, text="Search", command=self.run_search)
        self.search_button.grid(row=16, column=0, columnspan=3, pady=10, sticky="nsew")

        # Stop button
        self.stop_button = ttk.Button(master, text="Stop Search", command=self.stop_search, state=tk.DISABLED)
        self.stop_button.grid(row=17, column=0, columnspan=3, pady=5, sticky="nsew")

        # Results display
        self.results_text = scrolledtext.ScrolledText(master, height=10, width=80, bg="#3C3C3C", fg="#FFFFFF")
        self.results_text.grid(row=18, column=0, columnspan=3, padx=5, pady=5)

        # Grid Configuration for Centering
        master.grid_rowconfigure(10, weight=1)  # Center output section
        master.grid_rowconfigure(11, weight=1)  # Center output label
        master.grid_rowconfigure(12, weight=1)  # Center folder selection
        master.grid_rowconfigure(13, weight=1)  # Center output file button
        master.grid_rowconfigure(14, weight=1)  # Center output file label
        master.grid_rowconfigure(15, weight=1)  # Center save/load buttons
        master.grid_rowconfigure(16, weight=1)  # Center search button
        master.grid_rowconfigure(17, weight=1)  # Center stop button
        master.grid_rowconfigure(18, weight=1)  # Center results text area

        master.grid_columnconfigure(0, weight=1)  # Ensure the columns are flexible for centering
        master.grid_columnconfigure(1, weight=1)
        master.grid_columnconfigure(2, weight=1)

    # Folder Selection Function
    def select_folder(self):
        # Open the folder selection dialog
        folder = filedialog.askdirectory()
        
        if folder:  # If the user selected a folder
            self.folder_label.config(text=folder)
        else:  # If the user canceled the folder selection
            self.folder_label.config(text="No folder selected")

    def select_output(self):
        # Open the file selection dialog
        filename = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON Files", "*.json")])
        
        if filename:  # If the user selected a file
            self.output_label.config(text=filename)
        else:  # If the user canceled the file selection
            self.output_label.config(text="No file selected")

    def save_settings(self):
        settings = {
            "username": self.username_entry.get(),
            "verbose": self.verbose_var.get(),
            "csv": self.csv_var.get(),
            "xlsx": self.xlsx_var.get(),
            "tor": self.tor_var.get(),
            "unique_tor": self.unique_tor_var.get(),
            "dump_response": self.dump_response_var.get(),
            "no_txt": self.no_txt_var.get(),
            "nsfw": self.nsfw_var.get(),
            "print_all": self.print_all_var.get(),
            "print_found": self.print_found_var.get(),
            "browse": self.browse_var.get(),
            "local": self.local_var.get(),
            "timeout": self.timeout_entry.get(),
            "site": self.site_entry.get(),
            "proxy": self.proxy_entry.get(),
            "json_file": self.json_entry.get(),
            "output_file": self.output_label.cget("text")
        }

        settings_file = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON Files", "*.json")])
        if settings_file:
            with open(settings_file, "w") as f:
                json.dump(settings, f, indent=4)

    def load_settings(self):
        settings_file = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
        if settings_file:
            with open(settings_file, "r") as f:
                settings = json.load(f)
                self.username_entry.delete(0, tk.END)
                self.username_entry.insert(0, settings.get("username", ""))  # Default to empty string if not found
                self.verbose_var.set(settings.get("verbose", False))
                self.csv_var.set(settings.get("csv", False))
                self.xlsx_var.set(settings.get("xlsx", False))
                self.tor_var.set(settings.get("tor", False))
                self.unique_tor_var.set(settings.get("unique_tor", False))
                self.dump_response_var.set(settings.get("dump_response", False))
                self.no_txt_var.set(settings.get("no_txt", False))
                self.nsfw_var.set(settings.get("nsfw", False))
                self.print_all_var.set(settings.get("print_all", False))
                self.print_found_var.set(settings.get("print_found", False))
                self.browse_var.set(settings.get("browse", False))
                self.local_var.set(settings.get("local", False))
                self.timeout_entry.delete(0, tk.END)
                self.timeout_entry.insert(0, settings.get("timeout", "60"))
                self.site_entry.delete(0, tk.END)
                self.site_entry.insert(0, settings.get("site", ""))
                self.proxy_entry.delete(0, tk.END)
                self.proxy_entry.insert(0, settings.get("proxy", ""))
                self.json_entry.delete(0, tk.END)
                self.json_entry.insert(0, settings.get("json_file", ""))
                self.output_label.config(text=settings.get("output_file", "No file selected"))


    def run_search(self):
        username = self.username_entry.get()
        if not username:
            self.results_text.insert(tk.END, "Please enter a username.\n")
            return

        self.results_text.delete('1.0', tk.END)
        self.results_text.insert(tk.END, f"Searching for username(s): {username}\n\n")

        self.stop_button.config(state=tk.NORMAL)  # Enable stop button

        # Start the Sherlock search in a separate thread
        thread = threading.Thread(target=self.sherlock_search, args=(username,))
        thread.start()

    def sherlock_search(self, username):
        try:
            # Split the input username(s) by spaces to handle multiple usernames
            usernames = username.split()  # Splits the input string into a list of usernames

            # Start with the base Sherlock command
            command = ['sherlock'] + usernames  # Add usernames to the command

            # Add additional flags based on user input
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
            if self.browse_var.get():
                command.append('--browse')
            if self.local_var.get():
                command.append('--local')

            # Timeout
            timeout = self.timeout_entry.get()
            if timeout:
                command.extend(['--timeout', timeout])

            # Site
            site = self.site_entry.get()
            if site:
                command.extend(['--site', site])

            # Proxy
            proxy = self.proxy_entry.get()
            if proxy:
                command.extend(['--proxy', proxy])

            # JSON file
            json_file = self.json_entry.get()
            if json_file:
                command.extend(['--json', json_file])

            # Output file selection
            if self.output_checkbox_var.get():
                output_file = self.output_label.cget("text")
                if output_file != "No file selected":
                    command.extend(['--output', output_file])

            # Folder output selection
            folder = self.folder_label.cget("text")
            if folder and folder != "No folder selected":
                command.extend(['--folderoutput', folder])

            # Run the command
            self.process = subprocess.Popen(command, 
                                            stdout=subprocess.PIPE, 
                                            stderr=subprocess.PIPE,
                                            text=True)

            # Monitor process stdout
            for line in self.process.stdout:
                self.results_text.insert(tk.END, line)
                self.results_text.see(tk.END)
                self.results_text.update()

            # Wait for process to complete
            self.process.wait()

            # Check for errors
            if self.process.returncode != 0:
                error_output = self.process.stderr.read()
                self.results_text.insert(tk.END, f"Error: {error_output}\n")

            self.results_text.insert(tk.END, "\nSearch completed.\n")
            
            # After process finishes, disable the stop button
            self.master.after(0, self.stop_button.config, {'state': tk.DISABLED})

        except Exception as e:
            self.results_text.insert(tk.END, f"An error occurred: {str(e)}\n")

    def stop_search(self):
        if self.process:
            # Check if the process is still running
            if self.process.poll() is None:  # None means the process is still running
                self.process.terminate()
                self.results_text.insert(tk.END, "\nSearch stopped.\n")
                self.stop_button.config(state=tk.DISABLED)
            else:
                # If the process is not running (finished), disable the Stop button
                self.stop_button.config(state=tk.DISABLED)
        else:
            # If no process is active, disable the Stop button
            self.stop_button.config(state=tk.DISABLED)


root = tk.Tk()
gui = SherlockGUI(root)
root.mainloop()
