class ImageMetadata:
    def __init__(self, class_name: str, talent: str) -> None:
        self.class_name: str = class_name
        self.talent: str = talent
        self.has_cost: bool = True
        self.has_pitch: bool = True
        self.power_state: bool = True  # False: non-symbol, True: power
        self.defend_state: int = 0  # 0: non-symbol, 1: defend, 2: life
        self.color_id: int = -1  # 0: blue, 1: yellow, 2: red
