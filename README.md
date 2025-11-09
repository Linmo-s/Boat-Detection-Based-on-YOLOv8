# 🚢 Boat-Detection-Based-on-YOLOv8
基于 YOLOv8 模型构建了一个针对水域场景的目标检测系统，主要识别目标包括船只、水上摩托与港口（可以识别岸边车辆但精度较低）。通过在多样化水面影像数据集上进行训练与优化，模型有较高检测精度，为智能航运监测与海上安全管理提供了可行的技术方案。

## 🧩 项目结构

Boat-Detection-Based-on-YOLOv8/

├── gui.py # 图形界面入口文件

├── models/ # 训练好的模型与配置

│ └── best.pt

├── run/detect/ # 检测结果

├── images/ # 示例图片

├── requirements.txt # 依赖包列表

└── README.md # 项目说明文件

## ⚙️ 环境配置

1. 克隆项目

    git clone https://github.com/Linmo-s/Boat-Detection-Based-on-YOLOv8.git

2. 创建虚拟环境并安装依赖

    (建议使用虚拟环境)
    pip install -r requirements.txt

3. 若未安装 YOLOv8，可执行：

    pip install ultralytics

## 🧰 图形界面（GUI）
项目提供了一个简易的图形界面，支持图像加载与目标检测：

    python gui.py

## 🖼️ 示例结果
GUI界面
![GUI界面]("images/hub/gui.png")

测试图片
![测试图片]("images/hub/test.png")
![测试图片]("images/hub/test1.png")
![测试图片]("images/hub/test2.png")

## 🧑‍💻 作者信息

作者: 
LinMo[访问我的主页](https://github.com/Linmo-s)

