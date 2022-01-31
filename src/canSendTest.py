#! /usr/bin/python

import can
can.rc['interface'] = 'socketcan_ctypes'

from can import Bus
from can import Message

def main():
    bus = Bus(channel='can1',bustype='socketcan_ctypes')

    print "Send a message..."
    msg = Message(extended_id=0,arbitration_id=0x123,is_fd=0,data=[0x01])

#    Message.extended_id = True
#    Message.is_remote_frame = False
#    Message.id_type = 1
#    Message.is_error_frame = False
#    Message.arbitration_id = 0x00E07123
#    Message.dlc = 1
#    Message.data = [0x01]
#    try:
    bus.send(msg)
#    except:
#        print "Oops something went wrong!"

if __name__ == "__main__":
    main()
