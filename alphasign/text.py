from .packet import Packet
from .command import Command

class Text:
    # Modes (aka transitions)
    class Mode:
        # Standard modes
        rotate            = b"a" # Message travels right to left
        hold              = b"b" # Message remains stationary
        flash             = b"c" # Message flashes (stationary)
        ## "d" is reserved
        roll_up           = b"e" # Previous message is pushed up
        roll_down         = b"f" # Previous message is pushed down
        roll_left         = b"g" # Pevious message is pushed left
        roll_right        = b"h" # Previous message is pushed right
        wipe_up           = b"i" # Message is wiped over from bottom to top
        wipe_down         = b"j" # Message is wiped over from top to bottom
        wipe_left         = b"k" # Message is wiped over from right to left
        wipe_right        = b"l" # Message is wiped over from left to right
        scroll            = b"m" # Message pushes the bottom line to top line (2 line signs only)
        auto              = b"o" # Various modes chosen automatically
        roll_in           = b"p" # Previous message is pushed toward to center
        roll_out          = b"q" # Previous message is pushed outward the center
        wipe_in           = b"r" # Message is wiped over inward
        wipe_out          = b"s" # Message is wiped over outward
        compressed_rotate = b"t" # Message travels right to left with chars half width (only some signs)
        explode           = b"u" # Message flies apart from center (alpha 3.0 only)
        clock             = b"v" # Message is wiped over clockwise (alpha 3.0 only)

        # Special modes
        twinkle   = b"n0" # Message twinkles
        sparkle   = b"n1" # Message sparkle over previous
        snow      = b"n3" # Message snow over previous
        interlock = b"n3" # Message interlocks with previous
        switch    = b"n4" # Alternating chars switch up/down with previous
        slide     = b"n5" # Message slides one char at a time from right to left
        spray     = b"n6" # Message sprays across from right to left
        starburst = b"n7" # Message starbursts explode

        # Animations
        anim_welcome      = b"n8" # Welcome in script font animation
        anim_thank_you    = b"nS" # Thank you in script font animation
        anim_slot_machine = b"n9" # Slot machine (random) animation
        anim_newsflash    = b"nA" # Newsflash animation
        anim_trumpet      = b"nB" # Trumpet and notes animation
        anim_cycle        = b"nC" # Color cycle (?)
        anim_no_smoking   = b"nU" # No smoking animation
        anim_drink_drive  = b"nV" # Don't drink and drive animation
        anim_animal       = b"nW" # Running animal animation
        anim_fish         = b"nW" # Fishs and shark animation
        anim_fireworks    = b"nX" # Fireworks animation
        anim_turbocar     = b"nY" # Car across the sign animation
        anim_balloons     = b"nY" # Balloons animation
        anim_cherry_bomb  = b"nZ" # Cherry bomb animation

     # Format functions
    @staticmethod
    def _temperature(type):
        return {"c": "\x08\x1C", "f": "\x08\x1D"}.get(type, "\x08\x1C") # Screw you american units

    @staticmethod
    def _date(type):
        types = {
            "mmddyy": "\x0B0",
        }

    # Text control codes
    ctrl = {
        # Double high chars
        "DH": "\x051",
        "noDH": "\x050",

        # True descenders
        "TD": "\x061",
        "noTD": "\x060",

        # Flash
        "flash": "\x071",
        "noflash": "\x070",

        # Temperature (only solar series)
        "temperature": _temperature,

        # No hold speed
        "nospeed": "\x09",

        # Date
        "date": _date,

        # New page
        "np": "\x0C",
        "nl": "\x0D",

        # Speed control (alpha 2.0 only)
        ## TODO

        # String/variable
        ## TODO

        # Wide chars
        "wide": "\x11",
        "nowide": "\x12",

        # Time
        "time": "\x13",

        # Picture
        ## TODO

        # Speed
        ## TODO

        # Font
        ## TODO

        # Colors
        "red": "\x1C1",
        "green": "\x1C2",
        "amber": "\x1C3",
        "dimred": "\x1C4",
        "dimgreen": "\x1C5",
        "brown": "\x1C6",
        "orange": "\x1C7",
        "yellow": "\x1C8",
        "rain1": "\x1C9",
        "rain2": "\x1CA",
        "mix": "\x1CB",
        "auto": "\x1CC",
        ## RGB TODO

        # Attribute
        ## TODO

        # Spacing
        "spaceprop": "\x1E0",
        "spacefixed": "\x1E1"

        # Animation
        ## TODO
    }

    def __init__(self, text):
        self.text = Text.parse(text)
        print(self.text.encode())

    @staticmethod
    def parse(text):
        text = text.replace("{{", "{").replace("}}", "}")
        return text.format_map(Text.ctrl)

    def to_bytes(self):
        return self.text

    def to_packet(self, label="A", position="0", mode=Mode.rotate):
        packet = Packet()
        packet.add_command(Command.write_text(self.to_bytes(), label, position, mode))
        return packet
