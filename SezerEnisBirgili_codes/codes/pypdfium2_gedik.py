# coding: utf8
import pypdfium2 as pdfium
import os

order = 1
pdfs = []
for filename in os.listdir("data/gedik_PDF/"):
    pdf_dict = {}

    pdf = pdfium.PdfDocument(r"C:\Users\TKA\PycharmProjects\cs210proj\data\gedik_PDF\{}".format(filename))
    page = pdf[0] # which page
    textpage = page.get_textpage()

    width, height = page.get_size()

    text_all = textpage.get_text_range()

    text_all = text_all.replace("\u25cf", "###")
    text_all = text_all.replace('\ufffe', "-")
    text_all = text_all.replace("\r\n", " ")
    text_final = text_all[text_all.find("BIST-100 Strateji")+len("BIST-100 Strateji"): text_all.find('Önemli Sektör Şirket Haberleri')]
    print(filename)

    akbank, date, monthsAgo, count = filename[:-4].split("_")

    pdf_dict["date"] = date
    pdf_dict["monthAgo"] = monthsAgo
    pdf_dict["count"] = count
    pdf_dict["paragraph"] = text_final

    print("dict created", order)
    pdfs.append(pdf_dict)
    order = order + 1

print(pdfs)

with open ("data/pdf_dicts.txt", "a") as f:
    f.write(str(pdfs))