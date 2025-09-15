import os
from pathlib import Path

from PIL import Image

from .img_metadata import ImageMetadata
from .img_persistence import ImagePersistence


class ImageTransform:
    def __init__(
        self, image_file: str, color_base: str, class_name: str, talent: str
    ) -> None:
        # positions
        self._defend_position: tuple[int, int] = (0, 0)
        self._power_position: tuple[int, int] = (0, 0)
        self._cost_position: tuple[int, int] = (0, 0)
        self._blue_pitch_position: tuple[int, int] = (0, 0)
        self._yellow_pitch_position: tuple[int, int] = (0, 0)
        self._red_pitch_position: tuple[int, int] = (0, 0)
        self._pitch_position: tuple[int, int] = (0, 0)
        self._color_bar_position: tuple[int, int] = (0, 0)

        # images
        ASSETS_DIR = Path(__file__).parent / "assets"
        self._non_symbol = Image.open(ASSETS_DIR / "NonSymbol.png").convert("RGBA")
        self._non_color_bar = Image.open(ASSETS_DIR / "pitch/NonColorBar.png").convert(
            "RGBA"
        )
        self._cost_img = Image.open(ASSETS_DIR / "CostSymbol.png").convert("RGBA")
        self._pitch_img = self._cost_img.copy()
        self._power_img = Image.open(ASSETS_DIR / "PowerSymbol.png").convert("RGBA")
        self._defend_img = Image.open(ASSETS_DIR / "DefendSymbol.png").convert("RGBA")
        self._small_non_symbol = self._non_symbol.copy()
        self._life_img = Image.open(ASSETS_DIR / "LifeSymbol.png").convert("RGBA")

        # metadata
        self.__metadata = ImageMetadata(class_name, talent)
        self.__image_persistence = ImagePersistence(self.__metadata)

        self._color_bar: list[Image] = []
        PITCH_DIR = ASSETS_DIR / "pitch"
        files = os.listdir(PITCH_DIR)
        for file in files:
            if not file.endswith(".png") or color_base in file or "Non" in file:
                continue
            else:
                self._color_bar.append(Image.open(PITCH_DIR / file).convert("RGBA"))
        self.result_image = Image.open(image_file).convert("RGBA")
        self._original_image = self.result_image.copy()

        # position 0 = blue, 1 = yellow, 2 = red
        color_names = ["blue", "yellow", "red"]
        color_base = color_base.lower()
        self.color_base = (
            color_names.index(color_base.lower()) if color_base in color_names else -1
        )

    def save_image(self) -> None:
        """
        Saves the image in webp format.
        """
        self.__image_persistence.save_image(self.result_image)

    def replace_cost(self) -> None:
        """
        Paste the cost symbol in the image at the specified position.
        That replaces the non-cost symbol if it exists.
        """
        self.__metadata.has_cost = True
        self._blend_paste(self._cost_img, self._cost_position)

    def replace_power(self) -> None:
        """
        Paste the power symbol in the image at the specified position.
        That replaces the non-symbol if it exists.
        """
        self.__metadata.power_state = True
        self._blend_paste(self._power_img, self._power_position)

    def replace_defend(self) -> None:
        """
        Paste the defend symbol in the image at the specified position.
        That replaces the non-symbol if it exists or the life symbol.
        """
        self.__metadata.defend_state = 0
        self._blend_paste(self._defend_img, self._defend_position)

    def replace_life(self) -> None:
        """
        Paste the life symbol in the image at the specified position.
        That replaces the non-symbol if it exists or the defend symbol.
        """
        self.__metadata.defend_state = 1
        self._blend_paste(self._life_img, self._defend_position)

    def replace_pitch(self, pitch: int) -> None:
        """
        Replaces the pitch symbol in the image with the specified pitch and the corresponding color bar.
        :param pitch: The pitch value to replace.
            0: blue
            1: yellow
            2: red
        """
        possible_pitch_replaces = {
            0: lambda: self._blend_paste(self._pitch_img, self._red_pitch_position),
            1: lambda: self._blend_paste(self._pitch_img, self._yellow_pitch_position),
            2: lambda: self._blend_paste(self._pitch_img, self._blue_pitch_position),
        }
        if pitch < 0 or pitch >= len(possible_pitch_replaces):
            raise ValueError(f"{pitch} Pitch value out of range.")
        self.__metadata.has_pitch = True
        for range_pitch in range(len(possible_pitch_replaces) - pitch):
            possible_pitch_replaces[range_pitch]()

    def replace_bar(self, pitch: int) -> None:
        """
        Replaces the color bar in the image with the specified pitch.
        :param pitch: The pitch value to replace.
            0: blue
            1: yellow
            2: red
        """
        if pitch < 0 or pitch >= len(self._color_bar):
            raise ValueError(f"{pitch} Pitch value out of range.")
        self.__metadata.color_id = pitch
        self._blend_paste(self._color_bar[pitch], self._color_bar_position)

    def replace_non_symbol(self, position: tuple[int, int]) -> None:
        """
        Replaces the non-symbol in the image with the specified position.
        :param position: The position to place the non-symbol.
        """
        if position[0] < 0 or position[1] < 0:
            raise ValueError("Position must be non-negative.")
        position_map = {
            self._cost_position: (
                lambda: setattr(self.__metadata, "has_cost", False),
                self._non_symbol,
            ),
            self._color_bar_position: (
                lambda: setattr(self.__metadata, "color_id", -1),
                self._non_color_bar,
            ),
            self._power_position: (
                lambda: setattr(self.__metadata, "power_state", False),
                self._small_non_symbol,
            ),
            self._defend_position: (
                lambda: setattr(self.__metadata, "defend_state", -1),
                self._small_non_symbol,
            ),
            self._pitch_position: (
                lambda: setattr(self.__metadata, "has_pitch", False),
                self._non_symbol,
            ),
        }

        image_to_paste = self._non_symbol
        if position in position_map:
            metadata_action, image_to_paste = position_map[position]
            metadata_action()
        else:
            raise ValueError("ERROR [replace_non_symbol]: Position not recognized.")
        self._blend_paste(image_to_paste, position)

    def auto_replace_and_save(self) -> None:
        """
        Automatically use all the possible combinations of replace methods
        and save the image with the corresponding metadata and name.
        """
        for power_state in [False, True]:
            for defend_state in [-1, 0, 1]:
                for has_cost in [False, True]:
                    for has_pitch in [False, True]:
                        for pitch in [-1, 0, 1, 2]:
                            if power_state:
                                self.replace_power()
                            else:
                                self.replace_non_symbol(self._power_position)
                            if defend_state == 0:
                                self.replace_defend()
                            elif defend_state == 1:
                                self.replace_life()
                            else:
                                self.replace_non_symbol(self._defend_position)
                            if has_cost:
                                self.replace_cost()
                            else:
                                self.replace_non_symbol(self._cost_position)
                            if has_pitch:
                                self.replace_pitch(pitch if pitch >= 0 else 0)
                            else:
                                self.replace_non_symbol(self._pitch_position)
                            if pitch >= 0:
                                self.replace_bar(pitch)
                            else:
                                self.replace_non_symbol(self._color_bar_position)
                            self.save_image()
                            self.result_image = self._original_image.copy()

    def _blend_paste(self, image: Image.Image, position: tuple[int, int]) -> None:
        """
        Pega una imagen en la posición dada con blending alfa.
        """
        temp_layer = Image.new("RGBA", self.result_image.size, (0, 0, 0, 0))
        temp_layer.paste(image, position, image)
        self.result_image = Image.alpha_composite(self.result_image, temp_layer)
