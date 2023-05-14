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
