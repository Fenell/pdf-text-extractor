import pdfplumber
import pytesseract
from PIL import Image
import fitz
from pathlib import Path

FILE_TEST = "hd.pdf"
BASE_DIR = Path(__file__).resolve().parent.parent
IMG_PROCCESS = f"{BASE_DIR}/tests/outputs/img_pdf.jpg"


def get_path_file_test():
    file_patch = f"{BASE_DIR}/tests/inputs/{FILE_TEST}"
    # print(file_patch)
    return file_patch


def get_output_path():
    return f"{BASE_DIR}/tests/outputs/content_extract.txt"


def extract_pdf_to_img():
    file_patch = get_path_file_test()
    doc = fitz.open(file_patch)
    page = doc[0]
    pix = page.get_pixmap()
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    img.save(IMG_PROCCESS)

    return IMG_PROCCESS


def extract_pdf_to_text():
    file_patch = get_path_file_test()

    with pdfplumber.open(file_patch) as pdf:
        first_page = pdf.pages[0]
        content = first_page.extract_text()
        if content is None or content.strip() == "":
            print("extract img")
            return extract_pdf_to_img()
        else:
            path_output = get_output_path()
            with open(path_output, "w") as file:
                file.write(content)
            print("Extract done.")

        pdf.close()
