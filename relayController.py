
import serial
import sys
import time

serialInst = serial.Serial()

relayComport = sys.argv[1]
relayNumber = sys.argv[2]
relayState = sys.argv[3]

relayControl = [8, 8, 8, 8]


print("relayComport = "+relayComport)
print("relayNumber = "+relayNumber)
print("relayState = "+relayState)

serialInst.baudrate = 9600
serialInst.port = relayComport
serialInst.open()

if(relayState == '1'):
    relayControl[int(relayNumber)-1] = '1'
else:
    relayControl[int(relayNumber)-1] = '0'

for relay in relayControl:
    serialInst.write(str(relay).encode())
    time.sleep(.2)
serialInst.close()