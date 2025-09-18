class ImageMetadata:
    """
    A class to represent metadata for the card image.
    """

    def __init__(self, class_name: str, talent: str) -> None:
        """
        Initializes the ImageMetadata with class name and talent.

        Args:
            :param class_name: The class of the card (e.g., "warrior", "illusionist").
            :param talent: The talent of the card (e.g., "shadow", "draconic").
        """
        self.class_name: str = class_name
        self.talent: str = talent
        self.has_cost: bool = True
        self.has_pitch: bool = True
        self.power_state: bool = True  # False: non-symbol, True: power
        self.defend_state: int = -1  # -1: non-symbol 0: defend, 1: life
        self.color_id: int = -1  # -1: non-color 0: blue, 1: yellow, 2: red
