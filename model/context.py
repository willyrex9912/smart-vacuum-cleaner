from abc import ABC, abstractmethod


class Context:

    @abstractmethod
    def run(self):
        pass
