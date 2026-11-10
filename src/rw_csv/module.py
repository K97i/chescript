"""
DO NOT MODIFY!

You may have entered in here by mistake. Please go to the ./src/features folder!
"""

import tkinter as tk
from tkinter import filedialog
from ..classes import Feature, Entry
import csv

def load() -> list[Entry]:
    """
    Loads the user-selected CSV

    Returns:
        entry_list (list[Entry]): The list of the words in the CSV
    """
    entry_list = []

    # Ask for input CSV file
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title="Open CSV", filetypes=[("CSV file", "*.csv")])

    # If selected...
    if file_path:
        # Read file
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            # Create Entry object for every word
            for row in reader:
                entry_list.append(Entry.from_dict(row))

        # Return the list
        return entry_list

def save(data: list[Entry]):
    """
    Exports the final CSV containing the features

    Args:
        data (list[Entry]): The final list of entries with the calculated features
    """
    if not data:
        return

    # Ask for save location
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV file", "*.csv")])

    # If selected...
    if file_path:
        # Create headers for CSV, combine initial with features 
        field_names = [ "word_id", "sentence_id", "word", "label", ] + [ feature.name for feature in data[0].features ]
        
        # Open file for writing
        with open(file_path, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=field_names)
            writer.writeheader()
            
            # Create rows
            rows = [entry.to_dict() for entry in data]
            writer.writerows(rows)