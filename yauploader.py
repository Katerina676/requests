import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {"Authorization" : f'OAuth {self.token}'}

    def upload(self, file_path : str):
        headers = self.get_headers()
        params = {"path": file_path, "overwrite": "true"}
        url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        response = requests.get(url, headers=headers, params=params)
        res = response.json().get('href')
        response_upload = requests.put(res, data=open(file_path, 'rb'))
        return print(response_upload.status_code)


if __name__ == '__main__':
    uploader = YaUploader('')
    result = uploader.upload('file.txt')
