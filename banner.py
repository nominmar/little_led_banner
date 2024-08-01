import time
import random

import unicornhat as uh

from alphabet import alphabet

uh.set_layout(uh.PHAT)
uh.brightness(0.5)

# Set lower range of R, G, B values
lower_range = 100

def center_text() -> tuple:
    """Center the text on the Unicorn HAT (assuming at least 4x4 characters)"""
    width, height = uh.get_shape()
    offset_x = (width//2)-2 if width > 4 else 0
    offset_y = (height//2)-2 if height > 4 else 0
    return offset_x, offset_y


# Function to display a character
def display_char(char: str):
    """Display a character on the Unicorn HAT with a random color"""
    uh.clear()
    offset_x, offset_y = center_text()

    if char in alphabet:
        for x, y in alphabet[char.upper()]:
            uh.set_pixel(x+offset_x, y+offset_y, random.randint(lower_range, 255), 
                         random.randint(lower_range, 255), 
                         random.randint(lower_range, 255))
    uh.show()

def display_text(text):
    """Display text on the Unicorn HAT one character at a time"""
    for char in text:
        display_char(char)
        time.sleep(0.5)

    uh.clear()
    uh.show()

if __name__ == '__main__':
    text = input("Enter text to display: ")
    display_text(text.upper())
    