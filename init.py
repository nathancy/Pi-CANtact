# Init scripts to enable socketCAN
# python init.py

from subprocess import call

call(['sudo', 'modprobe', 'can'])
call(['sudo', 'modprobe', 'slcan'])
call(['sudo', 'slcand', '-o', '-c', '-s6', '/dev/ttyACM0', 'can0'])
call(['sudo', 'ifconfig', 'can0', 'up'])
call(['sudo', 'ifconfig', 'can0', 'txqueuelen', '10000'])
