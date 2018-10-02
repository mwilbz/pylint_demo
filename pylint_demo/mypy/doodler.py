from abc import ABC, abstractmethod


class Paper:
    """Something to doodle on!"""

    def __init__(self):
        self.drawings = ''

    def draw(self, ascii_drawing: str):
        self.drawings += ascii_drawing


class Doodler(ABC):
    """Abstract base class for doodling"""

    def doodle(self, paper: Paper) -> None:
        for _ in range(self.num_doodles):
            paper.draw(self.get_random_doodle())

    @property
    def num_doodles(self) -> int:
        return 3

    @abstractmethod
    def get_random_doodle(self) -> str:
        raise NotImplementedError
