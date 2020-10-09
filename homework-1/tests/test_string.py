import pytest


class TestClassStr:

    @pytest.fixture(scope='class')
    def string_example(self):
        yield 'hEllO, wOrLd'

    def test_register(self, string_example):
        assert string_example.title() == 'Hello, World'

    def test_uppercase(self, string_example):
        assert string_example.upper() == 'HELLO, WORLD'


def test_length():  # проверка длины дублированной строки
    a = 'test' * 3
    assert len(a) == 12


def test_substring_negative():  # проверка вызова ошибки если подстрока в строке не находится
    with pytest.raises(ValueError):
        a = 'wednesday'
        assert a.rindex('wed', 1)


@pytest.mark.parametrize('i', list('abcd'))
def test_isalpha(i):  # проверяет состоит ли строка из букв
    assert i.isalpha()


def test_substring():  # проверка количества непересекающихся вхождений подстроки
    a = 'testesttestestes'
    assert a.count('est', 1) == 4
