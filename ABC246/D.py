def f(a, b):
    return (a ** 2 + b ** 2) * (a + b)


def main():
    N = int(input())
    b = int(1e6)
    x = int(1e20)

    for a in range(b + 1):
        while f(a, b) >= N and b >= 0:
            x = min(x, f(a, b))
            b -= 1

    print(x)