import serial

def init():
	ser = serial.Serial('/dev/ttyAMA0')
	ser.baudrate = 115200
	ser.timeout = 1.0
	return ser

def read(ser ):
	tempA = 64.3
	voltA = 27632.0
	tempB = 94.5
	voltB = 37502.0
	slope = (tempA-tempB)/(voltA-voltB)
	offset = tempA - (voltA * slope)
	print("slope", slope, "offset", offset)

	try:
		# If the buffer is too long, flush it
		if ser.in_waiting > 20 :
			ser.reset_input_buffer()
			ser.read_until()

		text = ser.read_until()
		val = int(text)
		print("val read is", val)
	except:
		print("Invalid value read", text)
		# Don't heat. Return an obvious error
		temp = 1000
	else:
		temp = val * slope + offset
		
	return temp

if __name__ == '__main__':
	s = init()
	t = read(s)
	print("temperature is", t )


