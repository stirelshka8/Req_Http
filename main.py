import hero
from yaupload import YaUploader

print(f"[INFO] Самый умный супергерой --> {hero.smart_hero()}")

if __name__ == '__main__':
    path_to_file = '//home//stirelshka//Python.jpg'
    token = 'AQAAAAAaGso_AADLW3qdanTLIEX2nZks0A3bLNE'
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
