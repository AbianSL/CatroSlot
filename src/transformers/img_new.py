from .img_template import ImageTransform


class NewImageTransform(ImageTransform):
    def __init__(
        self,
        talent: str | None,
        class_name: str,
        action: str,
        color_base: str,
        image_file: str,
    ) -> None:
        super().__init__(image_file, color_base, action, talent)
        self._defend_position = (390, 552)
        self._power_position = (28, 551)
        self._pitch_position = (30, 30)
        self._cost_position = (370, 29)

        self._blue_pitch_position: tuple[int, int] = (57, 53)
        self._yellow_pitch_position: tuple[int, int] = (35, 53)
        self._red_pitch_position: tuple[int, int] = (45, 33)
        self._color_bar_position: tuple[int, int] = (70, 28)

        # resize images
        self._non_symbol = self._non_symbol.resize((50, 50))
        self._non_color_bar = self._non_color_bar.resize((312, 6))
        self._pitch_img = self._pitch_img.resize((17, 17))
        self._small_non_symbol = self._small_non_symbol.copy().resize((33, 33))
        self._defend_img = self._defend_img.resize((33, 33))
        self._power_img = self._power_img.resize((33, 34))
        self._cost_img = self._cost_img.resize((50, 50))
