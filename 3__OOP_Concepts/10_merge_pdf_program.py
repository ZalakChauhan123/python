# Imports the PdfWriter class from the pypdf library
from pypdf import PdfWriter

# Creates a new PdfWriter object called merger. This object will be used to combine multiple PDFs.
merger = PdfWriter()

for pdf in ["F:\python\OOP_Concepts\pdf-1.pdf" , "F:\python\OOP_Concepts\pdf-2.pdf"]:
    merger.append(pdf)

# Writes the combined PDF pages into a new file name
merger.write("merged_pdf.pdf")

# close merger object
merger.close()
