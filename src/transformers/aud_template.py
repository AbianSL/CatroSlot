from PIL import Image
import os

class AudioTransform():
    def __init__(self, audio_file: str, color_base: str, is_power: bool, is_defend: bool) -> None:
        self.defend_position = None
        self.power_position = None
        self.cost_position = None
        self.pitch_position = None

        self.non_symbol = Image.open("assets/NoSymbol.png").convert("RGBA")
        self.cost_img = Image.open("assets/CostSymbol.png").convert("RGBA")
        self.power_img = Image.open("assets/PowerSymbol.png").convert("RGBA")
        self.defend_img = Image.open("assets/DefendSymbol.png").convert("RGBA")
        self.pitch_imgs = []
        self.color_bar = []
        files = os.listdir("assets/pitch") 
        for file in files:
            if not file.endswith(".png") or color_base in file:
                continue
            if "Bar" in file:
                self.color_bar.append(Image.open(os.path.join("assets/pitch", file)).convert("RGBA"))
            else:    
                self.pitch_imgs.append(Image.open(os.path.join("assets/pitch", file)).convert("RGBA"))

        self.result_image = Image.open(audio_file).convert("RGBA")
        self.is_power = is_power
        self.is_defend = is_defend

    def save_image(self, format = "webp") -> None:
        """
        Saves the image in webp format.
        """
        self.result_image.save("output.webp", format=format)
    
    def auto_generate(self) -> None:
        """
        Automatically generates the image based on the audio file.
        """

