from .tour_data import TOURE_STRUCTURE


def get_index(value: str, data_list: list[dict]) -> int:
    """
    Возвращает индекс элемента в списке словарей по значению 'callback_data'.

    :param value: Значение 'callback_data', которое нужно найти.
    :param data_list: Список словарей, где ищется значение.
    :return: Индекс элемента в списке.
    """
    for index, item in enumerate(data_list):
        if item["callback_data"] == value:
            return index
    raise ValueError(f"Value '{value}' not found in the data list.")


def get_prev_data(dict: dict) -> list[str]:
    """
    Возвращает список предыдущих значений для inline-клавиатуры.

    :param dict: Словарь с данными.
    :return: Список предыдущих значений.
    """
    result = []
    for key, value in dict.items():
        result.append(value)
    print("Прошлые данные -> ", result)
    return result


def get_next_values(level: int, previous_values: list[str]) -> list[dict]:
    """
    Получает следующие значения для inline-клавиатуры на основе уровня и предыдущих значений.

    :param level: Уровень данных (0, 1, 2 или 3).
    :param previous_values: Список предыдущих значений 'callback_data' для навигации по структуре.
    :return: Список словарей с текстом и callback_data для кнопок.
    """
    # Основная структура данных
    data = TOURE_STRUCTURE

    # Уровень 0: Корневой уровень (все доступные варианты)
    if level == 0:
        return [
            {"text": item["text"], "callback_data": item["callback_data"]}
            for item in data["data"]
        ]

    # Уровень 1: Первый шаг (данные зависят от первого выбранного значения)
    elif level == 1:
        first_level_index = get_index(previous_values[0], data["data"])
        return [
            {"text": item["text"], "callback_data": item["callback_data"]}
            for item in data["data"][first_level_index]["next"]
        ]

    # Уровень 2: Второй шаг (данные зависят от первых двух выбранных значений)
    elif level == 2:
        first_level_index = get_index(previous_values[0], data["data"])
        second_level_index = get_index(
            previous_values[1], data["data"][first_level_index]["next"]
        )
        return [
            {"text": item["text"], "callback_data": item["callback_data"]}
            for item in data["data"][first_level_index]["next"][second_level_index][
                "next"
            ]
        ]

    # Уровень 3: Третий шаг (данные зависят от первых трех выбранных значений)
    elif level == 3:
        first_level_index = get_index(previous_values[0], data["data"])
        second_level_index = get_index(
            previous_values[1], data["data"][first_level_index]["next"]
        )
        third_level_index = get_index(
            previous_values[2],
            data["data"][first_level_index]["next"][second_level_index]["next"],
        )
        return [
            {"text": item["text"], "callback_data": item["callback_data"]}
            for item in data["data"][first_level_index]["next"][second_level_index][
                "next"
            ][third_level_index]["next"]
        ]

    # Если уровень не поддерживается
    else:
        raise ValueError(f"Unsupported level: {level}")


def get_labels_by_callback_path(callback_path: list[str]) -> list[str]:
    """
    Ищет путь по callback_data и возвращает соответствующие текстовые метки.

    :param callback_path: Список callback_data, которые нужно искать.
    :return: Список текстовых меток, соответствующих callback_data.
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
