from ._common import SignDef


class Alpha4200C(SignDef):
    # Base infos
    name = "Alpha 4200C"
    desc = "Alpha 4200C"

    # Size
    width = 200
    height = 16

    # Type of display
    type = "RGY"

    # Connection
    connection = "serial"
    default_baudrate = 9600

    # Supported features
    features = ["BEEP"]
