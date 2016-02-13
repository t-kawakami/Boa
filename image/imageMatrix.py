__author__ = 'kawakami'
import numpy
from PIL import Image
import csv

STANDARD_SIZE = (150, 150)

def img_to_matrix(file_name):
    img = Image.open(file_name)
    img = img.convert('RGB')
    img = img.resize(STANDARD_SIZE)
    img.show()
    img_array = numpy.asarray(img)
    return img_array

def flatten_image(img):
    s = img.shape[0] * img.shape[1] * img.shape[2]
    img_wide = img.reshape(1, s)
    return img_wide[0]

def create_data(file_name):
    mapping_file = open(file_name, 'r')
    reader = csv.reader(mapping_file)
    files_digit_data = []
    tags_data = []
    index = 0
    for line in reader:
        index += 1
        image_file_name = line[0]
        tags = str(line[1]).split(' ')
        img = img_to_matrix(image_file_name)
        img = flatten_image(img)
        files_digit_data.append(img)
        tags_data.append(tags)
        print(image_file_name + ' is processed')
    return files_digit_data, tags_data


def main():
    create_data('data/mapping.csv')

if __name__ == '__main__':
    main()
