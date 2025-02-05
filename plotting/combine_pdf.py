import os
from PyPDF2 import PdfMerger

def combine_pdfs(input_directory, output_filename):
    """
    Combines multiple PDF files in the input directory into a single PDF file.
    The files are sorted by the numeric part of their names.

    Args:
        input_directory (str): The directory containing the PDF files to combine.
        output_filename (str): The path for the combined PDF file.
    """
    # List all PDF files in the directory
    pdf_files = [f for f in os.listdir(input_directory) if f.endswith('.pdf') and not f.startswith('combined') and not f.startswith('pso_explanation')]

    # Sort files based on the numeric part of the filename
    pdf_files.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))

    # Create a PdfMerger instance
    merger = PdfMerger()

    # Add each PDF to the merger
    for pdf in pdf_files:
        pdf_path = os.path.join(input_directory, pdf)
        merger.append(pdf_path)

    # Write out the combined PDF
    merger.write(output_filename)
    merger.close()
    print(f"Combined PDF saved to {output_filename}")

# Example usage
#input_dir = "./plots/intro"  # Directory containing the PDF files
input_dir = "../plots/intro"  # Directory containing the PDF files
#input_dir = "./plots/intro"  # Directory containing the PDF files
output_file = input_dir + "/combined.pdf"  # Path for the output combined PDF
combine_pdfs(input_dir, output_file)
