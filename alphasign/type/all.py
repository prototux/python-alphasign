from ._common import SignDef

class All(SignDef):
    # Base infos
    name = "All"
    desc = "All"
    type_byte = "Z"

    # Size
    width = 255
    height = 255

    # Type of display
    type = "RGB"

    # Connection
    connection = "serial"
    default_baudrate = 9600

    # Supported features
    features = [
        "BEEP"
    ]
