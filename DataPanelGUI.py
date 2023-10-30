import pygame


class DataPanelGUI:
    def __init__(self, topics_list, var_list):
        self.topics_list = topics_list
        self.variables = var_list
        self.N = len(self.variables)

        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 255)

        pygame.init()
        self.font = pygame.font.SysFont("arial", 20)
        self.text_list = [0] * self.N
        for i in range(self.N):
            self.text_list[i] = self.font.render(f"{self.topics_list[i]}: {self.variables[i]}", True, self.black)

        self.screen = pygame.display.set_mode((200, len(self.variables)*30))

    def update_variables(self, v_list):
        for i in range(len(v_list)):
            self.variables[i] = v_list[i]
        self._display_variables()

    def _display_variables(self):
        for i in range(self.N):
            self.text_list[i] = self.font.render(f"{self.topics_list[i]}: {self.variables[i]}", True, self.black)

        self.screen.fill((255, 255, 255))

        for i in range(self.N):
            self.screen.blit(self.text_list[i], (20, i*30))

        pygame.display.flip()

