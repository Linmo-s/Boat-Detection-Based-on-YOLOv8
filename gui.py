import os
import tkinter as tk
from tkinter import filedialog, messagebox
from ultralytics import YOLO
from PIL import Image, ImageTk

# === 自动定位目录 ===
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODELS_DIR = os.path.join(BASE_DIR, "models")
IMAGES_DIR = os.path.join(BASE_DIR, "images")

# 确保 models 和 images 文件夹存在
os.makedirs(MODELS_DIR, exist_ok=True)
os.makedirs(IMAGES_DIR, exist_ok=True)


def select_model():
    """选择 YOLO 模型文件（默认打开 models 文件夹）"""
    model_path = filedialog.askopenfilename(
        title="选择 YOLO 模型文件 (.pt)",
        initialdir=MODELS_DIR,
        filetypes=[("YOLO 模型文件", "*.pt")]
    )
    if model_path:
        model_entry.delete(0, tk.END)
        model_entry.insert(0, model_path)


def select_image():
    """选择要检测的图片（默认打开 images 文件夹）"""
    image_path = filedialog.askopenfilename(
        title="选择要检测的图片",
        initialdir=IMAGES_DIR,
        filetypes=[("图像文件", "*.jpg;*.png;*.jpeg;*.bmp")]
    )
    if image_path:
        image_entry.delete(0, tk.END)
        image_entry.insert(0, image_path)


def run_detection():
    """运行 YOLO 检测"""
    model_path = model_entry.get()
    image_path = image_entry.get()

    if not model_path or not os.path.exists(model_path):
        messagebox.showerror("错误", "请先选择正确的模型文件！")
        return
    if not image_path or not os.path.exists(image_path):
        messagebox.showerror("错误", "请先选择目标图片！")
        return

    try:
        # 加载模型
        model = YOLO(model_path)

        # 执行检测
        results = model.predict(source=image_path, save=True, show=False)
        output_dir = results[0].save_dir
        result_image_path = os.path.join(output_dir, os.path.basename(image_path))

        messagebox.showinfo("完成", f"检测完成！\n结果保存在：\n{output_dir}")

        # 显示检测结果图片
        show_result_image(result_image_path)

    except Exception as e:
        messagebox.showerror("错误", f"检测失败：{e}")


def show_result_image(image_path):
    """显示检测结果图片（不自动关闭）"""
    if not os.path.exists(image_path):
        messagebox.showerror("错误", "未找到检测结果图片！")
        return

    top = tk.Toplevel(root)
    top.title("检测结果预览")

    img = Image.open(image_path)
    max_size = (800, 600)
    img.thumbnail(max_size)
    img_tk = ImageTk.PhotoImage(img)

    label = tk.Label(top, image=img_tk)
    label.image = img_tk
    label.pack()

    tk.Button(top, text="关闭预览", command=top.destroy).pack(pady=10)


# === GUI 主界面 ===
root = tk.Tk()
root.title("YOLO 目标检测工具")
root.geometry("500x280")

tk.Label(root, text="选择模型文件 (.pt):").pack(pady=5)
model_entry = tk.Entry(root, width=50)
model_entry.pack()
tk.Button(root, text="浏览模型", command=select_model).pack(pady=5)

tk.Label(root, text="选择检测图片:").pack(pady=5)
image_entry = tk.Entry(root, width=50)
image_entry.pack()
tk.Button(root, text="浏览图片", command=select_image).pack(pady=5)

tk.Button(root, text="开始检测", bg="#4CAF50", fg="white", command=run_detection).pack(pady=15)

root.mainloop()
