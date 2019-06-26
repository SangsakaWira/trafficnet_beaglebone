import requests
import time
import Adafruit_BBIO.GPIO as GPIO

output_pins = ["P8_7","P8_8","P8_9","P8_10","P8_11"]
lampu1 = 0
lampu2 = 0
lampu3 = 0
lampu4 = 0

for i in output_pins:
	GPIO.setup(i,GPIO.OUT)

while(True):
	r = requests.get("http://trafficnet.id:7000/traffic/mulyosari")
	print(r.json())
	lampu1 = r.json()["lampu1"]
	lampu2 = r.json()["lampu2"]
	lampu3 = r.json()["lampu3"]
	lampu4 = r.json()["lampu4"]

	if(lampu1 == "1"):
		GPIO.output(output_pins[0],GPIO.HIGH)
		GPIO.output(output_pins[1],GPIO.HIGH)
		GPIO.output(output_pins[2],GPIO.HIGH)
		GPIO.output(output_pins[3],GPIO.HIGH)
	elif(lampu1 == "2"):
		GPIO.output(output_pins[4],GPIO.HIGH)
		GPIO.output(output_pins[5],GPIO.HIGH)
		GPIO.output(output_pins[1],GPIO.HIGH)
		GPIO.output(output_pins[0],GPIO.HIGH)
	elif(lampu1 == "3"):
		GPIO.output(output_pins[0],GPIO.HIGH)
		GPIO.output(output_pins[0],GPIO.HIGH)
		GPIO.output(output_pins[0],GPIO.HIGH)
		GPIO.output(output_pins[0],GPIO.HIGH)
	else:
		print("merah")

	time.sleep(0.5)
		
