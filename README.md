# python-alphasign

## What is it

This is a python library that implements the "Alpha® Sign Communications Protocol" as defined [On alphasign website](https://alpha-american.com/p-alpha-communications-protocol.html).

This currently only supports the Alpha 1.0 (EZ95) protocol, as I don't own any device with the Alpha 2.0 and 3.0 protocols, nor any device with the EZKEY II protocol.

This was tested on an Alpha 210C sign, and should works with other signs (like the BetaBrite) as well.

## Quickstart guide

TODO

## Notes/Unsupported features

* The "ASCII PRINTABLE" formats (2 and 3 bytes) aren't used because we can raw bytes
* * This mode was designed for POCSAG pagers, which can't send bytes < 0x20
* The LARGE DOTS, RGB DOTS and ALPHAVISION BULLETIN aren't supported (my sign doesn't support these)
* The Alpha 2.0 and 3.0 protocols aren't supported as well for the same reasons
* Nesting isn't supported yet, this may change in the future
* * Nesting allows sending multiple commands in one packet, this removes a 8 bytes overhead when sending successive packets
