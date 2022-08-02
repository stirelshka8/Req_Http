import hero
from yaupload import YaUploader

#print(f"[INFO] Самый умный супергерой --> {hero.smart_hero()}")

if __name__ == '__main__':
    path_to_file = '/home/stirelshka/Python.txt'
    token = '000'
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
