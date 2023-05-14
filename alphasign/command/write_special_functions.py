# Write Text command, sends one or multiple text field
class WriteSpecialFunctions:
    code = b"E"

    def __init__(self):
        self.label = b""
        self.data = b""

        # Checksum?
        self.checksum = False

    # Each special function has it's own function here
    def set_time_of_day(self, hours, minutes):
        self.label = b"\x20"

    def set_speaker(self, enabled):
        self.label = b"\x21"
        self.data = b"00" if enabled else b"FF"

    def clear_memory(self):
        pass

    def set_memory_config(self):
        pass

    def set_day_of_week(self, day):
        self.label = b"\x26"
        days = {
            "sunday": b"1",
            "monday": b"2",
            "tuesday": b"3",
            # todo
        }
        self.data = days.get(day, "2")

    def set_time_format(self, format):
        self.label = b"\x27"
        self.data = "M" if format == "military" else "S"

    def generate_tone(self, type, freq=0, duration=5, repeat=0):
        self.label = b"\x28"
        self.data = type
        if type == b"\x32":
            self.data += f"{freq:02X}{duration:1X}{repeat:1X}".encode()

    def set_rune_time_table(self, label, start, stop):
        self.label = b"\x29"
        self.data = label + start + stop

    def soft_reset(self):
        self.label = b"\x2C"

    def set_run_sequence(self, sequence):
        self.label = b"\x2E"
        self.data = sequence

    def to_bytes(self):
        # Do not return anything if there's no command
        if not self.label:
            return

        # This one is simple: label (function) and it's data (parameters)
        bytes = self.label + self.data

        return bytes

