from model.quadrant import Quadrant
import logging
import time

logging.basicConfig(level=logging.INFO, format='[%(threadName)s] (%(levelname)s) %(message)s')


class VacuumCleaner:

    def __init__(self, initial_quadrant: Quadrant):
        self.current_quadrant = initial_quadrant

    def clean(self):
        time.sleep(5)
        self.current_quadrant.is_cleaned = True
        logging.info("Quadrant " + self.current_quadrant.name + " is cleaned")

    def move(self, new_quadrant: Quadrant):
        self.current_quadrant = new_quadrant
        # logging.info("Cleaner moved to quadrant " + self.current_quadrant.name)

    def is_necessary_to_clean(self):
        # logging.info("Testing if its necessary to clean the quadrant")
        return not self.current_quadrant.is_cleaned

