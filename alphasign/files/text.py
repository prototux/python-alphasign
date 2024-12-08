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
        rotate = b"a"
        hold = b"b"
        flash = b"c"
        roll_up = b"e"
        roll_down = b"f"
        roll_left = b"g"
        roll_right = b"h"
        wipe_up = b"i"
        wipe_down = b"j"
        wipe_left = b"k"
        wipe_right = b"l"
        scroll = b"m"
        auto = b"o"
        roll_in = b"p"
        roll_out = b"q"
        wipe_in = b"r"
        wipe_out = b"s"
        compressed_rotate = b"t"
        twinkle = b"n0"
        sparkle = b"n1"
        snow = b"n2"
        interlock = b"n3"
        switch = b"n4"
        slide = b"n5"
        spray = b"n6"
        starburst = b"n7"
        welcome = b"n8"
        slot_machine = b"n9"

    def __init__(self, position, mode, msg):
        self.position = position
        self.mode = mode
        self.msg = msg

    def to_bytes(self):
        # Format: ESC + position + mode + message + EOT
        return self.ESC + self.position + self.mode + self.msg.encode('ascii') + b'\x04'
