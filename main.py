# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
from model.context.cleaner_context import CleanerContext
from model.context.mess_maker_context import MessMakerContext
from model.cleaner.vacuum_cleaner import VacuumCleaner
from model.quadrant.quadrant import Quadrant
from enums.cleaner_type_enum import CleanerTypeEnum


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    quadrants: List[Quadrant] = [Quadrant("A"), Quadrant("B")]
    vacuum_cleaner = VacuumCleaner(quadrants[0])

    smart_str = str(CleanerTypeEnum.SMART.value)
    stupid_str = str(CleanerTypeEnum.STUPID.value)

    cleaner_type = input("Type " + smart_str + " for smart or " + stupid_str + " for stupid work: ")

    cleaner_context = CleanerContext(vacuum_cleaner, quadrants, CleanerTypeEnum(int(cleaner_type)))
    cleaner_context.run()

    mess_maker_context = MessMakerContext(quadrants)
    mess_maker_context.run()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
