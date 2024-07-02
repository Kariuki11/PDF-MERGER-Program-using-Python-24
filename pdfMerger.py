import PyPDF2
import os

# Create a PdfMerger object
merger = PyPDF2.PdfMerger()

# Specify the folder containing the PDF files
pdf_folder = r'C:\Users\Administrator\Desktop\PDF MERGER\pdf folders'

# List of specific PDF files to merge
pdf_files = [
    "PCEA UMBUI YOUTH FELLOWSHIP.pdf",
    "Gloxad Academy road map.pdf"
]

# Loop through the list of PDF files and append each to the merger
for pdf_file in pdf_files:
    file_path = os.path.join(pdf_folder, pdf_file)
    merger.append(file_path)

# Write the merged PDF to a new file
merger.write("combinedBSUniDocs.pdf")
merger.close()
