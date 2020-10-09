import pytest


class TestClassSet:

    @pytest.fixture(scope='class')
    def set_example(self):
        yield {'vk', 'telegram', 'facebook', 'twitter', 'whatsup'}

    b = {'twitter', 'facebook', 'instagram', 'viber'}

    def test_length(self, set_example):  # проверка размера множества
        assert len(set_example) == 5

    def test_intersection(self, set_example):  # проверка пересекающихся элементов в двух заданных множествах
        set_example &= self.b
        assert set_example == {'twitter', 'facebook'}


def test_comparison():  # проверка сравнения элементов двух множеств
    a = set('hello')
    b = set('halo')
    assert not (a == b)


@pytest.mark.parametrize('i', [{4, 2, 3}, {5, 7}, {0, 7, 3}])
def test_negative_search(i):  # проверяем, что в множествах нет заданного элемента
    print(i)
    assert 1 not in i


def test_subset():  # проверка того, что одно множество является подмножеством другого множества
    a = {i ** 2 for i in range(5)}
    b = {0, 4, 9}
    assert a >= b
