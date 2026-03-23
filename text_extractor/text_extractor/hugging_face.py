import requests
import process_pdf as pp

url = "https://c3be-35-227-171-9.ngrok-free.app/ocr"
# file_path = "text_extractor/ccd.jpg"


def extract_img(file_path):
    print("run extract_img")
    with open(file_path, "rb") as f:
        files = {"image": f}

        data = {"prompt": "<image>\nĐọc nội dung trong ảnh, trả về dạng text"}

        res = requests.post(url, files=files, data=data)
        print("Response in = ", res.elapsed.total_seconds())
        if res.status_code == 200:
            output_path = pp.get_output_path()
            with open(output_path, "w") as file:
                content = res.json().get("response_message")
                file.write(content)
            # print(res.json().get("response_message"))
        else:
            print("Error: ", res.status_code, res.text)
