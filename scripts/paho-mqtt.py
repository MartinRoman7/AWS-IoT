import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt
import time
# Button GPIO Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# MQTT Details
broker_address="test.mosquitto.org"
client_id="autobot"
sub_topic="home/switches/button1"
pub_topic="home/switches/button1"
# Callback function on message receive
def on_message(client, userdata, message):
	print("message received " ,str(message.payload.decode("utf-8")))
	print("message topic=",message.topic)
	print("message qos=",message.qos)
	print("message retain flag=",message.retain)

# Callback function on log
def on_log(client, userdata, level, buf):
	print("log: ", buf)

print("Initializing MQTT client instance: " + client_id)
client = mqtt.Client(client_id)

# Bind function to callback
client.on_message=on_message
client.on_log=on_log

# Connect to broker
print("Connecting to Broker: " + broker_address)
client.connect(broker_address)
try:
	client.loop_start()
	print("Subscribing to topic " + sub_topic)
	client.subscribe(sub_topic)
	while True:
		button_state = GPIO.input(23)
		if button_state == False:
			print('Button Pressed...')
			print("Publishing to topic " + pub_topic)
			client.publish(pub_topic, "PRESSED")
			time.sleep(4)
except:
	GPIO.cleanup()
	client.loop_stop()

