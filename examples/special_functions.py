from alphasign import Sign, Packet
from alphasign.command import WriteSpecialFunctions
import time


def send_command(sign: Sign, command: WriteSpecialFunctions, sleep_duration: int = 1):
    """Helper function to handle packet creation and sending.

    Args:
        sign (Sign): The sign object to send commands to
        command (WriteSpecialFunctions): The special function command to send
        sleep_duration (int, optional): Time to sleep after sending. Defaults to 1.
    """
    packet = Packet()
    packet.add_command(command)
    sign.send(packet)
    if sleep_duration:
        time.sleep(sleep_duration)


def main() -> None:
    """Initialize the sign connection and special functions command handler.

    Creates a Sign instance and opens a connection on /dev/ttyUSB0.
    Also creates a WriteSpecialFunctions instance that will be reused
    for all special function commands.
    """
    sign = Sign()
    sign.open(port="/dev/ttyUSB0")
    sf = WriteSpecialFunctions()  # Single instance for all operations

    # Memory allocation
    print("Configuring memory allocation for text file 'A'...")
    sf.add_memory_config(
        label="A",
        type="text",
        ir="locked",
        size=256,
        conf={"start": "1", "stop": "Z"},
    )
    print("Configuring memory allocation for graphics file 'B'...")
    sf.add_memory_config(
        label="B",
        type="dots",
        ir="locked",
        size=(32, 16),
        conf="8color",
    )
    print("Configuring memory allocation for string file 'C'...")
    sf.add_memory_config(
        label="C",
        type="string",
        ir="unlocked",
        size=128,
        conf=None,
    )
    send_command(sign, sf)

    # Execute commands
    print("Setting time to 14:30 (military time)...")
    sf.set_time_of_day(14, 30)
    send_command(sign, sf)

    print("Configuring time format to military...")
    send_command(sign, sf.set_time_format("military"))

    print("Setting daytime brightness to 72%...")
    sf.set_dimming_reg(dim=0, brightness=72)
    send_command(sign, sf)

    print("Configuring auto-dimming schedule (19:00 to 06:00)...")
    sf.set_dimming_time(start=0x19, stop=0x06)
    send_command(sign, sf)

    print("Generating beep tone...")
    sf.generate_tone(
        type=b"\x32",
        freq=0x40,
        duration=3,
        repeat=1,
    )
    send_command(sign, sf, sleep_duration=3)

    print("Displaying text 'Hello World!' at coordinates (10,5)...")
    send_command(
        sign, sf.display_text_at_xy(enabled=True, x=10, y=5, text="Hello World!")
    )

    print("Testing speaker control...")
    sf.set_speaker(enabled=True)
    send_command(sign, sf)

    print("Setting day of week to Wednesday...")
    sf.set_day_of_week("wednesday")
    send_command(sign, sf)

    print("Setting up a run time table for file 'A'...")
    sf.set_run_time_table(
        label=b"A",
        start=b"0800",  # 8:00 AM
        stop=b"1700",  # 5:00 PM
    )
    send_command(sign, sf)

    print("Setting up a run sequence...")
    sf.set_run_sequence(b"ABCA")  # Cycle through files A, B, C, A
    send_command(sign, sf)

    time.sleep(20)

    print("Performing a soft reset...")
    sf.soft_reset()
    send_command(sign, sf, sleep_duration=3)  # Keeping longer sleep for reset

    print("Clearing memory...")
    sf.clear_memory()
    send_command(sign, sf)


if __name__ == "__main__":
    main()
