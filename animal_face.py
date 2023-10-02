import cv2
import numpy as np


def transparent_sticker(sticker):
    rows, cols, _ = sticker.shape
    sticker_ghost = np.zeros(sticker.shape)
    sticker_transparent = np.zeros(sticker.shape)
    sticker_ghost = np.array(sticker_ghost, dtype=np.uint8)
    sticker_transparent = np.array(sticker_transparent, dtype=np.uint8)

    for row in range(rows):
        for col in range(cols):
            if sticker[row, col, 0] > 240 and sticker[row, col, 1] > 240 and sticker[row, col, 2] > 240:
                sticker_ghost[row, col] = [0, 0, 0]
            else:
                sticker_ghost[row, col] = sticker[row, col]

            if sticker_ghost[row, col, 0] < 1 and sticker_ghost[row, col, 1] < 1 and sticker_ghost[row, col, 2] < 1:
                sticker_ghost[row, col] = [1, 1, 1]
            else:
                sticker_ghost[row, col] = [0, 0, 0]

            if sticker_ghost[row, col, 0] == 0 and sticker_ghost[row, col, 1] == 0 and sticker_ghost[row, col, 2] == 0:
                sticker_transparent[row, col] = sticker[row, col]

    return sticker_ghost, sticker_transparent


image_cow = cv2.imread("input/cow.jpg")
my_image = cv2.imread("input/sina.jpg")
image_cow = cv2.resize(image_cow, [640, 640])
my_image = cv2.resize(my_image, [640, 640])

image_cow_ghost, image_cow_transparent = transparent_sticker(image_cow)

convert_image = my_image*image_cow_ghost + image_cow_transparent

cv2.imwrite("output/animal_face.jpg", convert_image)
