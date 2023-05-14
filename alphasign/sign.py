import serial
import time

from .singleton import Singleton
from .type import SignType
from .packet import Packet

class Sign(metaclass=Singleton):

    def __init__(self, type=SignType.All, address="00"):
        # Update self with properties from type class
        self.update_type(type)

        # Add address
        self.address = address

    # Open serial or usb port
    def open(self, port=None, **kwargs):
        if self.connection == 'serial':
            self._ser = serial.Serial(port, self.default_baudrate, timeout=1)
        else:
            print("ERROR: no connection type?!?")

    def update_type(self, type):
        # Copy type's attributes as own
        props = [x for x in dir(type) if not x.startswith("__")]
        for prop in props:
            setattr(self, prop, getattr(type, prop))

    # Actually sends data
    def write(self, data):
        if self.connection == 'serial' and self._ser:
            self._ser.write(data)
        else:
            print(f"ERROR sending data to {self.connection} link")

    # Send either raw data or packet, with pauses
    def send(self, data):
        # Packet or raw
        bytes = data.to_bytes() if isinstance(data, Packet) else data

        parts = bytes.split(b"\xFF")
        for part in parts:
            self.write(part)
            time.sleep(0.1)


    # TODO: be able to parse and send Packet back
    def read(self, raw=True):
        if raw:
            return self._ser.read()

    def close(self):
        self._ser.close()
