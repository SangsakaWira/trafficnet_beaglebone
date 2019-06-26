import requests
import time
import Adafruit_BBIO.GPIO as GPIO

output_pins = ["P8_7","P8_8","P8_9","P8_10","P8_11","P8_12","P8_14","P8_16","GPIO_65","P9_49","P9_117","P9_115"]
lampu1 = 0
lampu2 = 0
lampu3 = 0
lampu4 = 0

GPIO.setup("P8_7",GPIO.OUT)
GPIO.setup("P8_8",GPIO.OUT)
GPIO.setup("P8_9",GPIO.OUT)
# GPIO.setup(output_pins[3] ,GPIO.OUT)
# GPIO.setup(output_pins[4] ,GPIO.OUT)
# GPIO.setup(output_pins[5] ,GPIO.OUT)
# GPIO.setup(output_pins[6] ,GPIO.OUT)
# GPIO.setup(output_pins[7] ,GPIO.OUT)
# GPIO.setup(output_pins[8] ,GPIO.OUT)
# GPIO.setup(output_pins[9] ,GPIO.OUT)
# GPIO.setup(output_pins[10] ,GPIO.OUT)
# GPIO.setup(output_pins[11] ,GPIO.OUT)

while(True):
	r = requests.get("http://trafficnet.id:7000/traffic/mulyosari")
	print(r.json())
	lampu1 = r.json()["lampu1"]
	lampu2 = r.json()["lampu2"]
	lampu3 = r.json()["lampu3"]
	lampu4 = r.json()["lampu4"]

	for i in output_pins:
		GPIO.output(i,GPIO.HIGH)

	for i in output_pins:
		GPIO.output(i,GPIO.LOW)
	# if(lampu1 == "1"):
	# 	GPIO.output(output_pins[0],GPIO.HIGH)
	# 	GPIO.output(output_pins[1],GPIO.HIGH)
	# 	GPIO.output(output_pins[2],GPIO.HIGH)
	# 	GPIO.output(output_pins[3],GPIO.HIGH)
	# elif(lampu1 == "2"):
	# 	GPIO.output(output_pins[4],GPIO.HIGH)
	# 	GPIO.output(output_pins[5],GPIO.HIGH)
	# 	GPIO.output(output_pins[1],GPIO.HIGH)
	# 	GPIO.output(output_pins[0],GPIO.HIGH)
	# elif(lampu1 == "3"):
	# 	GPIO.output(output_pins[0],GPIO.HIGH)
	# 	GPIO.output(output_pins[0],GPIO.HIGH)
	# 	GPIO.output(output_pins[0],GPIO.HIGH)
	# 	GPIO.output(output_pins[0],GPIO.HIGH)
	# else:
	# 	print("merah")

	time.sleep(0.5)
		
