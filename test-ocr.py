from pdf2image import convert_from_path

import os

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract


pages = convert_from_path("test.pdf",500)
compte = 1
for page in pages:
    myfile = 'image' + str(compte) + '.jpg'
    compte = compte + 1
    page.save(myfile, "JPEG")

print(pytesseract.image_to_string(Image.open("image2.jpg"), lang='fra'))

'''pdf = pytesseract.image_to_pdf_or_hocr("image1.jpg", extension='pdf')

os.startfile(pdf)'''
