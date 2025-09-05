import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.geometry import rectangle_area

def test_rectangle_area_correct_length():
    """
    Тест вычисления площади с целыми положительными числами
    """
    width = "5"
    height = "5"
    expected_result = 25
    
    actual_result = rectangle_area(width, height)
    
    assert actual_result == pytest.approx(expected_result)


def test_area_with_empty_string():
    """
    Тест вычисления площади с пустой строкой в качестве длины стороны
    """
    width = ""
    height = "5"
    
    with pytest.raises(ValueError) as exc_info:
        rectangle_area(width, height)
    
    assert str(exc_info.value) == "Введено недопустимое значение"

if __name__ == "__main__":
    pytest.main()