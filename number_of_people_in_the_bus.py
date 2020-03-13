import pytest


def number(bus_stops):
    result = sum([value[0] - value[1] 
                 for value in bus_stops])
    return result


# Primeiro entra no ônibus e segundo sai do ônibus

def test_number5():
    assert number([[10, 0], [3, 5], [5, 8]]) == 5


def test_number17():
    assert number([[3, 0], [9, 1], [4, 10], [12, 2], [6, 1], [7, 10]]) == 17


def test_number21():
    assert number([[3, 0], [9, 1], [4, 8], [12, 2], [6, 1], [7, 8]]) == 21
