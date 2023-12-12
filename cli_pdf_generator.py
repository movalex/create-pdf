import weasyprint
import argparse
from pathlib import Path


def generate_pdf(html_content, output_pdf_path):
    if not html_content:
        print("HTML content is empty. Please provide HTML content.")
        return

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


def main():
    parser = argparse.ArgumentParser(description="Generate PDF from HTML content")
    parser.add_argument("--output", help="Specify the output PDF file path")

    args = parser.parse_args()

    if args.output:
        # Command-line mode
        html_content = input("Enter the HTML content:\n")
        generate_pdf(html_content, args.output)
    else:
        print("Please specify an output PDF file path using the --output argument.")


if __name__ == "__main__":
    main()
