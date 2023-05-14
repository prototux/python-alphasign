#!/usr/bin/env python3

## Simple hello world message
from alphasign import AlphaSign, Easy

sign = AlphaSign(port='/dev/ttyUSB0')
Easy.Text.show('Hello World!')

