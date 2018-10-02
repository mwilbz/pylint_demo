from pylint_demo.mypy.doodler import Doodler


class Image:
    """Represents an image, not a string"""
    pass


class ImageDoodler(Doodler):

    def get_random_doodle(self) -> Image:
        return Image()

    def num_doodles(self, a_positional_argument: int) -> int:
        return 5
