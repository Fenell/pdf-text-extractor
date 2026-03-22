import requests

url = "https://2d08-8-229-129-67.ngrok-free.app/ocr"
file_path = "text_extractor/ccd.jpg"

with open(file_path, "rb") as f:
    files = {"image": f}

    data = {"prompt": "<image>\nNhận diện thông tin trong ảnh, trả về dạng text"}

    res = requests.post(url, files=files, data=data)
    print("Response in = ", res.elapsed.total_seconds())
    if res.status_code == 200:
        print(res.json().get("response_message"))
    else:
        print("Error: ", res.status_code, res.text)
