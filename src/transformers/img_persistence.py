from PIL import Image

from .img_metadata import ImageMetadata
from .name_generator import NameGenerator


class ImagePersistence:
    def __init__(self, metada: ImageMetadata) -> None:
        self._metadata: ImageMetadata = metada
        self._name_generator: NameGenerator = NameGenerator(
            metada.talent, metada.class_name
        )

    def save_image(
        self,
        color_id: int,
        image: Image,
        format: str = "webp",
        verbose: bool = True,
    ) -> None:
        if verbose:
            print("Saving image...")
        result_name = self._name_generator.generate_name(
            self._metadata.has_cost,
            self._metadata.has_pitch,
            self._metadata.power_state,
            self._metadata.defend_state,
            color_id,
        )
        image.save(f"{result_name}.{format}", format=format.upper())
        if verbose:
            print(f"Image saved as {result_name}.{format}")
