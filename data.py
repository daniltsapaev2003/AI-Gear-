CATEGORIES = [
    {"slug": "smartphones", "name": "Смартфоны"},
    {"slug": "laptops", "name": "Ноутбуки"},
    {"slug": "audio", "name": "Наушники и аудио"},
    {"slug": "accessories", "name": "Аксессуары"},
]

PRODUCTS = [
    {
        "id": "phone-a1",
        "name": "Смартфон Demo Phone A1 8/256 ГБ",
        "category": "smartphones",
        "price": 34990,
        "old_price": 39990,
        "hit": True,
        "description": "Учебный товар для проверки витрины. 6.5 дюйма, двойная камера, аккумулятор 5000 мАч.",
    },
    {
        "id": "phone-b2",
        "name": "Смартфон Demo Phone B2 12/256 ГБ",
        "category": "smartphones",
        "price": 54990,
        "old_price": None,
        "hit": True,
        "description": "Учебный товар. 6.7 дюйма, тройная камера, быстрая зарядка 65 Вт.",
    },
    {
        "id": "laptop-c3",
        "name": "Ноутбук Demo Book C3 16 ГБ / 512 ГБ",
        "category": "laptops",
        "price": 89990,
        "old_price": 99990,
        "hit": True,
        "description": "Учебный товар. 14 дюймов, 16 ГБ оперативной памяти, SSD 512 ГБ.",
    },
    {
        "id": "audio-d4",
        "name": "Беспроводные наушники Demo Buds D4",
        "category": "audio",
        "price": 6990,
        "old_price": 8990,
        "hit": False,
        "description": "Учебный товар. Шумоподавление, до 24 часов работы с кейсом.",
    },
    {
        "id": "acc-e5",
        "name": "Зарядное устройство Demo Charge E5 65 Вт",
        "category": "accessories",
        "price": 2490,
        "old_price": None,
        "hit": False,
        "description": "Учебный товар. Два порта USB-C и USB-A, технология быстрой зарядки.",
    },
]


def find_product(pid):
    return next((p for p in PRODUCTS if p["id"] == pid), None)
