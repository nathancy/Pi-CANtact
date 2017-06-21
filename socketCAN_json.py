# Script to check if data on line matches json data id

from pyvit.hw import socketcan
from pyvit.file.db import jsondb
from pyvit import bus

DEBUG = False 

# Open json file
parser = jsondb.JsonDbParser()
frames = parser.parse('commands_db.json')

if DEBUG:
    print("--- Sending Frames --- ")
    print(frames)

# Initialize socketcan
dev = socketcan.SocketCanDev("can0")
dev.start()

while True:
    frame = dev.recv()
    signals = frames.parse_frame(frame)
    print('-' * 60)
    
    if DEBUG:
        print("--- Received frames ---")
        print("Received frame is", frame)

    # Checks if json data id matches recevied frame
    if signals:
        for signal in signals:
            print(signal)
    

