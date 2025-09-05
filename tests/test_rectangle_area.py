import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.geometry import rectangle_area

def test_rectangle_area_correct_length() -> None:
    """
    Тест вычисления площади с целыми положительными числами
    """
    width = "5"
    height = "5"
    expected_result = 25
    
    actual_result: float = rectangle_area(width, height)
    
    assert actual_result == pytest.approx(expected_result)


def test_area_with_empty_string() -> None:
    """
    Тест вычисления площади с пустой строкой в качестве длины стороны
    """
    width = ""
    height = "5"
    
    with pytest.raises(ValueError) as exc_info:
        rectangle_area(width, height)
    
    assert str(exc_info.value) == "Введено недопустимое значение"


def test_area_with_empty_height() -> None:
    """
    Тест вычисления площади с пустой строкой в качестве высоты
    """
    width = "3"
    height = ""
    
    with pytest.raises(ValueError) as exc_info:
        rectangle_area(width, height)
    
    assert str(exc_info.value) == "Введено недопустимое значение"


def test_area_with_float_dot_format() -> None:
    """
    Тест вычисления площади с числами с плавающей точкой через точку
    """
    width = "2.5"
    height = "4.0"
    expected_result: float = 10.0
    
    actual_result: float = rectangle_area(width, height)
    
    assert actual_result == pytest.approx(expected_result)


def test_area_with_float_comma_format() -> None:
    """
    Тест вычисления площади с числами с плавающей точкой через запятую
    """
    width = "3,5"
    height = "2,8"
    expected_result: float = 9.8
    
    actual_result: float = rectangle_area(width, height)
    
    assert actual_result == pytest.approx(expected_result)


def test_area_with_mixed_formats() -> None:
    """
    Тест вычисления площади со смешанными форматами (точка и запятая)
    """
    width = "10"
    height = "0,5"
    expected_result: float = 5.0
    
    actual_result: float = rectangle_area(width, height)
    
    assert actual_result == pytest.approx(expected_result)


def test_area_with_spaces() -> None:
    """
    Тест вычисления площади со строками, содержащими пробелы
    """
    width = " 4 "
    height = " 6 "
    expected_result: float = 24.0
    
    actual_result: float = rectangle_area(width, height)
    
    assert actual_result == pytest.approx(expected_result)


def test_area_with_negative_width() -> None:
    """
    Тест вычисления площади с отрицательной шириной
    """
    width = "-2"
    height = "5"
    
    with pytest.raises(ValueError) as exc_info:
        rectangle_area(width, height)
    
    assert str(exc_info.value) == "Сторона должна быть положительным числом"


def test_area_with_negative_height() -> None:
    """
    Тест вычисления площади с отрицательной высотой
    """
    width = "3"
    height = "-1"
    
    with pytest.raises(ValueError) as exc_info:
        rectangle_area(width, height)
    
    assert str(exc_info.value) == "Сторона должна быть положительным числом"


def test_area_with_zero_width() -> None:
    """
    Тест вычисления площади с нулевой шириной
    """
    width = "0"
    height = "5"
    
    with pytest.raises(ValueError) as exc_info:
        rectangle_area(width, height)
    
    assert str(exc_info.value) == "Сторона должна быть положительным числом"


def test_area_with_zero_height() -> None:
    """
    Тест вычисления площади с нулевой высотой
    """
    width = "3"
    height = "0"
    
    with pytest.raises(ValueError) as exc_info:
        rectangle_area(width, height)
    
    assert str(exc_info.value) == "Сторона должна быть положительным числом"


def test_area_with_invalid_string() -> None:
    """
    Тест вычисления площади с нечисловой строкой
    """
    width = "abc"
    height = "5"
    
    with pytest.raises(ValueError) as exc_info:
        rectangle_area(width, height)
    
    assert str(exc_info.value) == "Введено недопустимое значение"


def test_area_with_invalid_number_format() -> None:
    """
    Тест вычисления площади с неверным форматом числа
    """
    width = "3.5.2"
    height = "4"
    
    with pytest.raises(ValueError) as exc_info:
        rectangle_area(width, height)
    
    assert str(exc_info.value) == "Введено недопустимое значение"

if __name__ == "__main__":
    pytest.main()