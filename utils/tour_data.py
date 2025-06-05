# tour_data.py
import json
from pathlib import Path

# Путь к JSON-файлу
DATA_PATH = "utils/tours.json"

# Загрузим данные один раз при импорте
with open(DATA_PATH, "r", encoding="utf-8") as f:
    TOURE_STRUCTURE = json.load(f)
