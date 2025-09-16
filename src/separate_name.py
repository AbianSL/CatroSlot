def separate_name(full_name: str) -> list[str]:
    """
    Separate the full name of the image into its components:
    talent, class_name, action, color.
    if the the second section is not a valid action, it is considered a talent.
    Args:
        full_name (str): The full name of the image file.
    """
    class_name, action, color = full_name.split(".")[0].split("_")
    talent = ""
    if action.lower() not in [
        "attack",
        "ally",
        "non-attack",
        "non-ally",
        "non",
        "default"
    ]:
        talent = action
    return [talent, class_name, action, color]
