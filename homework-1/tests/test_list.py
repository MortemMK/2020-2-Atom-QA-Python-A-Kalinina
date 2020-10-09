import pytest


class TestClassList:

    @pytest.fixture(scope='class')
    def list_example(self):
        yield [1, 4, 1, 1, 4, 5, 9, 8, 9, 9]

    def test_elem_amount(self, list_example):  # сравнение количества элементов с разными значениями в списке
        assert list_example.count(4) < list_example.count(9)

    def test_index(self, list_example):  # проверка положения первого элемента с заданным значения после сортировки
        list_example.sort()
        assert list_example.index(4) == 3


@pytest.mark.parametrize('i', [list('hello stranger'), list('aaabbbccc')])
def test_removing_negative(i):  # проверка вызова ошибки, если элемента, который нужно удалить, не существует
    with pytest.raises(ValueError):
        assert i.remove('y')


def test_add_elem():  # проверка вставки значения на какую-то позицию в списке
    a = list('hello stranger')
    a.insert(5, ',')
    assert ''.join(a) == 'hello, stranger'


def test_count():  # проверка подсчета количества элементов с заданным значением
    a = [[1, 0, 0], [0, 1, 0], [1, 1, 0], [1, 1, 1], [0, 0, 1]]
    assert a[2].count(1) == 2
