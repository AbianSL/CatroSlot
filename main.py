import os
from PIL import Image

from src.img_gen import generate_images
from src.separate_name import separate_name


def main():
    option_selected = input("Are the images new edition or old? (Y/n): ").strip().lower()
    is_new = False if option_selected in ['n', 'no', ''] else True
    supported_formats = Image.registered_extensions().values()
    option_selected = input("Which format do you want to save the images? (default: webp)").strip().lower()
    format = "webp" if option_selected in ['webp', ''] else option_selected
    if format.upper() not in supported_formats:
        print(f"Format {format} is not supported. Supported formats are: {', '.join(supported_formats)}")
        return

    base_directory = os.path.dirname(os.path.abspath(__file__)) + "/base"
    for file_name in os.listdir(base_directory):
        complete_route = os.path.join(base_directory, file_name)
        if os.path.isfile(complete_route):
            talent, class_name, action, color = separate_name(file_name)
            generate_images(talent, class_name, action, color, is_new, complete_route, format)


if __name__ == "__main__":
    main()
