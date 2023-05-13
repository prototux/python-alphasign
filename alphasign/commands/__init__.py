from .write_text import WriteText
from .write_small_dots import WriteSmallDots
from .write_special_functions import WriteSpecialFunctions

# just a list of commands as attributes
class Command:
    write_text = WriteText
    write_small_dots = WriteSmallDots
    write_special_functions = WriteSpecialFunctions


# Commands code
WRITE_TEXT                 = b"A" # Write TEXT file
READ_TEXT                  = b"B" # Read TEXT file
WRITE_SPECIAL              = b"E" # Write special function commands
READ_SPECIAL               = b"F" # Read special function commands
WRITE_STRING               = b"G" # Write STRING file
READ_STRING                = b"H" # Read STRING file
WRITE_SMALL_DOTS           = b"I" # Write SMALL DOTS PICTURE file
READ_SMALL_DOTS            = b"J" # Read SMALL DOTS PICTURE file
WRITE_RGB_DOTS             = b"K" # Unsupported (RGB DOTS PICTURE file)
READ_RGB_DOTS              = b"L" # Unsupported (RGB DOTS PICTURE file)
WRITE_LARGE_DOTS           = b"M" # Unsupported (LARGE DOTS PICTURE file)
READ_LARGE_DOTS            = b"N" # Unsupported (LARGE DOTS PICTURE file)
WRITE_ALPHAVISION_BULLETIN = b"O" # Unsupported (ALPHAVISION BULLETIN message)
SET_TIMEOUT_MESSAGE        = b"T" # Unsupported (Set Timeout Message)
