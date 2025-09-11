class NameGenerator:
    def __init__(self, talent: str | None, class_name: str) -> None:
        self.__talent = talent
        self.__class_name = class_name
        self.__name_parts: list[str] = [talent if talent else "", class_name]
        self.__generated_name: str = ""

    def generate_name(
        self,
        has_cost: bool,
        has_pitch: bool,
        power_state: bool,
        defend_state: int,
        color_id: int,
    ) -> str:
        self.__name_parts.append("" if has_cost else "non-cost")
        self.__name_parts.append("" if has_pitch else "non-pitch")
        if not power_state:
            if defend_state == -1:
                self.__name_parts.append("default")
            elif defend_state == 0:
                self.__name_parts.append("non-attack")
            elif defend_state == 1:
                # TODO: Determinate name for this case
                self.__name_parts.append("?")
        else:
            if defend_state == -1:
                # TODO: Determinate name for this case
                self.__name_parts.append("?")
            elif defend_state == 0:
                self.__name_parts.append("attack")
            elif defend_state == 1:
                self.__name_parts.append("ally")
        self.__name_parts.append(color_id if color_id >= 0 else "")
        return self.get_name_generated()

    def get_name_generated(self) -> str:
        self.__generated_name = "-".join(filter(None, self.__name_parts)).lower()
        self.__name_parts = [self.__talent if self.__talent else "", self.__class_name]
        return self.__generated_name
