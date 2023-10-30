import paho.mqtt.client as mqtt
from random import uniform
import threading
import time


class Device:
    def __init__(self, address, topic):
        self.address = address
        self.topic = topic

        self.mqtt_broker = self.address

        self.client = mqtt.Client(self.topic)

        self.device_thread = threading.Thread(target=self._run)
        self.device_thread.setDaemon(True)

        self.end_thread = False

    def _send_to_broker(self, data):
        self.client.publish(self.topic, data)
        print(f"Published {data} to topic {self.topic}")

    def _run(self):
        while True:
            self._run_device()
            if self.end_thread:
                return

    def _run_device(self):
        pass

    def start(self):
        self.client.connect(self.mqtt_broker)
        self.end_thread = False
        self.device_thread.start()

    def stop(self):
        self.end_thread = True
        self.client.disconnect(self.mqtt_broker)


class TemperatureSensor(Device):
    def __init__(self, address, topic):
        super().__init__(address, topic)
        self.temperature = -999

    def _get_temp(self):
        self.temperature = round(uniform(18, 22), 2)

    def _run_device(self):
        self._get_temp()
        self._send_to_broker(self.temperature)
        time.sleep(1)

