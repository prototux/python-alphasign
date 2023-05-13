from PIL import Image
import math

class Image:
    palette = {
        (0, 0, 0):     "0", # Black
        (255, 0, 0):   "1", # Red
        (0, 255, 0):   "2", # Green
        (255, 191, 0): "3", # Amber
        (187, 3, 0):   "4", # Dim Red
        (0, 120, 0):   "5", # Dim Green
        (83, 34, 35):  "6", # Brown
        (255, 120, 0): "7", # Orange
        (255, 255, 0): "8"  # Yellow
    }

    def __init__(self, path):
        self.orig = Image.open(picture).convert('RGB')
        self.width = self.orig.width
        self.height = self.orig.height
        self.conv = self.img_convert(self.orig)

    def img_convert(self, img):
        # Final converted image
        conv = b""

        # Convert the image to palette
        for y in range(img.height):
            line = []
            for x in range(img.width):
                # Get the original RGB values
                r,g,b = img.getpixel((x,y))

                # Round to closest palette color (using Euclidean distance)
                distances = {index: math.sqrt((r - pr) ** 2 + (g - pg) ** 2 + (b - pb) ** 2) for (pr, pg, pb), index in self.palette.items()}
                index = min(distances, key=distances.get)

                conv += index.encode()
            conv += b"\x0D"

        return conv

    def to_bytes(self):
        return self.conv

