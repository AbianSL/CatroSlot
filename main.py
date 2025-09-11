import os

from src.img_gen import generate_images


def main():
    base_directory = os.path.dirname(os.path.abspath(__file__)) + "/base"
    for file_name in os.listdir(base_directory):
        complete_route = os.path.join(base_directory, file_name)
        if os.path.isfile(complete_route):
            class_name, action, color = file_name.split(".")[0].split("_")
            generate_images(None, class_name, action, color, True, complete_route)


if __name__ == "__main__":
    main()
