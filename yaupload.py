import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        self.file_path = file_path.split('/')
        self.file_name = self.file_path[-1]
        self.upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        self.head = ({'Content-Type': 'application/json', 'Authorization': 'OAuth {}'.format(self.token)})
        self.setting = {'path': self.file_name, 'overwrite': 'true'}
        self.send = requests.get(self.upload_url, headers=self.head, params=self.setting)
        #print(self.send.json())
        self.work_url = self.send.json().get("href","")
        #print(self.work_url)
        self.create_path = self.file_name.strip('.jpg')
        #print(self.create_path)
        self.upload_file = requests.put(self.work_url, data=self.file_name)
        self.upload_file.raise_for_status()



