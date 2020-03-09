def expanded_form(num):
    result = []

    for index, digit in enumerate(str(num)[::-1]):
        if int(digit) != 0:
            result.append(digit + ('0' * index))

    return ' + '.join(result[::-1])

print(expanded_form(890978))

def test_expanded_form():
    assert expanded_form(12) == '10 + 2'
    assert expanded_form(42) == '40 + 2'
    assert expanded_form(70304) == '70000 + 300 + 4'
    assert expanded_form(890978) == '800000 + 90000 + 900 + 70 + 8'
