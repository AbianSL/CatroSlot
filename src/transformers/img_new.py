from PIL import Image

from .img_template import ImageTransform


class NewImageTransform(ImageTransform):
    """
    A class to handle image transformations for the new edition of cards.
    Inherits from ImageTransform and sets specific positions and resized images
    for the new edition.
    """
    def __init__(
            self,
            talent: str | None,
            class_name: str,
            action: str,
            color_base: str,
            image_file: str,
            ) -> None:
        """
        Initializes the NewImageTransform with specific positions and resized images.
        Args:
            :param talent: The talent of the card (e.g., "shadow", "draconic").
            :param class_name: The class of the card (e.g., "warrior", "illusionist").
            :param action: The action of the card (e.g., "attack", "non-attack").
            :param color_base: The base color of the card ("red", "yellow", "blue").
            :param image_file: The path to the image file to be transformed.
        """
        super().__init__(image_file, color_base, class_name, talent)
        self._defend_position: tuple[int, int] = (390, 552)
        self._power_position: tuple[int, int] = (28, 552)
        self._pitch_position: tuple[int, int] = (30, 30)
        self._cost_position: tuple[int, int] = (371, 30)

        self._blue_pitch_position: tuple[int, int] = (57, 53)
        self._yellow_pitch_position: tuple[int, int] = (35, 53)
        self._red_pitch_position: tuple[int, int] = (45, 33)
        self._color_bar_position: tuple[int, int] = (70, 28)

        # resize images
        self._non_symbol = self._non_symbol.resize((50, 50), resample=Image.BILINEAR)
        self._non_color_bar = self._non_color_bar.resize(
            (312, 6), resample=Image.BILINEAR
        )
        self._pitch_img = self._pitch_img.resize((17, 17), resample=Image.BILINEAR)
        self._small_non_symbol = self._small_non_symbol.copy().resize(
            (33, 33), resample=Image.BILINEAR
        )
        self._defend_img = self._defend_img.resize((33, 33), resample=Image.BILINEAR)
        self._life_img = self._life_img.resize((33, 33), resample=Image.BILINEAR)
        self._power_img = self._power_img.resize((33, 33), resample=Image.BILINEAR)
        self._cost_img = self._cost_img.resize((51, 51), resample=Image.BILINEAR)
