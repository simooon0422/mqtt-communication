import devices
import DataPanelGUI


class DataPanel(devices.Device):
    def __init__(self, address, publish_topic, subscribe_topics, GUI):
        super().__init__(address, publish_topic)

        self.subscribe_topics = subscribe_topics
        self.N = len(self.subscribe_topics)
        self.topic_vars = [0] * self.N
        self.GUI = GUI

        self.client.on_message = self._on_message

        if self.GUI:
            self.Panel = DataPanelGUI.DataPanelGUI(self.subscribe_topics, self.topic_vars)
            self.Panel.update_variables(self.topic_vars)

    def _on_message(self, client, userdata, message):
        for i in range(self.N):
            if message._topic.decode('utf-8') == self.subscribe_topics[i]:
                self.topic_vars[i] = message.payload.decode('utf-8')
        print(f"Received {self.topic_vars}")

        if self.GUI:
            self.Panel.update_variables(self.topic_vars)

    def _run(self):
        self.client.connect(self.mqtt_broker)
        for i in range(len(self.subscribe_topics)):
            self.client.subscribe(self.subscribe_topics[i])
        self.client.loop_start()

        while True:
            if self.end_thread:
                self.client.loop_stop()
                for i in range(len(self.subscribe_topics)):
                    self.client.unsubscribe(self.subscribe_topics[i])

                return
