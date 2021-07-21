# !/usr/bin/python

import argparse
import PyPDF2


def get_cmdline_args():
    parser = argparse.ArgumentParser(
        description='Stamp all pages of a PDF with a watermark or logo image provided as a separate PDF page')
    parser.add_argument('input_path', metavar='input',
                        help='The main PDF to receive the stamp')
    parser.add_argument('watermark_file_path', metavar='watermark',
                        help='A single-page PDF with the watermark or logo to be stamped onto the main PDF')
    parser.add_argument('output_path', metavar='output',
                        help='File to write the result')

    return parser.parse_args()


if __name__ == '__main__':
    args = get_cmdline_args()

    with open(args.input_path, "rb") as input:
        pdf = PyPDF2.PdfFileReader(input)

        with open(args.watermark_file_path, "rb") as watermark_file:
            watermark = PyPDF2.PdfFileReader(watermark_file)

            watermark_page = watermark.getPage(0)

            pdf_writer = PyPDF2.PdfFileWriter()

            for i in range(0, pdf.getNumPages()):
                page = pdf.getPage(i)
                page.mergePage(watermark_page)
                pdf_writer.addPage(page)

            with open(args.output_path, "wb") as output:
                pdf_writer.write(output)
