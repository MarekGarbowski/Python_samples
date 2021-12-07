
from PyPDF2 import PdfFileWriter, PdfFileReader


def add_encryption(inp_pdf, out_pdf, password):
    pdf_writer = PdfFileWriter()
    pdf_reader = PdfFileReader(inp_pdf)

    for page in range(pdf_reader.getNumPages()):
        pdf_writer.addPage(pdf_reader.getPage(page))

    pdf_writer.encrypt(user_pwd=password, owner_pwd=None, use_128bit=True)

    with open(out_pdf, 'wb') as file:
        pdf_writer.write(file)


if __name__ == '__main__':
    add_encryption(
        inp_pdf='Jak porządnie opisać znaleziony błąd.pdf',
        out_pdf='encrypted.pdf',
        password='*****'
    )
