from PIL import Image

from .img_metadata import ImageMetadata
from .name_generator import NameGenerator


class ImagePersistence:
    def __init__(self, metada: ImageMetadata) -> None:
        """
        Initializes the ImagePersistence with metadata and a name generator.
        Args:
            :param metada: An instance of ImageMetadata containing the card's metadata.
        """
        self._metadata: ImageMetadata = metada
        self._name_generator: NameGenerator = NameGenerator(
            metada.talent, metada.class_name
        )

    def save_image(
        self,
        image: Image,
        format: str = "webp",
        verbose: bool = True,
    ) -> None:
        """
        Saves the image to the outputs directory with a generated name based on metadata and
        if it is necessary create a sub-directory for the class and talent.
        Args:
            :param image: The PIL Image object to be saved.
            :param format: The format to save the image in (default is "webp").
            :param verbose: If True, prints status messages (default is True).
        """
        if verbose:
            print("Saving image...")
        result_name = self._name_generator.generate_name(
            self._metadata.has_cost,
            self._metadata.has_pitch,
            self._metadata.power_state,
            self._metadata.defend_state,
            self._metadata.color_id,
        )
        DIRECTORY = "outputs"
        import os

        if not os.path.exists(DIRECTORY):
            os.makedirs(DIRECTORY)
        OUTPUT_DIR = (
            "outputs/"
            + ((self._metadata.talent + "_") if self._metadata.talent else "")
            + self._metadata.class_name
        )
        if not os.path.exists(OUTPUT_DIR):
            os.makedirs(OUTPUT_DIR)
        image.save(f"{OUTPUT_DIR}/{result_name}.{format}", format=format)
        if verbose:
            print(f"Image saved as {result_name}.{format} on {OUTPUT_DIR}/")
