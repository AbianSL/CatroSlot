def separate_name(full_name: str) -> list[str]:
    class_name, action, color = full_name.split(".")[0].split("_")
    talent = ""
    if action.lower() not in [
        "attack",
        "ally",
        "non-attack",
        "non-ally",
        "non",
    ]:
        talent = action
    return [talent, class_name, action, color]
