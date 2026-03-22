import pdfplumber
import pytesseract
from PIL import Image
import fitz
import cv2

FILE_PATCH = "text_extractor/test_scan.pdf"
IMG_PROCCESS = "text_extractorccd.jpg"
# with pdfplumber.open("text_extractor/test_scan.pdf") as pdf:
#     first_page = pdf.pages[0]
#     content = first_page.extract_text()
#     if content is None or content.strip() == "":
#         print("ok")
#     # with open("text_extractor/content.txt", "w") as file:
#     #     file.write(content)
#     pdf.close()
doc = fitz.open(FILE_PATCH)
text = ""
page = doc[0]
pix = page.get_pixmap()
img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
img.save(IMG_PROCCESS)

imgCV = cv2.imread(IMG_PROCCESS)
if imgCV is None:
    print("not conver")
img_gray = cv2.cvtColor(imgCV, cv2.COLOR_BGR2GRAY)
# denoise
blur = cv2.medianBlur(img_gray, 3)

page_text = pytesseract.image_to_string(blur)
print(page_text)
