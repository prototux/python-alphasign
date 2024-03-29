# Write Text command, sends one or multiple text field
class WriteText:
    code = b"A"

    # Text positions. probably to move
    class Position:
        middle_line = b"\x20"
        top_line = b"\x22"
        bottom_line = b"\x26"
        fill = b"\x30"
        left = b"\x31"
        right = b"\x32"


    def __init__(self, text, label="A", position=Position.fill, mode=b"a"):
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
        bytes += self.position + self.mode

        # Add the text (special ascii)
        if isinstance(self.text, str):
            bytes += self.text.encode()
        else:
            bytes += self.text

        return bytes

