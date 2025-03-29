import numpy as np
import os
# 文件路径
file_path = "Depth_1734351093699_0.raw"
name, _ = os.path.splitext(file_path)
# 分辨率
width = 640
height = 480

# 数据类型，假设是16位无符号整数（一般深度图是这样）
dtype = np.uint16

# 读取文件
with open(file_path, "rb") as f:
    depth_data = np.fromfile(f, dtype=dtype)

# 检查数据大小是否匹配分辨率
if depth_data.size != width * height:
    raise ValueError("文件大小与分辨率不匹配！")

# 重塑为二维数组
depth_image = depth_data.reshape((height, width))

# 打印或保存深度图
print(depth_image)

# 示例：将深度图保存为可视化图片
import cv2
new_file_path = f"{name}.png"
# cv2.imwrite(new_file_path, depth_image)

depth_normalized = cv2.normalize(depth_image, None, 0, 255, cv2.NORM_MINMAX)

new_file_normalized_path=f"{name}_normalized.png"
depth_visual = depth_normalized.astype(np.uint8)
cv2.imwrite(new_file_normalized_path, depth_visual)
