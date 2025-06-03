import json
from .tour_data import TOURE_STRUCTURE


def get_index(value: str, data: list[dict]):
    for i, item in enumerate(data):
        if item["callback_data"] == value:
            return i


def get_prev_data(dict: dict):
    result = []
    for key, value in dict.items():
        result.append(value)

    print("Прошлые данные -> ", result)
    return result


def get_next_values(level: int, previous_values: list[str]):

    # # tour_data.py
    # import json
    # from pathlib import Path

    # # Путь к JSON-файлу
    # DATA_PATH = "utils/toures.json"

    # # Загрузим данные один раз при импорте
    # with open(DATA_PATH, "r", encoding="utf-8") as f:
    #     TOURE_STRUCTURE = json.load(f)

    data = TOURE_STRUCTURE
    if level == 0:
        result = data["data"]
        return [
            {"text": result[i]["text"], "callback_data": result[i]["callback_data"]}
            for i in range(len(result))
        ]

    elif level == 1:
        return [
            {"text": item["text"], "callback_data": item["callback_data"]}
            for item in data["data"][get_index(previous_values[0], data["data"])][
                "next"
            ]
        ]
    elif level == 2:
        items = []
        for item in data["data"][get_index(previous_values[0], data["data"])]["next"][
            get_index(
                previous_values[1],
                data["data"][get_index(previous_values[0], data["data"])]["next"],
            )
        ]["next"]:
            items.append({"text": item["text"], "callback_data": item["callback_data"]})
        return items
    elif level == 3:
        items = []
        for item in data["data"][get_index(previous_values[0], data["data"])]["next"][
            get_index(
                previous_values[1],
                data["data"][get_index(previous_values[0], data["data"])]["next"],
            )
        ]["next"][
            get_index(
                previous_values[2],
                data["data"][get_index(previous_values[0], data["data"])]["next"][
                    get_index(
                        previous_values[1],
                        data["data"][get_index(previous_values[0], data["data"])][
                            "next"
                        ],
                    )
                ]["next"],
            )
        ][
            "next"
        ]:
            items.append({"text": item["text"], "callback_data": item["callback_data"]})
        return items


# print(get_next_values(3, ["less_6", "matrya", "sreda"]))


def get_labels_by_callback_path(callback_path):
    """
    Ищет путь по callback_data и возвращает соответствующие текстовые метки.
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
    data = TOURE_STRUCTURE["data"]
    found = dfs(data, callback_path, result_labels)
    return result_labels if found else None
