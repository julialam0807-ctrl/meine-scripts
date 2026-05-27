import os

# ====== 1. 在这里填写你的图片文件夹路径 ======
folder_path = r"D:\你的图片文件夹路径"   # ⚠️ 改成你自己的路径

# ====== 2. 支持的图片格式 ======
image_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif')

# ====== 3. 获取文件夹中的所有文件 ======
files = os.listdir(folder_path)

# ====== 4. 过滤出图片文件，并排序 ======
image_files = [f for f in files if f.lower().endswith(image_extensions)]
image_files.sort()  # 按文件名排序（可选）

# ====== 5. 开始批量重命名 ======
for index, filename in enumerate(image_files, start=1):
    # 获取原文件完整路径
    old_path = os.path.join(folder_path, filename)
    
    # 获取文件扩展名（比如 .jpg）
    ext = os.path.splitext(filename)[1]
    
    # 生成新文件名：照片_001.jpg
    new_name = f"照片_{index:03d}{ext}"
    
    # 新文件完整路径
    new_path = os.path.join(folder_path, new_name)
    
    # 重命名
    os.rename(old_path, new_path)

# ====== 6. 完成提示 ======
print("✅ 重命名完成！")
