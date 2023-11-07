import pygame
import paho.mqtt.client as mqtt


class DataPanelGUI:
    def __init__(self, address, publish_topic, subscribe_topics):
        self.mqtt_broker = address
        self.publish_topic = publish_topic
        self.subscribe_topics = subscribe_topics
        self.N = len(self.subscribe_topics)
        self.topic_vars = [0] * self.N

        self.client = mqtt.Client(self.publish_topic)
        self.client.on_message = self._on_message

        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 255)

        pygame.init()

        self.font = pygame.font.SysFont("arial", 20)
        self.text_list = [0] * self.N

        for i in range(self.N):
            self.text_list[i] = self.font.render(f"{self.subscribe_topics[i]}: {self.topic_vars[i]}", True, self.black)

        self.screen = pygame.display.set_mode((200, len(self.topic_vars) * 30))

    def start(self):
        self.client.connect(self.mqtt_broker)
        for i in range(len(self.subscribe_topics)):
            self.client.subscribe(self.subscribe_topics[i])
        self.client.loop_start()
        self._update_display()

    def stop(self):
        self.client.loop_stop()
        for i in range(len(self.subscribe_topics)):
            self.client.unsubscribe(self.subscribe_topics[i])

    def _on_message(self, client, userdata, message):
        for i in range(self.N):
            if message._topic.decode('utf-8') == self.subscribe_topics[i]:
                self.topic_vars[i] = message.payload.decode('utf-8')
        print(f"Received {self.topic_vars}")
        self._update_display()

    def _update_display(self):
        for i in range(self.N):
            self.text_list[i] = self.font.render(f"{self.subscribe_topics[i]}: {self.topic_vars[i]}", True, self.black)

        self.screen.fill((255, 255, 255))

        for i in range(self.N):
            self.screen.blit(self.text_list[i], (20, i * 30))

        pygame.display.flip()

    def check_exit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.stop()
                pygame.quit()

