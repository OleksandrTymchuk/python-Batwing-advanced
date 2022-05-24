from abc import ABC, abstractmethod


class Laptop:

    @abstractmethod
    def screen(self):
        raise NotImplementedError('This method is not realized')

    @abstractmethod
    def keyboard(self):
        raise NotImplementedError('This method is not realized')

    @abstractmethod
    def touchpad(self):
        raise NotImplementedError('This method is not realized')

    @abstractmethod
    def webcam(self):
        raise NotImplementedError('This method is not realized')

    @abstractmethod
    def ports(self):
        raise NotImplementedError('This method is not realized')

    @abstractmethod
    def dynamics(self):
        raise NotImplementedError('This method is not realized')


class HPLaptop(Laptop, ABC):

    def __init__(self, screen, keyboard, touchpad,
                 webcam, ports, dynamics):
        self.screen = screen
        self.keyboard = keyboard
        self.touchpad = touchpad
        self.webcam = webcam
        self.ports = ports
        self.dynamics = dynamics

    def get_screen(self):
        print(f'Screen size: {self.screen}')

    def get_keyboard(self):
        print(f'Language layout: {self.keyboard}')

    def get_touchpad(self):
        print(f'Touchpad availability: {self.touchpad}')

    def get_webcam(self):
        print(f'Webcam availability: {self.webcam}')

    def get_ports(self):
        print(f'Number of ports: {self.ports}')

    def get_dynamics(self):
        print(f'Dynamics availability: {self.dynamics}')


hp_laptop = HPLaptop(19, 'Ukr', "+", '-', 2, '+')
(hp_laptop.get_screen())
(hp_laptop.get_keyboard())
(hp_laptop.get_touchpad())
(hp_laptop.get_webcam())
(hp_laptop.get_ports())
(hp_laptop.get_dynamics())
