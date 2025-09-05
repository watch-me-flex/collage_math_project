def parse_number(value: str) -> float:
    """
    Преобразует строку в положительное число с плавающей точкой,
    проверяет корректность и положительность значения.
    :param value: Строка с числом
    """
    s = value.strip().replace(',', '.')
    if not s:
        raise ValueError("Введено недопустимое значение")
    try:
        number = float(s)
    except ValueError:
        raise ValueError("Введено недопустимое значение")
    if number <= 0:
        raise ValueError("Сторона должна быть положительным числом")
    return number


def rectangle_area(width: str, height: str) -> float:
    """
    Вычисляет площадь прямоугольника, проверяя входные данные.
    :param width: Ширина прямоугольника
    :param height: Высота прямоугольника
    :return: Площадь прямоугольника
    """
    w = parse_number(width)
    h = parse_number(height)
    return w * h