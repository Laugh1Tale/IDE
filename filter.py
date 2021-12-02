import sys
from PIL import Image
import numpy as np
import argparse
import datetime


def create_namespace():
    """
    Сreates and returns a namespace with specific arguments.
    """
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-i', '--image', default=None, metavar='',
                            help='set image to transform into a mosaic in grayscale')
    arg_parser.add_argument('-r', '--result', default='res.jpg', metavar='',
                            help='set name with which the result will be saved')
    return arg_parser.parse_args(sys.argv[1:])


def open_image(image_name):
    """
    Receives the name of the image and tries to open it, handles exceptions.

    :param image_name: name of the image in the current directory
    :type image_name: str
    """
    while True:
        try:
            image = Image.open(image_name)
            return image
        except Exception as e:
            register_an_error(e)
            print('Incorrect input.')
            print('Enter the image name in the current directory '
                  'or specify the full path to your file. Write "exit" if you want to exit.')
            image_name = input()
            if image_name == 'exit':
                exit()


def register_an_error(error):
    """
    Receives an error and logs it to a file log.txt, handles exceptions.

    :param error: name of the image in the current directory
    :type error: Exception
    """
    try:
        with open('./log.txt', 'a') as file:
            now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            file.write("[{}] - {}\n".format(now, error))
    except Exception as e:
        with open('./log.txt', 'w+') as file:
            now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            file.write("[{}] - {}\n".format(now, e))
            file.write("[{}] - {}\n".format(now, error))


def set_grayscale():
    """
    Requests grayscale input and returns, handles exceptions.

    :rtype: int
    """
    while True:
        try:
            grayscale = int(input('Set grayscale.\n'))
            break
        except Exception as e:
            register_an_error(e)
            print('Incorrect input. Please enter grayscale in correct format.')
    return grayscale


def set_mosaic_dimensions():
    """
    Requests mosaic height and width input and returns, handles exceptions.

    :rtype: object
    """
    while True:
        try:
            height = int(input('Set the mosaic height.\n'))
            break
        except Exception as e:
            register_an_error(e)
            print('Incorrect input. Please enter mosaic height in correct format.')
    while True:
        try:
            width = int(input('Set the mosaic width.\n'))
            break
        except Exception as e:
            register_an_error(e)
            print('Incorrect input. Please enter mosaic width in correct format.')
    return height, width


def get_color(brightness, step):
    """
    Receives the brightness of the mosaic fragment and grayscale,
    and returns the color to which the fragment will be converted.

    :param brightness: brightness of the mosaic fragment
    :type brightness: int
    :param step: grayscale
    :type step: int

    >>> get_color(49, 50)
    0

    >>> get_color(50, 50)
    50

    >>> get_color(51, 50)
    50
    """
    return int(brightness // step) * step


def replace_with_gray(dimensions, image, step):
    """
    Receives the mosaic dimensions, image and grayscale,
    processes and returns the image according to the specified parameters.

    :param dimensions: mosaic dimensions (height, width)
    :type dimensions: tuple(int, int)
    :param image: image
    :type image: Image
    :param step: grayscale
    :type step: int
    """
    array = np.array(image)
    height = dimensions[0]
    width = dimensions[1]
    for x in range(0, len(array), height):
        for y in range(0, len(array[1]), width):
            # find out the average brightness
            average_brightness = np.sum(array[x: x + height, y: y + width]) // (height * width * 3)
            # bring the color of average brightness to the step in increments of 50
            color = get_color(average_brightness, step)
            # paint the cell into mosaics in the resulting color
            array[x: x + height, y: y + width] = np.full(3, color)
    return Image.fromarray(array)


def save_image(result_name, image):
    """
    Receives the processed image and the image name, saves it, handles exceptions.

    :param result_name: the name under which the image should be saved
    :type result_name: str
    :param image: received  processed image
    :type image: Image
    """
    while True:
        try:
            return image.save(result_name)
        except Exception as e:
            register_an_error(e)
            print('Enter a different name for the output image or specify the correct file format.')
            result_name = input()


if __name__ == '__main__':
    namespace = create_namespace()
    img = open_image(namespace.image)
    processed_image = replace_with_gray(set_mosaic_dimensions(), img, set_grayscale())
    save_image(namespace.result, processed_image)
