from pyvit import can
from pyvit.hw import socketcan
import sys

def frame_dec(frame):
    print("Frame ID is", frame.arb_id)
    print("Frame data is", frame.data)
    print("Frame DLC is", frame.dlc)
    print("-" * 60)
def frame_hex(frame):
    print("Frame ID is", hex(frame.arb_id))
    hex_data = []
    for data in frame.data:
        hex_data.append(hex(data))
    print("Frame data is", hex_data)
    print("Frame DLC is", hex(frame.dlc))
    print("-" * 60)

# Check for current argument input
if len(sys.argv) is not 2:
    print('''
    Usage: python socketCAN.py [options]
    Mode options: -h        (Hex)
                  -d        (Decimal)
    Examples:
    python socketCAN.py -h  (Data in hex format)
    python socketCAN.py -d  (Data in decimal format)
        ''')
    sys.exit()

# Init socketcan
dev = socketcan.SocketCanDev("can0")
dev.start()
while True:
    frame = dev.recv()
    # Print in decimal
    if(sys.argv[1] == '-d'):
        frame_dec(frame)
    # Print in hex
    if(sys.argv[1] == '-h'):
        frame_hex(frame)
       
