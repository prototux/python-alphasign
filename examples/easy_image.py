#!/usr/bin/env python3

## Simple hello world image
from alphasign import AlphaSign, Easy

sign = AlphaSign(port='/dev/ttyUSB0')
Easy.Image.show("test.png")
