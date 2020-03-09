def fatorial(n):
    if n > 1:
        return n * fatorial(n - 1)
    else:
        return 1


def primo(n):
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


def user_digit():
    i = 1
    div = 0
    while True:
        n = int(input('Digite o número:\n'))

        if n > 0:
            print('Número Fatorial é: ', fatorial(n))

            if primo(n):
                print(n, 'é número primo!')
            else:
                print(n, 'não é primo!')
        else:
            exit()


if __name__ == "__main__":
    result = user_digit()
    print(result)
