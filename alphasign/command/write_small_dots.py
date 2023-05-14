from ..image import Image

# Write Small Dots Picture
class WriteSmallDots:
    code = b"I"

    def __init__(self, picture, label="0", width=0, height=0, compress=False):
        # Image label ("file")
        self.label = label

        # Picture data (from an Image or raw bytes)
        self.picture = picture.conv if isinstance(picture, Image) else picture
        self.width = picture.width if isinstance(picture, Image) else width
        self.height = picture.height if isinstance(picture, Image) else height

        # Compress the image?
        self.compress = compress

        # Checksum?
        self.checksum = False

    # FIXME: doesn't seems to work, but only because is small dots
    def compress_picture(self):
        bytes = b""

        cur_color = b"" #self.picture[0].to_bytes()
        cur_nb = 0
        for byte in self.picture:
            byte = byte.to_bytes()
            # If we changed color
            if byte != cur_color and byte != b"\x0D":
                # Check if we can compress it (useless before 4bytes)
                if cur_nb > 4:
                    bytes += b"\x11" + f"{cur_nb:02X}".encode() + cur_color
                elif cur_nb > 0: # it's useless to compress, just add the colors
                                 # the >0 check is only for the first iteration
                    bytes += cur_color * cur_nb

                cur_color = byte
                cur_nb = 0
                cur_nb += 1
            elif byte == b"\x0D":
                #if cur_nb != 0:
                #    bytes += cur_color * cur_nb
                bytes += cur_color * cur_nb + b"\x0D"
            else:
                cur_nb += 1
        return bytes

    def to_bytes(self):
        # A Write command sends a small dots picture.
        # it starts with the label
        bytes = self.label.encode()

        # Add the height and width
        bytes += f"{self.height:02X}{self.width:02X}".encode()

        # Insert FF byte for 100ms delay
        bytes += b"\xFF"

        # Add the picture (in ascii)
        bytes += self.picture #self.compress_picture() if self.compress else self.picture

        return bytes
