import cv2
import numpy as np

my_image = cv2.imread("input/sina.jpg")
celeb_image = cv2.imread("input/celeb.jpg")

my_image = my_image[10:, :, :]
w, h, _ = my_image.shape
celeb_image = cv2.resize(celeb_image, [h, w])

my_image = my_image.astype(np.float32)
celeb_image = celeb_image.astype(np.float32)

convert_image_0 = my_image*3/4 + celeb_image/4
convert_image_1 = my_image*2/4 + celeb_image*2/4
convert_image_2 = my_image/4 + celeb_image*3/4

convert_image = np.concatenate(
    (my_image, convert_image_0, convert_image_1, convert_image_2, celeb_image), axis=1)

convert_image = convert_image.astype(np.uint8)

cv2.imwrite("output/sina_celeb.jpg", convert_image)
