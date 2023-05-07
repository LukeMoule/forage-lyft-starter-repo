from abc import ABC

from tires.tires import Tires


class OctoprimeTires(Tires, ABC):
    def __init__(self, tire_wears):
        self.tire_wears = tire_wears

    def needs_service(self):
        total_wear = 0
        for tire in self.tire_wears:
            total_wear += tire
        
        return total_wear >= 3