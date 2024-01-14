from PIL import Image,ImageFilter

#открой файл с оригиналом картинки
original = Image.open("original.jpg")
original.show()
#сделай оригинал изображения чёрно-белым
gray = original.convert("L")
gray.show()
gray.save("gray.jpg")
#сделай оригинал изображения размытым
blured = original.filter(ImageFilter.BLUR)
blured.show()
blured.save("blured_original.jpg")
#поверни оригинал изображения на 180 градусов
rotate = original.transpose(Image.ROTATE_180)
rotate.show()
rotate.save("rotate_original.jpg")