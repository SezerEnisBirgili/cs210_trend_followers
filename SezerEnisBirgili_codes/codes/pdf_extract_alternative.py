from pdf2image import convert_from_bytes
import pytesseract
import cv2
import os
from pypdf import PdfReader

pdfs = []
order = 1

for filename in os.listdir("data/akbank_PDF/"):

    pdf_dict = {}

    images = convert_from_bytes(open("data/akbank_PDF/{}".format("akbank_01.12.2021_18_358.pdf"), 'rb').read(), dpi=400, first_page=2, last_page=2)

    for i, image in enumerate(images):
        fname = "image" + str(i) + ".png"
        image.save(fname, "PNG")

    img = cv2.imread("image0.png")
    crop = img[400:2000, 200:1500]

    #cv2.imshow("cropped", crop)
    cv2.imwrite("image0.png", crop)
    cv2.waitKey(0)

    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

    extracted_text = pytesseract.image_to_string("./image0.png", lang="tur")

    final_text = extracted_text[:extracted_text.find("Teknik Yorum:")]

    akbank, date, monthsAgo, count = filename[:-4].split("_")

    pdf_dict["date"] = date
    pdf_dict["monthAgo"] = monthsAgo
    pdf_dict["count"] = count
    pdf_dict["paragraph"] = final_text

    print("dict created", order)
    pdfs.append(pdf_dict)
    order = order + 1
    break

print(pdfs)

#with open ("data/pdf_dicts.txt", "a") as f:
 #   f.write(str(pdfs))