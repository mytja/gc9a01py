# gc9a01py

A fork of [Russ Hughes' awesome library for MicroPython](https://github.com/russhughes/gc9a01py).

# Why was this fork even created in first place?
[Russ Hughes](https://github.com/russhughes) has created an amazing library for controlling GC9A01 based displays, but is only compatible with MicroPython on microcontrollers, such as RP2 (Raspberry Pi Pico). Due to several projects of mine, that were based on this TFT display and had to be ran on Raspberry Pi 3B+, I had to look for a library to drive it with CircuitPython. [These libraries for CircuitPython](https://github.com/tylercrumpton/CircuitPython_GC9A01) certainly existed, but due to several issues with [DisplayIO/Adafruit Blinka](https://github.com/adafruit/Adafruit_Blinka_Displayio/issues/84) couldn't be used on Raspberry Pi 3B+ or other Linux based SoC-s. Many of these SoC-s don't support `displayio`, which is such an important library and should be supported on all SoC-s, but it just isn't.

This library doesn't use `displayio`, but rather uses direct SPI communication with TFT display.

I've also added a compatibility layer for this library, so that it can be used directly in CircuitPython and MicroPython.
Compatibility layer should be used like this:
```py
from gc9a01.circuitpython import *
```
Afterwards, you can use this library just like you would on MicroPython.

