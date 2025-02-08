import os
from plotting import defines
from PyPDF2 import PdfMerger

def combine_pdfs(input_directory, output_filename):
    """
    Combines multiple PDF files in the input directory into a single PDF file.
    The files are sorted by the numeric part of their names.

    Args:
        input_directory (str): The directory containing the PDF files to combine.
        output_filename (str): The path for the combined PDF file.
    """
    pdf_files = [f for f in os.listdir(input_directory) if f.endswith('.pdf') and not f.startswith('combined')]
    pdf_files.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))

    merger = PdfMerger()

    for pdf in pdf_files:
        pdf_path = os.path.join(input_directory, pdf)
        merger.append(pdf_path)

    merger.write(output_filename)
    merger.close()


def combine(option: int) -> None:
    """
    Combines PDF files from a specific directory based on the given option.

    Args:
        option (int): An integer representing the directory option to combine PDFs from.
                      - defines.INTRO: Combine PDFs from the intro directory.
                      - defines.SWARM: Combine PDFs from the swarm directory.

    Raises:
        ValueError: If the option is not valid.
    """
    if option == defines.INTRO:
        input_dir = "plots/intro"
    elif option == defines.SWARM:
        input_dir = "plots/swarm"
    else:
        raise ValueError

    output_file = input_dir + "/combined.pdf"  # Path for the output combined PDF
    combine_pdfs(input_dir, output_file)
