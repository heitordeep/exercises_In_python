def odd_or_even(arr):
    return 'even' if sum(arr) % 2 == 0 else 'odd'
    




def test_equal_odd():
    assert odd_or_even([0, 1, 2]) == 'odd'

def test_equal_even():
    assert odd_or_even([0, 1, 3]) == 'even'
    assert odd_or_even([1023, 1, 2]) == 'even'