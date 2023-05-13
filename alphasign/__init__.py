import serial
import time

from .packet import Packet
from .commands import Command

from .images import Image
Image = Image

class AlphaSign:
    def __init__(self, port, baudrate=9600, address='00'):
        self.port = port
        self.baudrate = baudrate
        self.address = address
        self.ser = serial.Serial(port, baudrate, timeout=1)

    # Advanced functions (for more complex commands)
    def init_packet(self, type="Z", address="00"):
        return Packet(type, address)

    def send_packet(self, packet):
        bytes = packet.to_bytes()
        parts = bytes.split(b"\xFF")

        for part in parts:
            self.ser.write(part)
            time.sleep(0.1)

    # Helper functions (for one-liners)
    def send_text(self, text, mode="a"):
        packet = Packet() # Default type and address here
        packet.add_command(Commands.write_text(text, label="0", mode=mode))
        self.send_packet(packet)

    def send_img(self, img, width=0, height=0, label="A"):
        # Send image first, then calls the text for that image
        packet = Packet() # Default type and address here
        packet.add_command(Commands.write_small_dots(img, label=label, width=width, height=height))
        #packet.add_command(Commands.write_text("\x14A", mode="b", label="0"))
        self.send_packet(packet)

        #time.sleep(2)
        packet = Packet()
        packet.add_command(Commands.write_text(f"\x14{label}".encode(), mode="b", label="A"))
        self.send_packet(packet)

        #time.sleep(1)
        #packet = Packet()
        #cmd = Commands.write_special_functions()
        #cmd.set_run_sequence(b"SUA")
        #packet.add_command(cmd)
        #self.send_packet(packet)

    def enable_buzzer(self):
        packet = Packet() # Default type and address here
        beep = Commands.write_special_functions()
        #beep.generate_tone(b"\x41")
        beep.set_speaker(True)
        packet.add_command(beep)
        self.send_packet(packet)

        #packet = Packet() # Default type and address here
        #beep = Commands.write_special_functions()
        #beep.generate_tone(b"\x31")
        #packet.add_command(beep)
        #self.send_packet(packet)



    def beep(self, freq, duration=5, repeat=0):
        packet = Packet() # Default type and address here
        beep = Commands.write_special_functions()
        beep.generate_tone(b"\x32", freq, duration, repeat)
        packet.add_command(beep)
        self.send_packet(packet)

    def close(self):
        self.ser.close()
