from PIL import Image
import math

# Write Small Dots Picture
class WriteSmallDots:
    code = b"I"
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

    def __init__(self, picture, label="A", width=0, height=0):
        # Image label ("file")
        self.label = label

        # Image can be sent either as a raw byte array or as a path to a png/jpg to convert
        if not isinstance(picture, str):
            self.picture = picture
            self.width = width
            self.height = height
        else:
            orig = Image.open(picture).convert('RGB')
            self.width, self.height, self.picture = self.img_convert(orig)

        print(f"Sending image of size {self.width}x{self.height} in label {self.label}")

        # Checksum?
        self.checksum = False

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

        return img.width, img.height, conv

    def to_bytes(self):
        # A Write command sends a small dots picture.
        # it starts with the label
        bytes = self.label.encode()

        # Add the height and width
        bytes += f"{self.height:02X}{self.width:02X}".encode()

        # Insert FF byte for 100ms delay
        bytes += b"\xFF"

        # Add the picture (in ascii)
        bytes += self.picture

        return bytes
