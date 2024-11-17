# Sherlock GUI Tool

![image](https://github.com/user-attachments/assets/cd642f89-8a31-4be7-af8f-a63ed906a59c)

The **Sherlock GUI** is a graphical user interface (GUI) designed for interacting with the **Sherlock** Python tool, which is used to search for social media accounts associated with a specific username. This GUI provides a more user-friendly way to configure and execute Sherlock searches without needing to use the command line.

## Features

1. **Username Search**  
   - Allows users to input one or more usernames to search across various social media platforms for account matches.

2. **Output Options**
   - **Verbose Output**: Enables detailed logging of the search process.
   - **CSV Output**: Saves results in a CSV format.
   - **XLSX Output**: Saves results in an Excel (XLSX) format.
   - **Dump Response**: Saves the raw response from the search.
   - **No TXT File**: Skips generating a `.txt` output file for results.
   - **NSFW Content**: Includes NSFW (Not Safe For Work) sites in the search.
   - **Print All Sites**: Displays all the sites that Sherlock checks, not just the found matches.
   - **Print Found Sites**: Displays only the sites where the username is found.

3. **Proxy and Network Options**
   - **Use Tor**: Runs the search through the Tor network for anonymity.
   - **Unique Tor**: Uses a different Tor circuit for each request to avoid detection.
   - **Proxy URL**: Option to configure a custom proxy server.

4. **File and Folder Selection**
   - **Select Output Folder**: Allows the user to choose a folder where the results will be saved.
   - **Select Output File**: Allows the user to specify a file for saving results (in JSON format).

5. **Advanced Search Settings**
   - **Timeout**: Sets a timeout (in seconds) for the search.
   - **Site**: Option to restrict the search to a specific site.
   - **Local Data**: Uses local data sources for the search rather than querying external websites.
   - **JSON File**: Option to specify a pre-existing JSON file for input.

6. **Save and Load Settings**
   - **Save Settings**: Saves the current configuration to a JSON file for later use.
   - **Load Settings**: Loads a saved configuration from a JSON file.

7. **Search Execution**
   - **Start Search**: Initiates the search with the current settings and displays results in real-time.
   - **Stop Search**: Allows the user to stop the search mid-process.

8. **Real-Time Results Display**
   - The results of the search are displayed in a scrollable text area, with each site checked being printed to the GUI. Errors and completion messages are also shown here.

## GUI Layout

- **Username Input**: Text entry field for entering the username(s) to search for.
- **Option Checkboxes**: Multiple checkboxes for controlling the behavior of the search (verbose, output format, etc.).
- **Timeout and Site Input**: Fields to configure timeout and restrict the search to a specific site.
- **Proxy and JSON File Input**: Fields for entering proxy URL and JSON file for input data.
- **Folder and Output File Selection**: Buttons for selecting the output folder and output file.
- **Save/Load Settings**: Buttons to save and load search settings.
- **Search and Stop Buttons**: Buttons to start and stop the search.

## Workflow

1. **Input Data**: The user enters the username(s) they want to search for, and optionally, sets the search parameters (output format, proxy, etc.).
2. **Select Output**: The user selects where to save the results (folder and file).
3. **Start Search**: The user clicks "Search", and the program begins searching using the Sherlock tool. The search is executed in a separate thread to keep the GUI responsive.
4. **View Results**: As the search progresses, results are displayed in a scrollable text area.
5. **Stop Search**: If needed, the user can stop the search by clicking the "Stop Search" button.

## Requirements

- **Sherlock Tool**: [The Sherlock Python tool must be installed and available on the system](https://sherlockproject.xyz/installation).
- **Python 3**: The program is written in Python 3 and requires the `tkinter` module for the GUI, `subprocess` for running the Sherlock tool, and `threading` for background execution. Should work as this is built in python WOMM.
