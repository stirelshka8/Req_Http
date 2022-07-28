import hero
from yaupload import YaUploader

print(f"[INFO] Самый умный супергерой --> {hero.smart_hero()}")

if __name__ == '__main__':
    path_to_file = '//home//stirelshka//Python.jpg'
    token = '00000000000000000000000000000'
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
