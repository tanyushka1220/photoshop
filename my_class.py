from PIL import Image, ImageFilter

class ImageEditor:
    def __init__(self, name_image):
        self.name_image = name_image
        self.original = None 
        self.changes = list()
        self.load_image()

    def load_image(self):
        try:
            original = Image.open(self.name_image)
        except:
            print("No file")
    
    def b_w(self):
        gray = self.gray.original.convert("L")
        self.changes.append(gray)

    def dlur_image(self):
        blur = self.blured.original.filter(ImageFilter.BLUR)
        self.changes.append(blur)

    def rotate(self):
        rotate90 = self.original.transpose(Image.ROTATE_90)
        self.changes.append(rotate90)

    def save(self, change, img):
        save = self.name_image.split(".")
        name = save[0] + "_" + change + ".jpg" 
        img.save(name)