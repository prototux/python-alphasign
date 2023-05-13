# Write Text command, sends one or multiple text field
class WriteText:
    code = b"A"

    def __init__(self, text, label="A", position="0", mode="a"):
        self.text = text
        self.label = label
        self.position = position
        self.mode = mode

        # Checksum?
        self.checksum = False

    def to_bytes(self):
        # A Write command sends a file text,
        # it starts with the label and the ESC byte
        bytes = self.label.encode() + b"\x1B"

        # Add the position and mode
        bytes += self.position.encode() + self.mode.encode()

        # Add the text (special ascii)
        if isinstance(self.text, str):
            bytes += self.text.encode()
        else:
            bytes += self.text

        return bytes

