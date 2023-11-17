from PIL import Image
from reportlab.pdfgen import canvas
import os

def image2pdf(sub_folder_path, pdf_filename):
    """
        将多张图片转换为PDF文件
    """

    # 图片文件名列表
    image_files = os.listdir(sub_folder_path)
    image_files = list(filter(lambda x: x.lower().endswith(".jpg") or x.lower().endswith(".jpeg"), image_files))
    image_files.sort()

    # 打开一个PDF文件，并设置页面大小（可以根据需要调整）
    c = canvas.Canvas(pdf_filename)

    for image_file in image_files:
        image_file = os.path.join(sub_folder_path, image_file)
        # 打开图片文件
        img = Image.open(image_file)

        # 获取图片的宽度和高度（以点为单位，1英寸=72点）
        width, height = img.size

        # 根据图片尺寸创建一个PDF页面
        c.setPageSize((width, height))
        
        # 将图片绘制到PDF页面上
        c.drawImage(image_file, 0, 0, width, height)

        # 添加新的页面，准备绘制下一张图片
        c.showPage()

    # 保存PDF文件
    c.save()
    print(f"{sub_folder_path} => {pdf_filename} done, total {len(image_files)} pages.")

if __name__ == "__main__":
    base_folder = "解压缩的文件夹"
    output_folder = "生成pdf的文件夹"

    # find sub folder name in base folder
    sub_folder_names = os.listdir(base_folder)
    for sub_folder_name in sub_folder_names:
        sub_folder_path = os.path.join(base_folder, sub_folder_name)
        if os.path.isdir(sub_folder_path) and "Monki" in sub_folder_name:
            pdf_filename = os.path.join(output_folder, sub_folder_name + ".pdf")
            image2pdf(sub_folder_path, pdf_filename)