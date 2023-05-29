from pypdf import PdfReader
import os






from pdf2image import convert_from_bytes
import pytesseract
import cv2
import numpy as np

pdfs = []
order = 1
for filename in os.listdir("data/akbank_PDF/"):

    pdf_dict = {}

    reader = PdfReader("data/akbank_PDF/{}".format("akbank_01.12.2021_18_358.pdf"))
    page = reader.pages[1]
    words = page.extract_text()

    akbank, date, monthsAgo, count = filename[:-4].split("_")
    words = words[words.find("●")+1:words.find("●", words.find("●")+1)]

    pdf_dict["date"]      = date
    pdf_dict["monthAgo"]  = monthsAgo
    pdf_dict["count"]     = count
    pdf_dict["paragraph"] = words

    print("dict created", order)
    pdfs.append(pdf_dict)
    order = order+1
    break


print(pdfs)

#with open ("data/pdf_dicts.txt", "a") as f:
 #   f.write(str(pdfs))








