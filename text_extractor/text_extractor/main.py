import hugging_face

import process_pdf


def main():
    file_patch = process_pdf.extract_pdf_to_img()
    # hugging_face.extract_img(file_patch)


if __name__ == "__main__":
    print("run main")
    main()


# imgCV = cv2.imread(IMG_PROCCESS)
# if imgCV is None:
#     print("not conver")
# img_gray = cv2.cvtColor(imgCV, cv2.COLOR_BGR2GRAY)
# # denoise
# blur = cv2.medianBlur(img_gray, 3)

# page_text = pytesseract.image_to_string(blur)
# print(page_text)
