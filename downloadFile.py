__author__ = 'kawakami_note'
import urllib.request

def download(url, title):
    urllib.request.urlretrieve(url, title)

download("https://retrip.s3.amazonaws.com/article/5324/images/5324b7fa81a5-4a73-40f1-812f-742f7ed7e429_m.jpg", "ゴリラ.jpg")