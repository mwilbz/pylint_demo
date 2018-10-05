import random

from pylint_demo.mypy.doodler import Doodler

TABLE_DOODLES = [
    '(┛ಠ_ಠ)┛彡┻━┻',
    '┻━┻︵ \\(°□°)/ ︵ ┻━┻',
    '┬─┬ノ( º _ ºノ)'
]


class TableDoodler(Doodler):
    """Doodles table flippers!"""

    def get_random_doodle(self) -> str:
        return random.choice(TABLE_DOODLES)
