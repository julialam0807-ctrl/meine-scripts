import os
import shutil

def organize_downloads(folder_path):
    # 定义文件类型和对应的目标文件夹
    file_types = {
        "Bilder": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
        "Dokumente": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx"],
        "Videos": [".mp4", ".avi", ".mov", ".mkv"],
        "Audio": [".mp3", ".wav", ".flac"],
        "Programme": [".exe", ".msi", ".zip", ".rar"]
    }

    # 创建分类文件夹
    for folder in file_types.keys():
        target_folder = os.path.join(folder_path, folder)
        if not os.path.exists(target_folder):
            os.makedirs(target_folder)

    # 遍历下载文件夹里的所有文件
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        # 跳过文件夹，只处理文件
        if os.path.isfile(file_path):
            # 获取文件扩展名
            ext = os.path.splitext(filename)[1].lower()
            
            # 判断文件类型并移动
            moved = False
            for folder, extensions in file_types.items():
                if ext in extensions:
                    target_path = os.path.join(folder_path, folder, filename)
                    shutil.move(file_path, target_path)
                    print(f"已移动: {filename} -> {folder}")
                    moved = True
                    break
            
            # 未知类型的文件，移动到 "Sonstiges" 文件夹
            if not moved:
                other_folder = os.path.join(folder_path, "Sonstiges")
                if not os.path.exists(other_folder):
                    os.makedirs(other_folder)
                target_path = os.path.join(other_folder, filename)
                shutil.move(file_path, target_path)
                print(f"已移动: {filename} -> Sonstiges")

if __name__ == "__main__":
    # 改成你的下载文件夹路径
    downloads_path = r"C:\Users\你的用户名\Downloads"
    organize_downloads(downloads_path)
    print("✅ 文件夹整理完成！")
