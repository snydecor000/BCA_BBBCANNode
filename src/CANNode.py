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

    error = 1
    non_error = 0

    print("Displaying received messages on the LCD")

    while True:
        try:
            recvMsg = bus.recv(timeout=1)

            #lcd.enable_display(True)
            #lcd.clear()
            lcd.home()
            if(recvMsg != None):
                if(recvMsg.arbitration_id==409):
                    strMsg = 'ID: ' + str(recvMsg.arbitration_id)
                    strMsg = strMsg+' Acc: '+str(int(100*non_error/(error+non_error)))+'%'
                    strMsg = strMsg.ljust(16) + '\n'
                    #for byte in recvMsg.data:
                    #    strMsg = strMsg + str(byte) + ' '
                    strMsg = strMsg + str(error) + ' ' + str(non_error)
                    lcd.message(strMsg)
                    print(strMsg)
                    non_error = non_error + 1
                else:
                    strMsg = 'ID: ' + str(recvMsg.arbitration_id) + '\n'
                    for byte in recvMsg.data:
                        strMsg = strMsg + str(byte) + ' '
                    print(strMsg)
                    error = error+1
            else:
                lcd.message('ID:             \n                ')
                
        except can.CanError:
            error = error+1
            print('There was an error')

if __name__ == "__main__":
    main()
