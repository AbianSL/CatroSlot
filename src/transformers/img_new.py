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
        self._defend_position = (343, 575)
        self._power_position = (65, 575)
        self._cost_position = (0, 0)
        self._pitch_position = [(0, 0)]
        self._color_bar_position = (0, 0)
