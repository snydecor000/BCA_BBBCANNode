from config import *
import time
import can
import Adafruit_CharLCD as LCD
can.rc['interface'] = 'socketcan_ctypes'

from can import Bus
from can import Message

def main():
    bus = Bus(channel='can1',bustype='socketcan_ctypes')
    lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
                                               lcd_columns, lcd_rows)

    print("Displaying received messages on the LCD")

    while True:
        recvMsg = bus.recv(timeout=1)
        #lcd.enable_display(True)
        #lcd.clear()
        lcd.home()
        if(recvMsg != None):
            strMsg = 'ID: ' + str(recvMsg.arbitration_id)
            strMsg = strMsg.ljust(16) + '\n'
            for byte in recvMsg.data:
                strMsg = strMsg + str(byte) + ' '
            lcd.message(strMsg)
            print(strMsg)
        else:
            lcd.message('ID:             \n                ')

if __name__ == "__main__":
    main()
