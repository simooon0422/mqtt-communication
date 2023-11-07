import paho.mqtt.client as mqtt


class DataPanel:
    def __init__(self, address, publish_topic, subscribe_topics):
        self.mqtt_broker = address
        self.publish_topic = publish_topic
        self.subscribe_topics = subscribe_topics

        self.N = len(self.subscribe_topics)
        self.topic_vars = [0] * self.N

        self.client = mqtt.Client(self.publish_topic)
        self.client.on_message = self._on_message

    def start(self):
        self.client.connect(self.mqtt_broker)
        for i in range(len(self.subscribe_topics)):
            self.client.subscribe(self.subscribe_topics[i])
        self.client.loop_start()

    def stop(self):
        self.client.loop_stop()
        for i in range(len(self.subscribe_topics)):
            self.client.unsubscribe(self.subscribe_topics[i])

    def _on_message(self, client, userdata, message):
        for i in range(self.N):
            if message._topic.decode('utf-8') == self.subscribe_topics[i]:
                self.topic_vars[i] = message.payload.decode('utf-8')

    def get_values(self):
        return self.topic_vars
