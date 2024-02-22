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
        self.cleaner.work_quadrant(self.quadrants)
        threading.Timer(interval=2, function=self.run).start()
