
from PyPDF2 import PdfFileWriter, PdfFileReader


def watermark_create(in_pdf, out_pdf, watermark):
    w_obj = PdfFileReader(watermark)
    w_page = w_obj.getPage(0)

    pdf_reader = PdfFileReader(in_pdf)
    pdf_writer = PdfFileWriter()

    for page in range(pdf_reader.getNumPages()):
        page = pdf_reader.getPage(page)
        page.mergePage(w_page)
        pdf_writer.addPage(page)

    with open(out_pdf, 'wb') as out:
        pdf_writer.write(out)


if __name__ == '__main__':
    watermark_create(
        in_pdf='files/Jak porządnie opisać znaleziony błąd.pdf',
        out_pdf='files/file_with_watermark.pdf',
        watermark='files/watermark.pdf'
    )
