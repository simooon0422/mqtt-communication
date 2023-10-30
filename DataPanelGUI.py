import pygame
import time
import threading


class DataPanelGUI:
    def __init__(self, topics_list, var_list):
        self.topics_list = topics_list
        self.variables = var_list

        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 255)

        pygame.init()
        self.font = pygame.font.SysFont("arial", 20)
        self.text = self.font.render(f"Iteration: {self.variables[0]}", True, self.black)
        self.screen = pygame.display.set_mode((len(self.variables)*100, 100))

    def update_variables(self, v_list):
        for i in range(len(v_list)):
            self.variables[i] = v_list[i]
        self._display_variables()

    def _display_variables(self):
        self.text = self.font.render(f"{self.topics_list[0]}: {self.variables[0]}", True, self.black)
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.text, (20, 30))
        pygame.display.flip()

