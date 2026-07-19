# Exercise 8- Merge the pdf
from pypdf import PdfReader, PdfWriter
import os 

os.chdir(r"D:\Code\100days challenge\data")


writer = PdfWriter()

# Add all PDF files in the folder
for file in os.listdir():
    if file.endswith(".pdf"):
        reader = PdfReader(file)

        for page in reader.pages:
            writer.add_page(page)

# Save the merged PDF
with open("merged.pdf", "wb") as output:
    writer.write(output)

print("PDFs merged successfully!")
