
# **No Shit Sherlock**

![image](https://github.com/user-attachments/assets/36166a26-d3d9-4519-a4fb-145bb32cde47)

**No Shit Sherlock** provides a user-friendly graphical interface for the powerful **Sherlock** Python tool, which searches for social media accounts associated with a specific username across multiple platforms. This GUI tool enables users to perform these searches without requiring the use of the command line.

## **Features**

### **1. Username Search**
- **Input One or More Usernames**: Enter the username(s) you want to search for. The GUI will check the availability of these usernames across various social media sites, using a similar approach to the command line, where wildcards like `{?}` can be used to check for similar usernames (e.g., replacing `{?}` with `_`, `-`, or `.`).

### **2. Output Options**
- **Verbose Output**: Enables detailed logs for the search process, similar to `--verbose`, `-v`, or `-d` in the command line.
- **CSV Output**: Saves the search results in CSV format, just like the `--csv` option in Sherlock.
- **XLSX Output**: Saves the results in Excel-friendly format (`.xlsx`).
- **Dump Response**: Dumps the HTTP response to stdout for debugging purposes, equivalent to the `--dump-response` flag.
- **No TXT File**: Skips generating a `.txt` file for results (`--no-txt`).
- **NSFW Content**: Includes results from NSFW sites, as enabled by the `--nsfw` option.
- **Print All Sites**: Displays results for all sites, including those where the username was not found (`--print-all`).
- **Print Found Sites**: Shows only the sites where the username is found (`--print-found`).

### **3. Proxy and Network Options**
- **Use Tor**: Runs the search through the Tor network for anonymity (`--tor`, `-t`).
- **Unique Tor**: Uses a new Tor circuit for each request to avoid detection (`--unique-tor`, `-u`).
- **Proxy URL**: Allows configuration of a custom proxy server (`--proxy PROXY_URL`).

**DISCLAIMER**

Tor options will be deprecated from the main branch.

### **4. File and Folder Selection**
- **Select Output Folder**: Choose where to save the results if searching for multiple usernames, similar to the `--folderoutput` option (`-fo`).
- **Select Output File**: Choose the file name for saving results, compatible with JSON output (`--output` for single username or `--json JSON_FILE`).

### **5. Advanced Search Settings**
- **Timeout**: Set a timeout for requests (in seconds), equivalent to the `--timeout TIMEOUT` option.
- **Site**: Restrict the search to a specific site or a list of sites (`--site SITE_NAME`).
- **Local Data**: Use local data sources for the search rather than querying external sites (`--local`).

### **6. Save and Load Settings**
- **Save Settings**: Save your current configuration to a JSON file, making it easy to reload the same settings later.
- **Load Settings**: Load previously saved configurations from a JSON file for quick reuse.

### **7. Search Execution**
- **Start Search**: Initiates the search with the current settings. The search process is run in a separate thread, ensuring the GUI remains responsive.
- **Stop Search**: Allows you to stop the search mid-process.

### **8. Real-Time Results Display**
- The results of the search are displayed in a scrollable text area, showing each site checked and whether the username was found. Errors and completion messages will also appear here.

## **Usage Workflow**

1. **Input Data**: Enter one or more usernames into the GUI.
2. **Set Search Parameters**: Configure additional settings (e.g., output format, timeout, proxy, etc.).
3. **Select Output**: Choose where and in which format to save the results.
4. **Start Search**: Click "Start Search" to begin the process.
5. **View Results**: Monitor the search progress in the real-time results area.
6. **Stop Search**: If necessary, click "Stop Search" to halt the search at any time.

---

## **Requirements**

- **Sherlock Tool**: The Sherlock Python tool must be installed and accessible on your system.
- **Python 3**: The GUI is built in Python 3, requiring the `tkinter` module for the interface, `subprocess` for running Sherlock, and `threading` for handling search tasks in the background.

Ensure that these dependencies are installed and correctly configured to run the **Sherlock GUI Tool** seamlessly.

