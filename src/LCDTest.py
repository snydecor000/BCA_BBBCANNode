import Adafruit_CharLCD as LCD
from config import *

# Initialize the LCD using the pins from the config file.
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
                                           lcd_columns, lcd_rows)

# Print a two line message
lcd.message('Hello\nworld!')
