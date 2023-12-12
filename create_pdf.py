import weasyprint
import os
import tkinter as tk
from tkinter import Text, Scrollbar, Button
import argparse


def generate_pdf(html_content, output_pdf_path):
    # Generate the PDF
    weasyprint.HTML(string=html_content).write_pdf(output_pdf_path)

    print(f"PDF created and saved at {output_pdf_path}")


def generate_pdf_gui(html_content):
    # Create a Tkinter window for the GUI
    root = tk.Tk()
    root.withdraw()
    root.title("HTML to PDF Converter")

    # Create a Text widget for entering HTML content
    html_text = Text(root, wrap=tk.WORD, width=60, height=15)
    html_text.pack(padx=10, pady=10)
    html_text.insert(tk.END, html_content)  # Pre-fill the Text widget

    # Create a scrollbar for the Text widget
    scrollbar = Scrollbar(root, command=html_text.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    html_text.config(yscrollcommand=scrollbar.set)

    # Create a button to generate the PDF
    def generate_pdf_from_gui():
        html_content = html_text.get("1.0", tk.END)
        generate_pdf(html_content, output_pdf_path.get())
        root.destroy()  # Close the GUI window after PDF generation

    generate_button = Button(root, text="Generate PDF", command=generate_pdf_from_gui)
    generate_button.pack(pady=10)

    root.mainloop()


def main():
    parser = argparse.ArgumentParser(description="Generate PDF from HTML content")
    parser.add_argument("--output", help="Specify the output PDF file path")

    args = parser.parse_args()

    if args.output:
        # Command-line mode
        html_content = input("Enter the HTML content:\n")
        generate_pdf(html_content, args.output)
    else:
        # GUI mode
        root = tk.Tk()
        generate_pdf_gui("")


if __name__ == "__main__":
    main()
