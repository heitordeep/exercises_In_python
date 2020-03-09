
def primok(n) -> bool:
    i = 1
    div = 0

    while i <= n:
        if n % i == 0:
            div += 1
        i += 1
    if div == 2:
        return True
    else:
        return False


def maior_primo(n) -> int:

    if n < 2:
        return 0

    primo = primok(n)
    while primo == False:
        n -= 1
        primo = primok(n)
    return n

if __name__ == "__main__":
    i = int(input(''))
    print(maior_primo(i))
