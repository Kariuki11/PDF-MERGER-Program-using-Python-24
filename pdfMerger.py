import PyPDF2
import sys
import os

merger = PyPDF2.PdfFileMerger()

pdf_folder = 'C:/Users/Administrator/Desktop/PDF MERGER/pdf folders'

for file in os.listdir(os.curdir):
    if file.endswith(".pdf"):
        merger.append(file)
    merger.write("combinedBSUniDocs.pdf")

import PyPDF2
import os

# Create a PdfFileMerger object
merger = PyPDF2.PdfFileMerger()

# Specify the folder containing the PDF files
pdf_folder = 'C:/Users/Administrator/Desktop/PDF MERGER/pdf folders'

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
