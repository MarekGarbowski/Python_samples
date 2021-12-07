
from PyPDF2 import PdfFileReader


def ext_info(path_to_pdf):
    with open(path_to_pdf, 'rb') as file:
        pdf = PdfFileReader(file)
        information = pdf.getDocumentInfo()
        pages = pdf.getNumPages()

    info = f"""
    Information about: {path_to_pdf}
    -----------------
    Author: {information.author}
    Creator: {information.creator}
    Producer: {information.producer}
    Subject: {information.subject}
    Number of pages: {pages}"""

    print(info)
    return information


if __name__ == '__main__':
    path = 'Jak porządnie opisać znaleziony błąd.pdf'
    ext_info(path)

