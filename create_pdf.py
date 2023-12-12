import weasyprint
import os

# Define the HTML content
html_content = """


"""


def main():
    # Specify the output file path (desktop in this example)

    home_path = os.getenv("HOMEPATH") or os.getenv("HOME")
    if not home_path:
        return
    output_pdf_path = f"{home_path}/Desktop/analysis.pdf"

    # Generate the PDF
    weasyprint.HTML(string=html_content).write_pdf(output_pdf_path)

    print(f"PDF created and saved at {output_pdf_path}")


if __name__ == "__main__":
    main()
