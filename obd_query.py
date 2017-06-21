import obd
import sys 

# Set debug "True" if not connected to OBD
# Set debug "False" for testing
DEBUG = False 

#OBD commands used to query 

'''
#  PID         Description                            Return value

0  00 PIDS_A - Supported PIDs [01-20]                 (bitarray)
1  03 FUEL_STATUS - Fuel system status                (string)
2  04 ENGINE_LOAD - Calculated engine load            (unit.percent)
3  05 COOLANT_TEMP - Engine coolant temperature       (unit.celsius)
4  0A FUEL_PRESSURE - Fuel pressure                   (unit.kilopascals)
5  0B INTAKE_PRESSURE - Intake manifold pressure      (unit.kilopascals)
6  0C RPM - Engine RPM                                (unit.rpm)
7  0D SPEED - Vehicle speed                           (unit.kph)
8  0F INTAKE_TEMP - Intake air temp                   (unit.celsius)
9  10 MAF - Air flow rate                             (unit.grams_per_second)
10 11 THROTTLE_POS - Throttle position                (unit.percent)
11 12 AIR_STATUS - Secondary air status               (string)
12 13 O2_SENSORS - O2 sensors present                 (special tuple)
13 14 O2_B1S1 - Bank 1 Sensor 1 voltage               (unit.volt)
14 1F RUN_TIME - Engine runtime                       (unit.second)
15 20 PIDS_B - Supported PIDs [21-40]                 (bitarray)
16 21 DISTANCE_W_MIL - Distance traveled with MIL on  (unit.kilometer)
17 22 FUEL_RAIL_PRESSURE_VAC - Fuel rail pressure     (unit.kilopascals)
18 2F FUEL_LEVEL - Fuel level input                   (unit.percent)
19 32 EVAP_VAPOR_PRESSURE - Evaporative system pres   (unit.pascal)
20 33 BAROMETRIC_PRESSURE - Barometric pressure       (unit.kilpascal)
21 34 O2_S1_WR_CURRENT - 02 sensor 1 WR current       (unit.milliamp)
22 3C CATALYST_TEMP_B1S1 - Temperature                (unit.celsius)
23 42 CONTROL_MODULE_VOLTAGE - Control module voltage (unit.volt)
24 43 ABSOLUTE_LOAD - Absolute load value             (unit.percent)
25 45 RELATIVE_THROTTLE_POS - Relative throttle pos   (unit.percent)
26 46 AMBIANT_AIR_TEMP - Ambiant air temp             (unit.celsius)
27 51 FUEL_TYPE - Fuel type                           (string)
28 52 ETHANOL_PERCENT - Ethanol furl percent          (unit.percent)
29 53 EVAP_VAPOR_PRESSURE_ABS - Absolute vapor pres   (unit.kilopascals)
30 5B HYBRID_BATTERY_REMAINING - Hybrid battery life  (unit.percent)
31 5C OIL_TEMP - Engine oil temperature               (unit.celsius)
32 5D FUEL_INJECT_TIMING - Fuel injection timing      (unit.degree)
33 5E FUEL_RATE - Engine fuel rate                    (unit.liters_per_hr)

'''

command_list = []
obd_commands = [
 'PIDS_A',
 'FUEL_STATUS',
 'ENGINE_LOAD',
 'COOLANT_TEMP',
 'FUEL_PRESSURE',
 'INTAKE_PRESSURE',
 'RPM',
 'SPEED',
 'INTAKE_TEMP',
 'MAF',
 'THROTTLE_POS',
 'AIR_STATUS',
 'O2_SENSORS',
 'O2_B1S1',
 'RUN_TIME',
 'PIDS_B',
 'DISTANCE_W_MIL',
 'FUEL_RAIL_PRESSURE_VAC',
 'FUEL_LEVEL', 
 'EVAP_VAPOR_PRESSURE',
 'BAROMETRIC_PRESSURE',
 'O2_S1_WR_CURRENT',
 'CATALYST_TEMP_B1S1',
 'CONTROL_MODULE_VOLTAGE',
 'ABSOLUTE_LOAD',
 'RELATIVE_THROTTLE_POS',
 'AMBIANT_AIR_TEMP',
 'FUEL_TYPE',
 'ETHANOL_PERCENT',
 'EVAP_VAPOR_PRESSURE_ABS',
 'HYBRID_BATTERY_REMAINING',
 'OIL_TEMP',
 'FUEL_INJECT_TIMING',
 'FUEL_RATE'
 ]

def command_generator():
    for item in obd_commands:
        command_list.append('obd.commands.' + item)

def request_all():
    i = 0
    if DEBUG:
        print("    There are a total of", len(command_list),"commands, please refer to the command help list.\n")
    else:
        for item in range(len(command_list)):
            response = connection.query(command_list[i])
            print(response.value)
            i +=1

def request_command(command):
    if DEBUG:
        response = command_list[int(command)]
        print("   ", response,'\n')
    else:
        response = connection.query(command_list[int(command)])
        print("   ", response.value, '\n')

def check_valid(command):
    command = str(command).lower()
    if (command == 'a' or command == 'h' or command == 'q'):
        return True
    if not command.isdecimal():
        print("    Please enter a valid integer\n")
    elif ((int(command) >= len(command_list)) or (int(command) < 0)):
        print("    Please enter valid index. Try again.\n")
    else:
        return True

def command_help():
    print('''

    #  Description                           

    0  PIDS_A - Supported PIDs [01-20]                
    1  FUEL_STATUS - Fuel system status               
    2  ENGINE_LOAD - Calculated engine load           
    3  COOLANT_TEMP - Engine coolant temperature      
    4  FUEL_PRESSURE - Fuel pressure                  
    5  INTAKE_PRESSURE - Intake manifold pressure     
    6  RPM - Engine RPM                               
    7  SPEED - Vehicle speed                          
    8  INTAKE_TEMP - Intake air temperature
    9  MAF - Air flow rate                            
    10 THROTTLE_POS - Throttle position               
    11 AIR_STATUS - Secondary air status              
    12 O2_SENSORS - O2 sensors present                
    13 O2_B1S1 - Bank 1 Sensor 1 voltage              
    14 RUN_TIME - Engine runtime                      
    15 PIDS_B - Supported PIDs [21-40]                
    16 DISTANCE_W_MIL - Distance traveled with MIL on 
    17 FUEL_RAIL_PRESSURE_VAC - Fuel rail pressure     
    18 FUEL_LEVEL - Fuel level input                   
    19 EVAP_VAPOR_PRESSURE - Evaporative system pressure
    20 BAROMETRIC_PRESSURE - Barometric pressure       
    21 O2_S1_WR_CURRENT - 02 sensor 1 WR current       
    22 CATALYST_TEMP_B1S1 - Temperature                
    23 CONTROL_MODULE_VOLTAGE - Control module voltage 
    24 ABSOLUTE_LOAD - Absolute load value             
    25 RELATIVE_THROTTLE_POS - Relative throttle position 
    26 AMBIANT_AIR_TEMP - Ambiant air temperature 
    27 FUEL_TYPE - Fuel type                           
    28 ETHANOL_PERCENT - Ethanol furl percent          
    29 EVAP_VAPOR_PRESSURE_ABS - Absolute vapor pressure
    30 HYBRID_BATTERY_REMAINING - Hybrid battery life  
    31 OIL_TEMP - Engine oil temperature               
    32 FUEL_INJECT_TIMING - Fuel injection timing      
    33 FUEL_RATE - Engine fuel rate                    
    ''')
    
# Auto-connect to USB or RF port
if not DEBUG:
    connection = obd.OBD()
else: 
    print('''
    ***DEBUG MODE*** ''')

# Generate commands 
command_generator()


while True:
    cmd = input(''' 
    Request all sensor values       [a]
    Request specific sensor         [command #]
    Help                            [h]
    Quit                            [q]
   
    ''')
    if check_valid(cmd):
        if cmd == 'a':
            request_all()
        elif cmd == 'h':
            command_help()
        elif cmd == 'q':
            sys.exit()
        else:
            request_command(cmd) 
    print("   ", '=' * 60)
        
