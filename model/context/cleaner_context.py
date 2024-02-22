from typing import List
from enums.cleaner_type_enum import CleanerTypeEnum
from model.cleaner.vacuum_cleaner import VacuumCleaner
from model.quadrant.quadrant import Quadrant
from model.context.context import Context
import threading


class CleanerContext(Context):

    def __init__(self, vacuum_cleaner: VacuumCleaner, quadrants: List[Quadrant], cleaner_type: CleanerTypeEnum):
        self.cleaner = vacuum_cleaner
        self.quadrants = quadrants
        self.cleaner_type = cleaner_type

    def run(self):
        self.cleaner.work(self.quadrants, self.cleaner_type)
        threading.Timer(interval=2, function=self.run).start()
