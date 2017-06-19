from pyvit import can
from pyvit.hw import socketcan

dev = socketcan.SocketCanDev("can0")
dev.start()

frame = can.Frame(0x123)
frame.data = [0x10, 0x11]
dev.send(frame)
