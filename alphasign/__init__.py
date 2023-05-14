# Helper defines

## Sign data
from .sign import Sign
Sign = Sign
from .type import SignType
SignType = SignType

## Type class
from .text import Text
Text = Text
from .image import Image
Image = Image

## Easy classes
from .easy import Easy
Easy = Easy

## Packet and command
from .packet import Packet
Packet = Packet
from .command import Command
Command = Command

# Main Class
class AlphaSign:
    def __init__(self, type=SignType.All, port=None):
        # Set the sign type
        self.sign = Sign(type=type)

        # Directly open the sign
        self.sign.open(port)
