import devices


class DataPanel(devices.Device):
    def __init__(self, address, publish_topic, subscribe_topic_1, subscribe_topic_2, subscribe_topic_3):
        super().__init__(address, publish_topic)

        self.topics = [subscribe_topic_1, subscribe_topic_2, subscribe_topic_3]
        self.topic_vars = [0, 0, 0]

    def _on_message(self, client, userdata, message):
        self.data = message.payload.decode('utf-8')
        print(f"Received {self.data}")

    def _run(self):
        for i in range(len(self.topics)):
            self.client.subscribe(self.topics[i])
        self.client.loop_start()

        if self.end_thread:
            self.client.loop_stop()
            for i in range(len(self.topics)):
                self.client.unsubscribe(self.topics[i])
            return
