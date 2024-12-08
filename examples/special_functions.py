from alphasign import Sign
from alphasign.command import WriteSpecialFunctions
import time

# Initialize the sign and special functions
sign = Sign()
sign.open(port="/dev/ttyUSB0")
special_functions = WriteSpecialFunctions()

print("Setting time to 14:30 (military time)...")
special_functions.set_time_of_day(14, 30)
sign.send(special_functions)
time.sleep(1)

print("Configuring time format to military...")
special_functions.set_time_format("military")
sign.send(special_functions)
time.sleep(1)

print("Configuring memory allocation for text file 'A'...")
special_functions.add_memory_config(
    label="A",
    type="text",
    ir="locked",
    size=256,
    conf={"start": "1", "stop": "Z"},
)
time.sleep(1)

print("Configuring memory allocation for graphics file 'B'...")
special_functions.add_memory_config(
    label="B",
    type="dots",
    ir="locked",
    size=(32, 16),
    conf="8color",
)
time.sleep(1)

print("Configuring memory allocation for string file 'C'...")
special_functions.add_memory_config(
    label="C",
    type="string",
    ir="unlocked",
    size=128,
    conf=None,
)
time.sleep(1)

print("Sending all memory configurations...")
sign.send(special_functions)
time.sleep(1)

print("Setting daytime brightness to 72%...")
special_functions.set_dimming_reg(dim=0, brightness=72)
sign.send(special_functions)
time.sleep(1)

print("Configuring auto-dimming schedule (19:00 to 06:00)...")
special_functions.set_dimming_time(start=0x19, stop=0x06)
sign.send(special_functions)
time.sleep(1)

print("Generating beep tone...")
special_functions.generate_tone(
    type=b"\x32",
    freq=0x40,
    duration=3,
    repeat=1,
)
sign.send(special_functions)
time.sleep(3)

print("Displaying text 'Hello World!' at coordinates (10,5)...")
special_functions.display_text_at_xy(enabled=True, x=10, y=5, text="Hello World!")
sign.send(special_functions)
