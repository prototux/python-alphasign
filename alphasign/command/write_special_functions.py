# Write Text command, sends one or multiple text field
class WriteSpecialFunctions:
    code = b"E"

    def __init__(self):
        self.label = b""
        self.data = b""

        # Memory configs
        self.memory_configs = []

        # Checksum?
        self.checksum = False

    # Each special function has it's own function here
    def set_time_of_day(self, hours, minutes):
        self.label = b"\x20"
        self.data = f"{hours:02d}{minutes:02d}".encode()

    def set_speaker(self, enabled):
        self.label = b"\x21"
        self.data = b"00" if enabled else b"FF"

    def clear_memory(self):
        self.label = b"\x24"
        self.data = b""

    def add_memory_config(self, label, type, ir, size, conf):
        self.label = b"\x24"

        # Label of file to configure
        config = label.encode()

        # Type of file to configure
        types = { "text": b"\x41", "string": b"\x42", "dots": b"\x43" }
        config += types.get(type, "\x41")

        # IR Keyboard protection status
        key = { "unlocked": b"\x55", "locked": b"\x4C" }
        config += key.get(ir, "\x4C")

        # Size (in bytes or in image size. WARN: image size is inverted, it's y*x natively)
        config += f"{size[1]:02X}{size[0]:02X}".encode() if isinstance(size, tuple) else f"{size:04X}".encode()

        # Type-specific config
        if type == "text":
            config += f"{conf['start']}{conf['stop']}".encode()
        elif type == "string":
            config += b"0000"
        elif type == "dots":
            colors = { "monochrome": b"1000", "3color": b"2000", "8color": b"8000" }
            config += colors.get(conf, "\x8000")
        else:
            print("ERROR: unknown type")

        self.memory_configs.append(config)


    def set_day_of_week(self, day):
        self.label = b"\x26"
        days = {
            "sunday": b"\x31",
            "monday": b"\x32",
            "tuesday": b"\x33",
            "wednesday": b"\x34",
            "thursday": b"\x35",
            "friday": b"\x36",
            "saturday": b"\x37",
        }
        self.data = days.get(day, b"\x32")

    def set_time_format(self, format):
        self.label = b"\x27"
        self.data = b"M" if format == "military" else b"S"

    def generate_tone(self, type, freq=0, duration=5, repeat=0):
        self.label = b"\x28"
        self.data = type
        if type == b"\x32":
            self.data += f"{freq:02X}{duration:1X}{repeat:1X}".encode()

    def set_run_time_table(self, label, start, stop):
        self.label = b"\x29"
        self.data = label + start + stop

    def display_text_at_xy(self, enabled, x, y, text):
        self.label = b"\x2B"
        status = "\x2B" if enabled else "\x2D"
        file = "\x2B" # Apparently mandatory?
        self.data = f"{status}{file}{x:02}{y:02}{text}".encode()

    def soft_reset(self):
        self.label = b"\x2C"

    def set_run_sequence(self, sequence):
        self.label = b"\x2E"
        self.data = sequence

    def set_dimming_reg(self, dim, brightness):
        self.label = b"\x2F"

        # Get index level closest to brightness
        level = min([100, 86, 72, 58, 44], key=lambda x:abs(x-brightness))
        index = [100, 86, 72, 58, 44].index(level)

        self.data = f"{dim:02X}{index:02}".encode()

    def set_dimming_time(self, start, stop):
        self.label = b"\x2F"
        self.data = f"{start:02X}{stop:02X}".encode()


    def to_bytes(self):
        # Do not return anything if there's no command
        if not self.label:
            return

        # This one is simple: label (function) and it's data (parameters)
        if self.label == "\x24" and self.memory_configs:
            bytes = self.label + self.data
        else:
            bytes = self.label
            for config in self.memory_configs:
                bytes += config

        return bytes

