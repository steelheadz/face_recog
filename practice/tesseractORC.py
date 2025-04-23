from PIL import Image
import pytesseract

path = "../img/text-img.png"
# path = r"D:\Personal\Materials\carnumber.jpg"
# 识别图片中的文字
text = pytesseract.image_to_string(Image.open(path), lang='chi_sim')
print(text)
