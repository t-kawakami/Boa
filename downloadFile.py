__author__ = 'kawakami_note'
import urllib
import csv

def download(url, title):
    urllib.urlretrieve(url, title)

def create_mapping_file(file_name, tags):
    mapping_file = open("data/mapping.csv", "w")
    writer = csv.writer(mapping_file)
    writer.writerow([file_name, tags])

def main():
    input_file = open("data/input.csv", "r")
    lines = csv.reader(input_file, delimiter=",")

    index = 0
    for line in lines:
        index += 1
        file_name = "data/images/" + str(index).zfill(10) + ".jpg"
        download(line[0], file_name)
        create_mapping_file(file_name, line[1])

if __name__ == "__main__":
    main()