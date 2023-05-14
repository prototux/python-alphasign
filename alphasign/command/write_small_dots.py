from ..image import Image

# Write Small Dots Picture
class WriteSmallDots:
    code = b"I"

    def __init__(self, picture, label="A", width=0, height=0):
        # Image label ("file")
        self.label = label

        # Picture data (from an Image or raw bytes)
        self.picture = picture.conv if isinstance(picture, Image) else picture
        self.width = picture.width if isinstance(picture, Image) else width
        self.height = picture.height if isinstance(picture, Image) else height

        # Checksum?
        self.checksum = False

    def to_bytes(self):
        # A Write command sends a small dots picture.
        # it starts with the label
        bytes = self.label.encode()

        # Add the height and width
        bytes += f"{self.height:02X}{self.width:02X}".encode()

        # Insert FF byte for 100ms delay
        bytes += b"\xFF"

        # Add the picture (in ascii)
        bytes += self.picture

        return bytes
