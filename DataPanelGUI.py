import pygame
import DataPanel


class DataPanelGUI(DataPanel.DataPanel):
    def __init__(self, address, publish_topic, subscribe_topics):
        super().__init__(address, publish_topic, subscribe_topics)

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
        self._update_display()

    def _on_message(self, client, userdata, message):
        super()._on_message(client, userdata, message)
        self._update_display()

    def _update_display(self):
        for i in range(self.N):
            self.text_list[i] = self.font.render(f"{self.subscribe_topics[i]}: {self.topic_vars[i]}", True, self.black)

        self.screen.fill(self.white)

        for i in range(self.N):
            self.screen.blit(self.text_list[i], (20, i * 30))

        pygame.display.flip()

    def check_exit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.stop()
                pygame.quit()

