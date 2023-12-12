import weasyprint
import os
from pathlib import Path
import tkinter as tk
from tkinter import Text, Scrollbar, Button, Entry


def generate_pdf(html_content, output_pdf_path):
    # If the file already exists, add a suffix to the name
    pdf_path = Path(output_pdf_path)
    pdf_name = pdf_path.stem  # Get the filename without extension
    pdf_dir = pdf_path.parent
    pdf_extension = pdf_path.suffix

    count = 1
    while pdf_path.exists():
        pdf_name = f"{pdf_name}_{count}"
        pdf_path = pdf_dir / f"{pdf_name}{pdf_extension}"
        count += 1

    # Generate the PDF
    weasyprint.HTML(string=html_content).write_pdf(pdf_path)

    print(f"PDF created and saved at {pdf_path}")


def generate_pdf_gui(html_content, output_pdf_path_var):
    # Create a Tkinter window for the GUI
    root = tk.Tk()

    # Create a StringVar for output PDF path
    output_pdf_path_var = tk.StringVar()

    # Function to generate the PDF
    def generate_pdf_from_gui():
        html_content = html_text.get("1.0", tk.END)
        generate_pdf(html_content, output_pdf_path_var.get())
        root.quit()  # Close the GUI window after PDF generation

    # Create a Text widget for entering HTML content
    html_text = Text(root, wrap=tk.WORD, width=60, height=15)
    html_text.pack(padx=10, pady=10)
    html_text.insert(tk.END, html_content)  # Pre-fill the Text widget

    # Create a scrollbar for the Text widget
    scrollbar = Scrollbar(root, command=html_text.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    html_text.config(yscrollcommand=scrollbar.set)

    # Create an entry widget for specifying the output PDF path
    output_pdf_entry = Entry(root, textvariable=output_pdf_path_var, width=50)
    output_pdf_entry.pack(pady=10)

    # Pre-fill the path
    home_path = Path.home().as_posix()
    output_pdf_path_var.set(f"{home_path}/Desktop/analysis.pdf")

    # Create a button to generate the PDF
    generate_button = Button(root, text="Generate PDF", command=generate_pdf_from_gui)
    generate_button.pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    generate_pdf_gui("", "")
