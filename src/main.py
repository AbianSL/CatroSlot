import os

from PIL import Image

from catroslot.img_gen import generate_images_from_directory


def main():
    option_selected = input("Are the images new edition? (Y/n): ").strip().lower()
    is_new = False if option_selected in ["n", "no", ""] else True
    supported_formats = Image.registered_extensions().values()
    option_selected = (
        input("Which format do you want to save the images? (default: webp)")
        .strip()
        .lower()
    )
    format = "webp" if option_selected in ["webp", ""] else option_selected
    if format.upper() not in supported_formats:
        print(
            f"Format {format} is not supported. Supported formats are: {', '.join(supported_formats)}"
        )
        return
    base_directory: str = os.path.dirname(os.path.abspath(__file__)) + "/../base"
    generate_images_from_directory(base_directory, is_new, format)


if __name__ == "__main__":
    main()
