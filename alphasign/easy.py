from .sign import Sign
from .packet import Packet
from .command import Command
from .image import Image

# Easy commands
class Easy:

    class Text:
        # Easy print text
        @staticmethod
        def show(text):
            # Send text immediately on priority label
            packet = Packet()
            packet.add_command(Command.write_text(text, label="0"))
            Sign().send(packet)

    class Image:
        @staticmethod
        def show(path, img_label="A"):
            # Load and convert image
            img = Image(path)

            # Send image
            packet = Packet()
            packet.add_command(Command.write_small_dots(img, label=img_label))
            Sign().send(packet)

            # Send text to show image
            packet = Packet()
            packet.add_command(Command.write_text(f"\x14{img_label}", mode="b", label="0"))
            Sign().send(packet)

    class Buzzer:
        @staticmethod
        def enable():
            packet = Packet()
            command = Command.write_special_functions()
            command.set_speaker(True)
            packet.add_command(command)
            Sign().send(packet)

        @staticmethod
        def beep(freq, duration=5, repeat=0):
            packet = Packet()
            beep = Command.write_special_functions()
            beep.generate_tone(b"\x32", freq, duration, repeat)
            packet.add_command(beep)
            Sign().send(packet)
