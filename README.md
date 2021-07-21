# pystamp
Python command line tool to stamp PDF files.

# Requirements
To run this script you need python3 and PyPDF2 installed. In linux you can install those with:

```bash
sudo apt-get install python3 python3-pip
pip3 install PyPDF2
```

# Usage
```
usage: pystamp.py [-h] [-o output] input watermark

Stamp all pages of a PDF with a watermark or logo image provided as a separate PDF page

positional arguments:
  input                 The main PDF to receive the stamp
  watermark             A single-page PDF with the watermark or logo to be stamped onto the main PDF

optional arguments:
  -h, --help            show this help message and exit
  -o output, --output output
                        File to write the result, if not provided the default is output.pdf
```

This simple script adds a watermark or logo to all pages of an existing PDF using [PyPDF2](https://github.com/mstamy2/PyPDF2). The tool merges the watermark page with each of the pages in the main PDF, so it can be used to add watermarks, logos, frames, etc.
