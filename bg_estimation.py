import cv2
import numpy as np

cap = cv2.VideoCapture("input/cars.mp4")

frame_ids = cap.get(cv2.CAP_PROP_FRAME_COUNT)*np.random.uniform(size=25)


frames = []
for fid in frame_ids:
    cap.set(cv2.CAP_PROP_POS_FRAMES, fid)
    _, frame = cap.read()
    frames.append(frame)

median_frame = np.median(frames, axis=0).astype(dtype=np.uint8)

cv2.imwrite("output/road.jpg", median_frame)
