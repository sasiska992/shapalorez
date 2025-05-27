import json


def get_toures():
    with open("utils/toures.json", "r") as f:
        data = json.load(f)
    return data


def get_index(value: str, data: list[dict]):
    for i, item in enumerate(data):
        if item["callback_data"] == value:
            return i


def get_data(level: int, previous_values: list[str]):
    data = get_toures()
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


keys_to_find = ["less_6", "drezina", "krasnoy_most"]


# Функция для поиска callback_data
def find_callback_data(keys: list[str]):
    data = get_toures()
    """
    Ищет значения 'text' в словаре по заданным ключам 'callback_data'.

    Параметры:
    keys (list): Список ключей 'callback_data', по которым будет осуществляться поиск.

    Возвращает:
    list: Уникальные значения 'text', соответствующие найденным 'callback_data'.
    """
    results = []
    
    def search(data):
        """
        Рекурсивно ищет значения 'text' в словаре или списке.

        Параметры:
        data (dict или list): Словарь или список, в котором будет производиться поиск.
        """
        if isinstance(data, dict):
            # Проверяем, есть ли текущий элемент в списке ключей
            if data.get('callback_data') in keys:
                results.append(data['text'])  # Добавляем 'text' в результаты
            # Рекурсивно ищем в подэлементах
            for key, value in data.items():
                if isinstance(value, (dict, list)):
                    search(value)
        elif isinstance(data, list):
            # Рекурсивно ищем в каждом элементе списка
            for item in data:
                search(item)
    
    search(data)  # Начинаем поиск
    return results  # Возвращаем результаты в порядке их следования
