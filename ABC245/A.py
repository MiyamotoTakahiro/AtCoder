def main():
    a, b, c, d = input().split()
    if a < c:
        print("Takahashi")
    elif a == c:
        if b <= d:
            print("Takahashi")
        else:
            print("Aoki")
    else:
        print("Aoki")


if __name__ == "__main__":
    main()