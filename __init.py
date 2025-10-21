import os
import cv2
import numpy as np

# 이미지 불러오기 (640x400)
img = cv2.imread("img/input4.jpg")
img_gray = cv2.imread("img/input4.jpg", cv2.IMREAD_GRAYSCALE)
w = 640
h = 400

# 전방 이미지에서 변환할 영역 (사다리꼴 형태)
# 여기서는 예시로 도로 하단 부분을 탑뷰로 변환한다고 가정
# 실제 주차환경에 맞게 조정 필요

# 소실점 : (320,228)
'''src_points = np.float32([
    [192, 295],  # 좌측 상단
    [448, 295],  # 우측 상단
    [640, 400], # 우측 하단
    [0, 400]  # 좌측 하단
])'''
# t - 320, 220
src_points = np.float32([
    [180, 280],  # 좌측 상단
    [460, 280],  # 우측 상단
    [800, 400], # 우측 하단
    [-160, 400]  # 좌측 하단
])

output1 = img.copy()
cv2.polylines(output1, np.int32([src_points]), True, (255, 0, 255), 2)
#cv2.line(output1, (50, 60), (150, 160), 255)
# 변환할 목표 좌표 (직사각형)
dst_points = np.float32([
    [0, 0],
    [w, 0],
    [w, h],
    [0, h]
])


# 투영 변환 행렬 구하기
matrix = cv2.getPerspectiveTransform(src_points, dst_points)

# 원근 변환 (탑뷰)
#warped = cv2.warpPerspective(img, matrix, (w, h))
#warped = cv2.warpPerspective(edges, matrix, (w, h))
warped = cv2.warpPerspective(img_gray, matrix, (w, h))

edges = cv2.Canny(warped, 100, 200)
# 결과 확인
cv2.imshow("Original", output1)
cv2.imshow("Top-Down View", warped)
#cv2.imwrite('./img/ROI.jpg', output1)
cv2.imwrite('./img/output4.jpg', warped)
cv2.waitKey(0)
cv2.destroyAllWindows()