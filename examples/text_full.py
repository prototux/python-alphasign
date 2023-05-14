from alphasign import Sign, SignType, Text

# Open sign
sign = Sign()
sign.open(port="/dev/ttyUSB0")

text = Text("{{red}}Hello{{green}}World!")
sign.send(text.to_packet(label="0", mode=Text.Mode.rotate))
