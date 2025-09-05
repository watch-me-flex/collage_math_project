import sys
import os
from .geometry import rectangle_area

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def main():
    """Основная функция с примерами использования rectangle_area"""
    
    print("Задание 1")
    print("-" * 40)
    
    # Примеры корректных вычислений
    test_cases = [
        ("5", "5", "Целые положительные числа"),
        ("5.5", "5.5", "Числа с плавающей точкой через точку"),
        ("5,5", "5,8", "Числа с плавающей точкой через запятую"),
        ("5", "0.5", "Смешанные форматы"),
        (" 5 ", " 6 ", "Строки с пробелами"),
    ]
    
    print("\nПримеры норм вычислений:")
    print("-" * 40)
    
    for width, height, description in test_cases:
        try:
            area = rectangle_area(width, height)
            print(f"{description}: {width} x {height} = {area}")
        except ValueError as e:
            print(f"{description}: {e}")
    
    # Примеры с ошибками
    error_cases = [
        ("", "5", "Пустая строка для ширины"),
        ("5", "", "Пустая строка для высоты"),
        ("-5", "5", "Отрицательная ширина"),
        ("5", "-1", "Отрицательная высота"),
        ("0", "5", "Нулевая ширина"),
        ("abc", "5", "Нечисловая строка"),
        ("3.5.2", "4", "Неверный формат числа"),
    ]
    
    print("\n\nПримеры ошибок:")
    print("-" * 40)
    
    for width, height, description in error_cases:
        try:
            area = rectangle_area(width, height)
            print(f"{description}: {width} x {height} = {area}")
        except ValueError as e:
            print(f"{description}: {e}")


if __name__ == "__main__":
    main()