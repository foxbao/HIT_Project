import numpy as np
from PIL import Image
import os
from pathlib import Path
import string

class Converter():
    def __init__(self):
        pass
    def convert_raw_to_image(self,data_folder,file_name):
        # 定义 RAW 文件参数（根据文件具体信息修改）
        name, _ = os.path.splitext(file_name)

        output_name = f"{name}_.jpg"  # 替换为目标 JPG 文件路径
        width = 640  # 图像宽度（像素）
        height = 480  # 图像高度（像素）
        channels = 3  # 通道数（灰度图=1，RGB图=3）
        dtype = np.uint8  # 数据类型（uint8: 0-255; uint16: 0-65535）

        # 加载 RAW 文件
        filepath=os.path.join(data_folder,file_name)
        with open(filepath, "rb") as f:
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
            pil_image = Image.fromarray(image, mode="L")  # 灰度图
        elif channels == 3:
            pil_image = Image.fromarray(image, mode="RGB")  # 彩色图
        else:
            raise ValueError("Unsupported number of channels.")

        # 保存为 JPG 格式
        jpg_folder_name="jpg"
        jpg_folder = os.path.join(data_folder, jpg_folder_name)
        if not os.path.exists(jpg_folder):
            os.makedirs(jpg_folder)
            print(f"文件夹已创建：{jpg_folder}")
        output_path=os.path.join(jpg_folder,output_name)
        pil_image.save(output_path, format="JPEG")
        print(f"Image saved as {output_path}")



    def convert_raw_to_image_batch(self,data_folder: string):
        folder_path = Path(data_folder)
        files = [
            f.name
            for f in folder_path.iterdir()
            if f.is_file() and f.name.startswith("Color")
        ]
        
        for filename in files:
            self.convert_raw_to_image(data_folder,filename)
    


if __name__ == "__main__":
    data_folder = "data/camera_hit"
    converter=Converter()
    converter.convert_raw_to_image_batch(data_folder)
