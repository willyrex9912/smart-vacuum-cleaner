from typing import List

from model.vacuum_cleaner import VacuumCleaner
from model.quadrant import Quadrant
from model.context import Context
import time
import threading


class CleanerContext(Context):

    def __init__(self, vacuum_cleaner: VacuumCleaner, quadrants: List[Quadrant]):
        self.cleaner = vacuum_cleaner
        self.quadrants = quadrants

    def run(self):
        if self.cleaner.is_necessary_to_clean():
            self.cleaner.clean()
        self.cleaner.move(self.get_next_quadrant())
        threading.Timer(interval=2, function=self.run).start()

    def get_next_quadrant(self) -> Quadrant:
        if self.cleaner.current_quadrant.name == "A":
            return self.quadrants[1]
        else:
            return self.quadrants[0]
