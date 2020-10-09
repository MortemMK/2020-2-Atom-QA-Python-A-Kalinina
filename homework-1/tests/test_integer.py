import pytest
import random


class TestClassInt:
    a = random.randint(0, 5)
    b = random.randint(0, 3)

    def test_comparison(self):  # проверка сравнения двух чисел
        assert self.a + self.b < 9

    def test_abs_value(self):  # проверка того, что модуль отрицательного числа всегда >= 0
        assert abs(0 - self.a) >= 0


def test_sum():  # проверка сложения двух чисел
    assert 1 + 1 == 2


@pytest.mark.parametrize('i', [2, 8, 14])
def test_modulo(i):  # проверка остатка от деления заданных чисел на 3
    assert i % 3 == 2


def test_sum_negative():  # проверка вызова ошибки при попытке сложить число со строкой
    with pytest.raises(TypeError):
        a = 3
        b = "1"
        print(a + b)
