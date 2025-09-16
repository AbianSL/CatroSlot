from .transformers import ImageTransform, NewImageTransform, OldImageTransform


def generate_images(
    talent: str | None,
    class_name: str,
    action: str | None,
    color: str,
    version: bool,
    file_path: str,
    format: str = "webp",
) -> None:
    """
    Generates images based on the provided parameters.
    Args:
        :param talent: The talent of the card (e.g., "shadow", "draconic").
        :param class_name: The class of the card (e.g., "warrior", "illusionist").
        :param color: The color of the card ("red", "yellow", "blue").
        :param version: The version of the card [New (True) or Old (False)].
    """
    imageTransformer: ImageTransform
    if version:
        imageTransformer = NewImageTransform(
            talent, class_name, action, color, file_path
        )
    else:
        imageTransformer = OldImageTransform(
            talent, class_name, action, color, file_path
        )
    imageTransformer.auto_replace_and_save()
