import os
from PIL import Image
from tqdm import tqdm

# 图像文件夹路径
folder_path = 'images'

# 遍历图像文件夹中的所有文件
for filename in tqdm(os.listdir(folder_path)):
    # 获取图像文件的完整路径
    file_path = os.path.join(folder_path, filename)
    
    # 读取图像
    image = Image.open(file_path)
    
    # 获取图像的宽度和高度
    width, height = image.size
    
    # 判断宽度和高度是否等于1920和1080
    if width != 1920 or height != 1080:
        # 输出图像文件名
        print(filename)
