import cv2
import random


def get_embeddings(im_path):
    im = cv2.imread(im_path)
    width = im.shape[1]
    height = im.shape[0]
    new_width = int(width * 0.5)
    new_height = int(height * 0.5)
    x = random.randint(0, new_width)
    y = random.randint(0, new_height)
    return im[y:y + new_width, x:x + new_width, :]
