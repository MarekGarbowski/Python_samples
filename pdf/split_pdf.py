
from PyPDF2 import PdfFileWriter, PdfFileReader


def split(path, split_name):
    pdf = PdfFileReader(path)

    for page in range(pdf.getNumPages()):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))

        output = f'{split_name}{page}.pdf'
        with open(output, 'wb') as out_pdf:
            pdf_writer.write(out_pdf)


if __name__ == '__main__':
    path = 'Jak porządnie opisać znaleziony błąd.pdf'
    split(path, 'testy')
