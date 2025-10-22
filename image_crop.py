import os
import cv2
import numpy as np

# 이미지 불러오기 (640x400)
img = cv2.imread("img/input4.jpg")
img_gray = cv2.imread("img/input4.jpg", cv2.IMREAD_GRAYSCALE)

w = 640
h = 400

src_points = np.float32([
    [180, 280],  # 좌측 상단
    [460, 280],  # 우측 상단
    [800, 400], # 우측 하단
    [-160, 400]  # 좌측 하단
])
crop_points_L = np.float32([
    [0, 0],
    [180, 0],
    [0, 64]
])
crop_points_R = np.float32([
    [640, 0],
    [460, 0],
    [640, 64]
])

output1 = img.copy()
cv2.polylines(output1, np.int32([src_points]), True, (255, 0, 255), 2)

croped_img = img_gray[280:400, 0:640]

cv2.fillPoly(croped_img, np.int32([crop_points_L]), (0, 0, 0))
cv2.fillPoly(croped_img, np.int32([crop_points_R]), (0, 0, 0))

# img = cv2.fillPoly(img, pts, color[, lineType[, shift[, offset]]])
# img = cv2.polylines(img, pts, isClosed, color[, thickness[, lineType[, shift]]])

croped_img = cv2.GaussianBlur(croped_img, (17, 17), 0)
edges = cv2.Canny(croped_img, 21, 51, L2gradient=1)

# 결과 확인
cv2.imshow("Original", output1)
cv2.imshow("Croped Image", croped_img)
cv2.imshow("Edge", edges)
#cv2.imwrite('./img/ROI.jpg', output1)
#cv2.imwrite('./img/output4.jpg', warped)
cv2.waitKey(0)
cv2.destroyAllWindows()