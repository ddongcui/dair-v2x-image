中文readme

# 1.Dair-V2X数据集
## 1.1 介绍
DAIR-V2X数据集是第一个用于车路协同自动驾驶研究的大规模、多模态、多视图数据集。所有数据都是从真实场景中收集的，包括2D和3D注释。  
## 1.2 特点
-参考[OpenXLab](https://opendatalab.com/OpenDataLab/DAIR-V2X)  
-本代码用于将dair-v2x路测图像部分的json文件转换为yolo格式，并使用yolov5进行训练  
-数据来源于[飞浆](https://aistudio.baidu.com/datasetdetail/179509)，下载[infrastructure.zip](https://aistudio.baidu.com/datasetdetail/179509)和[infrastructure-infrastructure-side-image.zip](https://aistudio.baidu.com/datasetdetail/179509)

# 2. 使用方法
## 2.1 检查图像大小
```
python check_hw.py  #根据实际情况修改图像位置，高，宽
```
检查图像大小，便于后期生成yolo格式时统一高宽
## 2.2 获取数据集中类别数
```
python get_classes.py
```
## 2.3 检查标注是否正确
```
# 检查标注文件和图像是否对应，这里图像在文件夹infrastructure-infrastructure-side-image\cooperative-vehicle-infrastructure-infrastructure-side-image下面
# 标注文件在\infrastructure\cooperative-vehicle-infrastructure\infrastructure-side\label下面
python check_box.py
```
## 2.4 生成yolo文件
```
python get_yolo.py
```
**特殊说明**
-这里一共找到9个类别，雪糕筒对自己项目用处不大，因此在数据集中去除了，需要的可以自行修改
