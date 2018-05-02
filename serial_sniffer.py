import serial
import sys

"""Reads serial port COM1 and returns a file with recorded data"""

try:
  ser = serial.Serial('\\.\COM1', 4800,timeout=None, parity=serial.PARITY_EVEN, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS)

except:
    sys.exit("CANNOT CONNECT")

s = ser.read(100)

data = bytes(s)
newfile.write(data)
