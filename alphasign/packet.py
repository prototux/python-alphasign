
# Implements the "Standard Transmission Packet" aka "1-byte"/"^A"
# This doesn't implement the multiple type code and address (no use for it)
class Packet:
    def __init__(self, type="Z", address="00"):
        # Type and address of sign(s) to target
        self.type = type.encode()
        self.addr = address.encode()

        # Commands within that packet
        self.commands = []

    def checksum(self, command):
        data = b"\x02" + command.code + command.to_bytes() + b"\x03"
        checksum = sum(data) % 65536
        return f"{checksum:04X}".encode()

    def add_command(self, cmd):
        self.commands.append(cmd)

    def to_bytes(self):
        # Packet sync (5 NUL bytes)
        # (could also be 5 0x01/SOH bytes)
        bytes = b"\x00\x00\x00\x00\x00"

        # SOH (Start Of Header) byte + Type code + Sign address
        bytes += b"\x01" + self.type + self.addr

        # Single or nested commands, with or without checksum
        for cmd in self.commands:
            # STX (Start of TeXt) byte + Command code + data field
            # Also adding a FF byte for sleep
            bytes += b"\x02\xFF" + cmd.code + cmd.to_bytes()

            ## If there's either a checksum or nested packed, we need the ETX byte
            if cmd.checksum or len(self.commands) > 1:
                # ETX (End of TeXt) byte
                bytes += b"\x03"

                # Checksum comes after the ETX byte
                if cmd.checksum:
                    bytes += self.checksum(cmd)

        # EOT (End Of Transmission) byte
        bytes += b"\x04"

        return bytes
