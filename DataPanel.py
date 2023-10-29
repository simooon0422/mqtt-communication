import paho.mqtt.client as mqtt


class DataPanel:
    def __init__(self, address, publish_topic, subscribe_topic_1, subscribe_topic_2, subscribe_topic_3):
        self.address = address
        self.publish_topic = publish_topic
        self.subscribe_topic_1 = subscribe_topic_1
        self.subscribe_topic_2 = subscribe_topic_2
        self.subscribe_topic_3 = subscribe_topic_3

        self.mqtt_broker = self.address

        self.client = mqtt.Client(self.publish_topic)
