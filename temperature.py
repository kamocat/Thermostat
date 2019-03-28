import serial

def init():
	ser = serial.Serial('/dev/ttyAMA0')
	ser.baudrate = 115200
	ser.timeout = 1.0
	return ser

def read(ser):
	tempA = 32
	voltA = 33000.0 / (32554 + 10000)
	tempB = 77
	voltB = 3.3/2
	slope = (tempB-tempA)/(voltB-voltA)
	offset = voltA * slope - tempA

	try:
		# If the buffer is too long, flush it
		if ser.in_waiting > 20 :
			ser.reset_input_buffer()
			ser.read_until()

		text = ser.read_until()
		val = int(text)
	except:
		print("Invalid value read", text)
	else:
		volts = val * 3.3 / (2**16 - 1)
		temp = volts * slope + offset

	return temp
