import os

from .transformers import ImageTransform, NewImageTransform, OldImageTransform
from .separate_name import separate_name


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

def generate_images_from_directory(base_directory: str, is_new: bool, format: str = "webp") -> None:
    """
    Generate images for all files in the specified directory. Generating their
    corresponding versions based on the naming convention.
    Args:
        base_directory (str): The directory containing the base images.
        is_new (bool): True for new edition, False for old edition.
        format (str): The format to save the images in (default is "webp").
    """
    for file_name in os.listdir(base_directory):
        complete_route = os.path.join(base_directory, file_name)
        if os.path.isfile(complete_route):
            talent, class_name, action, color = separate_name(file_name)
            generate_images(talent, class_name, action, color, is_new, complete_route, format)
