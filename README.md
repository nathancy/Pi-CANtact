# Pyvit-CANtact

Scripts to interface with CAN bus devices using CANtact and Pyvit

Note: uses can0 and /dev/ttyACM0

Initialize CANtact with:
```
python init.py
```

To display messages on the bus in realtime (Frame ID, packet data): 
```
python socketCAN.py [options]
```

To display messages on the bus filtered by IDs according to packets in comands_db.json. Scans bus only for IDs in .json file.
```
python socketCAN_json.py 
```

To send a single CAN frame onto the bus:
``` 
cansend can0 123#1122334455667788
```
will send a message on interface `can0` with identifier `0x123` and data bytes `[0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77, 0x88]`. This too assumes values are given in decimal.

To send CAN frames onto the bus using scripts:
```
python socketsend.py
```

To request sensor queries according to OBD command tables:
```
python obd_query.py
```

To generate random CAN data, useful for testing:
```
cangen can0
```


