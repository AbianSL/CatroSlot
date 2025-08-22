import os
from pathlib import Path

from PIL import Image


class ImageTransform:
    def __init__(
        self, image_file: str, color_base: str, action: str, talent: str
    ) -> None:
        # positions
        self._defend_position = (0, 0)
        self._power_position = (0, 0)
        self._cost_position = (0, 0)
        self._blue_pitch_position = (0, 0)

        self._yellow_pitch_position = (0, 0)
        self._red_pitch_position = (0, 0)
        self._color_bar_position = (0, 0)

        # images
        ASSETS_DIR = Path(__file__).parent / "assets"
        self.__non_symbol = Image.open(ASSETS_DIR / "NonSymbol.png")
        self.__non_color_bar = Image.open(ASSETS_DIR / "pitch/NonColorBar.png").convert("RGBA")
        self.__cost_img = Image.open(ASSETS_DIR / "CostSymbol.png").convert("RGBA")
        self.__power_img = Image.open(ASSETS_DIR / "PowerSymbol.png").convert("RGBA")
        self.__defend_img = Image.open(ASSETS_DIR / "DefendSymbol.png").convert("RGBA")

        # card action and talent
        self.__action = action
        self.__talent = talent

        self._color_bar: List[Image] = []
        PITCH_DIR = ASSETS_DIR / "pitch"
        files = os.listdir(PITCH_DIR)
        for file in files:
            if not file.endswith(".png") or color_base in file or "Non" in file:
                continue
            else:
                self._color_bar.append(
                    Image.open(PITCH_DIR / file).convert("RGBA")
                )
        self.result_image = Image.open(image_file).convert("RGBA")
        
        # position 0 = blue, 1 = yellow, 2 = red
        color_names = ["blue", "yellow", "red"]
        color_base = color_base.lower()
        self.color_base = (
            color_names.index(color_base.lower()) if color_base in color_names else -1
        )

    def save_image(self, format="webp") -> None:
        """
        Saves the image in webp format.
        """
        self.result_image.save("output." + format, format=format)

    def replace_cost(self) -> None:
        """
        Replaces the cost symbol in the image with the specified cost.
        :param cost: The cost to replace.
        :param position: The position to place the cost symbol.
        """
        self.result_image.paste(
            self.__cost_img,
            (self._cost_position[0], self._cost_position[1]),
            self.__cost_img,
        )

    def replace_power(self) -> None:
        """
        Replaces the power symbol in the image with the specified power.
        :param power: The power to replace.
        :param position: The position to place the power symbol.
        """
        self.result_image.paste(
            self.__power_img,
            (self._power_position[0], self._power_position[1]),
            self.__power_img,
        )

    def replace_defend(self) -> None:
        """
        Replaces the defend symbol in the image with the specified defend value.
        :param defend: The defend value to replace.
        :param position: The position to place the defend symbol.
        """
        self.result_image.paste(
            self.__defend_img,
            (self._defend_position[0], self._defend_position[1]),
            self.__defend_img,
        )

    def replace_pitch(self, pitch: int) -> None:
        """
        Replaces the pitch symbol in the image with the specified pitch and the corresponding color bar.
        :param pitch: The pitch value to replace.
            0: blue
            1: yellow
            2: red
        :param position: The position to place the pitch symbol.
        """  
        possible_pitch_replaces = {
            0: lambda: self.result_image.paste(
                self.__cost_img,
                (self._blue_pitch_position[0], self._blue_pitch_position[1]),
                self.__cost_img,
            ),
            1: lambda: self.result_image.paste(
                self.__cost_img,
                (self._yellow_pitch_position[0], self._yellow_pitch_position[1]),
                self.__cost_img,
            ),
            2: lambda: self.result_image.paste(
                self.__cost_img,
                (self._red_pitch_position[0], self._red_pitch_position[1]),
                self.__cost_img,
            ),
        }
        if pitch < 0 or pitch >= len(possible_pitch_replaces):
            raise ValueError("Pitch value out of range.")
        if pitch >= len(self._color_bar):
            raise ValueError("Color bar for pitch value not found.")
        self.result_image.paste(
            self._color_bar[pitch],
            (self._color_bar_position[0], self._color_bar_position[1]),
            self._color_bar[pitch],
        )
        for range_pitch in range(len(possible_pitch_replaces) - pitch):
            possible_pitch_replaces[range_pitch]()

    def replace_non_symbol(self, position: tuple) -> None:
        """
        Replaces the non-symbol in the image with the specified position.
        :param position: The position to place the non-symbol.
        """
        if position[0] < 0 or position[1] < 0:
            raise ValueError("Position must be non-negative.")
        self.result_image.paste(
            self.__non_symbol, (position[0], position[1]), self.__non_symbol
        )
        if position == self._pitch_position:
            self.result_image.paste(
                self.__non_color_bar,
                (self._color_bar_position[0], self._color_bar_position[1]),
                self.__non_color_bar,
            )

    def auto_replace_and_save(self) -> None:
        for pitch in range(3):
            self.replace_pitch(pitch)
            self.save_image()
