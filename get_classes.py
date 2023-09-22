import os
import json
from tqdm import tqdm
# 存储已经存在的type字段
existing_types = set()

# JSON文件的文件夹路径
folder_path = 'labels'

# 获取文件夹中的所有JSON文件
filenames = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.json')]

# 打开txt文件以追加写入
with open('types.txt', 'a') as f:
    # 遍历每个JSON文件
    for filename in tqdm(filenames):
        # 读取JSON文件
        with open(filename) as json_file:
            data = json.load(json_file)
        
        # 遍历每个JSON对象
        for item in data:
            # 提取type字段
            type_value = item.get('type')
            
            # 如果type字段不存在或已经存在于txt文件中，则跳过
            if not type_value or type_value in existing_types:
                continue
            
            # 写入type字段到txt文件
            f.write(type_value + '\n')
            
            # 将type字段添加到已存在的type集合中
            existing_types.add(type_value)
