import devices


class DataPanel(devices.Device):
    def __init__(self, address, publish_topic, subscribe_topics):
        super().__init__(address, publish_topic)

        self.subscribe_topics = subscribe_topics
        self.topic_vars = [0, 0, 0]

        self.client.on_message = self._on_message

    def _on_message(self, client, userdata, message):
        if message._topic.decode('utf-8') == self.subscribe_topics[0]:
            self.topic_vars[0] = message.payload.decode('utf-8')
        elif message._topic.decode('utf-8') == self.subscribe_topics[1]:
            self.topic_vars[1] = message.payload.decode('utf-8')
        elif message._topic.decode('utf-8') == self.subscribe_topics[2]:
            self.topic_vars[2] = message.payload.decode('utf-8')
        else:
            print(f"Error, topic received: {message._topic.decode('utf-8')}")
        print(f"Received {self.topic_vars}")

    def _run(self):
        for i in range(len(self.subscribe_topics)):
            self.client.subscribe(self.subscribe_topics[i])
        self.client.loop_start()

        if self.end_thread:
            self.client.loop_stop()
            for i in range(len(self.subscribe_topics)):
                self.client.unsubscribe(self.subscribe_topics[i])
            return
