#!/usr/bin/env python3

import time

## Send raw bytes image
from alphasign import Sign, Image, Packet, Command

# Raw bytes image
img =  b"\
111100222200333300444400555500666600777700888800000000000000\x0D\
111100222200333300444400555500666600777700888800000000000000\x0D\
111100222200333300444400555500666600777700888800000000000000\x0D\
111100222200333300444400555500666600777700888800000000000000\x0D\
000000000000000000000000000000000000000000000000000000000000\x0D\
000000000000000000000000000000000000000000000000000000000000\x0D\
000000000000000000000000000000000000000000000000000000000000\x0D"

# Open sign
sign = Sign()
sign.open("/dev/ttyUSB0")

# Configure memory
memconf = Packet()
sf = Command.write_special_functions()
sf.add_memory_config("A", "dots", "locked", (60,7), "3color")
sf.add_memory_config("A", "text", "locked", 2, {"start": 255, "stop": 255})
memconf.add_command(sf)
sign.send(memconf)
time.sleep(1)

# Send image
image = Packet()
image.add_command(Command.write_small_dots(img, width=60, height=7, label="A"))
sign.send(image)

# Send text to display image
text = Packet()
text.add_command(Command.write_text("\x14A", mode=b"b", label="A"))
sign.send(text)

