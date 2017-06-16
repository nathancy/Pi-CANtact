from pyvit import can
from pyvit.hw import socketcan

dev = socketcan.SocketCanDev("can0")

dev.start()
while True:
    print(dev.recv())
