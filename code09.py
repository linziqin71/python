# coding: utf-8
# made by reinforceai
# python实验第七节课，图像处理与opencv入门

import cv2
import numpy as np

# 1. 图像读取与显示
image = cv2.imread("D:/bite/python/ren.png")  # 读取图像
cv2.imshow("Original Image", image)  # 显示原始图像
cv2.waitKey(0)



# 2. 图像读取与显示,显示透过
image = cv2.imread("D:/bite/python/ren.png", -1)  # 读取图像
print(image)  # 显示图像内容
image2 = cv2.imread("D:/bite/python/jnu.png", -1)  # 读取图像
print(image2)  # 显示图像内容
a = image2[:, :, 3]
cv2.imshow("a", a)
cv2.waitKey(0)



# 3. 图像大小调整与裁剪
resized_image = cv2.resize(image, (400, 300))  # 调整图像大小为400x300
cropped_image = image[50:250, 100:300]         # 裁剪从(100, 50)到(300, 250)的区域

cv2.imshow("Resized Image", resized_image)
cv2.waitKey(0)
cv2.imshow("Cropped Image", cropped_image)
cv2.waitKey(0)

# 4. 图像颜色转换
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 转换为灰度图像
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)    # 转换为HSV颜色空间

cv2.imshow("Gray Image", gray_image)
cv2.waitKey(0)
cv2.imshow("HSV Image", hsv_image)
cv2.waitKey(0)

# 5. 图像矩形变换
image = cv2.imread("D:/bite/python/ren.png", -1)  # 读取图像
rows, cols = image.shape[:2]                               # 读取横纵尺寸

# 原图四点
pts1 = np.float32([[0, 0], [511, 0], [0, 479], [511, 479]])
# 目标图四点
pts2 = np.float32([[0, 200], [511, 0], [0, 279], [511, 479]])

# 计算透视变换矩阵 (3x3)
M = cv2.getPerspectiveTransform(pts1, pts2)
# 应用透视变换
perspective_warped = cv2.warpPerspective(image, M, (cols, rows))

# 展示结果
cv2.imshow("Image", perspective_warped)
cv2.waitKey(0)

# 6. 图像旋转变换
image = cv2.imread("D:/bite/python/ren.png", -1)  # 读取图像
rows, cols = image.shape[:2]                               # 读取横纵尺寸

# 定义旋转参数
angle = 45                                                 # 旋转角度，逆时针为正
scale = 1.0                                                # 缩放比例
center = (rows / 2, cols / 2)                              # 旋转中心点（图像中心）

# 生成旋转矩阵（2x3）
M = cv2.getRotationMatrix2D(center, angle, scale)

# 执行仿射变换
rotated = cv2.warpAffine(image, M, (rows, cols), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT, borderValue=(0,0,0))

# 展示结果
cv2.imshow('Rotated Image', rotated)
cv2.waitKey(0)