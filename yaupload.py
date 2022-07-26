class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        self.test_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'


