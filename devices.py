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
        self.temperature = uniform(18, 22)

    def _run_device(self):
        self._get_temp()
        self._send_to_broker(self.temperature)
        time.sleep(1)


class Subscriber(Device):
    def __init__(self, address, publish_topic, subscribe_topic):
        super().__init__(address, publish_topic)

        self.subscribe_topic = subscribe_topic
        self.client.on_message = self._on_message

        self.data = -999

    def _on_message(self, client, userdata, message):
        self.data = message.payload.decode('utf-8')
        print(f"Received {self.data}")

    def _run(self):
        self.client.subscribe(self.subscribe_topic)
        self.client.loop_start()
        if self.end_thread:
            self.client.loop_stop()
            self.client.unsubscribe(self.subscribe_topic)
            return
