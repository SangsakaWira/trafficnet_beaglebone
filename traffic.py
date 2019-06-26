import requests
import time
import Adafruit_BBIO.GPIO as GPIO

output_pins = ["P8_7","P8_8","P8_9","P8_10","P8_11","P8_12","P8_14","P8_16","P8_18","P9_49","P9_117","P9_115"]
lampu1 = 0
lampu2 = 0
lampu3 = 0
lampu4 = 0

# Merah 1
GPIO.setup("P8_7",GPIO.OUT) 
# Kuning 1
GPIO.setup("P8_8",GPIO.OUT)
# Ijo 1
GPIO.setup("P8_9",GPIO.OUT)

# Merah 2
GPIO.setup("P8_10",GPIO.OUT)
# Kuning 2
GPIO.setup("P8_11",GPIO.OUT)
# Ijo 2
GPIO.setup("P8_12",GPIO.OUT)

# Merah 3
GPIO.setup("P8_14",GPIO.OUT)
# Kuning 3
GPIO.setup("P8_16",GPIO.OUT)
# Ijo 3
GPIO.setup("P8_18",GPIO.OUT)

# Merah 4
GPIO.setup("P9_23",GPIO.OUT)
# Kuning 4
GPIO.setup("P9_30",GPIO.OUT)
# Ijo 4
GPIO.setup("P9_27",GPIO.OUT)

while(True):
	try:
		r = requests.get("http://trafficnet.id:7000/traffic/mulyosari")
		if(r == True):
			lampu1 = r.json()["lampu1"]
			lampu2 = r.json()["lampu2"]
			lampu3 = r.json()["lampu3"]
			lampu4 = r.json()["lampu4"]
		print("Success")
	except ConnectionError as e:
		pass
		print("Error")

	print("lampu1: "+str(lampu1))
	print("lampu2: "+str(lampu2))
	print("lampu3: "+str(lampu3))
	print("lampu4: "+str(lampu4))

	GPIO.output("P8_7",GPIO.HIGH)
	GPIO.output("P8_10",GPIO.HIGH)
	GPIO.output("P8_14",GPIO.HIGH)
	GPIO.output("P9_23",GPIO.HIGH)

	if(lampu1 == 1):
		GPIO.output("P8_7",GPIO.HIGH)
		GPIO.output("P8_8",GPIO.LOW)
		GPIO.output("P8_9",GPIO.LOW)
	if(lampu1 == 2):
		GPIO.output("P8_7",GPIO.LOW)
		GPIO.output("P8_8",GPIO.HIGH)
		GPIO.output("P8_9",GPIO.LOW)
	if(lampu1 == 3):
		GPIO.output("P8_7",GPIO.LOW)
		GPIO.output("P8_8",GPIO.LOW)
		GPIO.output("P8_9",GPIO.HIGH)
	if(lampu2 == 2):
		GPIO.output("P8_10",GPIO.LOW)
		GPIO.output("P8_11",GPIO.HIGH)
		GPIO.output("P8_12",GPIO.LOW)
	if(lampu2 == 3):
		GPIO.output("P8_10",GPIO.LOW)
		GPIO.output("P8_11",GPIO.LOW)
		GPIO.output("P8_12",GPIO.HIGH)
	if(lampu3 == 2):
		GPIO.output("P8_14",GPIO.LOW)
		GPIO.output("P8_16",GPIO.HIGH)
		GPIO.output("P8_18",GPIO.LOW)
	if(lampu3 == 3):
		GPIO.output("P8_14",GPIO.LOW)
		GPIO.output("P8_16",GPIO.LOW)
		GPIO.output("P8_18",GPIO.HIGH)
	if(lampu4 == 2):
		GPIO.output("P9_23",GPIO.LOW)
		GPIO.output("P9_30",GPIO.HIGH)
		GPIO.output("P9_27",GPIO.LOW)
	if(lampu4 == 3):
		GPIO.output("P9_23",GPIO.LOW)
		GPIO.output("P9_30",GPIO.LOW)
		GPIO.output("P9_27",GPIO.HIGH)
