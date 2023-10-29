import devices


class DataPanel(devices.Device):
    def __init__(self, address, publish_topic, subscribe_topic_1, subscribe_topic_2, subscribe_topic_3):
        super().__init__(address, publish_topic)

        self.topics = [subscribe_topic_1, subscribe_topic_2, subscribe_topic_3]
        self.topic_vars = [0, 0, 0]

        self.client.on_message = self._on_message

    def _on_message(self, client, userdata, message):
        if message._topic.decode('utf-8') == self.topics[0]:
            self.topic_vars[0] = message.payload.decode('utf-8')
        elif message._topic.decode('utf-8') == self.topics[1]:
            self.topic_vars[1] = message.payload.decode('utf-8')
        elif message._topic.decode('utf-8') == self.topics[2]:
            self.topic_vars[2] = message.payload.decode('utf-8')
        else:
            print(f"Error, topic received: {message._topic.decode('utf-8')}")
        print(f"Received {self.topic_vars}")

    def _run(self):
        for i in range(len(self.topics)):
            self.client.subscribe(self.topics[i])
        self.client.loop_start()

        if self.end_thread:
            self.client.loop_stop()
            for i in range(len(self.topics)):
                self.client.unsubscribe(self.topics[i])
            return
