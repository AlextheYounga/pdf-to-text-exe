import tkinter as tk
from tkinter import filedialog
from PyPDF2 import PdfReader
import subprocess as sp
from time import sleep
from os import name as os_name, path
from pathlib import Path



def open_file_explorer():
    # Create a Tkinter root window
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Show the file dialog to select a PDF file
    file_path = filedialog.askopenfilename(
        filetypes=[("PDF files", "*.pdf")],
        title="Select a PDF file"
    )

    # Check if a file was selected
    if file_path:
        print(f"Selected file: {file_path}")
        return file_path
        
    else:
        print("No file selected.")


def process_pdf(file_path):
    # This is a placeholder function to show where you can process the PDF file
    # You can add your PDF processing code here
    print(f"Processing file: {file_path}")
    reader = PdfReader(file_path)
    page_text = []

    for page in reader.pages:
        page_text.append(page.extract_text())

    page_text = '\n'.join(page_text)

    return page_text
    


def write_text_to_file(page_text):
    # This is a placeholder function to show how you can write the text to a file
    # You can add your file writing code here
    file_path = path.join(Path.home(), "Documents", "pdf_extracted.txt")

    with open(file_path, "w") as file:
        file.write(page_text)
        file.close()
    sleep(1)

    print(f"Text written to file: {file_path}")
    return file_path


def open_in_text_editor(file_path):
    if 'posix' in os_name.lower():
        sp.call(['open', '-a', 'TextEdit', file_path])
    elif 'nt' in os_name.lower(): 
        sp.Popen(["notepad.exe", file_path])
    else: 
        print("Unsupported OS. File saved to: ", file_path)



if __name__ == "__main__":
    file_path = open_file_explorer()
    page_text = process_pdf(file_path)
    txt_file_path = write_text_to_file(page_text)
    open_in_text_editor(txt_file_path)
