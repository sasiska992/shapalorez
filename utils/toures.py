import json


def get_toures():
    with open("utils/toures.json", "r") as f:
        data = json.load(f)
    return data


def get_index(value: str, data: list[dict]):
    for i, item in enumerate(data):
        if item["text"] == value:
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
        return [
            item["text"]
            for item in data["data"][get_index(previous_values[0], data["data"])][
                "next"
            ][
                get_index(
                    previous_values[1],
                    data["data"][get_index(previous_values[0], data["data"])]["next"],
                )
            ][
                "next"
            ]
        ]


print(get_data(2, ["До 6", "Матрица - муниципальный поезд в будние дни"]))
