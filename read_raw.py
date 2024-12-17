import numpy as np
from PIL import Image

# 定义 RAW 文件参数（根据文件具体信息修改）
# file_path = "Color_1734094619502_1.raw"  # 替换为你的 RAW 文件路径
# file_path = "Color_1734094619502_1.raw"  # 替换为你的 RAW 文件路径
file_path = "Depth_1734095745155_0.raw"  # 替换为你的 RAW 文件路径

output_path = "image.jpg"  # 替换为目标 JPG 文件路径
width = 640             # 图像宽度（像素）
height = 480            # 图像高度（像素）
channels = 1             # 通道数（灰度图=1，RGB图=3）
dtype = np.uint16         # 数据类型（uint8: 0-255; uint16: 0-65535）

# 加载 RAW 文件
with open(file_path, "rb") as f:
    raw_data = f.read()

# 将数据转为 NumPy 数组
image = np.frombuffer(raw_data, dtype=dtype)

# 重塑为图像数组
if channels == 1:
    image = image.reshape((height, width))  # 单通道灰度图
elif channels == 3:
    image = image.reshape((height, width, channels))  # RGB 图像
else:
    raise ValueError("Unsupported number of channels.")

# 转换为 PIL 图像
if channels == 1:
    pil_image = Image.fromarray(image, mode='L')  # 灰度图
elif channels == 3:
    pil_image = Image.fromarray(image, mode='RGB')  # 彩色图
else:
    raise ValueError("Unsupported number of channels.")

# 保存为 JPG 格式
pil_image.save(output_path, format="JPEG")
print(f"Image saved as {output_path}")