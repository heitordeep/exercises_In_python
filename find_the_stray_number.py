def stray(arr):
    odd = 0
    even = 0
    aux = 0

    for i in arr:
        if i % 2 != 0:
            odd += 1
        else:
            even += 1
          
            
    if odd > even:
        for i in arr:
            if odd == 1:
                return i

            if i % 2 == 0:
                return i
    else:
        for i in arr:
            if even == 1:
                return i
            if i % 2 != 0:
                return i
                

def test_find():            
    assert stray([1, 1, 1, 1, 1, 1, 2]) == 2
    assert stray([2, 3, 2, 2, 2]) == 3
    assert stray([3, 2, 1, 2, 2]) == 3
    assert stray([111234]) == 111234
    assert stray([7867]) == 7867
    assert stray([227915]) == 227915