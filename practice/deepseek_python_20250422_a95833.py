import cv2
import numpy as np

img = cv2.imread("../img/ag.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 构建高斯金字塔（4层）
gaussian_pyramid = [gray]
for i in range(3):
    gray = cv2.pyrDown(gray)  # 降采样
    gaussian_pyramid.append(gray)

# 显示金字塔
for i, level in enumerate(gaussian_pyramid):
    cv2.imshow(f"Level {i}", level)
cv2.waitKey(0)