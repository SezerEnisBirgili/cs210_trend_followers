import requests

LINK_LIST_PATH = "data/link_list.txt"
PDF_LIST_PATH  = "data/gedik_PDF/"
FAIL_PATH      = "data/failed_links.txt"

with open(LINK_LIST_PATH, "r") as f:

    list_content = f.readlines()
    list_content.pop(0)

    list_content = [x.split("\t") for x in list_content]

    date_list  = [x[0] for x in list_content]
    url_list = [x[1] for x in list_content]
    page_list = [x[2].strip() for x in list_content]

    # print(page_list)
    # print(date_list)
    # print(url_list)


headers = requests.utils.default_headers()

headers.update(
    {
        'User-Agent': 'My User Agent 1.0',
    }
)

count = 1

for date, url, page in zip(date_list, url_list, page_list):

    response = requests.get(url, headers=headers)

    pdf_path = "{}gedik_{}_{}_{}.pdf".format(PDF_LIST_PATH, date, page, count)

    try:
        with open(pdf_path, 'xb') as f:

            try:

                f.write(response.content)
                print(pdf_path)
            except:

                print("no download for ", pdf_path)
                with open(FAIL_PATH, 'a') as fail:
                    fail.write(pdf_path+"\n")
    except FileExistsError:
        print("same file")

    count = count+1

print("Done")