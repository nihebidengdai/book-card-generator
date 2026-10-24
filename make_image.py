from PIL import Image
image = Image.new("RGB", (1080, 1440), "#F7F4EF")
image.save("card.png")
print("图片已生成")