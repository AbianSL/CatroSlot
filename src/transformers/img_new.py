from .img_template import ImageTransform

class NewImageTransform(ImageTransform):
    def __init__(self, audio_file: str, color_base: str, action: str) -> None:
        super(audio_file, color_base, action)
        self._defend_position = (343, 575)
        self._power_position = (65, 575)
        self._cost_position = (0, 0)
        self._pitch_position = [(0, 0)]
        self._color_bar_position = (0, 0)
