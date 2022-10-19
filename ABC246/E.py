def main():
    N = int(input())
    Ax, Ay = list(map(int, input().split()))
    Bx, By = list(map(int, input().split()))
    S = []
    for _ in range(N):
        S.append(input())
    print(S)


if __name__ == "__main__":
    main()
