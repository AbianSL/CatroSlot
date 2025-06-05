from PIL import Image
import os

class ImageTransform():
    def __init__(self, audio_file: str, color_base: str, action: str) -> None:
        # Tuple (x, y) for positions
        self._defend_position = (0, 0)
        self._power_position = (0, 0)
        self._cost_position = (0, 0)
        self._pitch_position = (0, 0)
        self._color_bar_position = (0, 0)

        self.__non_symbol = Image.open("assets/NonSymbol.png").convert("RGBA")
        self.__non_color_bar = Image.open("assets/NonColorBar.png").convert("RGBA")
        self.__cost_img = Image.open("assets/CostSymbol.png").convert("RGBA")
        self.__power_img = Image.open("assets/PowerSymbol.png").convert("RGBA")
        self.__defend_img = Image.open("assets/DefendSymbol.png").convert("RGBA")
        
        self._pitch_imgs = []
        self._color_bar = []
        files = os.listdir("assets/pitch") 
        for file in files:
            if not file.endswith(".png") or color_base in file or "Non" in file:
                continue
            if "Bar" in file:
                self._color_bar.append(Image.open(os.path.join("assets/pitch", file)).convert("RGBA"))
            else:    
                self._pitch_imgs.append(Image.open(os.path.join("assets/pitch", file)).convert("RGBA"))
        self.result_image = Image.open(audio_file).convert("RGBA")

    def save_image(self, format = "webp") -> None:
        """
        Saves the image in webp format.
        """
        self.result_image.save("output.webp", format=format)
    
    def replace_cost(self) -> None:
        """
        Replaces the cost symbol in the image with the specified cost.
        :param cost: The cost to replace.
        :param position: The position to place the cost symbol.
        """
        self.result_image.paste(self.__cost_img, (self._cost_position[0], self._cost_position[1]), self.__cost_img)

    def replace_power(self) -> None:
        """
        Replaces the power symbol in the image with the specified power.
        :param power: The power to replace.
        :param position: The position to place the power symbol.
        """
        self.result_image.paste(self.__power_img, (self._power_position[0], self._power_position[1]), self.__power_img)

    def replace_defend(self) -> None:
        """
        Replaces the defend symbol in the image with the specified defend value.
        :param defend: The defend value to replace.
        :param position: The position to place the defend symbol.
        """
        self.result_image.paste(self.__defend_img, (self._defend_position[0], self._defend_position[1]), self.__defend_img)

    def replace_pitch(self, pitch: int) -> None:
        """
        Replaces the pitch symbol in the image with the specified pitch and the corresponding color bar.
        :param pitch: The pitch value to replace.
        :param position: The position to place the pitch symbol.
        """
        if pitch < 0 or pitch >= len(self._pitch_imgs):
            raise ValueError("Pitch value out of range.")
        if pitch >= len(self._color_bar):
            raise ValueError("Color bar for pitch value not found.")
        self.result_image.paste(self._pitch_imgs[pitch], (self._pitch_position[0], self._pitch_position[1]), self._pitch_imgs[pitch])
        self.result_image.paste(self._color_bar[pitch], (self._color_bar_position[0], self._color_bar_position[1]), self._color_bar[pitch])

    def resplace_non_symbol(self, position: tuple) -> None:
        """
        Replaces the non-symbol in the image with the specified position.
        :param position: The position to place the non-symbol.
        """
        if position[0] < 0 or position[1] < 0:
            raise ValueError("Position must be non-negative.")
        self.result_image.paste(self.__non_symbol, (position[0], position[1]), self.__non_symbol)
        if position == self._pitch_position:
            self.result_image.paste(self.__non_color_bar, (self._color_bar_position[0], self._color_bar_position[1]), self.__non_color_bar)

    def auto_replace_and_save(self) -> None:
         
