from alphasign import Sign, Image, Command, Packet
import cv2
from PIL import Image as pimg
import time
import sys
from base64 import standard_b64encode

sign = Sign()
sign.open("/dev/ttyUSB0")

# Open the video
cap = cv2.VideoCapture("bad_apple.mp4")
success, image = cap.read()
count = 0

# Configure memory (to enable A dots file)
def config_memory():
    # Configure memory
    memconf = Packet()
    sf = Command.write_special_functions()
    sf.add_memory_config("A", "dots", "locked", (60,7), "monochrome")
    sf.add_memory_config("A", "text", "locked", 2, {"start": 255, "stop": 255})
    memconf.add_command(sf)
    sign.send(memconf)
    time.sleep(1)

# Send image to file
def sendimg(img, width=60, height=7):
    # Write empty image
    image = Packet()
    image.add_command(Command.write_small_dots(img, width=width, height=height, label="A"))
    sign.send(image)

# Show full image in file...
def showimg():
    # Set text to display image
    text = Packet()
    text.add_command(Command.write_text("\x14A", mode=b"b", label="A"))
    sign.send(text)

# Init display (sending and displaying an empty image)
config_memory()
sendimg(b"0\x0D", 1, 1)
showimg()

# Iterate over each frame
while success:
    success, image = cap.read()
    print(f"read frame {count}/{round(cap.get(cv2.CAP_PROP_FRAME_COUNT))}")

    # If next frame is valid
    if success:
        bytes = b""

        # Reduce it to 60x7
        frame = cv2.resize(image, (60, int(60 * image.shape[0] / image.shape[1])), interpolation = cv2.INTER_AREA)
        mid_height = frame.shape[0] // 2
        cropped = frame[mid_height - 3:mid_height + 4, :]

        # Convert it to PIL image
        img = pimg.fromarray(cropped)

        # Convert it to bytes data
        for y in range(img.height):
            for x in range(img.width):
                r,g,b = img.getpixel((x,y))
                if r > 128 and g >12 and b > 128:
                    bytes += b"3"
                else:
                    bytes += b"0"
            bytes += b"\x0D"

        # Send to sign
        sendimg(bytes)

        # Wait for next frame
        time.sleep(0.25)

    count += 1
