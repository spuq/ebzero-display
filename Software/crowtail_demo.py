#import board
#import digitalio
#from PIL import Image, ImageDraw, ImageFont
#import adafruit_ssd1306
from edgeberry import Edgeberry
from gpiozero import PWMLED, MCP3008, LED
from time import sleep

# Create the Edgeberry object
edgeberry = Edgeberry()

# Available methods
edgeberry.set_application_info("Crowtail-demo", "1.0", "A simple demo with Crowtail modules")    # Called when the program (re)starts
edgeberry.set_status("ok", "Everything's fine!")


#create an object called pot that refers to MCP3008 channel 0
pot = MCP3008(0)

#create a PWMLED object called led that refers to GPIO 14
led = PWMLED(12)
max_indicator = LED(13)     # Digital output 3
min_indicator = LED(25)     # Digital output 4

# Initialize OLED display dimensions
#WIDTH = 128
#HEIGHT = 64

# Set up I2C communication with the OLED display
#i2c = board.I2C()  # Utilizes board's SCL and SDA pins
#oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x3C)

# Clear the OLED display
#oled.fill(0)
#oled.show()

# Create a new image with 1-bit color for drawing
#image = Image.new("1", (oled.width, oled.height))

# Obtain a drawing object to manipulate the image
#draw = ImageDraw.Draw(image)

# Draw a filled white rectangle as the background
#draw.rectangle((0, 0, oled.width, oled.height), outline=255, fill=255)

# Define border size for an inner rectangle
#BORDER = 1
# Draw a smaller black rectangle inside the larger one
#draw.rectangle(
#    (BORDER, BORDER, oled.width - BORDER - 1, oled.height - BORDER - 1),
#    outline=0,
#    fill=0,
#)

# Load the default font for text
#font = ImageFont.load_default()

#def getfontsize(font, text):
    # Calculate the size of the text in pixels
#    left, top, right, bottom = font.getbbox(text)
#    return right - left, bottom - top

# Define the text to be displayed
#text = "EDGEBERRY"
# Get the width and height of the text in pixels
#(font_width, font_height) = getfontsize(font, text)
# Draw the text, centered on the display
#draw.text(
#    (oled.width // 2 - font_width // 2, oled.height // 2 - font_height),
#    text,
#    font=font,
#    fill=255,
#)
#text = "  ZERO"
#draw.text(
#    (oled.width // 2, oled.height // 2 + font_height//2),
#    text,
#    font=font,
#    fill=255,
#)

# Send the image to the OLED display
#oled.image(image)
#oled.show()

while True:
    analog = round(pot.value, 2)
    if(analog < 0.001):
        led.value = 0
    else:
        led.value = analog
    #print(analog)

    # Maximum indication
    if(analog > 0.85):
        max_indicator.on()
    else:
        max_indicator.off()

    # Minimum indication
    if(analog < 0.15):
        min_indicator.on()
    else:
        min_indicator.off()

    sleep(0.1)

