import threading

import paho.mqtt.client as mqtt
from random import uniform
import time
import devices


# mqtt_broker = "mqtt.eclipseprojects.io"
# client = mqtt.Client("Temperature")
# client.connect(mqtt_broker)
#
# t = 0
#
# while t < 10:
#     rand_num = uniform(20, 22)
#     client.publish("Temperature", rand_num)
#     print(f"Published {rand_num} to topic Temperature")
#     time.sleep(1)
#     t = t + 1



# for i in range(10):
#     temp = uniform(10, 20)
#     sensor.send_to_broker(temp)
#     time.sleep(1)

