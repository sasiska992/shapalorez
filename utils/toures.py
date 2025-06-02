import json
from tour_data import TOUR_STRUCTURE


def get_index(value: str, data: list[dict]):
    for i, item in enumerate(data):
        if item["callback_data"] == value:
            return i


def TOURE_STRUCTURE(level: int, previous_values: list[str]):
    data = TOUR_STRUCTURE
    if level == 0:
        result = data["data"]
        return [
            {"text": result[i]["text"], "callback_data": result[i]["callback_data"]}
            for i in range(len(result))
        ]

    if level == 1:
        return [
            {"text": item["text"], "callback_data": item["callback_data"]}
            for item in data["data"][get_index(previous_values[0], data["data"])][
                "next"
            ]
        ]
    if level == 2:
        items = []
        for item in data["data"][get_index(previous_values[0], data["data"])]["next"][
            get_index(
                previous_values[1],
                data["data"][get_index(previous_values[0], data["data"])]["next"],
            )
        ]["next"]:
            items.append({"text": item["text"], "callback_data": item["callback_data"]})
        return items


def get_labels_by_callback_path(callback_path):
    """
    Ищет путь по callback_data и возвращает соответствующие текстовые метки.
    Данные берутся из уже загруженной структуры (один раз при старте).
    """

    def dfs(current_level, path_remaining, result):
        if not path_remaining:
            return True

        for item in current_level:
            if item["callback_data"] == path_remaining[0]:
                result.append(item["text"])
                next_level = item.get("next", [])
                if dfs(next_level, path_remaining[1:], result):
                    return True
                result.pop()  # Откатываем, если путь не совпал дальше
        return False

    result_labels = []
    found = dfs(TOUR_STRUCTURE, callback_path, result_labels)
    return result_labels if found else None
