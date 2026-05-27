from PIL import Image
import os

def compress_images(folder_path, quality=85):
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            img_path = os.path.join(folder_path, filename)
            img = Image.open(img_path)
            img.save(img_path, quality=quality, optimize=True)
            print(f"已压缩: {filename}")

if __name__ == "__main__":
    folder = r"C:\Users\你的用户名\Pictures"
    compress_images(folder)
    print("✅ 图片压缩完成！")
