from model.quadrant import Quadrant
import logging
import time
from typing import List

logging.basicConfig(level=logging.INFO, format='[%(threadName)s] (%(levelname)s) %(message)s')


class VacuumCleaner:

    def __init__(self, initial_quadrant: Quadrant):
        self.current_quadrant = initial_quadrant

    def clean(self):
        time.sleep(5)
        self.current_quadrant.is_cleaned = True
        logging.info("Quadrant " + self.current_quadrant.name + " is cleaned")

    def move(self, quadrants: List[Quadrant]):
        if self.current_quadrant.name == "A":
            self.move_right(quadrants)
        else:
            self.move_left(quadrants)
        # logging.info("Cleaner moved to quadrant " + self.current_quadrant.name)

    def move_left(self, quadrants: List[Quadrant]):
        self.current_quadrant = quadrants[0]

    def move_right(self, quadrants: List[Quadrant]):
        self.current_quadrant = quadrants[1]

    def is_necessary_to_clean(self):
        # logging.info("Testing if its necessary to clean the quadrant")
        return not self.current_quadrant.is_cleaned

    def work_quadrant(self, quadrants: List[Quadrant]):
        if self.is_necessary_to_clean():
            self.clean()
        self.move(quadrants)
