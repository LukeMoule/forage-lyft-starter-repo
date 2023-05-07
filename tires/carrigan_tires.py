from abc import ABC

from tires.tires import Tires


class CarriganTires(Tires, ABC):
    def __init__(self, tire_wears):
        self.tire_wears = tire_wears

    def needs_service(self):
        for tire in self.tire_wears:
            if tire >= 0.9:
                return True
        
        return False