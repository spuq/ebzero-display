from luma.core.interface.serial import i2c
from luma.oled.device import ssd1306
from PIL import Image, ImageDraw, ImageFont
import socket
import time

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        # doesn't even have to be reachable
        s.connect(('10.254.254.254', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP


# Use I2C bus 0 (HAT EEPROM pins)
serial = i2c(port=0, address=0x3C)
device = ssd1306(serial, width=128, height=64)

# Create blank image for drawing
#image = Image.new("1", (device.width, device.height))
image = Image.open("/home/spuq/python/Edgeberry_Zero_display_128x64.png") \
             .convert("1") \
             .resize((device.width, device.height))
draw = ImageDraw.Draw(image)

while True:
  # Draw something
  #draw.rectangle((0, 0, device.width-1, device.height-1), outline=255, fill=0)
  #draw.text((11, 0), "EDGEBERRY", font=ImageFont.load_default(20), fill=255)
  #draw.text((91, 18), "ZERO", font=ImageFont.load_default(13), fill=255)
  draw.text((10, 40), "IP address:", font=ImageFont.load_default(), fill=255)
  draw.text((10, 52), get_ip(), font=ImageFont.load_default(), fill=255)

  # Display image
  device.display(image)
  time.sleep(15)

