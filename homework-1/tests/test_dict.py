import pytest


class TestClassDict:

    @pytest.fixture(scope='class')
    def dict_example(self):
        yield {1: 2, 2: 2, 3: 2}

    def test_key_negative(self, dict_example):  # проверка вызова ошибки при попытке извлечь значение несуществующего
        # ключа
        with pytest.raises(KeyError):
            assert dict_example[5] == 2


@pytest.mark.parametrize('i', [1, 2, 3])
def test_search_negative(i):  # проверяем, что в словарях нет значения
    d = {i: i + 1}
    assert 0 not in d


def test_comparison():  # проверка равенства значений разных ключей
    d = dict.fromkeys(['x', 'y', 'z'], 5)
    assert d['x'] == d['y'] == d['z']


def test_key_value():  # проверка сравнения значений двух ключей (если ключа не существует, создается новый ключ с
    # заданным значением)
    d = dict.fromkeys(['x', 'y'], 5)
    assert d.setdefault('y', 7) < d.setdefault('z', 7)


def test_values_amount():  # проверка сравнения количества разных значений в словаре
    d = dict.fromkeys(['x', 'y'], 5)
    d.update({'z': 9})
    assert list(d.values())[2] > list(d.values())[1]
