from PyPDF2 import PdfWriter
import os

path = "/home/rajesh/Documents/Python/cluter"
merger = PdfWriter()
files = [file for file in os.listdir(path) if file.endswith(".pdf")]

for pdf in files:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()