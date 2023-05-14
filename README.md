# python-alphasign

## What is it

This is a python 3 library that implements the "Alpha® Sign Communications Protocol" as defined [On alphasign website](https://alpha-american.com/p-alpha-communications-protocol.html).

This was tested on an Alpha 210C sign, and should works with other signs (like the BetaBrite) as well.

Documentation is available in the `docs/` dir

## Quickstart/Easy guide

python-alphasign implements so-called Easy classes, which enables easy functions to send text, show images and other functions easily.

Examples are available in examples/ (easy demos starts with `easy_`)

## TODO

* Implement proper text parsing for special chars and modifiers
* Implement features checks (for alpha 2.0 and 3.0 protocols, and sign-specific features)
* Implement LARGE DOTS, RGB DOTS and ALPHAVISION BULLETIN commands
* Implement image compression
* Implement read functions
* Implement counters and date
* Fix bug where first image sent isn't shown (it works when image is "created" manually, even if no such thing exists in the documentation)

## Notes

* The "ASCII PRINTABLE" formats (2 and 3 bytes) aren't used because we can raw bytes
* * This mode was designed for POCSAG pagers, which can't send bytes < 0x20
