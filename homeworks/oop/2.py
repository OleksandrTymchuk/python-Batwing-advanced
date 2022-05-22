#  2.a.______________________________

class Person:
    def __init__(self):
        left_arm = Arm('Left arm')
        right_arm = Arm('Right arm')
        self.arms = [left_arm.fingers, right_arm.fingers]


class Arm:
    def __init__(self, fingers):
        self.fingers = fingers


person = Person()
print(person.arms)


#  2.b._________________________________
class CellPhone:
    def __init__(self, screen):
        self.screen = screen


class Screen:
    def __init__(self, screen_type):
        self.screen_type = screen_type


screen = Screen('IPS')
iphone = CellPhone(screen)
print(screen)
print(iphone)

