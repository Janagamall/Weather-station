from Adafruit_GPIO import I2C
import Adafruit_SSD1306
from PIL import Image, ImageDraw, ImageFont

# Initialize OLED Display
disp = Adafruit_SSD1306.SSD1306_128_32(rst=None)
disp.begin()
disp.clear()
disp.display()

def update_display(temperature, humidity):
    width, height = disp.width, disp.height
    image = Image.new('1', (width, height))
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()
    
    draw.text((0, 0), f"Temp: {temperature}°C", font=font, fill=255)
    draw.text((0, 15), f"Humidity: {humidity}%", font=font, fill=255)
    
    disp.image(image)
    disp.display()
