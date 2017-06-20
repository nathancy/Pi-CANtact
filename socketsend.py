# Script to send data using socketCAN

from pyvit import can
from pyvit.hw import socketcan

dev = socketcan.SocketCanDev("can0")
dev.start()

frame = can.Frame(0x23)
frame.data = [0x10, 0x11]
dev.send(frame)
