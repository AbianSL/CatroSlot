import os

from src.img_gen import generate_images
from src.separate_name import separate_name


def main():
    is_new = True
    base_directory = os.path.dirname(os.path.abspath(__file__)) + "/base"
    for file_name in os.listdir(base_directory):
        complete_route = os.path.join(base_directory, file_name)
        if os.path.isfile(complete_route):
            talent, class_name, action, color = separate_name(file_name)
            generate_images(talent, class_name, action, color, is_new, complete_route)


if __name__ == "__main__":
    main()
