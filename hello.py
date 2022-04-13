"""
hello.py

    Writes "Hello!" in random colors at random locations on the display

"""
import random
import board
import gc9a01py as gc9a01
import digitalio

# Choose a font

# from fonts import vga1_8x8 as font
# from fonts import vga2_8x8 as font
# from fonts import vga1_8x16 as font
# from fonts import vga2_8x16 as font
# from fonts import vga1_16x16 as font
# from fonts import vga1_bold_16x16 as font
# from fonts import vga2_16x16 as font
# from fonts import vga2_bold_16x16 as font
# from fonts import vga1_16x32 as font
# from fonts import vga1_bold_16x32 as font
# from fonts import vga2_16x32 as font
import gc9a01py.fonts.vga1_16x16 as font

class Pin:
    def __init__(self, pin: int):
        self.pin = digitalio.DigitalInOut(pin)
        self.pin.direction = digitalio.Direction.OUTPUT
    
    def off(self):
        self.pin.value = False
    
    def on(self):
        self.pin.value = True
    
    def value(self, value: int):
        self.pin.value = value


def main():
    spi = board.SPI()
    tft = gc9a01.GC9A01(
        spi,
        dc=Pin(board.D25),
        cs=Pin(board.CE0),
        reset=Pin(board.D5),
        backlight=Pin(board.D24),
        rotation=0,
    )

    while True:
        for rotation in range(8):
            tft.rotation(rotation)
            tft.fill(0)
            col_max = tft.width - font.WIDTH*6
            row_max = tft.height - font.HEIGHT

            for _ in range(25):
                tft.text(
                    font,
                    "Hello!",
                    random.randint(0, col_max),
                    random.randint(0, row_max),
                    gc9a01.color565(
                        random.getrandbits(8),
                        random.getrandbits(8),
                        random.getrandbits(8),
                    ),
                    gc9a01.color565(
                        random.getrandbits(8),
                        random.getrandbits(8),
                        random.getrandbits(8),
                    )
                )


main()
