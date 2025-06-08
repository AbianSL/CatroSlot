from aud_template import AudioTransform 

class OldImageTransform(AudioTransform):
    def __init__(self) -> None:
        super()
        self._defend_position = (0, 0)
        self._power_position = (0, 0)
        self._cost_position = (0, 0)
        self._pitch_position = [(0, 0)]
        self._color_bar_position = (0, 0)
