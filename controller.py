import pygame


class Controller:
    def __init__(self):
        def __init__(self):
            pygame.init()
            pygame.joystick.init()
            self.joystick = pygame.joystick.Joystick(0)
            self.joystick.init()
            print(self.joystick.get_name())
            self.button_count = self.joystick.get_numbuttons()
            self.axis_count = self.joystick.get_numaxes()

        def get_button_values(self):
            return [self.joystick.get_button(i) for i in range(self.button_count)]

        def get_axis_values(self):
            return [self.joystick.get_axis(i) for i in range(self.axis_count)]

        def get_axis_value(self, axis_num):
            return self.joystick.get_axis(axis_num)
