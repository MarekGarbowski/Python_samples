
from PyPDF2 import PdfFileReader, PdfFileWriter


def page_rotate(path):
    pdf_writer = PdfFileWriter()
    pdf_reader = PdfFileReader(path)
    # rotate 90 degree right
    page1 = pdf_reader.getPage(0).rotateClockwise(90)
    pdf_writer.addPage(page1)
    # rotate 90 degree left
    page2 = pdf_reader.getPage(1).rotateCounterClockwise(90)
    pdf_writer.addPage(page2)
    # add page in normal orientation
    pdf_writer.addPage(pdf_reader.getPage(2))

    with open('rotate_page.pdf', 'wb') as file:
        pdf_writer.write(file)


if __name__ == '__main__':
    file = 'Jak porządnie opisać znaleziony błąd.pdf'
    page_rotate(file)
