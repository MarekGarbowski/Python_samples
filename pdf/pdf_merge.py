
from PyPDF2 import PdfFileReader, PdfFileWriter


def pdf_merge(paths, output):
    pdf_writer = PdfFileWriter()

    for path in paths:
        pdf_reader = PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page))

    with open(output, 'wb') as out:
        pdf_writer.write(out)


if __name__ == '__main__':
    paths = ['Jak porządnie opisać znaleziony błąd.pdf', 'rotate_page.pdf']
    pdf_merge(paths, output='merged.pdf')
