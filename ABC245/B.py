def main():
    N = int(input())
    A = list(map(int, input().split()))

    MAX_N = 2004
    bool_list = [False]*MAX_N
    for index in A:
        bool_list[index] = True

    print(bool_list.index(False))

if __name__ == "__main__":
    main()
