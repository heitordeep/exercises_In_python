def iq_test(numbers):

    result_list = numbers.split()
    count_even = 0
    count_odd = 0
    position = 0

    for i in range(0, len(result_list)):
        if int(result_list[i]) % 2 == 0:
            count_even += 1
        else:
            count_odd += 1

    # Se tiver mais ímpar, procura a posição do par.
    if count_odd > count_even:
        for i in range(0, len(result_list)):
            if int(result_list[i]) % 2 == 0:
                position = i+1
    else:
    # Se tiver mais par, procura a posição do ímpar.
        for i in range(0, len(result_list)):
            if int(result_list[i]) % 2 != 0:
                position = i+1

    return position


def test_iq_test():
    assert iq_test("2 4 7 8 10") == 3
    assert iq_test("1 2 2") == 1
    assert iq_test("3 5 6 1 2 10") == 4
