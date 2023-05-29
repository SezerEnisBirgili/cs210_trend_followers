import pypdfium2 as pdfium
import os

order = 1
pdfs = []
for filename in os.listdir("data/akbank_PDF/"):

    pdf_dict = {}

    pdf = pdfium.PdfDocument(r"C:\Users\TKA\PycharmProjects\cs210proj\data\akbank_PDF\{}".format(filename))
    page = pdf[1]
    textpage = page.get_textpage()

    width, height = page.get_size()

    text_all = textpage.get_text_range()

    text_all = text_all.replace("\u25cf", "###")
    text_all = text_all.replace('\ufffe', "-")
    text_all = text_all.replace("\r\n", " ")
    text_final = text_all[text_all.find("###")+4: text_all.find("###", text_all.find("###")+1)]
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