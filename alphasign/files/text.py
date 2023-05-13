

class TextFile:
    ESC = b"\x1B"

    # Text position (for multi-line signs only)
    # Mandatory but ignored on single-line signs
    class Position:
        middle_line = b"\x20"
        top_line = b"\x22"
        bottom_line = b"\x26"
        fill = b"\x30"
        left = b"\x31"
        right = b"\x32"

    class Mode:
        # 

    def __init__(self, position, mode, msg):
        self.position = position
        self.mode = mode
        self.msg = msg

    def to_bytes(self):
        bytes = ESC + 
