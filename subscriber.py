import paho.mqtt.client as mqtt
from random import randrange, uniform
import time
import DataPanel


# def on_message(client, userdata, message):
#     print(f"Received {message.payload.decode('utf-8')}")
#
#
# mqtt_broker = "mqtt.eclipseprojects.io"
# client = mqtt.Client("Smartphone")
# client.connect(mqtt_broker)
#
# client.loop_start()
# client.subscribe("Temperature")
# client.on_message = on_message
# time.sleep(30)
# client.loop_stop()

sub = DataPanel.DataPanel("mqtt.eclipseprojects.io", "Subscriber", "Temperature", "Humidity", "Pressure")
sub.start()

while True:
    pass



