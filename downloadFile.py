__author__ = 'kawakami_note'
import urllib

def download(url, title):
    urllib.urlretrieve(url, "{0}".format(title))

download("", "")